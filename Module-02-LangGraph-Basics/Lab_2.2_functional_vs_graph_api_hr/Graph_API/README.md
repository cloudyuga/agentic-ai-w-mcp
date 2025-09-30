🗺️ The Graph API: The Architect's Toolkit for Precision Control

Welcome to the Graph API. This is LangGraph's foundational and most explicit way to build agentic systems. If the Functional API is like writing a script, the Graph API is like being an architect with a blueprint, designing a complex system with full control over every component and connection.



🤔 What is the Graph API? The Subway Map Analogy

Imagine you are designing a city's subway system. The Graph API gives you a blank map and a set of tools to build it from the ground up. You are the chief architect.



StateGraph(State) (The Blueprint): You must first declare a formal blueprint for all the data that will travel through your system. This is your TypedDict state.



add\_node() (The Stations): You place every station on the map yourself. Each station (node) is a specific function where a task is performed.



add\_edge() (The Tracks): You lay the tracks between the stations, defining the exact, unchangeable path the subway cars (data) will follow.



add\_conditional\_edges() (The Track Switches): You install smart switches at intersections. These switches check the subway car's "ticket" (the state) and route it down the correct track based on a set of rules you've written.



This approach gives you the power to create incredibly complex, reliable, and visualizable systems with loops, branches, and guaranteed paths.



🚀 How It Works: Architecting the Same Workflow

Let's build the exact same HR screening workflow from the Functional API example, but this time using the architect's tools.



from langgraph.graph import StateGraph, START, END

from langgraph.checkpoint.memory import MemorySaver

from langgraph.types import interrupt, Command

from typing import TypedDict



\# Step 1: The Blueprint (Define the State)

class CandidateState(TypedDict):

&nbsp;   resume: str

&nbsp;   skills: list\[str]

&nbsp;   score: int

&nbsp;   hr\_approval: str

&nbsp;   decision: str



\# Step 2: The Stations (Define the Node Functions)

def extract\_skills\_node(state: CandidateState) -> dict:

&nbsp;   print("📋 NODE: Extracting skills...")

&nbsp;   skills = \[s.title() for s in \["python", "java"] if s in state\["resume"].lower()]

&nbsp;   score = len(skills) \* 50

&nbsp;   return {"skills": skills, "score": score}



def approval\_node(state: CandidateState) -> dict:

&nbsp;   print(f"   AI Score: {state\['score']}/100")

&nbsp;   print("⏸️  NODE: Pausing for HR approval...")

&nbsp;   hr\_response = interrupt("Proceed with this candidate? (yes/no)")

&nbsp;   return {"hr\_approval": hr\_response}



def final\_decision\_node(state: CandidateState) -> dict:

&nbsp;   print(f"✅ NODE: Resumed with HR decision: '{state\['hr\_approval']}'")

&nbsp;   if state\["hr\_approval"] == "yes":

&nbsp;       return {"decision": f"Approved! (AI Score: {state\['score']})"}

&nbsp;   else:

&nbsp;       return {"decision": "Rejected by HR."}



\# Step 3: The Assembly (Build the Graph)

workflow = StateGraph(CandidateState)

workflow.add\_node("extract\_skills", extract\_skills\_node)

workflow.add\_node("await\_approval", approval\_node)

workflow.add\_node("make\_decision", final\_decision\_node)



workflow.set\_entry\_point("extract\_skills")

workflow.add\_edge("extract\_skills", "await\_approval")

workflow.add\_edge("await\_approval", "make\_decision")

workflow.add\_edge("make\_decision", END)



app = workflow.compile(checkpointer=MemorySaver())



\# --- Let's run it ---

\# (The invocation is identical to the Functional API example)



Notice the key difference: every single component and connection is explicitly defined. This gives you unparalleled clarity and control over the workflow's structure.

