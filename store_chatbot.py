from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import traceback
import sys

app = Flask(__name__)
CORS(app)

client = OpenAI()

@app.route("/chat", methods=["POST"])
def chat():
    try:
        print("🔹 chat endpoint hit")
        user_message = request.json["message"]

        system_prompt = "You are a helpful assistant for an online clothing store. Answer customer questions clearly and politely."

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        reply = completion.choices[0].message.content
        return jsonify({"reply": reply})
    
    except Exception as e:
        print("\n⚠️  Error occurred:", e)
        traceback.print_exc()
        sys.stdout.flush()
        return jsonify({"reply": "Sorry, something went wrong."})

if __name__ == "__main__":
    app.run(debug=True)
