from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Tapaiko API URL
API_BASE_URL = "https://visi-tapi-free-fire-ckrpro-on-top.vercel.app/bd/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_visit/<uid>')
def send_visit(uid):
    try:
        # API call gardai
        response = requests.get(f"{API_BASE_URL}{uid}")
        if response.status_code == 200:
            data = response.json()
            # Success: 1000 visits pathako jasto result pathaune
            return jsonify({
                "status": "success",
                "nickname": data.get("nickname", "Unknown"),
                "region": data.get("region", "BD"),
                "message": "1000 Visits Sent Successfully!"
            })
        else:
            return jsonify({"status": "error", "message": "Invalid UID or API Error"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)