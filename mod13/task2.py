from flask import Flask, jsonify

app = Flask(__name__)

airports = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "EDDF": {"Name": "Frankfurt Airport", "Location": "Frankfurt"},
    "LFPG": {"Name": "Charles de Gaulle Airport", "Location": "Paris"},
    "RJTT": {"Name": "Haneda Airport", "Location": "Tokyo"},
    "WSSS": {"Name": "Singapore Changi Airport", "Location": "Singapore"},
    "VIDP": {"Name": "Indira Gandhi International Airport", "Location": "Delhi"},
    "YSSY": {"Name": "Sydney Kingsford Smith Airport", "Location": "Sydney"},
    "ZBAA": {"Name": "Beijing Capital International Airport", "Location": "Beijing"}
}


@app.route('/airport/<icao_code>')
def get_airport(icao_code):
    icao_code = icao_code.upper()

    if icao_code in airports:
        airport = airports[icao_code]
        return jsonify({
            "ICAO": icao_code,
            "Name": airport["Name"],
            "Location": airport["Location"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)