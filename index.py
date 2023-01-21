from flask import Flask, request, render_template
from itertools import combinations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtenha os dados do formulário
        quantity = request.form["quantity"]
        numbers = request.form["numbers"].split(",")

        # Calcule as combinações
        combinations_list = list(combinations(numbers, int(quantity)))
        combinations_list = [",".join(comb) for comb in combinations_list]
        combinations_count = len(combinations_list)
    else:
        combinations_list = []
        combinations_count = 0
    return render_template("index.html", combinations=combinations_list, combinations_count=combinations_count)

if __name__ == "__main__":
    app.run(debug=True)
