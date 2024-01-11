from flask import Flask, request, jsonify , render_template
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

# Initialize Flask app
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# Define route for /prompt with POST method
@app.route("/prompt", methods=["POST"])
def prompt():
    # Get prompt string from request body
    prompt_str = request.json.get("prompt")

    # Call OpenAI API to generate response based on prompt
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_str,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Extract generated text from API response
    generated_text = response.choices[0].text.strip()

    # Return generated text as JSON payload in response body
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run()
