import json
from datetime import datetime

def log_params_json(filename, params, results):
    filepath = f"logs/{filename}.json"
    entry = {
        "timestamp": datetime.now().isoformat(),
        "parameters": params,
        "results": results
    }
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
