# Speec-to-Text-WebApp

This is a web application that performs speech recognition on audio files. It allows you to upload an audio file (in .wav, .mp3, or .ogg format) and transcribes the speech content using an AI speech recognition model.

## Features

- Accepts .wav, .mp3, and .ogg audio file formats.
- Transcribes the speech content of the uploaded audio file.
- Displays the transcription result in a user-friendly interface.
- Provides a "Copy" button to easily copy the transcription text.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask (install using `pip install flask`)
- Whisper (install using `pip install openai-whisper`)


### Installation

1. Clone the repository:
   ```git clone https://github.com/hakunamatata1997/Speec-to-Text-WebApp.git```
   
3. Navigate to the project directory:
   ```cd speech-recognition-webapp```

4. Install the required dependencies:
    ```pip install -r requirements.txt```

### Usage

1. Start the Flask development server:
   ``` python app.py```

3. Open your web browser and go to `http://localhost:52323`.

4. Upload an audio file using the provided form.

5. Click the "Recognize Speech" button to initiate the transcription process.

6. The transcription result will be displayed on the page. You can copy the text by clicking the "Copy" button.


## Acknowledgments

- The Whisper ASR model used in this project is developed by OpenAI. Visit the [Whisper GitHub repository](https://github.com/openai/whisper) for more information.




