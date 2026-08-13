# PyVoiceAI

### Intelligent Voice Interaction with Python

PyVoiceAI is a lightweight voice assistant built with Python that combines **speech recognition** and **text-to-speech** to create a simple, hands-free human–computer interaction experience.

Designed with a clean and minimal architecture, the project focuses on making voice interaction easy to understand, extend, and run locally.

---

## Overview

PyVoiceAI listens to spoken commands through the microphone, processes the recognized speech, and responds using synthesized voice.

The project demonstrates the core building blocks behind voice-enabled applications while keeping the implementation lightweight and beginner-friendly.

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
Voice Response
    │
    ▼
Text-to-Speech
```

---

## Key Capabilities

* **Speech Recognition** — Converts spoken input into text.
* **Voice Response** — Converts generated responses into natural speech.
* **Real-Time Interaction** — Enables continuous microphone-based interaction.
* **Lightweight Architecture** — Uses a small set of focused Python libraries.
* **Extensible Design** — Provides a foundation for adding commands and intelligent features.

---

## Technology Stack

| Technology            | Role                                 |
| --------------------- | ------------------------------------ |
| **Python**            | Core application logic               |
| **SpeechRecognition** | Speech-to-text processing            |
| **pyttsx3**           | Text-to-speech synthesis             |
| **PyAudio**           | Microphone and audio stream handling |

---

## Project Structure

```text
PyVoiceAI/
│
├── main.py              # Application entry point
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git exclusions
└── LICENSE              # Project license
```

---

## Getting Started

### Prerequisites

Make sure you have:

* Python 3.x
* A working microphone
* Internet access where required by the configured speech-recognition service

### 1. Clone the repository

```bash
git clone https://github.com/bhoomijn/PyVoiceAI.git
cd PyVoiceAI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch PyVoiceAI

```bash
python main.py
```

Allow microphone access when prompted and start interacting with the assistant.

---

## Requirements

Dependencies are maintained in [`requirements.txt`](requirements.txt).

```text
SpeechRecognition
pyttsx3
PyAudio
```

---

## How It Works

PyVoiceAI follows a simple voice-processing pipeline:

**1. Listen**
The application captures audio through the system microphone.

**2. Recognize**
Speech recognition converts the captured audio into text.

**3. Process**
The recognized command is handled by the Python application.

**4. Respond**
The assistant generates a response.

**5. Speak**
`pyttsx3` converts the response into audible speech.

---

## Future Scope

The project can be extended with:

* Custom voice commands
* Web search capabilities
* Application and system automation
* Weather and news integrations
* AI-powered conversational responses
* Modular command handling
* Personalized assistant settings

---

## Project Goals

PyVoiceAI was created to explore practical concepts in:

* Voice-based interfaces
* Speech recognition
* Text-to-speech systems
* Python automation
* Human–computer interaction

The architecture is intentionally simple so that new capabilities can be added without making the core project unnecessarily complex.

---

## Author

**Bhoomi Jain**

GitHub: [@bhoomijn](https://github.com/bhoomijn)

---

## License

This project is licensed under the **MIT License**.

---

<p align="center">
  Built with Python • Speech Recognition • Voice Technology
</p>
