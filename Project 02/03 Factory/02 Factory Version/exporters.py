"""
Exporter Classes
"""

import pathlib
from abc import ABC, abstractclassmethod


# Video Exporter Classes ---------------------------------
class VideoExporter(ABC):
    '''Basic represention of video exporting codec.'''

    @abstractclassmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting"""

    @abstractclassmethod
    def do_export(self, folder: pathlib.Path):
        """Export the video data to a folder"""


class HighQualityVideoExporter(VideoExporter):
    """High quality exporting codec."""

    def prepare_export(self, video_data):
        print(f'Preparing video data for High Quality export')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data in High Quality format to "{folder}"')


class MediumQualityVideoExporter(VideoExporter):
    """Medium quality exporting codec."""

    def prepare_export(self, video_data):
        print(f'Preparing video data for Medium Quality export')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data in Medium Quality format to "{folder}"')


class LowQualityVideoExporter(VideoExporter):
    """Low quality exporting codec."""

    def prepare_export(self, video_data):
        print(f'Preparing video data for Low Quality export')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting video data in Low Quality format to "{folder}"')


# Audio Exporter Classes ------------------------------
class AudioExporter(ABC):
    '''Basic represention of audio exporting codec.'''

    @abstractclassmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""

    @abstractclassmethod
    def do_export(self, folder: pathlib.Path):
        """Export the audio data to a folder"""


class HighQualityAudioExporter(AudioExporter):
    """High quality exporting codec."""

    def prepare_export(self, audio_data):
        print(f'Preparing audio data for High Quality export')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio data in High Quality format to "{folder}"')


class MediumQualityAudioExporter(AudioExporter):
    """Medium quality exporting codec."""

    def prepare_export(self, video_data):
        print(f'Preparing audio data for Medium Quality export')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio data in Medium Quality format to "{folder}"')


class LowQualityAudioExporter(AudioExporter):
    """Low quality exporting codec."""

    def prepare_export(self, video_data):
        print(f'Preparing audio data for Low Quality export')

    def do_export(self, folder: pathlib.Path):
        print(f'Exporting audio data in Low Quality format to "{folder}"')