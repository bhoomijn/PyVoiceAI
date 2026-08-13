# PyVoiceAI

### Intelligent Voice Interaction with Python

PyVoiceAI is a lightweight Python voice assistant that combines **speech recognition** and **text-to-speech** to create a simple, hands-free human–computer interaction experience.

Built with a minimal and modular approach, the project provides a clean foundation for developing voice-enabled Python applications.

---

## Overview

PyVoiceAI captures audio through a microphone, converts spoken input into text, processes the command, and responds through synthesized speech.

### Voice Pipeline

```text
Microphone
    │
    ▼
Speech Recognition
    │
    ▼
Command Processing
    │
    ▼
Response Generation
    │
    ▼
Text-to-Speech
```

---

## Features

* **Speech Recognition** — Converts spoken input into text.
* **Text-to-Speech** — Produces spoken responses using `pyttsx3`.
* **Real-Time Interaction** — Supports microphone-based voice interaction.
* **Lightweight Architecture** — Built with a focused set of Python libraries.
* **Extensible Foundation** — Designed to support additional commands and features.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core application logic |
| **SpeechRecognition** | Speech-to-text processing |
| **pyttsx3** | Text-to-speech synthesis |
| **PyAudio** | Microphone and audio input |

---

## Project Structure

```text
PyVoiceAI/
│
├── main.py              # Application entry point
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
├── .gitignore           # Git exclusions
└── LICENSE              # Project license
```

---

## Getting Started

### Prerequisites

Before running PyVoiceAI, make sure you have:

* Python 3.x
* A working microphone
* Required audio permissions
* Internet access if required by the configured speech-recognition service

### 1. Clone the Repository

```bash
git clone https://github.com/bhoomijn/PyVoiceAI.git
cd PyVoiceAI
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Assistant

```bash
python main.py
```

Allow microphone access when prompted and start interacting with PyVoiceAI.

---

## Dependencies

The project dependencies are maintained in [`requirements.txt`](requirements.txt).

```text
SpeechRecognition
pyttsx3
PyAudio
```

---

## How It Works

### 01 — Listen

PyVoiceAI captures audio input through the system microphone.

### 02 — Recognize

The speech-recognition layer converts the captured audio into text.

### 03 — Process

The Python application processes the recognized input.

### 04 — Respond

The assistant prepares an appropriate response.

### 05 — Speak

`pyttsx3` converts the response into audible speech.

---

## Future Scope

The architecture can be extended with:

* Custom voice commands
* Web search integration
* System and application automation
* Weather and news services
* AI-powered conversational capabilities
* Modular command handlers
* Personalized assistant preferences

---

## Project Objective

PyVoiceAI was developed to explore practical concepts in:

* Voice-based interfaces
* Speech recognition
* Text-to-speech systems
* Python automation
* Human–computer interaction

The project focuses on keeping the core implementation simple while providing a foundation for future voice-assistant capabilities.

---

## Author

**Bhoomi Jain**

[GitHub Profile](https://github.com/bhoomijn)

---

## License

This project is licensed under the **MIT License**.

---

<p align="center">
  Built with Python • Speech Recognition • Text-to-Speech
</p>
