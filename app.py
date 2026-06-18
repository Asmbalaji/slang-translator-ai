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
        language = request.form["language"]    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""


Translate the following text into {language}.

Rules:

* If language is Tamil, return the answer in Tamil.
* If language is Hindi, return the answer in Hindi.
* If language is Telugu, return the answer in Telugu.
* If language is Malayalam, return the answer in Malayalam.
* If language is English, return the answer in English.
* Explain any slang used.
* Keep the explanation in the selected language.

Text:
{slang}
"""
}
]
)


    result = response.choices[0].message.content

return render_template("index.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)