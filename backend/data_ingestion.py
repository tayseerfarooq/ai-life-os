import json

def load_google_fit_data():
    """
    Loads Google Fit data from JSON and returns parsed dictionary.
    """
    with open("/Users/tayseerfarooq/Documents/ai-life-os/data/google_fit_sample.json", 'r') as f:
        data = json.load(f)
    return data
