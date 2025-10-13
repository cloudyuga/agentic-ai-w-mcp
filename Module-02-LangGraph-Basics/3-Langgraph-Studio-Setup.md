# 🚀 LangGraph Studio 1.0 (Alpha) - Local Setup Guide

Complete instructions for running LangGraph Studio v1.0-alpha locally on **Mac**, **Windows**, and **Linux**.

---

## 📋 Prerequisites

### All Platforms
- **Python 3.10+** (3.11 or 3.12 recommended)
- **pip** (Python package manager)
- **API Keys**:
  - [LangSmith API Key](https://smith.langchain.com/settings) (free signup)
  - [OpenAI API Key](https://platform.openai.com)

### Platform-Specific Requirements

#### **macOS**
- Xcode Command Line Tools (install with: `xcode-select --install`)
- Homebrew (optional, for Python installation)

#### **Windows**
- Microsoft C++ Build Tools (usually included with Python installer)
- Windows Terminal (recommended for better experience)

#### **Linux**
- build-essential package: `sudo apt-get install build-essential` (Ubuntu/Debian)
- python3-dev: `sudo apt-get install python3-dev` (Ubuntu/Debian)

---

## 🔧 Step 1: Check Python Installation

Open your terminal/command prompt and verify Python is installed:

```bash
python --version
# or
python3 --version
```

You should see Python 3.10 or higher.

### Installing Python (if needed)

**macOS:**
```bash
# Using Homebrew
brew install python@3.11
```

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during installation

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

---

## 📁 Step 2: Create Project Directory

**All Platforms:**
```bash
# Create and navigate to project directory
mkdir langgraph-studio
cd langgraph-studio
```

---

## 🌐 Step 3: Create Virtual Environment

### Option A: Using venv (Recommended)

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

*If you get an execution policy error on Windows PowerShell:*
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Option B: Using Conda

**All Platforms:**
```bash
conda create -n langgraph python=3.11
conda activate langgraph
```

### Verify Virtual Environment

You should see `(venv)` or `(langgraph)` at the start of your terminal prompt.

---

## 📦 Step 4: Install LangGraph 1.0 Alpha

**All Platforms:**
```bash
# Upgrade pip first
pip install --upgrade pip

# Install LangGraph 1.0 alpha and dependencies
pip install --pre -U langgraph langchain-openai langchain-core "langgraph-cli[inmem]"


# Verify installation
langgraph --version
```

---

## 🛠️ Step 5: Create Project Structure

### Create the Agent File

**All Platforms:**
```bash
# Create a file named agent.py
touch agent.py  # macOS/Linux
# or
type nul > agent.py  # Windows CMD
# or
New-Item agent.py  # Windows PowerShell
```

Now open `agent.py` in your favorite text editor and paste:

```python
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition

def create_agent():
    """Create a simple LangGraph v1.0 agent with tools"""
    
    # Define simple tools
    def get_weather(location: str) -> str:
        """Get the weather for a location.
        
        Args:
            location: The city or location to get weather for
        """
        weather_data = {
            "san francisco": "Foggy and 55°F",
            "new york": "Sunny and 68°F",
            "london": "Rainy and 52°F",
            "tokyo": "Clear and 72°F"
        }
        location_lower = location.lower()
        return weather_data.get(location_lower, f"The weather in {location} is sunny and 70°F")
    
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
        """
        return a * b
    
    def calculate_area(radius: float) -> float:
        """Calculate the area of a circle.
        
        Args:
            radius: The radius of the circle
        """
        import math
        return math.pi * radius ** 2
    
    tools = [get_weather, multiply, calculate_area]
    
    # Create LLM with tools
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm_with_tools = llm.bind_tools(tools)
    
    # Define the agent node
    def call_model(state: MessagesState):
        response = llm_with_tools.invoke(state["messages"])
        return {"messages": [response]}
    
    # Build the graph
    builder = StateGraph(MessagesState)
    
    # Add nodes
    builder.add_node("agent", call_model)
    builder.add_node("tools", ToolNode(tools))
    
    # Add edges
    builder.add_edge(START, "agent")
    builder.add_conditional_edges("agent", tools_condition)
    builder.add_edge("tools", "agent")
    
    # Compile and return
    return builder.compile()
```

---

## ⚙️ Step 6: Create Configuration File

Create a file named `langgraph.json`:

```json
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:create_agent"
  },
  "env": ".env"
}
```

---

## 🔑 Step 7: Set Up Environment Variables

Create a file named `.env` in your project directory:

**All Platforms:**

```bash
# .env file content
LANGSMITH_API_KEY=lsv2_pt_your_key_here
OPENAI_API_KEY=sk-your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langgraph-local
```

**Replace the placeholder values with your actual API keys!**

### Quick way to create .env file:

**macOS/Linux:**
```bash
cat > .env << 'EOF'
LANGSMITH_API_KEY=lsv2_pt_your_key_here
OPENAI_API_KEY=sk-your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langgraph-local
EOF
```

**Windows (PowerShell):**
```powershell
@"
LANGSMITH_API_KEY=lsv2_pt_your_key_here
OPENAI_API_KEY=sk-your_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=langgraph-local
"@ | Out-File -FilePath .env -Encoding ASCII
```

---

## ✅ Step 8: Verify Project Structure

Your directory should look like this:

```
langgraph-studio/
├── venv/              (virtual environment)
├── agent.py           (your agent code)
├── langgraph.json     (configuration)
└── .env               (environment variables)
```

**Verify files exist:**

**macOS/Linux:**
```bash
ls -la
```

**Windows:**
```cmd
dir
```

---

## 🚀 Step 9: Start LangGraph Studio

**All Platforms:**

```bash
# Make sure you're in the project directory and venv is activated
langgraph dev
```

### With Tunneling (Optional)

If you want to access Studio from another device or share the URL:

```bash
langgraph dev --tunnel
```

### What You Should See

```
🚀 Starting LangGraph Server...
📡 Server running at http://127.0.0.1:2024
🎨 Studio UI at https://smith.langchain.com/studio?baseUrl=http://127.0.0.1:2024
```

---

## 🌐 Step 10: Access the Studio UI

1. Open your browser
2. Go to: **https://smith.langchain.com/studio?baseUrl=http://127.0.0.1:2024**
3. You should see the LangGraph Studio interface!

### Alternative: Direct Local Access

Some setups also expose Studio directly at:
- **http://localhost:2024** (if supported in your version)

---

## 🎯 Test Your Agent

Try these example prompts in the Studio UI:

- "What's the weather in Bengaluru?"
- "Calculate 15 times 23"
- "What's the area of a circle with radius 5?"

---

## 🛑 Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

---

## 🔄 Restarting Later

**Every time you want to use LangGraph Studio:**

1. **Activate virtual environment:**
   ```bash
   # macOS/Linux
   cd langgraph-studio
   source venv/bin/activate
   
   # Windows CMD
   cd langgraph-studio
   venv\Scripts\activate
   
   # Windows PowerShell
   cd langgraph-studio
   venv\Scripts\Activate.ps1
   ```

2. **Start the server:**
   ```bash
   langgraph dev
   ```

---

## 🐛 Troubleshooting

### "langgraph: command not found"

**Solution:** Make sure virtual environment is activated and LangGraph CLI is installed:
```bash
pip install --pre "langgraph-cli>=1.0.0a0"
```

### Port 2024 Already in Use

**Solution:** Kill the process or use a different port:
```bash
langgraph dev --port 2025
```

### Module Import Errors

**Solution:** Reinstall in the virtual environment:
```bash
pip install --upgrade --pre "langgraph>=1.0.0a0" langchain-openai langchain-core
```

### API Key Errors

**Solution:** 
1. Check `.env` file exists and has correct keys
2. Verify no extra spaces around the `=` sign
3. Make sure keys are valid and active

### Windows: "Script execution is disabled"

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Cannot Connect to Studio UI

**Solution:**
1. Make sure server is running (check terminal)
2. Try `http://127.0.0.1:2024` instead of `localhost`
3. Check firewall settings
4. Try with `--tunnel` flag

### macOS: SSL Certificate Errors

**Solution:**
```bash
/Applications/Python\ 3.11/Install\ Certificates.command
```

---

## 📚 Additional Resources

- **LangGraph v1 Documentation:** https://docs.langchain.com/oss/python/langgraph/studio
- **LangSmith Platform:** https://smith.langchain.com
- **LangGraph GitHub:** https://github.com/langchain-ai/langgraph
- **LangChain Discord:** https://discord.gg/langchain

---

## 💡 Next Steps

1. **Modify the agent** - Edit `agent.py` to add more tools
2. **Check LangSmith traces** - View detailed execution logs at https://smith.langchain.com
3. **Build complex graphs** - Explore multi-agent systems and conditional routing
4. **Deploy your agent** - Use LangGraph Cloud for production deployment

---

## ⚠️ Important Notes

- **LangGraph 1.0 is in alpha** - APIs may change
- **Keep API keys secure** - Never commit `.env` to version control
- **Add `.env` to `.gitignore`** if using Git
- **Virtual environment** - Always activate it before working

---

**Happy Building! 🎉**
