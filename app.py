from flask import Flask, render_template, request
from google import genai
from google.genai import types
import PyPDF2
import os
from dotenv import load_dotenv
import markdown

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_api_key_here":
    raise ValueError("GEMINI_API_KEY not set in .env file. Please set it to your Google Gemini API key.")
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "your-secret-key-here")
# Load Gemini model
client = genai.Client(api_key=api_key)
model = "gemini-1.5-flash"
system_prompt ="""
    You are an AI resume reviewer. Score the resume and provide suggestions for improvement. 
    1. Do not include any personal information or sensitive data in your response. 
    2. If its not a resume, respond with "This is not a resume."
    3. Provide a score from 1-10 based on clarity, grammar, professionalism, and ATS-friendliness.
    4. Provide bullet-point suggestions for improvement.
    5. Suggest what job the resume is suitable for.
    6. Respond in **Markdown format** with the following structure
    7. if suggestion improvement is true, then provide suggestions for improvement, otherwise do not provide suggestions.
"""
def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_text = ""
        
        # Handle file upload
        file = request.files["resume_file"]
        if file and file.filename != "":
            # Extract both text and style information
            resume_text = extract_text_from_pdf(file)

        if not resume_text.strip():
            resume_text = request.form.get("resume_text", "")

        if not resume_text.strip():
            return render_template("index.html", error="Please provide a resume.")

        improvements = "true" if request.form.get("improvements") else "false"
        # Send to Gemini for scoring
        prompt = f"""
        Suggest improvements :{improvements}
        ### Score
        - Overall: X/10
        - Clarity: ...
        - Grammar: ...
        - Professionalism: ...
        - ATS-friendliness: ...

        ### Suggestions for Improvement
        - Bullet point 1
        - Bullet point 2

        ### Suitable Roles
        - Role 1
        - Role 2

        ### Resume Text
        {resume_text}
        """

        # Generate content using Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0), # Disables thinking
                system_instruction=system_prompt
            ),
        )

        if not response.text:
            return render_template("index.html", error="No response from Gemini. Please try again.")
        
        else:
            feedback = markdown.markdown(response.text)
            
            return render_template("index.html", feedback=feedback)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
