import os
from flask import Flask, render_template, request
import whisper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize():
    # Check if audio file was uploaded
    if 'file' not in request.files:
        return render_template('index.html', error='No audio file uploaded')

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No audio file selected')

    # Save the uploaded audio file
    audio_path = 'audio.wav'
    #file.save(audio_path)

    # Perform speech recognition
    transcription = transcribe_audio(audio_path)
    
    text = transcription['text']

    # Delete the temporary audio file
    os.remove(audio_path)

    return render_template('index.html', transcription=text)

def transcribe_audio(audio_path):
    # Load the Whisper model
    model = whisper.load_model("base")

    # Perform speech recognition using the Whisper model
    result = model.transcribe(audio_path)

    return result

if __name__ == '__main__':
    app.run(debug=True,port=52323)

