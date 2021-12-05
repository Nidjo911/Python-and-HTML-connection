import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    tajni_broj = request.cookies.get("tajni_broj")  # check if there is already a cookie named secret_number

    response = make_response(render_template("index.html"))
    if not tajni_broj:
        nova_tajna = random.randint(1, 30)

        response.set_cookie("tajni_broj", str(nova_tajna))
    return response

@app.route("/rezultat", methods=["POST"])
def rezultat():
    guess = int(request.form.get("guess"))
    tajni_broj = int(request.cookies.get("tajni_broj"))

    if guess == tajni_broj:
        poruka = "Correct! The secret number is {0}".format(str(tajni_broj))
        response = make_response(render_template("rezultat.html", poruka=poruka))
        response.set_cookie("tajni_broj", str(random.randint(1, 30)))
        return response
    elif guess > tajni_broj:
        poruka = "manji broj."
        return render_template("rezultat.html", poruka=poruka)
    elif guess < tajni_broj:
        poruka = "veci broj."
        return render_template("rezultat.html", poruka=poruka)


if __name__ == "__main__":
    app.run(use_reloader = True)