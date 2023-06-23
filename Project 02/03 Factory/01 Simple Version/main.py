import pathlib

from exporters import (
    VideoExporter, LowQualityVideoExporter, MediumQualityVideoExporter, HighQualityVideoExporter,
    AudioExporter, LowQualityAudioExporter, MediumQualityAudioExporter, HighQualityAudioExporter,
)


def main() -> None:
    """Main function"""

    # read the desired quality
    export_quality: str
    while True:
        export_quality = input('Enter desired output quality (low, medium, high):')
        if export_quality in {'low', 'medium', 'high'}:
            break
        print(f'Unknown output quality option: {export_quality}')

    # create the video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == 'low':
        video_exporter = LowQualityVideoExporter()
        audio_exporter = LowQualityAudioExporter()

    elif export_quality == 'high':
        video_exporter = HighQualityVideoExporter()
        audio_exporter = HighQualityAudioExporter()

    else:
        video_exporter = MediumQualityVideoExporter()
        audio_exporter = MediumQualityAudioExporter()

    # prepare the export
    video_exporter.prepare_export('placeholder_for_video_data')
    audio_exporter.prepare_export('placeholder_for_audio_data')

    # do the export
    folder = pathlib.Path('./video')
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == '__main__':
    main()