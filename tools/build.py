import datetime as dt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

D = dt.date
F = "Arial"
def fnt(bold=False, color="000000", size=10, italic=False):
    return Font(name=F, bold=bold, color=color, size=size, italic=italic)
HDR_FILL = PatternFill("solid", fgColor="1F4E3D")
FILLS = {
    "Full": PatternFill("solid", fgColor="FFFFFF"),
    "Light": PatternFill("solid", fgColor="FFF4CC"),
    "Half": PatternFill("solid", fgColor="FFE3C2"),
    "Off": PatternFill("solid", fgColor="E0E0E0"),
    "Weekend": PatternFill("solid", fgColor="E8F1FB"),
    "Catch-up": PatternFill("solid", fgColor="FBE3E3"),
}
thin = Side(style="thin", color="D0D0D0")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")

def header(ws, cols, widths, row=1):
    for i, (c, w) in enumerate(zip(cols, widths), 1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font = fnt(True, "FFFFFF"); cell.fill = HDR_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BORDER
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=row+1, column=1)

# ---------------- 100x (estimated) by Friday date ----------------
X = {
 D(2026,9,25): "100x wk 11: UI/UX and APIs",
 D(2026,10,2): "100x wk 12: Databases (Supabase)",
 D(2026,10,9): "100x wk 13: LLMs and prompt engineering",
 D(2026,10,16): "100x wk 14: Vibe coding, launch your MVP",
 D(2026,10,23): "100x wk 15: MVP build and mini hackathon",
 D(2026,10,30): "100x wk 16: Tool calling, MCP, RAG",
 D(2026,11,6): "100x wk 17: Advanced RAG, LLM memory",
 D(2026,11,13): "100x wk 18: Architecting LLM apps, PEFT fine-tuning, evaluation",
 D(2026,11,20): "100x wk 19: Intro to AI agents, first agent",
 D(2026,11,27): "100x wk 20: Multi-agent systems",
 D(2026,12,4): "100x wk 21: Agent SDKs (OpenAI, Claude, Google ADK)",
 D(2026,12,11): "100x wk 22: Guardrails, monitoring, evaluation, agentic workflows",
 D(2026,12,18): "100x wk 23: Agent deployment and production patterns",
}
def x_topic(d):
    fri = d - dt.timedelta(days=(d.weekday()-4) % 7)
    return X.get(fri, "100x class")

# ---------------- IK weeks ----------------
W = [
 dict(start=D(2026,10,11), wk="IK W1", theme="Agent foundations", topic="Agentic AI Foundations & Reflex Agents",
      proj="P1 CRM Lead Qualifier Agent", sat="W1 assignment review (Agentic foundations)", nxt="W2 RAG I",
      ms=["Agents 02: Exploring agentic frameworks","Agents 03: Agentic design patterns","Agents 04: Tool use + GenAI 11: Function calling"],
      pr=["BigBinary ch 26 Operator overloading, ch 29 Bitwise","BigBinary ch 32 itertools, ch 33 Measuring performance","Playground drills"]),
 dict(start=D(2026,10,18), wk="IK W2", theme="RAG", topic="RAG-Powered Knowledge Agents I",
      proj="P2 SupportDesk-RAG (part 1)", sat="RAG I assignment review", nxt="W3 RAG II",
      ms=["GenAI 08: Search apps with embeddings","GenAI 15: RAG and vector databases","Notes: retrieval metrics (Precision@K, groundedness)"],
      pr=["100x MVP build","100x MVP build","100x MVP: hackathon prep"],
      light_swap=(D(2026,10,20), D(2026,10,21))),
 dict(start=D(2026,10,25), wk="IK W3", theme="RAG", topic="RAG-Powered Knowledge Agents II",
      proj="P2 SupportDesk-RAG (part 2)", sat=None, nxt="W4 Multi-Agent Systems",
      ms=["Agents 05: Agentic RAG","Agents 07: Planning design pattern","Agents 08: Multi-agent pattern (prep, since you miss the W4 live class)"],
      pr=["pytest basics: tests for your P2 retrieval code","async/await and httpx","Playground drills"]),
 dict(start=D(2026,11,1), wk="IK W4", theme="Multi-agent and tools", topic="Multi-Agent Systems",
      proj="P3 Multi-Agent Travel Planner", sat="Multi-agent assignment review", nxt="W5 Conversational & Multimodal",
      ms=None, pr=None),
 dict(start=D(2026,11,8), wk="IK W5", theme="Conversational agents, memory", topic="Conversational & Multimodal Agents",
      proj="P4 AxiomCart Shopping Assistant", sat="Conversational assignment review", nxt="W6 Agent Communication Protocols",
      ms=["Agents 12: Context engineering","Agents 13: Managing agentic memory","GenAI 12: Designing UX for AI apps"],
      pr=["FastAPI basics: routes and pydantic models","FastAPI: expose your P1 agent as an endpoint","Playground drills"]),
 dict(start=D(2026,11,15), wk="IK W6", theme="Protocols", topic="Agent Communication Protocols (MCP, A2A, ACP)",
      proj="P5 Real-Estate Negotiation Simulator", sat="Protocols assignment review", nxt="W7 Hybrid Search & Retrieval",
      ms=["Agents 11: Agentic protocols (MCP, A2A, NLWeb)","Agents 14: Microsoft Agent Framework (part 1)","Agents 14: Microsoft Agent Framework (part 2)"],
      pr=["Build a minimal FastMCP server","Docker basics: containerize the FastAPI app","Playground drills"]),
 dict(start=D(2026,11,22), wk="IK W7", theme="Retrieval at scale", topic="Hybrid Search & Retrieval",
      proj="P6 Vertical Insights Agent", sat="Hybrid search assignment review", nxt="W8 Safe, Evaluated & Cost-Optimized",
      ms=["Azure AI Search: hybrid search and semantic ranker (Microsoft Learn)","GenAI 16: Open-source models and Hugging Face","AI Engineering capstone: write the one-page brief"],
      pr=["Deploy the container to Azure Container Apps","git hygiene: branches, PRs, CI lint on one repo","Playground drills"]),
 dict(start=D(2026,11,29), wk="IK W8", theme="Safety, evals, cost (edge week)", topic="Safe, Evaluated & Cost-Optimized Agents",
      proj="P7 Production-Ready Fintech Support Agent", sat="Safe agents assignment review", nxt="W9 Fine-Tuning",
      ms=["GenAI 13: Securing generative AI apps","Agents 18: Securing AI agents","Agents 06: Building trustworthy agents"],
      pr=["Threat model for P7: prompt injection, PII, data exfiltration","Map P7 controls to OWASP Top 10 for LLM apps","Playground drills"],
      ship="Publish P7 write-up plus security review (portfolio piece)"),
 dict(start=D(2026,12,6), wk="IK W9", theme="Fine-tuning", topic="Fine-Tuning & Domain Adaptation",
      proj="P8 Domain-Specific Fine-Tuned Agent", sat="Fine-tuning assignment review", nxt="Capstone resources (out Thu 10 Dec)",
      ms=["GenAI 18: Fine-tuning LLMs","Agents 10: AI agents in production","GenAI 14: GenAI application lifecycle (LLMOps)"],
      pr=["DSA: arrays and hashing (5 problems)","DSA: two pointers (5 problems)","DSA review"]),
 dict(start=D(2026,12,13), wk="IK W10", theme="AI Engineering capstone", topic="AI Engineering Capstone (build 1)",
      proj="AI Engineering capstone", sat="IK Saturday session (not yet published)", nxt="IK W11 materials",
      ms=["Agents 16: Deploying scalable agents","Capstone: architecture doc","Capstone: build an eval set"],
      pr=["Capstone build","Capstone build","DSA: sliding window"]),
]

rows = []  # (date, phase, theme, daytype, m, a, e, note, hrs)
def add(d, phase, theme, dtype, m, a, e, note, hrs):
    rows.append([d, phase, theme, dtype, m, a, e, note, hrs])

# ---------------- Python sprint (explicit) ----------------
P = "Python foundation"
T = "Python sprint (deadline 10 Oct)"
add(D(2026,9,24),P,T,"Full","", "2-4 BigBinary ch 12 While loop, ch 13 Challenges II","5-7 BigBinary ch 14 Comments, ch 15 Functions","Sprint starts. BigBinary at 41%.",4)
add(D(2026,9,25),P,T,"Full","BigBinary ch 16 Function arguments, ch 17 Lambdas","Prep for this week's 100x class","6-8 "+x_topic(D(2026,9,25)),"",6)
add(D(2026,9,26),P,T,"Weekend","BigBinary ch 18 Strings, ch 19 More about lists","GenAI 00: Course setup (environment, Azure OpenAI or Foundry key) + GenAI 01: Intro to GenAI","6-8 "+x_topic(D(2026,9,26)),"",6)
add(D(2026,9,27),P,T,"Weekend","BigBinary ch 20 Handling exceptions, ch 21 Collections","GenAI 02: Exploring and comparing LLMs","4:00-4:30 Weekly review","",4.5)
add(D(2026,9,28),P,T,"Full","BigBinary ch 24 Classes and objects","GenAI 03: Responsible AI + GenAI 04: Prompt engineering fundamentals","BigBinary ch 22 datetime, ch 25 Inheritance","",6)
add(D(2026,9,29),P,T,"Full","BigBinary ch 23 Decorators, ch 28 More about decorators","GenAI 05: Advanced prompts","BigBinary ch 27 Generators, ch 31 Iterators","",6)
add(D(2026,9,30),P,T,"Light","BigBinary ch 30 Raising exceptions; revisit weak chapters","2-3 Playground drills","Reserve: catch-up, else an ai-weekend-builds project","Core BigBinary chapters done",3)
add(D(2026,10,1),P,T,"Full","Files, JSON, pathlib","IK Python for GenAI slides, part 1 (setup, venv, pip, basics)","Environment variables and .env files","",6)
add(D(2026,10,2),P,T,"Full","Calling an HTTP API from Python (httpx)","Prep for this week's 100x class","6-8 "+x_topic(D(2026,10,2)),"Gandhi Jayanti",6)
add(D(2026,10,3),P,T,"Half","IK FDE Foundational Content","Out (second half)","Out. 100x class missed, watch the recording Mon 5 Oct","Half day: out afternoon and evening",2)
add(D(2026,10,4),P,T,"Off","Off","Off","Off","Day off",0)
add(D(2026,10,5),P,T,"Full","IK Python for GenAI slides, part 2 (NumPy, pandas)","Type hints and pydantic basics","100x Sat 3 Oct class recording","",6)
add(D(2026,10,6),P,T,"Full","GenAI 06: First text-generation app in your own code","GenAI 07: Building chat apps","Playground: mixed checkpoint drills","",6)
add(D(2026,10,7),P,T,"Light","IK Week 0 mini project (start)","2-3 Playground drills","Reserve: catch-up, else an ai-weekend-builds project","",3)
add(D(2026,10,8),P,T,"Full","IK Week 0 mini project (finish)","IK Week 1 pre-class resources","Agents 01: Intro to AI agents","",6)
add(D(2026,10,9),P,T,"Full","git and GitHub setup: one repo per project, README template","Prep for this week's 100x class","6-8 "+x_topic(D(2026,10,9)),"",6)
add(D(2026,10,10),P,T,"Weekend","PYTHON CHECKPOINT: self-test in the playground","Fix gaps found in the checkpoint","6-8 "+x_topic(D(2026,10,10)),"MILESTONE: Python foundation done",6)

# ---------------- IK weeks ----------------
def ik_week(w):
    s = w["start"]; wk=w["wk"]; th=f'{wk}: {w["theme"]}'; ph="AI Engineering Spine"
    days = [s + dt.timedelta(days=i) for i in range(7)]
    sun, mon, tue, wed, thu, fri, sat = days
    proj = w["proj"]
    if wk == "IK W4":
        add(sun,ph,th,"Off","Off (family commitment). IK live class missed, recorded","Off","Off","Watch the recording Mon 2 Nov",0)
        add(mon,ph,th,"Catch-up","IK Multi-Agent Systems class recording (part 1)","IK class recording (part 2)","P3: read the assignment, design the approach","",6)
        add(tue,ph,th,"Catch-up",f"{proj}: build core","IK RAG II review recording (1.5x speed)","100x Sat 31 Oct class recording","",6)
        add(wed,ph,th,"Catch-up",f"{proj}: build","P3: build and test","Playground drills","Wednesday is a full day this week to protect the Friday cutoff",6)
        add(thu,ph,th,"Full",f"{proj}: finish and test against the rubric",f"IK slides for {w['nxt']} (out today)",f"Ship: README and short write-up for {proj}","",6)
        add(fri,ph,th,"Full",f"{proj}: polish and submit","Prep for this week's 100x class","6-8 "+x_topic(fri),"IK assignment cutoff tonight",6)
        add(sat,ph,th,"Weekend","9-1 IK: "+w["sat"],"","6-8 "+x_topic(sat),"",6)
        return
    if wk == "IK W5":
        ms, pr = w["ms"], w["pr"]
        add(sun,ph,th,"Off","Off (Diwali). IK live class missed, recorded","Off","Off","Watch the recording Mon 9 Nov",0)
        add(mon,ph,th,"Catch-up",f"IK {w['topic']} class recording (part 1)","IK class recording (part 2)",f"{proj}: read the assignment, design","",6)
        add(tue,ph,th,"Full",f"{proj}: build core",ms[0],pr[0],"",6)
        add(wed,ph,th,"Light",ms[1],"2-3 Playground drills","Reserve: catch-up, else an ai-weekend-builds project","Bhai Dooj. GenAI 12 moved to optional",3)
        add(thu,ph,th,"Full",f"{proj}: finish and test against the rubric",f"IK slides for {w['nxt']} (out today)",f"Ship: README and short write-up for {proj}","",6)
        add(fri,ph,th,"Full",f"{proj}: polish and submit","Prep for this week's 100x class","6-8 "+x_topic(fri),"IK assignment cutoff tonight",6)
        add(sat,ph,th,"Weekend","9-1 IK: "+w["sat"],"","6-8 "+x_topic(sat),"",6)
        return
    note_sun = ""
    if sun == D(2026,10,11): note_sun = "IK starts. Navratri begins"
    if sun == D(2026,12,13): note_sun = "IK capstone submission form (Uplevel)"
    if sun == D(2026,11,22): note_sun = "MILESTONE: choose AI Engineering capstone problem (scout ideas in 500-AI-Agents-Projects)"
    add(sun,ph,th,"Weekend","9-1 IK live class: "+w["topic"],"3:00-3:30 Weekly review","",note_sun,4.5)
    ms, pr = w["ms"], w["pr"]
    light_day, full_wed = w.get("light_swap",(wed,None))
    add(mon,ph,th,"Full",f"{proj}: read the assignment, design, set up repo",ms[0],pr[0],"",6)
    if light_day == tue:
        add(tue,ph,th,"Light",f"{proj}: build core","2-3 "+ms[1],"Reserve: catch-up, else an ai-weekend-builds project","Dussehra. Light day swapped from Wednesday",3)
        add(wed,ph,th,"Full",f"{proj}: build",ms[2],pr[1],"Full day (swapped with Tuesday)",6)
    else:
        add(tue,ph,th,"Full",f"{proj}: build core",ms[1],pr[1],"",6)
        add(wed,ph,th,"Light",ms[2],"2-3 "+pr[2],"Reserve: catch-up, else an ai-weekend-builds project","",3)
    ship = w.get("ship", f"Ship: README and short write-up for {proj}")
    if wk=="IK W10": ship="Capstone: progress notes and demo script"
    add(thu,ph,th,"Full",f"{proj}: finish and test against the rubric",f"IK slides for {w['nxt']} (out today)",ship,"",6)
    fri_note = "IK assignment cutoff tonight" if wk!="IK W10" else ""
    if wk=="IK W3": fri_note = "IK assignment cutoff tonight (submit before your 2 days off)"
    add(fri,ph,th,"Full",f"{proj}: polish and submit" if wk!="IK W10" else "Capstone build","Prep for this week's 100x class","6-8 "+x_topic(fri),fri_note,6)
    if sat == D(2026,10,31):
        add(sat,ph,th,"Off","Off. IK RAG II review missed, recorded","Off","Off. 100x class missed, recorded","Watch recordings Tue 3 Nov",0)
    else:
        add(sat,ph,th,"Weekend","9-1 IK: "+w["sat"],"","6-8 "+x_topic(sat),"",6)

for w in W: ik_week(w)
add(D(2026,12,20),"AI Engineering Spine","IK W11: AI Engineering capstone","Weekend","9-1 IK live class: Capstone build 2 (date projected)","3:00-3:30 Weekly review","","Daily plan ends; phase plan continues",4.5)


import re
URL = {
 "IK": "https://uplevel.interviewkickstart.com/schedule/",
 "BB": "https://courses.bigbinaryacademy.com/learn-python/",
 "X": "https://learn.100xbuilders.com/v3/myaccount",
 "GENAI": "https://github.com/microsoft/generative-ai-for-beginners",
 "AGENTS": "https://github.com/microsoft/ai-agents-for-beginners",
 "COLAB": "https://colab.research.google.com/",
 "WKND": "https://github.com/vipinchenthamara/ai-weekend-builds",
 "500": "https://github.com/vipinchenthamara/500-AI-Agents-Projects",
 "AZSEARCH": "https://learn.microsoft.com/azure/search/hybrid-search-overview",
}
GF = {0:"00-course-setup",1:"01-introduction-to-genai",2:"02-exploring-and-comparing-different-llms",3:"03-using-generative-ai-responsibly",4:"04-prompt-engineering-fundamentals",5:"05-advanced-prompts",6:"06-text-generation-apps",7:"07-building-chat-applications",8:"08-building-search-applications",11:"11-integrating-with-function-calling",12:"12-designing-ux-for-ai-applications",13:"13-securing-ai-applications",14:"14-the-generative-ai-application-lifecycle",15:"15-rag-and-vector-databases",16:"16-open-source-models",18:"18-fine-tuning"}
AF = {1:"01-intro-to-ai-agents",2:"02-explore-agentic-frameworks",3:"03-agentic-design-patterns",4:"04-tool-use",5:"05-agentic-rag",6:"06-building-trustworthy-agents",7:"07-planning-design",8:"08-multi-agent",10:"10-ai-agents-production",11:"11-agentic-protocols",12:"12-context-engineering",13:"13-agent-memory",14:"14-microsoft-agent-framework",16:"16-deploying-scalable-agents",18:"18-securing-ai-agents"}
def link_for(t):
    if not t or t.startswith("Off") or t.startswith("Out"): return None
    m = re.search(r"GenAI (\d+)", t)
    if m and int(m.group(1)) in GF: return URL["GENAI"]+"/tree/main/"+GF[int(m.group(1))]
    m = re.search(r"Agents (\d+)", t)
    if m and int(m.group(1)) in AF: return URL["AGENTS"]+"/tree/main/"+AF[int(m.group(1))]
    if "BigBinary" in t: return URL["BB"]
    if "100x" in t: return URL["X"]
    if "Azure AI Search" in t: return URL["AZSEARCH"]
    if "ai-weekend-builds" in t: return URL["WKND"]
    if "500-AI" in t: return URL["500"]
    if re.search(r"IK|P\d|Capstone|capstone|assignment|Week 0", t): return URL["IK"]
    if re.search(r"Playground|drills|DSA|Files, JSON|Environment variables|HTTP API|Type hints|pytest|async|CHECKPOINT|checkpoint|Fix gaps", t): return URL["COLAB"]
    return None

wb = Workbook()
# ---------------- README ----------------
rd = wb.active; rd.title = "Read me"
rd.column_dimensions["A"].width = 26; rd.column_dimensions["B"].width = 100
lines = [
 ("FDE learning plan: review copy", None),
 ("Covers", "Day by day from 24 Sep to 20 Dec 2026, then week by week to 20 Mar 2027. Built for review before anything goes into the FDE Calendar."),
 ("", ""),
 ("HOW A DAY WORKS", None),
 ("Morning 10-12: Build", "Hardest work while fresh: the IK assignment of the week, or a project."),
 ("Afternoon 2-4: Learn", "The week's concept: the mapped Microsoft lesson, IK slides (released Thursdays), 100x prep on Fridays."),
 ("Evening 5-7: Practice", "Python depth now, FastAPI/Docker in November, DSA from December. Thursdays: ship the README and write-up."),
 ("Weekends", "Sat: IK review 9-1, 100x 6-8. Sun: IK live 9-1, weekly review 3:00-3:30. Before 11 Oct, weekend mornings use the normal blocks."),
 ("", ""),
 ("DAY TYPES", None),
 ("Full", "About 6 hours: three blocks, or two blocks plus a class."),
 ("Light", "3 hours: 10-12 plus 2-3. Default light day is Wednesday, so you never lose the flow. The 5-7 slot stays empty as a catch-up reserve."),
 ("Half / Off", "Your own dates: 3 Oct half, 4 Oct off, 31 Oct and 1 Nov off, 8 Nov (Diwali) off."),
 ("Catch-up", "Full days rearranged to recover missed sessions (2 to 4 Nov)."),
 ("Weekly total", "About 37.5 hours (Sun 4.5, Mon/Tue/Thu/Fri/Sat 6, Wed 3). The Weekly hours tab adds each week up against your 36-hour target."),
 ("", ""),
 ("BANGALORE TRAVEL RULE", None),
 ("On a travel weekday", "The day becomes Light. Keep Learn (slides and recordings work on the move), drop Practice, and move that day's Build block into the next Wednesday 5-7 reserve slot."),
 ("Travel on Thu or Fri", "Finish the IK assignment by Wednesday evening, because Friday night is the cutoff."),
 ("How to tell me", "Say 'travelling 14 Oct' and I'll shift the calendar and dashboard."),
 ("", ""),
 ("ASSUMPTIONS TO CHECK", None),
 ("100x dates", "Estimated. Week 11 = 25/26 Sep, one week per week, no breaks (none published yet). Topics follow the public 100x curriculum order."),
 ("IK dates", "Up to 13 Dec copied from your Uplevel schedule. After that, projected one week per week from the brochure (W12 from 27 Dec, W23 ends about 20 Mar). Replace when IK publishes."),
 ("3 Oct", "Out for the second half. 100x class watched from the recording on Mon 5 Oct."),
 ("Holidays", "Dussehra (Tue 20 Oct) is a light day, swapped with that Wednesday. Diwali (Sun 8 Nov) is a day off; the IK class is watched from the recording on Mon 9 Nov."),
 ("Microsoft lessons", "Mapped to the IK week teaching the same idea. Skipped as optional: GenAI 09, 10, 17, 19, 20, 21 and Agents 09, 15, 17."),
]
r=1
for a,b in lines:
    ca = rd.cell(row=r, column=1, value=a)
    if b is None:
        ca.font = fnt(True, "1F4E3D", 12 if r==1 else 11)
        if r==1: ca.font = fnt(True,"1F4E3D",14)
    else:
        ca.font = fnt(True); cb = rd.cell(row=r, column=2, value=b); cb.font = fnt(); cb.alignment = WRAP
    r+=1

# ---------------- Daily plan ----------------
ws = wb.create_sheet("Daily plan")
cols = ["Week of (Sun)","Date","Day","Phase","Week theme","Day type","Morning (10-12 unless timed)","Afternoon (2-4 unless timed)","Evening (5-7 unless timed)","Due / milestone / note","Planned hrs"]
header(ws, cols, [12,11,6,20,30,10,44,44,40,38,9])
for i,(d,ph,th,dtp,m,a,e,n,h) in enumerate(rows, start=2):
    ws.cell(row=i,column=1,value=f"=B{i}-WEEKDAY(B{i},1)+1").number_format="dd mmm"
    c=ws.cell(row=i,column=2,value=d); c.number_format="ddd dd mmm"
    ws.cell(row=i,column=3,value=d.strftime("%a"))
    vals=[ph,th,dtp,m,a,e,n]
    for j,v in enumerate(vals, start=4): ws.cell(row=i,column=j,value=v)
    hc=ws.cell(row=i,column=11,value=h); hc.font=fnt(color="0000FF")
    fill = FILLS.get(dtp, FILLS["Full"])
    for j in range(1,12):
        cell=ws.cell(row=i,column=j); cell.fill=fill; cell.border=BORDER; cell.alignment=WRAP
        if j!=11: cell.font=fnt(bold=(j==10 and ("MILESTONE" in (n or "") or "cutoff" in (n or ""))))
        if j in (7,8,9):
            u = link_for(cell.value)
            if u: cell.hyperlink = u; cell.font = Font(name=F, size=10, color="1155CC", underline="single")
    lk = link_for(n) if n and "500-AI" in n else None
    if lk: ws.cell(row=i,column=10).hyperlink = lk
last = len(rows)+1
ws.auto_filter.ref = f"A1:K{last}"

# ---------------- Weekly hours ----------------
wh = wb.create_sheet("Weekly hours")
header(wh, ["Week of (Sun)","Planned hrs","Target hrs","Difference","Note"],[14,12,12,12,60])
weeks = sorted({d - dt.timedelta(days=(d.weekday()+1)%7) for d,*_ in rows})
notes = {D(2026,9,20):"Partial week (plan starts Thu 24 Sep)", D(2026,10,4):"Includes your half day and day off", D(2026,11,1):"Two days off; Wednesday made full to recover",D(2026,10,18):"Dussehra light day swapped",D(2026,12,20):"Only Sunday in the daily plan",D(2026,11,8):"Diwali off; class recording on Monday"}
for i,wk in enumerate(weeks, start=2):
    c=wh.cell(row=i,column=1,value=wk); c.number_format="dd mmm yyyy"
    wh.cell(row=i,column=2,value=f"=SUMPRODUCT(('Daily plan'!$B$2:$B${last}>=A{i})*('Daily plan'!$B$2:$B${last}<A{i}+7)*'Daily plan'!$K$2:$K${last})")
    t=wh.cell(row=i,column=3,value=36); t.font=fnt(color="0000FF")
    wh.cell(row=i,column=4,value=f"=B{i}-C{i}")
    wh.cell(row=i,column=5,value=notes.get(wk,""))
    for j in range(1,6):
        cell=wh.cell(row=i,column=j); cell.border=BORDER
        if j!=3: cell.font=fnt()
n=len(weeks)+2
wh.cell(row=n,column=1,value="Total").font=fnt(True)
wh.cell(row=n,column=2,value=f"=SUM(B2:B{n-1})").font=fnt(True)
wh.cell(row=n+2,column=1,value="Target of 36 comes from you (6 hrs a day, 6 days). Blue cells are inputs.").font=fnt(italic=True)

# ---------------- Phase plan ----------------
pp = wb.create_sheet("Phase plan")
header(pp, ["Week","IK week (projected)","IK topic","Your focus","100x","Milestone / holiday"],[16,12,34,62,30,44])
PH = [
 ("21-26 Dec","W11","AI Engineering capstone (build 2)","Finish and submit the capstone. Publish the write-up. Light days 24-26 Dec to recover.","wk 24 (25/26 Dec, likely holiday, TBC)","MILESTONE: AI Engineering capstone submitted. Christmas 25 Dec"),
 ("27 Dec-2 Jan","W12","Pair programming with Claude (Personalised DSA Coach)","AI-assisted coding practice, daily DSA. Decide FDE capstone: PriorAuth AI recommended.","Final week / demo day (TBC)","New Year 1 Jan (light day). MILESTONE: FDE capstone chosen by 2 Jan"),
 ("3-9 Jan","W13","Customer discovery & scoping","PriorAuth discovery; start DECISIONS.md. Set up Azure AI Foundry agent service if IK allows the Azure stack.","",""),
 ("10-16 Jan","W14","SoW, pricing & solution architecture","Draft the PriorAuth SoW. Your consulting background counts here: write it like a real engagement.","","Sankranti / Pongal 14-15 Jan"),
 ("17-23 Jan","W15","Building production agents","PriorAuth architecture. Multi-tenant RAG, token budgets, semantic caching.","",""),
 ("24-30 Jan","W16","APIs, MCP servers & RBAC","PriorAuth build. FastAPI tools, per-tenant scoping, audit logging.","","Republic Day 26 Jan (light day)"),
 ("31 Jan-6 Feb","W17","Evals, observability & handover","PriorAuth handover: runbook, RCA drill, compliance mapping (SOC 2, HIPAA, DPDP). Start resume and LinkedIn rewrite.","","MILESTONE: FDE capstone done"),
 ("7-13 Feb","W18","Agentic research systems","Interview prep begins. Resume, LinkedIn, portfolio site drafts. Target list of 30 companies.","",""),
 ("14-20 Feb","W19","Agentic text-to-SQL","Mock interviews start. Referral outreach.","",""),
 ("21-27 Feb","W20","Multi-agent coordination","System design reps. Final pass on portfolio write-ups.","","MILESTONE 21 Feb: resume, LinkedIn, portfolio final"),
 ("28 Feb-6 Mar","W21","Self-improving agents","Applications open 1 Mar. About 10 targeted applications a week.","","MILESTONE 1 Mar: start applying"),
 ("7-13 Mar","W22","Decomposition & case interviews","Case prompt drills (fintech, healthcare, SaaS). Interviews.","","Ramzan Id about 10 Mar (tentative)"),
 ("14-20 Mar","W23","Behavioural & procurement-security","STAR stories from your consulting engagements. Procurement and security simulation.","","IK program ends"),
]
for i,rw in enumerate(PH, start=2):
    for j,v in enumerate(rw, start=1):
        c=pp.cell(row=i,column=j,value=v); c.font=fnt(bold=(j==6 and "MILESTONE" in v)); c.alignment=WRAP; c.border=BORDER

# ---------------- Skill map ----------------
sm = wb.create_sheet("Skill map")
header(sm, ["Week of (Sun)","Skill theme","IK (lead)","100x (estimated)","Microsoft lessons","Project"],[14,26,36,40,56,36])
SM = [(D(2026,9,27),"Python foundation","Python for GenAI, Foundational Content, Week 0 mini project","wk 11-13: UI/UX, APIs, databases, LLMs & prompting","GenAI 00-07, Agents 01","Python checkpoint (10 Oct)")]
for w in W:
    msl = "; ".join(w["ms"]) if w["ms"] else "Catch-up week (recordings)"
    SM.append((w["start"], w["theme"], w["topic"], x_topic(w["start"]+dt.timedelta(days=5)), msl, w["proj"]))
for i,rw in enumerate(SM, start=2):
    for j,v in enumerate(rw, start=1):
        c=sm.cell(row=i,column=j,value=v); c.font=fnt(); c.alignment=WRAP; c.border=BORDER
        if j==1: c.number_format="dd mmm"

# ---------------- Projects ----------------
pj = wb.create_sheet("Projects")
header(pj, ["ID","Project","Source","IK week","Build window","Status","Stack","Repo link","Write-up link","Notes"],[6,34,12,10,18,12,24,20,20,54])
PJ = [
 ("W0","Week 0 mini project","IK","W0","7-8 Oct","Not started","Python","","",""),
 ("P1","CRM Lead Qualifier Agent","IK","W1","11-16 Oct","Not started","","","","First agent making a business judgment call"),
 ("P2","SupportDesk-RAG","IK","W2-3","18-30 Oct","Not started","","","","Two assignments (RAG I, RAG II)"),
 ("X1","100x MVP","100x","","16-24 Oct","Not started","","","","Suggestion: build it on top of P1 or P2 so one piece of work counts twice during the hackathon week"),
 ("P3","Multi-Agent Travel Planner","IK","W4","2-6 Nov","Not started","","","","Compressed week: live class watched on 2 Nov"),
 ("P4","AxiomCart Shopping Assistant","IK","W5","8-13 Nov","Not started","","","",""),
 ("P5","Real-Estate Negotiation Simulator","IK","W6","15-20 Nov","Not started","","","",""),
 ("P6","Vertical Insights Agent","IK","W7","22-27 Nov","Not started","","","",""),
 ("P7","Production-Ready Fintech Support Agent","IK","W8","29 Nov-4 Dec","Not started","","","","Edge week: add a threat model and OWASP LLM mapping to the write-up"),
 ("P8","Domain-Specific Fine-Tuned Agent","IK","W9","6-11 Dec","Not started","","","",""),
 ("C1","AI Engineering capstone","IK","W10-11","13-26 Dec","Not started","","","","Choose from IK list or bring your own. Candidate BYOP: M365 audit-evidence agent (collect tenant config, map to controls). Decide by 22 Nov"),
 ("P9","Personalised DSA Coach","IK","W12","27 Dec-2 Jan","Not started","","","",""),
 ("C2","FDE capstone: PriorAuth AI (recommended) or ClaimSense AI","IK","W13-17","3 Jan-6 Feb","Not started","","","","Must pick one of the two. PriorAuth is the one the IK weeks 15-17 are built around"),
 ("O1","ai-weekend-builds (fork of kju4q/ai-weekend-builds)","Own","","Wed reserve slots","Not started","Python, Anthropic API","https://github.com/vipinchenthamara/ai-weekend-builds","","Only counts as portfolio once your own commits and write-ups are in it"),
 ("O2","500-AI-Agents-Projects (fork of ashishpatel26)","Own","","Reference","n/a","","https://github.com/vipinchenthamara/500-AI-Agents-Projects","","A reference catalogue, not a portfolio project"),
 ("","(your own project)","Own","","","","","","",""),
]
for i,rw in enumerate(PJ, start=2):
    for j,v in enumerate(rw, start=1):
        c=pj.cell(row=i,column=j,value=v); c.font=fnt(); c.alignment=WRAP; c.border=BORDER

# ---------------- Python checklist ----------------
py = wb.create_sheet("Python checklist")
header(py, ["Item","Source","Target date","Status"],[52,22,14,12])
chap = {12:"While loop",13:"Comprehensive challenges II",14:"Comments",15:"Functions",16:"Function arguments",17:"Lambdas",18:"Working with strings",19:"More about lists",20:"Handling exceptions",21:"Working with collections",22:"datetime module",23:"Decorators",24:"Classes and objects",25:"Inheritance",26:"Overloading operators",27:"Generators",28:"More about decorators",29:"Bitwise operators",30:"Creating and raising exceptions",31:"Iterators",32:"itertools",33:"Measuring code performance"}
cdate = {12:(9,24),13:(9,24),14:(9,24),15:(9,24),16:(9,25),17:(9,25),18:(9,26),19:(9,26),20:(9,27),21:(9,27),22:(9,28),23:(9,29),24:(9,28),25:(9,28),26:(10,12),27:(9,29),28:(9,29),29:(10,12),30:(9,30),31:(9,29),32:(10,13),33:(10,13)}
items = [(f"Ch {k}: {v}","BigBinary",D(2026,*cdate[k]),"Done" if False else "Not started") for k,v in chap.items()]
items += [
 ("Files, JSON, pathlib","Bridge topic",D(2026,10,1),"Not started"),
 ("IK Python for GenAI, part 1","IK pre-work",D(2026,10,1),"Not started"),
 ("Environment variables and .env","Bridge topic",D(2026,10,1),"Not started"),
 ("Calling an HTTP API (httpx)","Bridge topic",D(2026,10,2),"Not started"),
 ("IK Python for GenAI, part 2 (NumPy, pandas)","IK pre-work",D(2026,10,5),"Not started"),
 ("Type hints and pydantic","Bridge topic",D(2026,10,5),"Not started"),
 ("First LLM call from your own code (GenAI 06)","Microsoft",D(2026,10,6),"Not started"),
 ("git and GitHub: repo per project","Bridge topic",D(2026,10,9),"Not started"),
 ("Python checkpoint self-test","Playground",D(2026,10,10),"Not started"),
]
items.sort(key=lambda t:t[2])
for i,rw in enumerate(items, start=2):
    for j,v in enumerate(rw, start=1):
        c=py.cell(row=i,column=j,value=v); c.font=fnt(); c.border=BORDER
        if j==3: c.number_format="ddd dd mmm"
py.cell(row=len(items)+3,column=1,value="Ch 1-11 already done (41%). Ch 26, 29, 32, 33 moved after the 10 Oct deadline on purpose.").font=fnt(italic=True)


so = wb.create_sheet("Sources", 1)
header(so, ["Source","What it's for","Link","Where it appears in the plan"],[30,48,62,46])
SRC = [
 ("Interview Kickstart (Uplevel)","FDE program: live classes, slides, assignments, reviews",URL["IK"],"Every IK class, assignment and review block"),
 ("100x Engineers LMS","Cohort, code path: Fri and Sat classes, recordings",URL["X"],"Friday prep, 100x classes, recordings"),
 ("BigBinary Academy: Learn Python","Python fundamentals, ch 12-33 remaining",URL["BB"],"Python sprint to 10 Oct, ch 26/29/32/33 in W1"),
 ("Microsoft: Generative AI for Beginners","21 lessons; each block links to its lesson folder",URL["GENAI"],"Afternoon Learn blocks"),
 ("Microsoft: AI Agents for Beginners","18 lessons on Microsoft Agent Framework and Foundry",URL["AGENTS"],"Afternoon Learn blocks"),
 ("Google Colab","Python practice and drills",URL["COLAB"],"Practice blocks, checkpoint, DSA"),
 ("ai-weekend-builds (your fork)","15 weekend-sized AI builds",URL["WKND"],"Wednesday 5-7 reserve slot when no catch-up is needed"),
 ("500-AI-Agents-Projects (your fork)","Catalogue of agent use cases by industry",URL["500"],"Capstone idea scouting before 22 Nov"),
 ("Azure AI Search docs","Hybrid search and semantic ranker",URL["AZSEARCH"],"IK W7 Learn block"),
]
for i,rw in enumerate(SRC, start=2):
    for j,v in enumerate(rw, start=1):
        c=so.cell(row=i,column=j,value=v); c.font=fnt(); c.alignment=WRAP; c.border=BORDER
    c=so.cell(row=i,column=3); c.hyperlink=rw[2]; c.font=Font(name=F,size=10,color="1155CC",underline="single")
so.cell(row=len(SRC)+3,column=1,value="In the Daily plan, blue underlined tasks open their source when clicked.").font=fnt(italic=True)

wb.save("FDE_Learning_Plan.xlsx")
print(len(rows),"daily rows")
