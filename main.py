from flask import Flask
from flask import request

app = Flask(__name__)


def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        # add sanity check for out of range celcius values
        celsius = float(celsius)
        if celsius < -273.15:
            return "invalid input"
        if celsius > 1000:
            return "invalid input"
        fahrenheit = celsius * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


@app.route("/")
def index():
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""
    return (
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + fahrenheit
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)
