import os
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
            return redirect(url_for('home'))

    return render_template("index.html")


REDIRECT_URL = os.getenv("REDIRECT_URL", "https://example.com")


@app.route("/welcome")
def welcome():
    email = request.args.get("email", "гость")
    return render_template("welcome.html", email=email, redirect_url=REDIRECT_URL)


@app.route("/health")
def health():
    return "OK", 200


@app.route('/home')
def home():
    products = [
        {'name': 'BioBoost', 'desc': 'Органическое удобрение для роста растений'},
        # сделал RootMax чтобы совпадало
        {'name': 'RootMax', 'desc': 'Минеральный стимулятор для почвы'},
        {'name': 'EcoSoil', 'desc': 'Натуральное удобрение для овощей'}
    ]
    return render_template('home.html', products=products)


@app.route('/product/<name>')
def product(name):
    products = {
        'BioBoost': 'Органическое удобрение для стимуляции роста и укрепления корней.',
        'RootMax': 'Минеральный состав для восстановления почвы и роста урожайности.',
        'EcoSoil': 'Экологичное удобрение на основе растительных компонентов.'
    }

    description = products.get(name, "Описание не найдено.")
    return render_template('product.html', name=name, description=description)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
