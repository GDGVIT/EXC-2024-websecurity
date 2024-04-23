from flask import Flask, request, jsonify
from functools import wraps
import time

app = Flask(__name__)

# Rate limit configuration (change values as needed)
MAX_REQUESTS_PER_MINUTE = 100
TIME_WINDOW_SECONDS = 60  # Track requests for the last minute

# User data (replace with your authentication method)
users = {"user1": {"last_request": 0}}  # Stores timestamps of last requests

def rate_limit(func):
  """Decorator function to rate limit API requests"""
  @wraps(func)
  def wrapper(*args, **kwargs):
    # Get user identity (replace with your method)
    user_id = request.headers.get("X-User-ID")
    if not user_id:
      return jsonify({"error": "Missing X-User-ID header"}), 401

    # Check user data dictionary for last request time
    if user_id in users:
      last_request = users[user_id]["last_request"]
      current_time = time.time()
      if current_time - last_request < TIME_WINDOW_SECONDS:
        return jsonify({"error": "Rate limit exceeded"}), 429  # Too Many Requests
      else:
        # Update last request time
        users[user_id]["last_request"] = current_time
    else:
      # New user, add to user data dictionary
      users[user_id] = {"last_request": time.time()}

    # Call the original function if rate limit is not exceeded
    return func(*args, **kwargs)
  return wrapper

@app.route("/api/data")
@rate_limit
def get_data():
  # Your API logic to retrieve data
  return jsonify({"data": "This is some data"})

if __name__ == "__main__":
  app.run(debug=True)
