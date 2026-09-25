"""Build index.html from the page template, the gist sync store and the plan data.
Usage (from the repo root):  python tools/assemble.py
To regenerate the plan itself:  cd tools && python build.py && python export.py && mv plan.json ../plan/plan.json
"""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
tpl = (root / "tools/template.html").read_text(encoding="utf-8")
store = (root / "tools/ghstore.js").read_text(encoding="utf-8")
plan = (root / "plan/plan.json").read_text(encoding="utf-8")
head_end = tpl.index("</style>") + len("</style>")
head, body = tpl[:head_end], tpl[head_end:]
body = body.replace("<script>const PLAN = /*__PLAN__*/;</script>", "<script>\n" + store + "\n</script>\n<script>const PLAN = " + plan + ";</script>", 1)
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="description" content="A personal learning dashboard for a six-month transition to Forward Deployed Engineer: schedule, focus timer, Python practice, projects, career pipeline and review.">\n'
        + head + '\n<style>body{margin:0}</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html) // 1024, "KB")
