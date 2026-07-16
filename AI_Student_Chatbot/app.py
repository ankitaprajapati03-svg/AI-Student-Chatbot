from flask import Flask, render_template, request, session, redirect, url_for
from chatbot import get_response

app = Flask(__name__)
app.secret_key = "student_chatbot_secret"

@app.route("/", methods=["GET", "POST"])
def home():

    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        question = request.form["question"]
        answer = get_response(question)

        messages = session["messages"]
        messages.append({
            "user": question,
            "bot": answer
        })

        session["messages"] = messages

    return render_template("index.html", messages=session["messages"])


@app.route("/clear")
def clear():
    session.pop("messages", None)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)