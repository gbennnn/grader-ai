# Smart PDF Grader

Smart PDF Grader is an AI-powered web-based system designed to automatically evaluate student assignment PDF files. This tool helps educators and teaching assistants to efficiently assess, score, and provide feedback based on customizable grading parameters.

## 🚀 Features

- 📄 Upload and process multiple student PDFs
- 🤖 AI analysis of writing structure, relevance, grammar, and references
- 📊 Customizable grading rubrics
- ✍️ Automatic feedback generation
- 📈 Score calculation and result export

## 🛠️ Tech Stack

- **Frontend**: React.js / Next.js
- **Backend**: Python (Flask / FastAPI) or Node.js
- **AI/NLP**: OpenAI API (GPT), spaCy, HuggingFace Transformers
- **PDF Extraction**: PyMuPDF, pdfplumber, Tesseract (OCR)
- **Database**: PostgreSQL / MongoDB
- **Deployment**: Vercel / Render / Heroku

## 📚 Use Case

Initially built to solve the real-world problem of grading 40+ student reports manually, this tool aims to save time, ensure consistent grading, and enhance the quality of feedback.

## 🔧 Getting Started (Dev)

```bash
# clone the repository
git clone https://github.com/iambeno1/smart-pdf-grader.git
cd smart-pdf-grader

# install backend dependencies
cd backend
pip install -r requirements.txt

# install frontend dependencies
cd ../frontend
npm install
