⚡ Lab 2.4: High-Performance Workflows with Asynchronous Execution

🎯 Learning Outcomes



By the end of this lab, you will:



✅ Understand the difference between sync vs async execution



✅ Learn how to structure workflows with Graph API and Functional API



✅ Run tasks in parallel to cut execution time



✅ Apply async patterns for real-world agent pipelines



🔹 Lab 2.4.1 — Sequential Execution (Sync vs Async)

Concept



async def defines a coroutine.



await suspends execution until the coroutine is done.



Sequential execution: tasks run one after the other, total time is the sum of all task durations.



.invoke() → synchronous entrypoints



.ainvoke() → asynchronous entrypoints



Example (Sequential)

import asyncio



async def parse\_resume(name: str):

&nbsp;   print(f"📄 Parsing resume for {name} (2s)...")

&nbsp;   await asyncio.sleep(2)

&nbsp;   print(f"   ✅ Resume parsed")



async def check\_background(name: str):

&nbsp;   print(f"🔍 Background check for {name} (3s)...")

&nbsp;   await asyncio.sleep(3)

&nbsp;   print(f"   ✅ Background complete")



async def check\_references(name: str):

&nbsp;   print(f"📞 Reference check for {name} (2s)...")

&nbsp;   await asyncio.sleep(2)

&nbsp;   print(f"   ✅ References complete")



async def sequential\_screening(name: str):

&nbsp;   print(f"\\n🎯 Sequential screening for {name}")

&nbsp;   start = asyncio.get\_running\_loop().time()

&nbsp;   

&nbsp;   await parse\_resume(name)

&nbsp;   await check\_background(name)

&nbsp;   await check\_references(name)

&nbsp;   

&nbsp;   total = asyncio.get\_running\_loop().time() - start

&nbsp;   print(f"\\n⏱️  Sequential Total Time: {total:.1f} seconds")

&nbsp;   print("Expected ≈ 2s + 3s + 2s = 7s")



asyncio.run(sequential\_screening("Alice Johnson"))



🔹 Lab 2.4.2 — Parallel Execution with Async

Concept



Independent tasks can run at the same time.



Graph API: parallel edges = parallel execution.



Functional API: use asyncio.gather() for concurrency.



Runtime is total of longest branch, not sum.



1️⃣ Graph API Parallelism

from typing import TypedDict

from langgraph.graph import StateGraph, START, END



class CandidateState(TypedDict):

&nbsp;   name: str



async def parse\_resume(state: CandidateState):

&nbsp;   print(f"📄 Parsing resume for {state\['name']} (2s)...")

&nbsp;   await asyncio.sleep(2)

&nbsp;   print("   ✅ Resume parsed")

&nbsp;   return {}



async def background\_check(state: CandidateState):

&nbsp;   print(f"🔍 Background check (3s)...")

&nbsp;   await asyncio.sleep(3)

&nbsp;   print("   ✅ Background check complete")

&nbsp;   return {}



async def reference\_check(state: CandidateState):

&nbsp;   print(f"📞 Reference check (2s)...")

&nbsp;   await asyncio.sleep(2)

&nbsp;   print("   ✅ References complete")

&nbsp;   return {}



async def decision(state: CandidateState):

&nbsp;   print(f"📋 Final decision for {state\['name']}...")

&nbsp;   return {"decision": "HIRED"}



def build\_graph():

&nbsp;   g = StateGraph(CandidateState)

&nbsp;   g.add\_node("parse", parse\_resume)

&nbsp;   g.add\_node("background", background\_check)

&nbsp;   g.add\_node("references", reference\_check)

&nbsp;   g.add\_node("decide", decision)



&nbsp;   g.add\_edge(START, "parse")

&nbsp;   g.add\_edge("parse", "background")

&nbsp;   g.add\_edge("parse", "references")

&nbsp;   g.add\_edge("background", "decide")

&nbsp;   g.add\_edge("references", "decide")

&nbsp;   g.add\_edge("decide", END)

&nbsp;   return g.compile()



async def run\_graph():

&nbsp;   graph = build\_graph()

&nbsp;   start = asyncio.get\_running\_loop().time()

&nbsp;   await graph.ainvoke({"name": "Bob Lee"})

&nbsp;   total = asyncio.get\_running\_loop().time() - start

&nbsp;   print(f"\\n⏱️ Graph Parallel Total Time: {total:.1f} seconds (Expected ~5s)")



asyncio.run(run\_graph())



2️⃣ Functional API Parallelism

from langgraph.func import entrypoint, task



@task

async def parse\_resume\_task(name: str):

&nbsp;   print(f"📄 Parsing resume for {name} (2s)...")

&nbsp;   await asyncio.sleep(2)

&nbsp;   print("   ✅ Resume parsed")

&nbsp;   return {"parsed": True}



@task

async def background\_task(name: str):

&nbsp;   print(f"🔍 Background check (3s)...")

&nbsp;   await asyncio.sleep(3)

&nbsp;   print("   ✅ Background complete")

&nbsp;   return {"status": "Clear"}



@task

async def reference\_task(name: str):

&nbsp;   print(f"📞 Reference check (2s)...")

&nbsp;   await asyncio.sleep(2)

&nbsp;   print("   ✅ References complete")

&nbsp;   return {"status": "Positive"}



@entrypoint

async def screen\_candidate(name: str):

&nbsp;   print(f"\\n🎯 Functional API screening for {name}")

&nbsp;   await parse\_resume\_task(name)



&nbsp;   # Run in parallel

&nbsp;   background, reference = await asyncio.gather(

&nbsp;       background\_task(name),

&nbsp;       reference\_task(name)

&nbsp;   )



&nbsp;   print(f"📋 Final decision for {name}...")

&nbsp;   return f"HIRED - Background: {background\['status']}, Refs: {reference\['status']}"



async def run\_func():

&nbsp;   start = asyncio.get\_running\_loop().time()

&nbsp;   await screen\_candidate.ainvoke("Clara Smith")

&nbsp;   total = asyncio.get\_running\_loop().time() - start

&nbsp;   print(f"\\n⏱️ Functional Parallel Total Time: {total:.1f} seconds (Expected ~5s)")



asyncio.run(run\_func())



📊 Expected Timing Results



Sequential: ≈ 7s



Parallel (Graph \& Functional): ≈ 5s



✅ You save 2 seconds with parallelism.

That’s the power of async execution.



🖼️ Visual Comparison



Sequential Flow



graph TD

&nbsp;   A\[Parse Resume 2s] --> B\[Background Check 3s] --> C\[Reference Check 2s] --> D\[Decision]





Parallel Flow



graph TD

&nbsp;   A\[Parse Resume 2s] --> B\[Background Check 3s]

&nbsp;   A --> C\[Reference Check 2s]

&nbsp;   B --> D\[Decision]

&nbsp;   C --> D



🎯 Why This Matters



Sequential execution → safer when tasks depend on each other.



Parallel execution → critical for independent I/O-bound tasks.



Hybrid models → combine both for real-world scalability.



By mastering these async patterns, you’re ready to design production-grade AI agents 🚀.

