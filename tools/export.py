import json, re, datetime as dt
import build as B

def hm(s):
    if ":" in s: h,m = s.split(":"); return int(h), int(m)
    return int(s), 0
def parse_time(text, slot):
    m = re.match(r"^(\d{1,2}(?::\d\d)?)-(\d{1,2}(?::\d\d)?)\s+(.*)$", text or "")
    defaults = {"m":(10,12),"a":(14,16),"e":(17,19)}
    if m:
        (h1,m1),(h2,m2) = hm(m.group(1)), hm(m.group(2))
        if h1 < 9: h1 += 12
        if h2 < 9 or h2 < h1: h2 += 12
        return h1+m1/60, h2+m2/60, m.group(3)
    s,e = defaults[slot]; return s, e, text

def stream(t):
    if "Weekly review" in t: return "review"
    if t.startswith("Reserve"): return "reserve"
    if "100x" in t: return "x100"
    if re.search(r"GenAI \d|Agents \d|Azure AI Search", t): return "ms"
    if re.search(r"^Ship|^Publish|Threat model|Map P7|write-up", t): return "ship"
    if re.search(r"BigBinary|Playground|drills|DSA|Files, JSON|Environment variables|HTTP API|Type hints|pytest|async|CHECKPOINT|Fix gaps|git|FastAPI|FastMCP|Docker|Deploy the container", t): return "py"
    if re.search(r"IK|P\d|[Cc]apstone|assignment|Week 0", t): return "ik"
    return "py"

days = []
for (d, ph, th, dtype, m, a, e, note, hrs) in B.rows:
    blocks = []
    for slot, txt in (("m",m),("a",a),("e",e)):
        if not txt or txt.startswith("Off") or txt.startswith("Out"): continue
        s, en, title = parse_time(txt, slot)
        st = stream(title)
        blocks.append(dict(id=f"{d.isoformat()}-{slot}", slot=slot, s=round(s,2), e=round(en,2), t=title,
                           k=st, h=0 if st=="reserve" else round(en-s,2), u=B.link_for(title) or B.link_for(txt)))
    days.append(dict(d=d.isoformat(), ph=ph, th=th, ty=dtype, n=note or "", b=blocks))

phase = [dict(w=r[0], ik=r[1], topic=r[2], focus=r[3], x=r[4], ms=r[5]) for r in B.PH]
projects = [dict(id=r[0] or f"own{i}", name=r[1], src=r[2], ikw=r[3], win=r[4], stack=r[6], repo=r[7], notes=r[9])
            for i,r in enumerate(B.PJ) if r[1] != "(your own project)"]
py = [dict(id=f"py{i}", t=r[0], src=r[1], due=r[2].isoformat()) for i,r in enumerate(B.items)]
srcs = [dict(name=r[0], what=r[1], url=r[2], where=r[3]) for r in B.SRC]
json.dump(dict(days=days, phase=phase, projects=projects, py=py, sources=srcs), open("plan.json","w"))
print(len(days), sum(len(x["b"]) for x in days), "blocks")
from collections import Counter
print(Counter(b["k"] for x in days for b in x["b"]))
for x in days[:3]+days[17:19]:
    for b in x["b"]: print(x["d"], b["s"], b["e"], b["k"], b["t"][:50])
