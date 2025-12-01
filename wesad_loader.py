# wesad_loader.py
import os
from typing import Dict, Any, List

import numpy as np
import pandas as pd

# Default base path – adjust if your unzip created a different folder name
WESAD_PATH = "data/WESAD"

# Files we care about from the Empatica E4 device
E4_FILES = ["ACC", "BVP", "EDA", "HR", "IBI", "TEMP", "tags"]


def _read_signal_csv(path: str) -> np.ndarray:
    """
    Read a 1-column CSV into a 1D numpy array.
    WESAD CSVs have no header, just one value per line.
    """
    return pd.read_csv(path, header=None).values.squeeze()


def load_subject_e4(subject_id: str,
                    base_path: str = WESAD_PATH) -> Dict[str, Any]:
    """
    Load Empatica E4 wrist signals for one subject.

    Parameters
    ----------
    subject_id : str
        Subject folder name, e.g. "S2", "S3", ...
    base_path : str
        Root WESAD folder that contains S2, S3, ... subfolders.

    Returns
    -------
    data : dict
        {
            "acc":  np.ndarray,  # accelerometer
            "bvp":  np.ndarray,  # blood volume pulse
            "eda":  np.ndarray,  # skin conductance
            "hr":   np.ndarray,  # heart rate
            "ibi":  np.ndarray,  # inter-beat interval
            "temp": np.ndarray,  # skin temperature
            "tags": np.ndarray,  # condition markers
            "meta": dict         # parsed info.txt (sampling rates, etc.)
        }
    """
    subj_dir = os.path.join(base_path, subject_id)
    e4_dir = os.path.join(subj_dir, f"{subject_id}_E4_Data")

    if not os.path.isdir(e4_dir):
        raise FileNotFoundError(
            f"E4 folder not found for subject {subject_id} at {e4_dir}"
        )

    data: Dict[str, Any] = {}

    # Load the core signals
    for name in E4_FILES:
        csv_path = os.path.join(e4_dir, f"{name}.csv")
        if os.path.exists(csv_path):
            data[name.lower()] = _read_signal_csv(csv_path)
        else:
            # For robustness: don’t crash if one file is missing
            print(f"[wesad_loader] WARNING: {csv_path} not found")

    # Try to parse info.txt for metadata (sampling rates etc.)
    info_path = os.path.join(e4_dir, "info.txt")
    meta: Dict[str, str] = {}
    if os.path.exists(info_path):
        with open(info_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line or ":" not in line:
                    continue
                key, val = [x.strip() for x in line.split(":", 1)]
                meta[key] = val
    data["meta"] = meta

    return data


def list_subjects(base_path: str = WESAD_PATH) -> List[str]:
    """
    Convenience helper: list all S* subject folders under base_path.
    """
    if not os.path.isdir(base_path):
        raise FileNotFoundError(f"WESAD base path not found: {base_path}")

    return sorted(
        d for d in os.listdir(base_path)
        if d.startswith("S") and os.path.isdir(os.path.join(base_path, d))
    )
