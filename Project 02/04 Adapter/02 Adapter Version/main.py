from pathlib import Path
from utils import read_config_from_file
from experiment import Experiment


def main(file_path) -> None:
    config = read_config_from_file(file_path)
    experiment = Experiment(config)
    experiment.run()


if __name__ == "__main__":

    file_path = Path("data/config.json")
    main(file_path)