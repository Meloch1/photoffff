from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>photoffff</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
</head>
<body class="bg-gray-950 text-white min-h-screen flex flex-col items-center justify-center">
    <div class="flex flex-col items-center gap-6 px-6 text-center">
        <div class="text-6xl">📸</div>
        <h1 class="text-3xl font-bold tracking-tight">photoffff</h1>
        <p class="text-gray-400 text-lg max-w-sm">
            Welcome to the photo battle mini app. Open this through Telegram to get started.
        </p>
        <div class="mt-4 px-6 py-3 bg-blue-600 hover:bg-blue-500 transition-colors rounded-xl font-semibold text-white cursor-pointer select-none"
             onclick="Telegram.WebApp.close()">
            Open in Telegram
        </div>
    </div>
    <script>
        const tg = window.Telegram.WebApp;
        tg.ready();
        tg.expand();
    </script>
</body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

