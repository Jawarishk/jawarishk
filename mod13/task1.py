from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/prime_number/<int:number>')
def check_prime(number):
    if number < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

    result = {
        "Number": number,
        "isPrime": is_prime
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)