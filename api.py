from flask import Flask, render_template, request
from chat import ask_agent

app = Flask(__name__, template_folder="template")


#
@app.route("/chat", methods=["POST"])
def chat():
    query = request.json["query"]
    print(query)
    return ask_agent(query)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
