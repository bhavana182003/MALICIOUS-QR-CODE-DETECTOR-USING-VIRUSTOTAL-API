from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sqlite3
import base64
import time

app = Flask(__name__)
CORS(app)

# Initialize the database

def init_db():
    with sqlite3.connect('malicious_qrcodes.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS malicious_qrcodes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/api/analyze', methods=['POST'])
def analyze_qr_code():
    data = request.json
    qr_code_data = data.get('qrCodeData')
    
    if not qr_code_data:
        return jsonify({'error': 'No QR code data provided'}), 400
    
    is_malicious = check_malicious(qr_code_data)
    
    if is_malicious:
        store_malicious_qr_code(qr_code_data)
    
    return jsonify({'isMalicious': is_malicious})
def check_malicious(data):
    api_key = "#YOUR_API_KEY"
    headers = {"x-apikey": api_key}
    
    try:
        # Submit the URL for scanning
        submission_response = requests.post(
            "https://www.virustotal.com/api/v3/urls", 
            headers=headers, 
            data={"url": data}
        )
        print("Submission Response:", submission_response.json())  # Debugging

        if submission_response.status_code != 200:
            return False
        
        # Get the analysis ID
        analysis_id = submission_response.json().get('data', {}).get('id')
        if not analysis_id:
            return False

        # Poll for analysis results
        analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        
        for _ in range(10):  
            analysis_response = requests.get(analysis_url, headers=headers)
            print("Analysis Response:", analysis_response.json())  # Debugging
            
            if analysis_response.status_code == 200:
                analysis_data = analysis_response.json()
                status = analysis_data['data']['attributes']['status']
                
                if status == 'completed':
                    malicious_count = analysis_data['data']['attributes']['stats']['malicious']
                    print("Malicious Count:", malicious_count)  # Debugging
                    
                    # Return True if malicious count is greater than 0
                    return malicious_count > 0  

            time.sleep(1)

        return False
    
    except Exception as e:
        print("Exception:", e)
        return False


# Store malicious QR codes
def store_malicious_qr_code(data):
    with sqlite3.connect('malicious_qrcodes.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO malicious_qrcodes (data) VALUES (?)', (data,))
        conn.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
