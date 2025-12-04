# Multimodal Physiological Signals for Predicting Risky Financial Decisions
_CP322 - Group 9_

## 1. Overview
This project investigates whether physiological arousal and market context jointly predict risky investment decisions under uncertainty.
---
### We use two datasets:
- **Affective Economics (AE)** — trial-level anticipatory skin conductance response (SCR), stock context (mean return, volatility), and binary investment decisions. https://researchdata.bath.ac.uk/699/

- **WESAD** - wearable electrodermal activity (EDA) collected during stress / baseline tasks, used as an external physiological validation dataset. https://www.kaggle.com/datasets/orvile/wesad-wearable-stress-affect-detection-dataset/discussion?sort=hotness
  
---

## Our central question:
Does anticipatory arousal (measured via SCR/EDA) meaningfully predict investment risk-taking, beyond what market information alone explains?

**Key Takeaways**
1. Physiological features alone achieve ~0.88–0.89 accuracy (logistic regression + MLP).
Market context alone performs similarly (~0.88) but does not outperform physiology.
2. Combined multimodal features (SCR + market) yield the most stable and highest test accuracy (~0.96) using an MLP.
3. WESAD analysis shows that EDA-based arousal features are generalizable across tasks, supporting physiological validity.

## **What this repo contains**
- Complete AE preprocessing
- AE SCR + market feature engineering
- WESAD EDA loading and window-based feature extraction
- Logistic Regression baseline
- PyTorch MLP and PhysioEncoder classifier
- Ablation study
- Full visualization suite (SCR trajectories, market signals, distributions, correlations, confusion   matrices, loss curves)

*Everything can be reproduced through a single Jupyter Notebook.*

## 2. Repository Structure
```
├── cp322_FINAL.ipynb          # Main end-to-end notebook for entire project
├── wesad_loader.py            # Helper for reading WESAD subject files
├── DATASET/
│   └── AE_investment_dataset.csv  # AE dataset (included)
├── README.md                   # This file
├── Multimodal Physiological Representation Learning for Predicting Risky Financial Decisions.PDF  #our IEEE style Machine Learning analysis paper!
├── MPRL for Financial Risks.PDF #Slide deck for presentation! 


├── google drive/
│   └── WESAD/                  # WESAD raw data (download via Kaggle), mounted to your google drive when you run the kaggle.JSON api :)
```
## 3. Environment Setup

Ensure you have a google account. 
On the ipynb file within this repository, the easiest way to run the notebook would be to click 'view in colab' and click 'run all' from there!

## 4. Data Access
--
### 4.1 University of Bath Affective Economics Dataset
The AE investment dataset is already provided to you within this github repo as a .csv file.
### 4.2 WESAD Dataset (Downloaded via Kaggle API)
WESAD is too large for GitHub. Download it directly into the colab environment.
**Step A** — Install & configure Kaggle
Get your kaggle.json from Kaggle:
- Account → API → Create New Token
- make a new file in your editor called 'kaggle.JSON' and format it as:
```

{ "username": "YOURKAGGLEUSERNAME",
    "key": "YOURKAGGLEAPIKEY"
}

```

Run the Google Colab IPYNB file as intended by clicking 'run all'. When prompted by section 1.2 with a 'choose file' input, input your kaggle.JSON file from your devices' directory

###Structure
```
DATASET/WESAD/
    ├── S2/
    │   └── S2_E4_Data/
    │       ├── ACC.csv
    │       ├── EDA.csv
    │       ├── TEMP.csv
    │       └── ...
    ├── S3/
    └── ...


```
## 5. Running the Project
Run the sections sequentially on the Colab file.

## 5. AE Data Pipeline (Main Dataset)
<img width="2120" height="1405" alt="image" src="https://github.com/user-attachments/assets/0e5daa15-9954-40f7-bae8-36accc88f82d" />


### 5.1 Cleaning & Transformation
The AE dataset was provided in wide format. We:
- Removed missing SCR values  
- Reconstructed all trials and sessions  
- Converted wide → long format  
- Produced a 1,200-row trial-level dataset (30 participants × 40 trials)  

### 5.2 SCR Feature Engineering
We engineered dynamic physiological features, including:
- Raw anticipatory SCR  
- Participant-normalized SCR (z-score)  
- SCR slope  
- Lag features (previous trial SCR)  
- SCR deltas (trial-to-trial change)  
- Rolling window statistics (3-trial mean, std)  

### 5.3 Market Feature Engineering
We extracted contextual financial variables:
- Expected return per trial  
- Stock fluctuation (volatility)  
- Combined contextual signal  

### 5.4 Visualization Suite (Appendix)
Visualizations include:
- SCR time series per participant  
- 30-participant SCR overview grid  
- Market return and volatility trajectories  
- SCR distribution & per-participant averages  
- Investment rate per participant  
- SCR → P(invest) logistic curve  
- Correlation matrix  
(See Appendix section in the manuscript.)

## 7. Ablation Study

We compare three feature sets:

| Model Type      | Inputs                 | Accuracy |
|-----------------|------------------------|----------|
| SCR-only        | physiological only     | ~0.88    |
| Market-only     | return + volatility    | ~0.88    |
| Combined (MLP)  | physiology + market    | ~0.96    |

**Findings:**
- SCR-only ≈ Market-only → physiology is equally predictive  
- Combined features yield strongest results  
- Market variables alone cannot capture “not invest” behaviour  
- Physiological arousal contains unique information about avoidance decisions  

## 8. WESAD Pipeline (External Physiological Validation) (Figures provided in ipynb)

### 8.1 EDA Loading (Figures provided in paper & ipynb)
Using `wesad_loader.py`, we extract:
- EDA/SCR  
- ECG  
- Accelerometer  
- Temperature  
- Respiration  
- Heart rate & IBI  
- Metadata and ground-truth emotional labels  

### 8.2 Window-Based Feature Engineering (Figures provided in ipynb)
We segment continuous EDA into **60-second windows** with **30-second overlap**.

Extracted features:
- mean  
- standard deviation  
- max  
- min  
- slope  

### 8.3 WESAD Baseline Classifier (Figures provided in paper & ipynb)
A logistic regression baseline on windowed WESAD features achieves:
- Accuracy: ~0.80–0.82  

This demonstrates strong discriminability between **high** and **low** arousal states and supports the use of physiologically-derived features in the AE dataset.
## 9. Reproducing Main Results

### 9.1 AE Logistic Regression Baseline (Figures provided in paper & ipynb)
Run AE → preprocessing → LR code block.  
Expected:
- ACC ≈ 0.88  
- F1 ≈ 0.94  

### 9.2 AE MLP (Figures provided in paper & ipynb)
Run the MLP training block.  
Expected:
- ACC ≈ 0.96  
- F1 ≈ 0.98  

### 9.3 Ablation Study (Figures provided in paper & ipynb)
Run the ablation section.  
Expected:
- SCR-only ≈ 0.88  
- Market-only ≈ 0.88  
- Combined ≈ 0.96  

### 9.4 WESAD Classifier (Figures provided in paper & ipynb)
Run WESAD preprocessing → logistic regression.  
Expected:
- ACC ≈ 0.80–0.82  

## 10. Limitations

- AE dataset contains only 30 participants → limited generalization  
- WESAD labels are coarse and collected in a different context  
- Physiological variability across participants required within-subject normalization  
- Time constraints limited hyperparameter tuning  
- Only EDA/SCR was modeled, not full multimodal signals (ECG, EMG, etc.)  
## 11. Authors & Contribution Summary

This project was completed by Group 9 for CP322 (Machine Learning).  
A summary of roles is included in the paper and repeated here.

### Michelle Chala
- Selected datasets & research question  
- Built GitHub repo & Colab environment  
- Full AE preprocessing pipeline  
- SCR + market feature engineering  
- Visualization suite (all figures, statistical plots, trajectories)  
- WESAD loader integration  
- MLP model & PhysioEncoder  
- Ablation experiments  
- Report writing, appendix, and README  

### Jay Patel
- Main manuscript writing (Abstract, Introduction, Methodology, Analysis)  
- Modeling support & validation diagnostics  
- Experiment replication  
- Slide preparation & presentation
- Formatted the final IEEE paper
- Reviewed code on the GitHub repository, completed the
Experiments and Results section

### Other Members
- Limited contributions as detailed in the Group Contribution Table in the appendix of the final report.


## 12. Appendix Overview (Referenced in Notebook & Report)

The Appendix (in the report) contains:

### 12.1 AE Exploratory Plots
- Per-participant SCR time series  
- 30-participant SCR grid  
- Market signal time series  
- SCR distribution & per-participant means  
- Investment rate per participant  

### 12.2 SCR–Investment Diagnostics
- Correlation heatmaps  
- Logistic regression curve (trial-level SCR → P(invest))  

### 12.3 Model Diagnostics
- Confusion matrix  
- Loss curves  
- Ablation chart  

### 12.4 WESAD Supplementary
- Console loader logs  
- Window segmentation examples  
- Baseline WESAD classifier output  
- AE vs WESAD EDA distribution comparison  

### 12.5 Kaggle API (WESAD)
- Full programmatic download instructions  
- Exact path structure  

## 13. Final Notes

This repository provides a complete, reproducible pipeline for analyzing how **physiological arousal** and **market context** influence risky financial decisions. All figures, analyses, and models can be reproduced by running:


  
