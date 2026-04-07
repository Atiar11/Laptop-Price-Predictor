# 💻 Laptop Price Predictor

A machine learning-powered web application that predicts the price of a laptop based on its specifications. 

Built with **Streamlit** and **Scikit-learn**.

## 🚀 Live Demo
The application is hosted on GitHub Pages:
**[View Live App](https://atiar11.github.io/Laptop-Price-Predictor/)**

## ✨ Features
- Predict prices based on **Company**, **Type**, **RAM**, **OS**, **Weight**, etc.
- Support for **Touchscreen**, **IPS**, **SSD**, **HDD**, and **Flash Storage** detection.
- Fast and interactive UI.

## 🛠️ Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Atiar11/Laptop-Price-Predictor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Laptop-Price-Predictor
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📊 Dataset & Model
The model uses a **Random Forest Regressor** (within a Scikit-learn Pipeline) trained on a curated laptop prices dataset. The data includes features like CPU, GPU, Resolution, and Storage types.

## 🔗 Technologies Used
- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Stlite** (for serverless GitHub Pages hosting)
