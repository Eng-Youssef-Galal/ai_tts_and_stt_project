# AI Text-to-Speech and Speech-to-Text Project

This repository contains code and resources for an AI-based project that focuses on text-to-speech (TTS) and speech-to-text (STT) functionalities. The project aims to provide an automated solution for converting text to voice and voice to text using artificial intelligence techniques.

## Features

- Convert text to voice using AI-based Text-to-Speech technology.
- Convert voice to text using AI-based Speech-to-Text technology.
- Integration of speech processing and text processing modules.
- Business logic implementation for handling different user intents.
- Web application for user interaction and testing.

## Getting Started

To get started with the project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/Eng-Youssef-Galal/ai_tts_and_stt_project.git
   ```

2. Install the required dependencies. Refer to the `requirements.txt` file for the specific packages and versions needed.

   ```bash
   pip install -r requirements.txt
   ```

3. Run the web application:

   ```bash
   python streamlit_app.py
   ```

   The application will be accessible at `http://localhost:8501`.

4. Use the provided web interface to interact with the TTS and STT functionalities.

## Project Structure

The repository is organized as follows:

- `business_logic.py`: Contains the implementation of business logic for handling different user intents.
- `speech_processing.py`: Provides functions for converting voice data to text and text to voice using speech recognition and text-to-speech services.
- `text_processing.py`: Includes functions for processing text inputs, extracting intents and locations, and retrieving data from a database.
- `streamlit_app.py`: Implements a web application using Streamlit for user interaction and testing.
- `requirements.txt`: Lists the required packages and their versions for easy installation.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

# Screenshot for the final webapp
![app](https://github.com/Eng-Youssef-Galal/ai_tts_and_stt_project/assets/138930263/772ec337-a415-4281-a38f-5c97fdf1d05f)
