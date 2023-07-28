import json
import yaml


def write_json(fn: str, input_json):
    """
    Export dict or list to json files

    Parameters
    ---------
    fn : filename
    input_json: dict or list python
    """
    with open(fn, 'w') as f:
        json.dump(input_json, f)


def read_json(fn):
    """
    Read json files

    Parameters
    ---------
    fn : filename
    """
    with open(fn) as f:
        read_data = f.read()
    file_json = json.loads(read_data)
    return file_json


def read_yaml(fn: str) -> dict:
    """
    Read Yaml files

    Parameters
    ---
    fn: filename
    """
    with open(fn, 'r') as file:
        read_data = yaml.safe_load(file)
    return read_data
