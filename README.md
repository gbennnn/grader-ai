# Grader AI

**Grader-AI** is an AI-powered web-based system designed to automatically evaluate student assignment PDF files. This tool helps educators and teaching assistants to efficiently assess, score, and provide feedback based on customizable grading parameters.

## 🚀 Features

- 📄 Upload and Extract pdf file to text
- 🤖 AI analysis of writing structure, relevance, grammar, and references
- 📊 Customizable grading rubrics
- ✍️ Automatic feedback generation
- 📈 Score calculation and result export

## 🛠️ Tech Stack

- **Frontend**: HTML, Tailwind CSS
- **Backend**: Python (Flask / FastAPI)
- **AI/NLP**: OpenAI API (GPT)
- **PDF Extraction**: PyMuPDF

## 📚 Use Case

Initially built to solve the real-world problem of grading 40+ student reports manually, this tool aims to save time, ensure consistent grading, and enhance the quality of feedback.

## 🔧 Getting Started (Dev)

```bash
# clone the repository
git clone https://github.com/gbennnn/grader-ai.git
cd grader-ai

# install backend dependencies
pip install -r requirements.txt

# run the application
# make sure to set the OPENAI_API_KEY environment variable
python app.py
```
