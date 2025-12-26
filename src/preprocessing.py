import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def prepare_frequency_data(df):
    df_freq = df.copy()
    df_freq["log_exposure"] = np.log(df_freq["Exposure"])
    freq_cols = ["ClaimNb", "VehPower", "VehAge", "DrivAge", "BonusMalus", "Density", "log_exposure"]
    return df_freq[freq_cols]

def prepare_severity_data(df):
    df_sev = df[df["ClaimNb"] > 0].copy()
    sev_cols = ["ClaimAmount", "VehPower", "VehAge", "DrivAge", "BonusMalus", "Density"]
    return df_sev[sev_cols]
