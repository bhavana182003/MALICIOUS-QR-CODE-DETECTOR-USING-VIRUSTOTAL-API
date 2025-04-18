-- Create the malicious_qrcodes table if it does not exist
CREATE TABLE IF NOT EXISTS malicious_qrcodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Insert a sample malicious QR code entry
INSERT INTO malicious_qrcodes (data) VALUES ('sample QR code data');
