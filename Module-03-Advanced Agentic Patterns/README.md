<h1 align="center">🧠 Module 3: Advanced Agentic Patterns</h1>
<h3 align="center">From Workflows ➡️ to Autonomy with LangGraph</h3>

<p align="center">
  <img src="https://img.shields.io/badge/LangGraph-Advanced-blue" />
  <img src="https://img.shields.io/badge/Level-Intermediate%20to%20Advanced-orange" />
  <img src="https://img.shields.io/badge/Open%20In-Google%20Colab-brightgreen" />
</p>

---

Welcome to **Module 3** of _"Practical Agentic AI with LangGraph"_!  
In this module, we move beyond basic LangGraph usage and dive into designing **intelligent, autonomous systems** capable of complex reasoning, self-correction, and dynamic decision-making.

---

## 🚀 What You’ll Learn

By the end of this module, you’ll have hands-on experience building:

| 🧩 Pattern                        | 💡 Description                                                                 |
|----------------------------------|-------------------------------------------------------------------------------|
| ✅ **Complex Workflows**         | Implement patterns like chaining, parallelization, smart routing, and orchestrator-worker models. |
| ✅ **Self-Correcting Loops**     | Create workflows that refine their own outputs through evaluation and iteration. |
| ✅ **Autonomous Agents**         | Build agents that dynamically select tools, reason about tasks, and adapt in real-time. |
| ✅ **Workflow vs. Agent Design** | Learn when to choose predictable workflows vs. adaptive, autonomous approaches. |

---

## 🧪 Labs Overview

Each lab is standalone, beginner-friendly, and builds on the core concepts from earlier modules:

```plaintext
📁 Module-03-Advanced-Agentic-Patterns/
│
├── 📄 lab_1_prompt_chaining.py              → Build linear prompt-based chains
├── 📄 lab_2_parallel_evaluation.py          → Evaluate multiple tools in parallel
├── 📄 lab_3_smart_routing.py                → Route inputs based on context
├── 📄 lab_4_orchestrator_worker.py          → Use modular orchestrator/worker design
├── 📄 lab_5_self_correcting_workflow.py     → Add quality checks and feedback loops
├── 📄 lab_6_autonomous_agent.py             → Implement an adaptive, autonomous agent
├── 📄 lab_7_workflow_vs_agent_comparison.py → Compare workflows vs. agents in practice
└── 📄 README.md                             ← You are here!
⚙️ Getting Started
1️⃣ Open in Google Colab
🟢 No installation required!

To run a lab:

Click on any .py file in this module

Select “Open in Colab” from the options

2️⃣ Set Up Your OpenAI API Key
You'll need an OpenAI API key to run the labs:

Go to platform.openai.com/api-keys

Copy your API key

In Colab, click the 🗝️ Secrets icon in the left sidebar

Add a new secret:

vbnet
Copy code
Name:  OPENAI_API_KEY  
Value: [Paste your API key here]
Enable the Notebook Access toggle

3️⃣ Run the Labs
Each notebook is self-contained and should be executed top to bottom.
👉 Start from Lab 1 and move sequentially for the best experience.

🤝 Contributing & Support
We welcome all feedback and contributions!

🐞 Found a bug? → Open an issue

🙋 Need help? → Use our issue templates

⭐ Enjoying the course? → Star the repo and share with your network!

🛠️ Built With
Tool	Role in the Project
🔁 LangGraph	Framework for building stateful, agentic systems
🧱 LangChain	Language model abstraction & integration
🧠 OpenAI API	Powers the agent's intelligence
☁️ Google Colab	Interactive cloud-based development
