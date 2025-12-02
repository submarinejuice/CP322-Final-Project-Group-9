# 🧠 Cognitive Arousal & Investment Decision Prediction  
### **Using Skin Conductance Response (SCR) and Market Indicators**  
**CP322 – Final Project | Group 9**

---

## 📑 Table of Contents
1. [Overview](#overview)
2. [Research Question](#research-question)
3. [Datasets](#datasets)
   - [WESAD – Physiological Data](#1-wesad--physiological-data)
   - [Market Dataset – Financial Indicators](#2-market-dataset--financial-indicators)
4. [Project Structure](#project-structure)
5. [Environment Setup](#environment-setup)
6. [Methodology](#methodology)
7. [Experiments](#experiments)
8. [Results Summary](#results-summary)
9. [Limitations](#limitations)
10. [Team Members](#team-members)

---

## 🧠 Overview
This project investigates how **cognitive arousal**, measured through **Skin Conductance Response (SCR)**, influences decision-making during **risky investment choices**. We evaluate whether combining **physiological signals** with **market indicators** improves a model’s ability to predict whether a participant chooses a *risky* or *safe* option.

We explore:
- Physiological signal preprocessing  
- Multimodal feature engineering  
- Logistic Regression and Neural Network models  
- Participant-level evaluation splits  
- Comparative analysis of unimodal vs. multimodal setups  

Our central goal is to understand if **changes in physiological arousal correlate with risk-taking behaviour** in financial contexts.

---

## 🎯 Research Question
**Does integrating physiological arousal (SCR) with market indicators improve prediction accuracy for risky investment decisions compared to using financial features alone?**

---

## 📂 Datasets

### **1. WESAD – Physiological Data**
The WESAD (Wearable Stress and Affect Detection) dataset provides multimodal physiological signals collected from 15 participants under different emotional conditions.

We primarily use:
- **Electrodermal Activity (EDA) / Skin Conductance Response (SCR)**  
- Preprocessed into **tonic** and **phasic** components  
- Smoothed, filtered, and windowed to align with investment decision intervals  

**Dataset Link:**  
https://www.kaggle.com/datasets/prasadvpatil/wesad-dataset  

**Original Paper:**  
https://ubicomp.eti.uni-siegen.de/home/datasets/icmi18/

---

### **2. AE Investment Market Dataset – Financial Indicators**
A custom curated dataset representing market conditions during a simulated investment task.

Engineered features include:
- Daily returns  
- 5-day rolling volatility  
- Momentum indicators  
- Cumulative return windows  
- Market uncertainty features  

These features are aligned with corresponding SCR windows to build multimodal examples.

---

## 🗂️ Project Structure
