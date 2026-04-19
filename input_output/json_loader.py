import json

def load_json(path="data.json"):
    with open(path, "r") as f:
        return json.load(f)