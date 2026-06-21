from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        slang = request.form["slang"]
        dialect = request.form["dialect"]

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
           messages=[
        {
            "role": "user",
           "content": f"""
You are an expert in Tamil regional dialects.

Convert the text into {dialect}.

Rules:
- Keep the original meaning exactly.
- Output only the converted text.
- Do not explain the answer.
- Use authentic local vocabulary.

Examples:

Standard Tamil: எப்படி இருக்கிறாய்?
Kongu Tamil: எப்படிப்பா இருக்கே?

Standard Tamil: என்ன செய்கிறாய்?
Kongu Tamil: என்னப்பா பண்றே?

Standard Tamil: நான் வீட்டுக்கு போகிறேன்.
Kongu Tamil: நா வீட்டுக்குப் போறேன்பா.

Text:
{slang}
"""        }
    ]
)
        result = response.choices[0].message.content

    return render_template("index.html", result=result)



if __name__ == "__main__":
    app.run(debug=True)