🐍 Module 4: The Functional API
Building Workflows with Native Python
Welcome to Module 4! In this section, we unlock a more intuitive and Python-native way to build stateful, resilient, and interactive workflows: the Functional API.

Instead of manually defining nodes and edges, we will use simple decorators (@entrypoint, @task) and familiar Python control flow (if/else, loops) to construct powerful applications. This approach allows you to write code that is easier to read, faster to prototype, and more natural for Python developers.

🚀 What You'll Master in This Module
This module is designed to make you proficient in creating production-ready workflows with minimal boilerplate. By the end, you'll be able to:

✅ Build Checkpointed Workflows: Use @entrypoint and @task to create resilient workflows that save their progress, saving time and money by not re-running expensive operations.
✅ Implement Human-in-the-Loop: Master the interrupt() function to pause a workflow, wait for human approval or feedback, and seamlessly resume execution.
✅ Use Natural Control Flow: Implement complex branching logic using standard Python if/else statements instead of explicit conditional edges.
✅ Compare API Styles: Gain a deep understanding of the trade-offs between the Functional API and the Graph API, enabling you to choose the right tool for any job.

🗂️ Labs in This Module
All labs are code-only, self-contained, and designed to be run in Google Colab.

📁 Module-04-The-Functional-API/
│
├── 📄 lab_1_entrypoint_and_task.py
├── 📄 lab_2_human_in_the_loop_interrupt.py
├── 📄 lab_3_multi_stage_approval.py
├── 📄 lab_4_api_comparison.py
│
└── 📄 README.md  ← You're here!

🚀 Getting Started
Open in Google Colab: The easiest way to run these labs is to open them directly in Google Colab.

Set Your OpenAI API Key: Before running, add your OpenAI API key to the Colab Secrets manager with the name OPENAI_API_KEY.

Run Sequentially: Execute the cells in each notebook from top to bottom.