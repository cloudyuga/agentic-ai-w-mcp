🐍 The Functional API: Writing Workflows like Pure Python

Welcome to the Functional API—LangGraph's most intuitive and Python-native way to build powerful, stateful, and resumable workflows. Forget about graphs, nodes, and edges for a moment. If you can write a Python script, you can build a production-ready agentic workflow.



🤔 What is the Functional API? The Supercharged Script Analogy

Imagine you have a regular Python script. It's a series of steps, calling one function after another.



Now, what if you could give that script superpowers?



A "Save Game" Feature: The ability to save its progress at any step.



A "Pause" Button: The ability to stop and wait for a human to make a decision.



Automatic Memory: The ability to remember the results of expensive steps so it never has to do them twice.



This is exactly what the Functional API does. It lets you write normal-looking Python code and then "supercharges" it with decorators.



⭐ The Core Components: Decorators as Superpowers

The Functional API is built on three simple decorators:



Decorator



Superpower



Analogy



@entrypoint



Makes it a Workflow



The main entrance to your building. It's the one door that turns a simple script into a managed, stateful process.



@task



Adds Checkpoints



A save point in a video game. It saves the result of an expensive or slow function. If the workflow resumes, it loads from this point instead of re-running it.



interrupt()



Adds a Pause Button



The waiter asking, "Are you ready to order?" The entire kitchen (workflow) pauses until you give your answer.



🚀 How It Works: A Practical Example

Let's build a simple HR screening workflow using this natural style. Notice how it reads just like a standard script.



from langgraph.func import entrypoint, task, interrupt

from langgraph.checkpoint.memory import MemorySaver

from langgraph.types import Command



\# Superpower 1: This is a checkpoint-able "save point"

@task

def extract\_skills\_from\_resume(resume\_text: str) -> list\[str]:

&nbsp;   print("📋 TASK: Extracting skills (expensive operation)...")

&nbsp;   # ... (imagine a costly API call here)

&nbsp;   skills = \[skill.title() for skill in \["python", "java"] if skill in resume\_text.lower()]

&nbsp;   return skills



\# Superpower 2: This is the main entrance to our stateful workflow

@entrypoint(checkpointer=MemorySaver())

def screen\_candidate(resume: str) -> str:

&nbsp;   print(f"\\n🎯 WORKFLOW: Screening candidate...")



&nbsp;   # Call the task just like a normal function

&nbsp;   skills = extract\_skills\_from\_resume(resume)

&nbsp;   score = len(skills) \* 50



&nbsp;   print(f"   AI Score: {score}/100")



&nbsp;   # Superpower 3: This is the pause button

&nbsp;   print("⏸️  WORKFLOW: Pausing for HR approval...")

&nbsp;   hr\_approval = interrupt("Proceed with this candidate? (yes/no)")



&nbsp;   # The workflow resumes here after the human responds

&nbsp;   print(f"✅ WORKFLOW: Resumed with HR decision: '{hr\_approval}'")

&nbsp;   if hr\_approval == "yes":

&nbsp;       return f"Approved! (AI Score: {score})"

&nbsp;   else:

&nbsp;       return "Rejected by HR."



\# --- Let's run it ---

\# 1. Run until it pauses

screen\_candidate.invoke(

&nbsp;   "Experienced Python developer",

&nbsp;   config={"thread\_id": "candidate\_001"}

)



\# 2. Provide the human input to resume

final\_result = screen\_candidate.invoke(

&nbsp;   None, # No new input needed

&nbsp;   config={"thread\_id": "candidate\_001"},

&nbsp;   resume=Command(resume="yes")

)

print(f"\\nFinal Result: {final\_result}")



This code is intuitive, easy to read, and you get checkpointing and human-in-the-loop capabilities almost for free!

