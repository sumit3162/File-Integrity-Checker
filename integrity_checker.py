import os
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Database to store file hashes (in-memory for demo)
file_hashes = {}

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate file hash using specified algorithm."""
    hash_func = getattr(hashlib, algorithm)()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)
    return hash_func.hexdigest()

@app.route('/scan', methods=['POST'])
def scan_files():
    """Scan a directory and store file hashes."""
    data = request.json
    directory = data.get('directory')
    if not directory or not os.path.isdir(directory):
        return jsonify({"error": "Invalid directory"}), 400

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)
            file_hashes[file_path] = file_hash

    return jsonify({"message": "Scan completed", "files_scanned": len(file_hashes)})

@app.route('/check', methods=['POST'])
def check_integrity():
    """Check if files have been modified."""
    data = request.json
    directory = data.get('directory')
    if not directory or not os.path.isdir(directory):
        return jsonify({"error": "Invalid directory"}), 400

    modified_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in file_hashes:
                modified_files.append({"file": file_path, "status": "NEW"})
                continue
            current_hash = calculate_hash(file_path)
            if current_hash != file_hashes[file_path]:
                modified_files.append({"file": file_path, "status": "MODIFIED"})

    return jsonify({"modified_files": modified_files})

if __name__ == '__main__':
    app.run(debug=True)