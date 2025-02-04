Readme.md
# AI Voice Agent

An AI-powered voice assistant built using **Ollama**, **NLP**, **Speech Recognition**, and **Text-to-Speech** technologies. This agent processes voice input, generates responses using **Ollama**'s models, and responds back in voice format.

## Features
- **Voice Input**: Takes voice commands from the user.
- **Intent Recognition**: Recognizes user intent (e.g., weather, time, news) using **spaCy**.
- **Text Generation**: Generates dynamic responses using **Ollama**'s models.
- **Voice Output**: Converts the generated response back into speech.

## Requirements
- Python 3.x
- Ollama (install from [ollama.com](https://ollama.com/download))
- `speechrecognition` library
- `pyttsx3` library
- `spaCy` library
- `ollama` library

## Installation

1. Install dependencies:
   ```bash
   pip install speechrecognition pyaudio pyttsx3 ollama spacy

2. python -m spacy download en_core_web_sm

3. ollama serve

4. python ai_voice_agent.py

