# Hand-Gesture-Recognition

## Overview
The Hand Gesture Control Tool is a real-time application that allows users to interact with their computer using hand gestures. Utilizing computer vision techniques, this tool detects hand movements and translates them into keyboard inputs, enabling users to navigate their system hands-free.

## Features
- **Real-Time Hand Tracking**: Utilizes MediaPipe to detect and track hand landmarks in real-time.
- **Gesture Recognition**: Recognizes up to five different gestures based on finger counts and performs corresponding keyboard actions.
- **User-Friendly Interface**: Provides a simple interface to visualize hand gestures through the webcam.
- **Keyboard Control**: Maps gestures to keyboard actions, such as moving the cursor, clicking, and scrolling.
- **Customizable Controls**: Allows users to modify the keyboard mappings for gestures according to their preferences.

## Technologies Used and their versions:
- Python (`python.exe` - Python 3.12.6)
- OpenCV (`opencv-python` - 4.10.0.84)
- MediaPipe (`mediapipe` - 0.10.14)
- PyAutoGUI (`pyautogui` - 0.9.54)

## Getting Started
To run the application locally:
   - Create Virtual Environment
   - `python -m venv venv`
   - Activate virtual environment `.\venv\Scripts\activate`
   - Virtual Environment is Started!
   - Install python site-packages `pip install -r /path/to/requirements.txt`
   - run `python mediaplayer.py runserver`

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hand-gesture-control-tool.git
   cd hand-gesture-control-tool
