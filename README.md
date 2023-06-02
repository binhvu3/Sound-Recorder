# Sound-Recorder
Python module for recording audio and saving it as a file using sounddevice library. Provides customizable duration, output directory, and file format (WAV, MP3, FLAC). Easy integration for audio capture.

# Features
- Record audio with customizable duration
- Save recordings in various formats: WAV, MP3, FLAC
- Specify the output directory for saving the audio files
- Easy integration into your Python projects

# Installation

1. Ensure you have Python installed (version 3.6 or above).
2. Install the required dependencies by running the following command:

````
pip install sounddevice
````

# Usage

```
from voice_recorder import VoiceRecorder

# Create a VoiceRecorder instance
recorder = VoiceRecorder(duration=10, output_path="./recordings/", file_format="wav")

# Start recording
recording_path = recorder.start_record()
print("Recording saved at:", recording_path)
```

In the above example, we create a VoiceRecorder instance with a recording duration of 10 seconds. The audio file will be saved in the "recordings" directory with the WAV format. The start_record() method is then called to begin the recording process, and the path to the saved recording is printed.

Feel free to adjust the parameters according to your requirements.



# Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
