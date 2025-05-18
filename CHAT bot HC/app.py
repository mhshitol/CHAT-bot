from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Default route to render the front-end HTML
@app.route("/")
def index():
    return render_template("index.html")

# API route to handle POST requests from the frontend
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the frontend JSON request
    message = request.json.get("message")
    if not message:
        return jsonify({"error": "No message received"}), 400

    try:
        # Send the message to Ollama (LLaMA 3.2) and get the response
        response = ollama.chat(
            model='llama3.2',
            messages=[{'role': 'user', 'content': message}]
        )
        return jsonify({"response": response['message']['content'].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
