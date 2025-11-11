from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        agree = request.form.get("agree")

        if not email or "@" not in email:
            message = "Введите корректный Email!"
            return render_template("index.html", message=message)
        elif len(password) < 6:
            message = "Пароль должен содержать не менее 6 символов!"
            return render_template("index.html", message=message)
        elif not agree:
            message = "Вы должны согласиться с условиями!"
            return render_template("index.html", message=message)
        else:
            # Если всё верно — переход на новую страницу
            return redirect(url_for("welcome", email=email))

    return render_template("index.html")

@app.route("/welcome")
def welcome():
    email = request.args.get("email", "гость")
    return render_template("welcome.html", email=email)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)