from pathlib import Path
import json
from bs4 import BeautifulSoup

from config_adapter import XMLConfig, Config

def read_config_from_file(file_path: Path) -> tuple[Config, dict]:
    suffix = file_path.suffix
    suffixes = {".xml", ".json"}
    if suffix not in suffixes:
        raise Exception(f"Not supported file suffix {suffix!r}")

    with open(file_path, encoding="utf8") as file:
        if suffix == ".json":
            config = json.load(file)

        elif suffix == ".xml":
            bs = BeautifulSoup(file.read(), "xml")
            config = XMLConfig(bs)

    return config
