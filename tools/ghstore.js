/* GitHub Gist sync store.
   Emulates the small document-store API the page uses (doc().set/delete/onSnapshot, collection().onSnapshot).
   Data lives in this browser's localStorage and, once connected, in one private gist:
   fde-command-center.json = {docs:{path:body}, ts:{path:isoTime}}.
   Merge rule: per-document last-writer-wins by timestamp; deletions keep a timestamp (tombstone). */
window.GHStore = (() => {
  const FILE = "fde-command-center.json", DESC = "FDE Command Center data (private)";
  const ls = { get: k => { try { return localStorage.getItem(k); } catch (e) { return null; } }, set: (k, v) => { try { localStorage.setItem(k, v); } catch (e) {} }, del: k => { try { localStorage.removeItem(k); } catch (e) {} } };
  let state = { docs: {}, ts: {} }, token = null, gistId = null, pushT = null, lastRemote = "";
  const docL = {}, colL = {};
  let statusFn = () => {};
  try { const s = JSON.parse(ls.get("fdecc.data") || "null"); if (s && s.docs) state = Object.assign({ ts: {} }, s); } catch (e) {}
  token = ls.get("fdecc.token"); gistId = ls.get("fdecc.gist");
  const status = (t, s) => statusFn(t, s);
  const snapDoc = p => { const d = state.docs[p]; return { id: p.split("/").pop(), exists: d !== undefined, data: () => d, metadata: { fromCache: false, hasPendingWrites: false } }; };
  const snapCol = c => { const docs = Object.keys(state.docs).filter(p => p.split("/").length === 2 && p.startsWith(c + "/")).map(snapDoc); return { docs, size: docs.length, empty: !docs.length, docChanges: () => [], metadata: { fromCache: false, hasPendingWrites: false } }; };
  const emitAll = () => { Object.keys(docL).forEach(p => docL[p].forEach(f => f(snapDoc(p)))); Object.keys(colL).forEach(c => colL[c].forEach(f => f(snapCol(c)))); };
  const saveLocal = () => ls.set("fdecc.data", JSON.stringify(state));
  function touch(){ saveLocal(); if (!token || !gistId){ status("Saved on this device", "local"); return; } clearTimeout(pushT); status("Syncing…", "busy"); pushT = setTimeout(push, 1200); }
  async function api(method, url, body){
    const r = await fetch("https://api.github.com" + url, { method, cache: "no-store", headers: Object.assign({ "Authorization": "Bearer " + token, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" }, body ? { "Content-Type": "application/json" } : {}), body: body ? JSON.stringify(body) : undefined });
    if (!r.ok) throw new Error(r.status === 401 ? "token rejected" : r.status === 404 ? "gist not found" : "GitHub " + r.status);
    return r.status === 204 ? null : r.json();
  }
  async function readRemote(){ const g = await api("GET", "/gists/" + gistId); const f = g.files && g.files[FILE]; if (!f) return null; let c = f.content; if (f.truncated) c = await (await fetch(f.raw_url, { cache: "no-store" })).text(); return c; }
  function merge(remote){
    let changed = false, needPush = false; const rt = remote.ts || {}, lt = state.ts || (state.ts = {});
    new Set([...Object.keys(rt), ...Object.keys(lt)]).forEach(p => { const r = rt[p] || "", l = lt[p] || "";
      if (r > l){ if (remote.docs[p] === undefined) delete state.docs[p]; else state.docs[p] = remote.docs[p]; lt[p] = r; changed = true; }
      else if (l > r) needPush = true; });
    return { changed, needPush };
  }
  async function push(){
    try {
      const c = await readRemote(); if (c){ const m = merge(JSON.parse(c)); if (m.changed){ saveLocal(); emitAll(); } }
      const content = JSON.stringify(state); await api("PATCH", "/gists/" + gistId, { files: { [FILE]: { content } } }); lastRemote = content; status("Synced to GitHub", "ok");
    } catch (e){ status("Sync failed (" + e.message + "). Retrying", "err"); clearTimeout(pushT); pushT = setTimeout(push, 20000); }
  }
  async function pull(){
    if (!token || !gistId) return;
    try { const c = await readRemote(); if (!c || c === lastRemote){ status("Synced to GitHub", "ok"); return; }
      const m = merge(JSON.parse(c)); lastRemote = c; if (m.changed){ saveLocal(); emitAll(); } if (m.needPush) touch(); else status("Synced to GitHub", "ok");
    } catch (e){ status("Can't reach GitHub (" + e.message + ")", "err"); }
  }
  async function connect(t){
    token = t.trim(); if (!token) throw new Error("Paste a token first");
    const list = await api("GET", "/gists?per_page=100");
    const found = list.find(g => g.description === DESC && g.files && g.files[FILE]);
    if (found) gistId = found.id;
    else { const g = await api("POST", "/gists", { description: DESC, public: false, files: { [FILE]: { content: JSON.stringify(state) } } }); gistId = g.id; }
    ls.set("fdecc.token", token); ls.set("fdecc.gist", gistId);
    await pull(); touch(); return gistId;
  }
  function disconnect(){ token = null; gistId = null; ls.del("fdecc.token"); ls.del("fdecc.gist"); clearTimeout(pushT); status("Saved on this device", "local"); }
  const db = {
    doc: path => ({
      get: async () => snapDoc(path),
      set: async data => { state.docs[path] = JSON.parse(JSON.stringify(data)); state.ts[path] = new Date().toISOString(); touch(); },
      update: async data => { state.docs[path] = Object.assign({}, state.docs[path], JSON.parse(JSON.stringify(data))); state.ts[path] = new Date().toISOString(); touch(); },
      delete: async () => { delete state.docs[path]; state.ts[path] = new Date().toISOString(); touch(); },
      onSnapshot: next => { (docL[path] = docL[path] || []).push(next); setTimeout(() => next(snapDoc(path)), 0); return () => {}; }
    }),
    collection: c => ({ onSnapshot: next => { (colL[c] = colL[c] || []).push(next); setTimeout(() => next(snapCol(c)), 0); return () => {}; } })
  };
  setInterval(pull, 60000);
  document.addEventListener("visibilitychange", () => { if (!document.hidden) pull(); });
  return {
    db, connect, disconnect, pull,
    onStatus: f => { statusFn = f; if (token && gistId){ status("Checking GitHub…", "busy"); pull(); } else status("Saved on this device", "local"); },
    info: () => ({ connected: !!(token && gistId), gistId }),
    exportJSON: () => JSON.stringify(state, null, 2)
  };
})();
