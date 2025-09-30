# 🐍 The Functional API: Writing Workflows like a Python Pro  

Welcome to the **Functional API**—the most **intuitive** and **Python-native** way to build powerful, stateful workflows in LangGraph.  

This approach is designed for developers who love the simplicity and power of writing regular Python code, without needing to learn a new DSL.  

---

## 🏛️ The Core Idea  

Instead of learning a complex graph-building language, you write **normal Python functions** and give them superpowers with special decorators:  

- **`@entrypoint`** → The **main Recipe Card** – defines the entire dish from start to finish.  
- **`@task`** → Your **Mise en Place steps** – reusable, checkpointed steps (chop once, reuse forever).  
- **`interrupt()`** → The **taste test** – pause execution and wait for feedback before continuing.  

> 🧑‍🍳 **Analogy:** Think of the Functional API like writing a recipe.  
> - Sequential steps you already know (Python code)  
> - Clear, intuitive, and checkpointed  
> - Easy to pause and resume  

---

## 🚀 How It Works: A Code-First Look  

Here’s a simple **interview workflow** that routes candidates based on experience level:  

```python
from langgraph.func import entrypoint, task
from langgraph.checkpoint.memory import MemorySaver

# TASK: A checkpointed "prep step"
@task
def analyze_experience(resume: str) -> str:
    """Determine experience level. This result will be saved."""
    print("📊 Analyzing experience level...")
    if "senior" in resume.lower(): return "senior"
    if "mid-level" in resume.lower(): return "mid"
    return "junior"

# TASK: Another prep step
@task
def senior_process() -> str:
    """The specific process for senior candidates."""
    print("👔 Routing to Senior Interview Process...")
    return "Senior interview scheduled"

# ENTRYPOINT: The main recipe
@entrypoint(checkpointer=MemorySaver())
def route_interview(resume: str) -> str:
    """
    Main workflow – calls tasks and uses Python control flow
    to make decisions.
    """
    print(f"\n🎯 Processing candidate...")
    
    # 1. Analyze experience
    level = analyze_experience(resume)
    
    # 2. Route with simple if/else logic
    if level == "senior":
        result = senior_process()
    elif level == "mid":
        result = "Mid-level interview scheduled"
    else:
        result = "Junior interview scheduled"
    
    print(f"✅ Decision: {result}")
    return result

# --- Running the Workflow ---
route_interview.invoke("A senior software architect with 10 years experience.")
````

---

## ✨ Key Superpowers of the Functional API

| Superpower                               | What It Means                                                                                            |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Checkpointing with `@task`**           | Any function decorated with `@task` becomes a **save point**. Results are cached & reused automatically. |
| **Human-in-the-Loop with `interrupt()`** | Pause the workflow, wait for input, then seamlessly resume execution.                                    |
| **Code Reuse**                           | Tasks can be reused across workflows like ingredients in multiple recipes.                               |
| **Native Python Control Flow**           | Use `if/else`, `for`, `while` loops directly—no extra syntax.                                            |

### Example: Human-in-the-Loop

```python
# Pause the workflow and wait for HR input
hr_approval = interrupt("Should we proceed? (yes/no)")

# Execution continues AFTER the human responds
if hr_approval == "yes":
    print("✅ Proceeding with the interview process...")
else:
    print("❌ Interview halted by HR.")
```

---

## ✅ When Should You Use the Functional API?

The **Functional API** is your best starting point and is perfect when:

* 🐍 **You Prefer Python** → Logic looks & feels like a standard Python script.
* 📖 **Readability is Key** → Any Python dev can read & understand it instantly.
* ⚡ **Rapid Prototyping** → Get a working, stateful workflow running in minutes.
* 🔀 **Simple Control Flow** → If your logic fits within `if/else`, `for`, or `while`.

---

## 🎯 TL;DR

The Functional API is like a **Chef’s Recipe**:

* Simple ingredients (Python functions)
* Easy-to-follow steps (sequential logic)
* Superpowers (checkpointing, interrupts, human-in-the-loop)

Start here if you want to **build quickly, read clearly, and scale naturally**. 🚀

```
