from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from pydub import AudioSegment
import random
import string

app = Flask(__name__)
app.config['APP_URL'] = 'https://from-wav-to-mp3.e3lanotopia.software'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Set the maximum file size to 50MB
app.config['ALLOWED_EXTENSIONS'] = {'wav'}
CORS(app, resources={r"/*": {"origins": "*"}})

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        try:
            # Generate a random name for the file
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], random_name + '.wav')
            mp3_file_path = os.path.join(app.config['UPLOAD_FOLDER'], random_name + '.mp3')

            file.save(file_path)

            # Convert the WAV file to MP3
            sound = AudioSegment.from_wav(file_path)
            sound.export(mp3_file_path, format='mp3')

            # Clean up: delete the WAV file
            os.remove(file_path)

            return jsonify({'url': f"{app.config['APP_URL']}/{os.path.basename(mp3_file_path)}"}) 
        except Exception as e:
            # Error handling for conversion process
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory(app.config['UPLOAD_FOLDER'], path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=2001)
