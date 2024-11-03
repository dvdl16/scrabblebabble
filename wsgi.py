from babble.babbler import Babbler
from flask import Flask, render_template, request, jsonify


web_app = Flask(__name__)


@web_app.route("/")
def index():
    return render_template("index.html")


@web_app.route("/process", methods=["POST"])
def process_sentence():
    sentence = request.form.get("sentence")
    if not sentence:
        return jsonify({"error": "Please enter a sentence"}), 400

    processor = Babbler()
    new_words = processor.get_new_words(sentence)
    return new_words


if __name__ == "__main__":
    web_app.run()
