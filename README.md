# Fintech_Research_AI_Assistant
Multi-agent AI research system built with CrewAI orchestrating specialized agents for automated fintech research and reporting.
This application orchestrates three distinct agents to gather, analyze, and report on fintech topics with comprehensive insights.
<img width="570" height="745" alt="image" src="https://github.com/user-attachments/assets/65b80491-4aab-4587-9934-9ee44d65e9ab" />


## 🌟 Features

- **Multi-Agent Architecture**: Three specialized AI agents working collaboratively
  - 🔍 **Research Specialist**: Gathers comprehensive information from multiple sources
  - 📊 **Fintech Analyst**: Analyzes data and identifies trends 
  - ✍️ **Reporting Specialist**: Creates structured, professional reports

- **Interactive Web Interface**: Streamlit-powered dashboard for easy topic input and result viewing
- **Real-time Progress Tracking**: Visual progress indicators and status updates
- **Multiple Output Formats**: Generates research findings, analysis reports, and final comprehensive reports
- **File Download Capability**: Export all generated reports as markdown files
- **API Key Validation**: Built-in configuration management and validation

## 🏗️ Architecture

The system follows a multi-agent workflow:

```
User Input → Streamlit UI → CrewAI Orchestrator → [Research Agent → Fintech Analyst → Reporting Agent] → Output Reports
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- API Keys for:
  - Serper API (for web search)
  - Groq API (for LLM processing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/fintech-research-ai-assistant.git
   cd fintech-research-ai-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   
   **Option A: Web Interface (Recommended)**
   ```bash
   streamlit run app.py
   ```
   
   **Option B: Command Line**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
fintech-research-ai-assistant/
├── app.py                  # Streamlit web interface
├── main.py                 # Command-line interface
├── crew.py                 # CrewAI configuration and orchestration
├── .env                    # Environment variables (create this)
├── requirements.txt        # Python dependencies
├── agents/                 # AI agent definitions
│   ├── research_specialist.py
│   ├── fintech_analyst.py
│   └── reporting_specialist.py
├── tasks/                  # Task definitions for each agent
│   ├── research_task.py
│   ├── analysis_task.py
│   └── reporting_task.py
└── outputs/               # Generated reports (auto-created)
    ├── research_findings.md
    ├── analysis_report.md
    └── final_report.md
```

## 💡 Usage

### Web Interface

1. Open your browser to `http://localhost:8501`
2. Enter your research topic (e.g., "Fintech trends in 2025", "Digital Banking innovations")
3. Click "🚀 Start Research"
4. Monitor progress through the real-time status updates
5. View and download generated reports in the Results section

### Command Line

1. Edit the topic in `main.py`
2. Run `python main.py`
3. Check the generated files in the project directory

## 📋 Requirements

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
crewai>=0.1.0
python-dotenv>=1.0.0
groq>=0.4.0
langchain>=0.1.0
langchain-community>=0.0.20
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SERPER_API_KEY` | API key for Serper search service | Yes |
| `GROQ_API_KEY` | API key for Groq LLM service | Yes |

### Getting API Keys

1. **Serper API**: Sign up at [serper.dev](https://serper.dev) for web search capabilities
2. **Groq API**: Get your key from [groq.com](https://groq.com) for fast LLM processing

## 📊 Output Files

The system generates three types of reports:

- **research_findings.md**: Raw research data and sources
- **analysis_report.md**: Processed analysis and insights  
- **final_report.md**: Comprehensive final report with conclusions

## 🛠️ Tech Stack

- **Framework**: CrewAI for multi-agent orchestration
- **UI**: Streamlit for web interface
- **LLM**: Groq for fast language model processing
- **Search**: Serper API for web research
- **Language**: Python 3.8+

## 🚦 Troubleshooting

**Common Issues:**

1. **Missing API Keys**: Ensure your `.env` file contains valid API keys
2. **Import Errors**: Run `pip install -r requirements.txt` to install dependencies
3. **Port Conflicts**: If port 8501 is busy, Streamlit will suggest an alternative port

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Built for

This tool is designed for:
- Fintech researchers and analysts
- Investment professionals
- Business strategists
- Anyone needing comprehensive fintech market insights

---

*Built with CrewAI, Streamlit, and Groq for intelligent fintech research automation.*
