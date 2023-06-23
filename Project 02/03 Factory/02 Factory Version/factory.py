"""
Exporter Factory
"""

from abc import ABC, abstractclassmethod

from exporters import (
    VideoExporter, LowQualityVideoExporter, MediumQualityVideoExporter, HighQualityVideoExporter,
    AudioExporter, LowQualityAudioExporter, MediumQualityAudioExporter, HighQualityAudioExporter,
)


class ExporterFactory(ABC):
    """
    Factory that represents a compination of video and audio codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractclassmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""

    @abstractclassmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance"""


class LowQualityExporter(ExporterFactory):
    """Factory aimed at providing a Low Quality Video and Audio exporters."""

    def get_video_exporter(self) -> VideoExporter:
        return LowQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return LowQualityAudioExporter()


class MediumQualityExporter(ExporterFactory):
    """Factory aimed at providing a Medium Quality Video and Audio exporters."""

    def get_video_exporter(self) -> VideoExporter:
        return MediumQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return MediumQualityAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a High Quality Video and Audio exporters."""

    def get_video_exporter(self) -> VideoExporter:
        return HighQualityVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return HighQualityAudioExporter()
    

def read_exporter() -> ExporterFactory:
    factories = {
        'low': LowQualityExporter(),
        'medium': MediumQualityExporter(),
        'high': HighQualityExporter(),
    }

    while True:
        export_quality = input('Enter desired output quality (low, medium, high):')
        if export_quality in factories:
            return factories[export_quality]
        print(f'unknown output auqlity option: {export_quality}')
