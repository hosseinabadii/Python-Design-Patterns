import pathlib
from factory import read_exporter, ExporterFactory

def main(fac: ExporterFactory) -> None:
    """Main function"""

    # get video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export('placeholder_for_video_data')
    audio_exporter.prepare_export('placeholder_for_audio_data')

    # do the export
    folder = pathlib.Path('./video')
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == '__main__':

    fac = read_exporter()
    main(fac)