# Multimodal Physiological Representation Learning for Predicting Risky Financial Decisions

## 📋 Project Overview
This project investigates whether physiological arousal can predict risky financial decisions. We combine market context data with skin conductance responses (SCR) to build predictive models, and explore whether physiological patterns learned from a wearable stress dataset (WESAD) can transfer to financial decision-making.

## 🎯 Research Questions
1. **Primary**: Can we predict whether a participant will invest in a risky asset from market context + physiological arousal?
2. **Secondary**: Do we see comparable physiological signatures in a real-world wearable dataset (WESAD), and can we learn a shared representation that transfers across tasks?

## 📁 Datasets

### **1. Affective Economics (AE) Dataset**
- **Source**: Internal research dataset obtained for academic purposes
- **Access**: Included in this repository at `DATASET/AE_investment_dataset.csv`
- **Description**: 40 investment trials per participant with:
  - Anticipatory Skin Conductance Response (SCR)
  - Market context (mean return, volatility)
  - Investment decisions (money allocated to stocks)
  - Participant demographics (age, gender, etc.)
- **Note**: This dataset was provided for this course project. For research use, please contact the original researchers or seek appropriate permissions.

### **2. WESAD (Wearable Stress and Affect Detection) Dataset**
- **Source**: [Kaggle - WESAD Dataset](https://www.kaggle.com/datasets/orvile/wesad-wearable-stress-affect-detection-dataset)
- **Description**: Multimodal dataset from 15 subjects wearing Empatica E4 and RespiBAN devices during stress induction
- **Signals**: ECG, EDA (electrodermal activity), EMG, respiration, body temperature, 3-axis acceleration
- **Conditions**: Baseline, stress, amusement, meditation
- **Size**: ~2.4 GB
- **Citation**: Schmidt, P., Reiss, A., Duerichen, R., Marberger, C., & Van Laerhoven, K. (2018). Introducing WESAD, a multimodal dataset for wearable stress and affect detection. ICMI.

## 🛠️ Setup Instructions

### **Prerequisites**
- Python 3.8+
- Google Colab (recommended) or local environment with GPU
- Kaggle account (for WESAD dataset download)

### **Installation**
```bash
# Clone repository
git clone https://github.com/submarinejuice/CP322-Final-Project-Group-9.git
cd CP322-Final-Project-Group-9

# Install dependencies
pip install -r requirements.txt
