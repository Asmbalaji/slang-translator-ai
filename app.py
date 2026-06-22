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

        if dialect == "Kongu Tamil":
            prompt = f"""
You are a native Kongu Tamil speaker.

Convert the text into authentic Kongu Tamil.

Examples:
எப்படி இருக்கிறாய்? → எப்படிப்பா இருக்கே?
என்ன செய்கிறாய்? → என்னப்பா பண்றே?
நான் வீட்டுக்கு போகிறேன். → நா வீட்டுக்குப் போறேன்பா.
சாப்பிட்டாயா? → சாப்ப்ட்டியா பா?
நண்பா, இங்கே வா. → மாப்ளே, இங்க வா.

Text:
{slang}
"""

        elif dialect == "Chennai Tamil":
            prompt = f"""
You are a native Chennai Tamil speaker.

Convert the text into authentic Chennai Tamil slang.

Examples:
எப்படி இருக்கிறாய்? → எப்படி டா இருக்க?
என்ன செய்கிறாய்? → என்ன டா பண்ற?
நண்பா, இங்கே வா. → டா, இங்க வா.

Text:
{slang}
"""

        elif dialect == "Madurai Tamil":
            prompt = f"""
You are a native Madurai Tamil speaker.

Convert the text into authentic Madurai Tamil.

Examples:
எப்படி இருக்கிறாய்? → எப்படி மாப்ள இருக்க?
என்ன செய்கிறாய்? → என்ன மாப்ள பண்ற?
நண்பா, இங்கே வா. → மாப்ள, இங்க வா.

Text:
{slang}
"""

        elif dialect == "Tirunelveli Tamil":
            prompt = f"""
You are a native Tirunelveli Tamil speaker.

Convert the text into authentic Tirunelveli Tamil.

Examples:
எப்படி இருக்கிறாய்? → எப்படிலே இருக்க?
நண்பா, இங்கே வா. → லே, இங்க வா.

Text:
{slang}
"""

        else:
            prompt = f"""
Convert the following text into {dialect}.

Text:
{slang}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)