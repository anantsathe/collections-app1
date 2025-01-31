from flask import Flask

app = Flask(__name__)

def get_zodiac_sign(day, month):
    zodiac_signs = [
        ("Capricorn", (1, 20)), ("Aquarius", (2, 19)), ("Pisces", (3, 20)), 
        ("Aries", (4, 20)), ("Taurus", (5, 21)), ("Gemini", (6, 21)), 
        ("Cancer", (7, 23)), ("Leo", (8, 23)), ("Virgo", (9, 23)), 
        ("Libra", (10, 23)), ("Scorpio", (11, 22)), ("Sagittarius", (12, 22)), 
        ("Capricorn", (12, 31))
    ]
    
    for sign, (m, d) in zodiac_signs:
        if (month == m and day <= d) or (month < m):
            return sign
    return "Invalid date"

@app.route("/<int:month>/<int:day>")
def zodiac(month, day):
    if 1 <= month <= 12 and 1 <= day <= 31:
        sign = get_zodiac_sign(day, month)
        return f"Your Zodiac sign is: {sign}"
    else:
        return "Invalid month or day. Please enter in format: /month/day", 400

if __name__ == "__main__":
    app.run(debug=True, port=8080)