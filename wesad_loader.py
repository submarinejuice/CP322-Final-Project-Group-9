import os
import numpy as np
import pandas as pd

# Default path to where the WESAD dataset E4 folders live on this machine.
# Remove the surrounding single-quotes if you copied a path that included them.
WESAD_PATH = "/Users/michellesavage/Desktop/year 4/WESAD"


def load_subject_e4(subject_id: str, base_path: str = WESAD_PATH):
    """
    Load E4 sensor CSVs for a given subject from the WESAD dataset.

    Returns a dict with keys: 'eda', 'hr', 'temp', 'tags' (numpy arrays).
    Raises FileNotFoundError with a helpful message if files/directories are missing.
    """
    base_path = os.path.expanduser(base_path)
    subj_dir = os.path.join(base_path, subject_id)
    e4_dir = os.path.join(subj_dir, f"{subject_id}_E4_Data")

    if not os.path.isdir(e4_dir):
        raise FileNotFoundError(
            f"E4 directory not found: {e4_dir!r}. Check `WESAD_PATH` and the provided subject_id."
        )

    def _read_array(filename: str) -> np.ndarray:
        path = os.path.join(e4_dir, filename)
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Missing expected file: {path!r}")
        df = pd.read_csv(path, header=None)
        # flatten/convert to 1D array when appropriate
        arr = df.values
        try:
            return arr.squeeze()
        except Exception:
            return arr

    eda = _read_array("EDA.csv")
    hr = _read_array("HR.csv")
    temp = _read_array("TEMP.csv")
    tags = _read_array("tags.csv")

    # TODO: read sampling rates from info.txt and return them too
    return {
        "eda": eda,
        "hr": hr,
        "temp": temp,
        "tags": tags,
    }
