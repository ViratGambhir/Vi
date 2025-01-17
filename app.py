from flask import Flask, render_template, request

app = Flask(__name__)

# Function to check password strength
def check_password_strength(password):
    strength = 0
    feedback = []

    # Password length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password too short. Aim for 8+ characters.")

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        strength += 1
    else:
        feedback.append("Consider adding uppercase letters for better strength.")

    # Check for lowercase letters
    if any(c.islower() for c in password):
        strength += 1
    else:
        feedback.append("Consider adding lowercase letters for better strength.")

    # Check for digits
    if any(c.isdigit() for c in password):
        strength += 1
    else:
        feedback.append("Consider adding digits for better strength.")

    # Check for special characters
    if any(c in "!@#$%^&*(){}[]<>?/" for c in password):
        strength += 1
    else:
        feedback.append("Consider adding special characters for better strength.")

    # Determine overall password strength
    if strength >= 5:
        return "Strong password!", feedback
    elif strength <= 3:
        return "Weak password.", feedback
    else:
        return "Moderate password.", feedback

# Define route for the password strength checker
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    suggestions = []
    
    if request.method == "POST":
        password = request.form["password"]
        result, suggestions = check_password_strength(password)
    
    return render_template("index.html", result=result, suggestions=suggestions)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
