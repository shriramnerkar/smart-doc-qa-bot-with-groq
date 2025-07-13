from flask import Flask, render_template, request
from app.qa_bot import load_and_prepare_doc, get_qa_chain
import os

app = Flask(__name__)
UPLOAD_FOLDER = "app/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        file = request.files["document"]
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        chunks = load_and_prepare_doc(filepath)
        qa_chain = get_qa_chain(chunks)
        answer = qa_chain.run(question)

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
