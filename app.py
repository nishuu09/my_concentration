from flask import Flask, render_template, request

app = Flask(__name__)

# Faktor konversi ke kilogram
conversion_factors = {
    'kg': 1,
    'g': 0.001,
    'lb': 0.453592,
    'oz': 0.0283495
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        # Konversi ke kilogram terlebih dahulu, lalu ke satuan tujuan
        weight_in_kg = weight * conversion_factors[from_unit]
        converted = weight_in_kg / conversion_factors[to_unit]

        result = f"{weight} {from_unit} = {round(converted, 4)} {to_unit}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
