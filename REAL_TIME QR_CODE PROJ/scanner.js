const video = document.getElementById('preview');
const resultDiv = document.getElementById('result');
const scanButton = document.getElementById('scanButton');

let scanning = false;
let lastScannedData = '';

scanButton.addEventListener('click', startScanning);

function startScanning() {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
        .then((stream) => {
            video.srcObject = stream;
            video.setAttribute('playsinline', true);
            video.play();
            scanning = true;
            requestAnimationFrame(scanFrame);
        })
        .catch(error => {
            alert('Error accessing camera: ' + error.message);
        });
}

function scanFrame() {
    if (video.readyState === video.HAVE_ENOUGH_DATA && scanning) {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
        const code = jsQR(imageData.data, canvas.width, canvas.height);

        if (code && code.data !== lastScannedData) {
            lastScannedData = code.data;
            resultDiv.textContent = `QR Code Data: ${code.data}`;
            scanning = false;
            analyzeQRCode(code.data);
        }
    }
    requestAnimationFrame(scanFrame);
}

function analyzeQRCode(data) {
    fetch('http://localhost:5000/api/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ qrCodeData: data }),
    })
    .then(response => response.json())
    .then(responseData => {
        if (responseData.isMalicious) {
            alert("Malicious QR Code Detected!");
        } else {
            alert("QR Code is Safe.");
        }
    })
    .catch(error => {
        alert('Error analyzing QR Code: ' + error.message);
    })
    .finally(() => {
        scanning = true;
        lastScannedData = '';
    });
}
