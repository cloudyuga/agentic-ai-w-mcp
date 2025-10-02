# 🚀 Lab 2.5 — Advanced Workflow Control

[![Colab](https://img.shields.io/badge/Open-in%20Colab-4285F4?logo=googlecolab&logoColor=white)](https://colab.research.google.com/) [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![SQLite](https://img.shields.io/badge/SQLite-persistent-orange)]() [![License](https://img.shields.io/badge/License-MIT-green.svg)]

> **Lab 2.5** moves beyond basic graphs to teach you production-grade workflow patterns: persistence, human-in-the-loop, time travel, streaming execution, conversational memory, subgraphs, and integrated systems.

---

## 📚 Table of Contents
1. [What you'll master](#-what-youll-master)  
2. [Quick visual overview](#-quick-visual-overview)  
3. [Labs (expandable)](#-labs-expandable)  
4. [Getting started (Colab / Local)](#-getting-started-colab--local)  
5. [Tips & best practices](#-tips--best-practices)  
6. [Contributing & License](#-contributing--license)

---

## 🧠 What you'll master
This module teaches the core operational skills to make agentic systems reliable, debuggable, and auditable:

- **Durable Persistence** — Save workflow state (SQLite) so execution survives restarts.  
- **Human-in-the-Loop** — Pause workflows, collect approvals/inputs, resume safely.  
- **Time Travel & Debugging** — Inspect any checkpoint in the timeline for audit & debugging.  
- **Streaming Real-Time Updates** — Get node-by-node execution output as the graph runs.  
- **Conversational Memory** — Appendable message histories for robust chat agents.  
- **Subgraphs & Modularity** — Build reusable subgraphs for complex logic.  
- **Integrated Systems** — Combine the above into a multi-stage, production-style workflow.

---

## 🗺️ Quick visual overview

flowchart TD
  Start([START]) --> Persistence[SQLite<br/>Checkpointer]
  Persistence --> Screening[Initial Screening]
  Screening --> HR(HR Approval ↺ pause)
  HR --> Verification[Verification Subgraph]
  Verification --> Manager(Manager Approval ↺ pause)
  Manager --> Decision[Final Decision]
  Decision --> End([END])

  subgraph Subgraph ["Verification Subgraph"]
    Exp(Experience Check) --> Skills(Skills Check)
  end
🔎 Labs (click to expand)
<details> <summary><strong>Lab 2.5.1 — Durable Persistence</strong> (click to expand)</summary>
Goal: Persist workflow state to SQLite so progress survives process restarts.

Key APIs: langgraph.checkpoint.sqlite.SqliteSaver, workflow.compile(checkpointer=...)

What you do:

Install a SQLite checkpointer.

Run workflow and confirm checkpoints are written.

Restart process and resume() from saved checkpoint.

Expected outcome: Your workflows persist state and can be resumed reliably.

</details> <details> <summary><strong>Lab 2.5.2 — Human-in-the-Loop</strong></summary>
Goal: Pause a workflow, ask for a human decision, then resume.

Key APIs: interrupt_before, app.update_state(...), app.invoke(None, config=...)

What you do:

Mark nodes as interrupt_before to pause.

Use update_state to inject a human decision.

Resume execution and verify the branch taken.

Expected outcome: Controlled, auditable pause → human approval → resume.

</details> <details> <summary><strong>Lab 2.5.3 — Time Travel & Debugging</strong></summary>
Goal: Inspect any checkpoint in the timeline to debug or audit past states.

Key APIs: The checkpointer methods (e.g., memory.list(...), memory.get(...))

What you do:

Run a workflow that creates multiple checkpoints.

Use the checkpointer to list checkpoint entries and inspect their saved states (timestamp, values, history).

Expected outcome: A chronological, queryable history of workflow states.

</details> <details> <summary><strong>Lab 2.5.4 — Streaming Real-Time Updates</strong></summary>
Goal: Receive node-level updates as the graph executes instead of waiting for the final result.

Key APIs: .stream() (or equivalent streaming API the framework exposes)

What you do:

Run the graph in stream mode and display node outputs as they happen.

Validate that long-running nodes produce timely logs/updates.

Expected outcome: Immediate feedback for long-running graphs.

</details> <details> <summary><strong>Lab 2.5.5 — Managing Conversational Memory</strong></summary>
Goal: Append conversation messages to state safely and build a persistent chat history.

Key APIs: typing.Annotated + operator.add to enable append semantics for list fields.

What you do:

Use an Annotated messages field to append Human/AI messages.

Validate that repeated invokes build a rich conversation log.

Expected outcome: Stateful chat that grows a conversation history, persisted across sessions.

</details> <details> <summary><strong>Lab 2.5.6 — Building with Subgraphs</strong></summary>
Goal: Encapsulate complex logic in a subgraph you can call from a parent graph.

Key APIs: workflow.compile() + subgraph.invoke(sub_input)

What you do:

Create a verification subgraph (experience → skills).

Call it from a main hiring workflow and collect the returned report.

Expected outcome: Cleaner, reusable modules and simpler parent workflows.

</details> <details> <summary><strong>Lab 2.5.7 — The Integrated System</strong></summary>
Goal: Combine persistence, interrupts, subgraphs, streaming, and memory in a multi-stage hiring pipeline.

What you do:

Build a multi-step flow: screening → HR approval (interrupt) → verification subgraph → manager approval (interrupt) → final decision.

Persist state to SQLite, stream logs, and allow time travel through checkpoints.

Expected outcome: Production-ready demonstration of advanced workflow control.

</details>
▶️ Getting started (Colab / Local)
Quick install

bash
Copy code
# Run in Colab / local environment
pip install langgraph langchain_core==0.1.52
Minimal snippet (run in a notebook cell)

python
Copy code
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver

# Define a tiny workflow
def hello(state: dict)->dict:
    print("Hello world!")
    return {}

workflow = StateGraph(dict)
workflow.add_node("hello", hello)
workflow.add_edge(START, "hello")
workflow.add_edge("hello", END)

memory = SqliteSaver.from_conn_string(":memory:")
app = workflow.compile(checkpointer=memory)
app.invoke({}, config={"configurable": {"thread_id": "demo-1"}})
Colab tips

If you run async code in Colab, install & apply nest_asyncio.

Set OPENAI_API_KEY in Colab secrets if future labs require LLM access.

💡 Tips & best practices
Start functional, switch to graph for complexity. Functional = fast prototyping; Graph = explicit control & loops.

Always use configurable for checkpoint keys (e.g. {"configurable": {"thread_id": "xxx"}}) when using checkpointers.

Use Annotated + operator.add for appendable fields (conversation lists).

Use streaming for observability in long-running graphs.

Keep subgraphs small & focused so they remain reusable and testable.

🤝 Contributing & License
Feel free to open PRs & issues. This repository is licensed under the MIT License — adapt freely for labs and demos.

If you want, I can:

add an "Open in Colab" badge that links to a runnable notebook,

embed a runnable code block demonstrating interrupt_before + update_state, or

produce a matching lab-2.5 Jupyter notebook you can drop into Colab.

Which of those would you like next? 🚀
