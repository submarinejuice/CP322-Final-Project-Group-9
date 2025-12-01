import os
import numpy as np
import pandas as pd

WESAD_PATH = "'/Users/michellesavage/Desktop/year 4/WESAD'"  

def load_subject_e4(subject_id: str, base_path: str = WESAD_PATH):
    subj_dir = os.path.join(base_path, subject_id)
    e4_dir = os.path.join(subj_dir, f"{subject_id}_E4_Data")

    eda = pd.read_csv(os.path.join(e4_dir, "EDA.csv"), header=None)
    hr = pd.read_csv(os.path.join(e4_dir, "HR.csv"), header=None)
    temp = pd.read_csv(os.path.join(e4_dir, "TEMP.csv"), header=None)
    tags = pd.read_csv(os.path.join(e4_dir, "tags.csv"), header=None)

    # TODO: read sampling rates from info.txt and return everything in a dict
    return {
        "eda": eda.values.squeeze(),
        "hr": hr.values.squeeze(),
        "temp": temp.values.squeeze(),
        "tags": tags.values.squeeze()
    }
