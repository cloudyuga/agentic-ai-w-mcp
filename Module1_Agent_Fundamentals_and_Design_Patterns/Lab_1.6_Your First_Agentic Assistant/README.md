# 🤖 Module 1: Your First Agentic Assistant  

Welcome to the **start of your journey into agentic AI**!  
In this foundational module, we will **build a complete, intelligent HR Assistant** from the ground up.  

This is a **fresh start**, aligned with the latest **LangChain v1.0+ standards**, ensuring the skills you learn are **modern, robust, and production-ready**.  

💡 By the end of this module, you’ll have an **interactive assistant** that can **reason, use tools, and solve real-world HR problems**.  

---

## 🧠 What You'll Master in This Module  

This module is broken into **three focused labs**, each building on the last:  

### 🔹 Lab 1.1: Setting the Foundation *(Data & Tools)*  
- **Concept:** At the heart of any useful agent is its ability to access information and perform actions.  
- **Hands-on:**  
  - Define the agent’s knowledge base (`hr_data.py`)  
  - Build its capabilities (`hr_tools.py` using `@tool`)  
  - Test each tool independently  

---

### 🔹 Lab 1.2: Constructing the Agent  
- **Concept:** Learn the modern approach to building agents using `create_tool_calling_agent`.  
- **Hands-on:**  
  - Combine the 3 essential ingredients → **LLM + Prompt + Tools**  
  - Build the reasoning engine in `hr_agent.py`  
  - Wrap it inside an `AgentExecutor` to run the **Reason-Act loop**  

---

### 🔹 Lab 1.3: Creating an Interactive Experience  
- **Concept:** Agents shine when users can interact easily.  
- **Hands-on:**  
  - Build a **clean CLI interface** (`interactive_hr_agent.py`)  
  - Run interactive chat sessions with your HR Assistant  
  - Test its ability to **answer, reason, and solve multi-step problems**  

---

## 🚀 Getting Started  

📂 **File Structure**  
Ensure all lab files are in the **same directory** for smooth imports.  

🖊 **Open in Editor**  
Use **VS Code** (recommended) or any text editor.  

💻 **Run from Terminal**  
```bash
python interactive_hr_agent.py
