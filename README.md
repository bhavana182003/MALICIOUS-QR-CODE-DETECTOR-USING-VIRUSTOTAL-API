A malware scanning using Flask,Python and Virustotal API
# Malicious QR Code Detector using VirusTotal API (Python + Flask)

This project is a web-based QR code security scanner built using Python and Flask. It allows users to upload a QR code image, extract the embedded URL, and scan it using the VirusTotal API to determine if the link is safe, suspicious, or malicious. The application demonstrates full-stack Python development with a focus on backend API integration and real-time security analysis.

## How It Works

1. Users upload a QR code image through the web interface.  
2. The backend extracts the URL from the QR code.  
3. The extracted URL is sent to the VirusTotal API.  
4. The application displays a detailed safety report, including detection verdicts from multiple antivirus engines.

## Tech Stack

- Python 3  
- Flask – backend framework  
- Flask-CORS – enables cross-origin access  
- requests – for interacting with the VirusTotal API  
- dotenv – for securely managing the API key  
- HTML/CSS/JavaScript – for the user interface (optional)

## Features

- Web interface for uploading QR code images  
- URL extraction and validation  
- Real-time threat scanning using VirusTotal  
- Displays detection count and risk verdict  
- CORS-enabled backend for frontend integration  
- Secure environment variable usage for API keys

## Python Skills Demonstrated

- RESTful API development using Flask  
- Third-party API integration (VirusTotal)  
- Secure handling of API keys using environment variables  
- File upload processing and input validation  
- JSON parsing and dynamic response rendering  
- CORS configuration for full-stack app separation

## Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
