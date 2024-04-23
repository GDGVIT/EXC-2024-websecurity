from flask import Flask, render_template, request
import secrets

app = Flask(__name__)

# Secret key for generating tokens (replace with your own)
app.secret_key = "YOUR_SECRET_KEY_HERE"

@app.route("/")
def index():
  # Generate a new CSRF token on each request
  csrf_token = secrets.token_hex(32)
  # Store token in session (alternative: send in cookie)
  session["csrf_token"] = csrf_token
  return render_template("index.html", csrf_token=csrf_token)

@app.route("/transfer", methods=["POST"])
def transfer():
  # Retrieve CSRF token from session
  csrf_token = session.get("csrf_token")
  # Check if token is present and matches the one stored
  if not csrf_token or csrf_token != request.form.get("csrf_token"):
    return "Invalid CSRF Token", 403  # Forbidden

  return "Transfer successful!"

if __name__ == "__main__":
  app.run(debug=True)