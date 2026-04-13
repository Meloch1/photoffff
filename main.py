from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>photoffff</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0f0f0f;
            color: #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        .container {
            text-align: center;
            padding: 2rem;
        }
        h1 {
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -1px;
            margin-bottom: 0.5rem;
        }
        p {
            font-size: 1.1rem;
            color: #888;
        }
        .dot {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #22c55e;
            border-radius: 50%;
            margin-right: 8px;
            animation: pulse 2s infinite;
        }
        .status {
            display: inline-flex;
            align-items: center;
            margin-top: 1.5rem;
            font-size: 0.9rem;
            color: #22c55e;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>photoffff</h1>
        <p>Your app is up and running.</p>
        <div class="status">
            <span class="dot"></span> Online
        </div>
    </div>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

