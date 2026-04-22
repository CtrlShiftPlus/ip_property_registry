from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Paste your deployed contract ID here
CONTRACT_ID = "CC7LJ7NVULQ5S43MCA664GMB7LFRT6EVDIOIGP5AQ7B4SA3252K4MZ2X"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None

    if request.method == 'POST':
        ip_id = request.form['ip_id']

        cmd = [
            "stellar", "contract", "invoke",
            "--id", CONTRACT_ID,
            "--network", "testnet",
            "--",
            "get",
            "--id", ip_id
        ]

        try:
            output = subprocess.check_output(cmd, text=True)
            result = output
        except Exception as e:
            result = f"Error fetching record: {str(e)}"

    return render_template("search.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)