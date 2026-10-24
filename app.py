from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    person = request.form.get("person")
    purpose = request.form.get("purpose")

    return render_template(
        "success.html",
        name=name,
        phone=phone,
        email=email,
        person=person,
        purpose=purpose
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)