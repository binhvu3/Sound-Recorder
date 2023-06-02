"""
Voice Recorder Module

This module provides a VoiceRecorder class that allows recording audio 
using the sounddevice library and saving it as a file.

Dependencies:
- sounddevice

Example usage:
    recorder = VoiceRecorder(duration=10, output_path="./recordings/", file_format="wav")
    recording_path = recorder.start_record()
    print("Recording saved at:", recording_path)

"""

import time
import os
import sounddevice as sd
import soundfile as sf


class VoiceRecorder:
    """
    VoiceRecorder is a class that allows recording audio
    using the sounddevice library and saving it as a file.

    Args:
        duration (int, optional): The duration of
        the recording in seconds. Defaults to 5.
        output_path (str, optional): The directory where
        the audio file will be saved. Defaults to "./audio/".
        file_format (str, optional): The format of the audio
        file. Accepted formats: WAV, MP3, and FLAC. Defaults to "wav".
    """

    SUPPORTED_FORMATS = {"wav", "mp3", "flac"}
    DEFAULT_FORMAT = "wav"
    SAMPLE_RATE = 44100

    def __init__(self, duration=5, output_path="./recordings/", file_format="wav"):
        """
        Initializes a new instance of the VoiceRecorder class.

        Args:
            duration (int, optional): The duration of the recording in seconds. Defaults to 5.
            output_path (str, optional): The directory where the audio file will be saved.
            Defaults to "./recordings/".
            file_format (str, optional): The format of the audio file. Accepted formats:
            WAV, MP3, and FLAC. Defaults to "wav".
        """

        self.duration = duration
        self.output_path = output_path
        self.file_format = file_format.lower()

        self.validate_path()
        self.validate_format()

    def validate_path(self):
        """
        Validates the output directory path and creates it if it doesn't exist.

        Raises:
            FileNotFoundError: If the specified directory or any intermediate directory
            doesn't exist and cannot be created.
            PermissionError: If the user does not have permission to create the directory.
        """

        try:
            os.makedirs(self.output_path, exist_ok=True)

        except (FileNotFoundError, PermissionError) as error:
            print("Error occurred while creating the directory:", error)

    def validate_format(self):
        """
        Validates the audio file format and sets it to the default format if not supported.
        """

        if self.file_format not in self.SUPPORTED_FORMATS:
            print(
                "Audio file format is not supported. Accepted formats: WAV, MP3, and FLAC."
            )
            print("Using default value: WAV")
            self.file_format = self.DEFAULT_FORMAT

    def start_record(self):
        """
        Starts the audio recording.

        Returns:
            str: The path to the recorded audio file.
        """

        print("Recording...")
        recording = sd.rec(
            int(self.duration * self.SAMPLE_RATE),
            samplerate=self.SAMPLE_RATE,
            channels=1,
        )
        sd.wait()

        output_path = os.path.join(
            self.output_path, f"{int(time.time())}.{self.file_format}"
        )
        sf.write(output_path, recording, self.SAMPLE_RATE)

        return output_path


recorder = VoiceRecorder(duration=5, output_path="./recordings/", file_format="wavf")
recording_path = recorder.start_record()
print("Recording saved at:", recording_path)
