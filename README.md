# 🧠 Question Answering with Transformers

"""
This repository contains the implementation of an Extractive Question Answering (QA) System 
using BERT-base and DistilBERT from Hugging Face Transformers. 
The task was to train and evaluate models on a QA dataset and compare their performance. 

As a bonus, we also built a Streamlit App to interact with the trained model locally. 🚀
"""

# Repository Structure
"""
data/                # Dataset (available on Google Drive)
notebooks/           # Training & evaluation notebooks
models/              # Saved models after training
qa_app.py            # Streamlit app (bonus)
README.md            # Project documentation
"""

# Dataset & Notebooks
"""
- The dataset and training notebooks are available on Google Drive:  
  [Google Drive Link](https://drive.google.com/drive/folders/1LCFKTY2qX8SxSA8yw3fqpHg5Vqlbynfh?usp=sharing)

- Training notebook includes:
  - Preprocessing the dataset
  - Fine-tuning BERT-base and DistilBERT
  - Evaluation using Exact Match (EM) and F1 score
  - Comparing the results of both models
"""

# Streamlit App
"""
- File: qa_app.py
- Allows the user to:
  - Input a passage (context)
  - Ask a question
  - Get the answer predicted by the trained model
- Framework: PyTorch backend (to avoid TensorFlow/Keras version issues)
"""

# Results Example
"""
BERT-base    -> EM: 46.28 | F1: 56.73
DistilBERT   -> EM: 61.22 | F1: 71.27
"""

# How to Run
"""
1. Clone the repository
2. Download dataset from the Google Drive link and place inside data/
3. Run the training notebook if you want to retrain the models
4. Run the Streamlit app locally:

   streamlit run qa_app.py

- Enter a passage and a question to test the model.
"""

# Notes
"""
- DistilBERT trains faster and achieved higher F1 on this task.
- Training parameters were optimized to reduce runtime.

## ✍️ Author  
Mostafa Abbas Saleh  
AI Student | NLP Practitioner

## 🙏 Acknowledgment  
Thanks to **Elevvo** for the valuable internship experience and professional training.

- Streamlit app is optional bonus to showcase QA functionality.
"""
