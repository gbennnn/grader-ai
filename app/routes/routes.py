import os
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from app.utils.pdf_utils import extract_text_from_pdf
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

# Load API key dari .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

main = Blueprint("main", __name__)


@main.route("/", methods=["GET"])
def index():
    return render_template("index.html", current_year=datetime.now().year)


@main.route("/upload", methods=["POST"])
def upload_file():
    if "clear" in request.form:
        # Render ulang tanpa hasil
        return render_template("index.html", current_year=datetime.now().year)
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]

    if file.filename == "":
        return "No selected file", 400

    if not file.filename.lower().endswith(".pdf"):
        return "Invalid file type", 400

    filename = secure_filename(file.filename)
    filepath = os.path.join("uploads", filename)
    file.save(filepath)

    extracted_text = extract_text_from_pdf(filepath)
    feedback_text = analyze_with_gpt(extracted_text)

    # Parse feedback menjadi list of dict
    feedback_table = []
    total_score = None
    for line in feedback_text.strip().split("\n"):
        line = line.strip()
        if line.lower().startswith("total skor"):
            try:
                total_score = line.split(":")[1].strip()
            except IndexError:
                continue
        else:
            try:
                aspek, skor, komentar = line.split("|")
                feedback_table.append(
                    {
                        "aspek": aspek.strip(),
                        "skor": skor.strip(),
                        "komentar": komentar.strip(),
                    }
                )
            except ValueError:
                continue  # skip baris yang tidak sesuai

    return render_template(
        "index.html",
        text=extracted_text,
        feedback_table=feedback_table,
        total_score=total_score,
        current_year=datetime.now().year,
    )


def analyze_with_gpt(text):
    prompt = f"""
Tugas kamu adalah menjadi penilai esai mahasiswa berdasarkan rubrik di bawah ini. Berikan skor untuk setiap aspek dan totalnya. Jelaskan singkat alasannya (maks. 1 kalimat per aspek). Ini rubriknya:

- Struktur Tulisan (maks 25)
- Kejelasan Argumen (maks 25)
- Tata Bahasa (maks 20)
- Ketepatan Konten (maks 20)
- Kreativitas/Gaya (maks 10)

Format jawaban kamu adalah sebagai berikut:

Struktur Tulisan|Skor/25|Komentar
Kejelasan Argumen|Skor/25|Komentar
Tata Bahasa|Skor/20|Komentar
Ketepatan Konten|Skor/20|Komentar
Kreativitas/Gaya|Skor/10|Komentar

Total Skor: xx/100

Berikut teks esainya:

\"\"\"{text}\"\"\"
"""

    response = client.chat.completions.create(
        model="gpt-4.1",  # atau gpt-4 jika kamu punya akses
        messages=[
            {
                "role": "system",
                "content": "Kamu adalah dosen yang menilai esai mahasiswa berdasarkan rubrik akademik.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
        max_tokens=500,
    )

    return response.choices[0].message.content
