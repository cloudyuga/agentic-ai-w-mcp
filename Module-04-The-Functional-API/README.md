
````markdown
# 🐍 Module 4: The Functional API  
## Building Workflows with Native Python

Welcome to **Module 4**!  
Here, you'll explore a more **Pythonic**, **readable**, and **flexible** way to build interactive, stateful, and resilient workflows — the **Functional API** in LangGraph.

---

### 🧠 Why Use the Functional API?

Forget manually wiring nodes and edges. With decorators like `@task` and `@entrypoint`, and familiar Python control flow (`if`, `else`, loops), you can:

✨ Write clean, intuitive code  
⚡ Rapidly prototype ideas  
🔁 Integrate natural control flow  
💡 Keep everything Python-native  

---

## 🚀 What You’ll Learn

By the end of this module, you’ll be able to:

---

✅ **Checkpointed Workflows**  
Use `@entrypoint` and `@task` to build **resumable** workflows that avoid repeating expensive steps.

✅ **Human-in-the-Loop Execution**  
Pause workflows with `interrupt()` for human feedback or approvals, then resume seamlessly.

✅ **Natural Control Flow**  
Replace complex graphs with simple `if/else`, loops, and Python functions.

✅ **API Comparison Mastery**  
Understand when to use the **Functional API** vs the **Graph API** — and how to blend both when needed.

---

## 🧪 Labs Included

Each lab is self-contained, runnable in Google Colab, and focuses on real-world patterns.

```bash
📁 Module-04-The-Functional-API/
│
├── 🧪 lab_1_entrypoint_and_task.py
├── 🧪 lab_2_human_in_the_loop_interrupt.py
├── 🧪 lab_3_multi_stage_approval.py
├── 🧪 lab_4_api_comparison.py
│
└── 📘 README.md ← You are here!
````

---

## ⚙️ Getting Started

### 1️⃣ Run in Google Colab

> 💡 Use "Open in Colab" badges (below) or upload labs to Colab manually.

### 2️⃣ Add Your OpenAI API Key

Before running the labs, add your key:

* Go to **Colab → Settings → Secrets**
* Add a key named `OPENAI_API_KEY`
* Paste your OpenAI key as the value

### 3️⃣ Run Cells Top to Bottom

Execute cells **sequentially** in each lab for smooth execution.

---

## 🧰 Requirements

Install the required dependencies:

```bash
pip install langgraph openai
```

---

## 🧭 When to Use the Functional API

| Use Case                      | Functional API ✅ | Graph API ✅  |
| ----------------------------- | ---------------- | ------------ |
| Simple control flow (if/else) | ✅ Natural fit    | 🚫 Overkill  |
| Human-in-the-loop needed      | ✅ Easy interrupt | ⚠️ Manual    |
| Visual graph modeling         | 🚫 Not visual    | ✅ Graph view |
| Complex state machines        | 🚫 Limited       | ✅ Ideal      |

---

## ✅ Outcome

After completing this module, you'll confidently:

* ✅ Build **resilient, checkpointed** workflows
* ✅ Integrate **humans into AI pipelines**
* ✅ Write elegant, Pythonic logic in LangGraph
* ✅ Choose between **Functional** and **Graph API** like a pro

---

## 📸 Want to See a Graph?

If you're working with the Graph API, many labs include a visual:

```python
graph_workflow.visualize("graph.png")
```

> 🔍 To view in Colab:

```python
from IPython.display import Image
Image("graph.png")
```

---

## 🔗 Open in Google Colab

| Lab                            | Open Link                                                                                                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Lab 1: `@entrypoint` & `@task` | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo/blob/main/Module-04-The-Functional-API/lab_1_entrypoint_and_task.py)         |
| Lab 2: Human-in-the-Loop       | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo/blob/main/Module-04-The-Functional-API/lab_2_human_in_the_loop_interrupt.py) |
| Lab 3: Multi-stage Approval    | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo/blob/main/Module-04-The-Functional-API/lab_3_multi_stage_approval.py)        |
| Lab 4: Functional vs Graph     | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-repo/blob/main/Module-04-The-Functional-API/lab_4_api_comparison.py)              |
