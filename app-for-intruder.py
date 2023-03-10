import random
import string
from flask import Flask, request, Response

app = Flask(__name__)

users = [
    {
        "name": "Alice",
        "password": random.choice(string.ascii_lowercase),
    },
    {
        "name": "Bob",
        "password": random.choice(string.ascii_lowercase),
    },
    {
        "name": "Charlie",
        "password": random.choice(string.ascii_lowercase),
    },
]


@app.route("/")
def index():
    return """
<html>

<head></head>

<body>
    <form action="/api" method="POST">
        Name: <input type="text" name="name">
        Password: <input type="text" name="password">
        <input type="submit" value="Submit">
    </form>
</body>

</html>
"""


@app.route("/api", methods=["POST"])
def api():
    name = request.form["name"]
    password = request.form["password"]
    if name not in list(map(lambda user: user["name"], users)):
        return Response("User not found", status=401)
    user_index = list(map(lambda user: user["name"], users)).index(name)
    target_user = users[user_index]

    if target_user["password"] == password:
        return Response(response=f'Logged in as {target_user["name"]}', status=200)
    else:
        return Response("Wrong password", status=401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
