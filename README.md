# Medical Diagnosis Prediction System ⚕️

This is a web application built with Streamlit that predicts the likelihood of several medical conditions based on user-provided diagnostic measurements. It uses pre-trained machine learning models.

## Overview

The application provides a simple web interface where users can:
1.  Select a disease they want to get a prediction for.
2.  Enter the required medical parameters.
3.  Receive a prediction indicating the likelihood of having the disease based on the input data.

**Diseases Covered:**
* Diabetes
* Heart Disease
* Parkinson's Disease
* Lung Cancer
* Hypo-Thyroidism

## Features
* User-friendly web interface powered by Streamlit.
* Prediction capabilities for 5 different diseases.
* Clear input fields with tooltips for guidance.
* Instant prediction results upon submission.
* Styled interface with a background image for better user experience.

## Technology Stack
* **Python:** Core programming language.
* **Streamlit:** Framework for building the interactive web application.
* **Scikit-learn:** Used for building/training the machine learning models (and required for loading them).
* **Pickle:** Used for saving and loading the pre-trained models.

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites
* Python 3.7+ (Check with `python --version`)
* pip (Python package installer) (Check with `pip --version`)
* Git (for cloning the repository)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/huiguys/Medical-Diagnosis-Using-AI.git](https://github.com/huiguys/Medical-Diagnosis-Using-AI.git)
    ```
    *(Replace the URL if it's different)*

2.  **Navigate to the project directory:**
    ```bash
    cd Medical-Diagnosis-Using-AI
    ```

3.  **Create and activate a virtual environment (Recommended):**
    * **On Windows:**
        ```bash
        python -m venv .venv
        .\.venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage / Running the App

Once the setup is complete, run the following command in your terminal (make sure your virtual environment is activated):

```bash
streamlit run app.py

This will start the Streamlit application, and it should automatically open in your default web browser.

## Project Structure

```
Medical-Diagnosis-Using-AI/
├── Models/
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   ├── parkinsons_model.sav
│   ├── lungs_disease_model.sav  # Model for Lung Cancer
│   └── Thyroid_model.sav      # Model for Hypo-Thyroid
├── .gitignore             # Specifies intentionally untracked files that Git should ignore
├── app.py                 # The main Streamlit application script
├── requirements.txt       # List of Python dependencies for the project
└── README.md              # This file - project documentation
```

## Models

The pre-trained machine learning models used for prediction are stored in the `Models/` directory. These models were saved using Python's `pickle` module and likely trained using libraries compatible with Scikit-learn. Each `.sav` file corresponds to one of the diseases the application can predict.

* *(Optional: Add a sentence here if you know where the training data came from, e.g., "Models were trained on publicly available datasets like PIMA Indians Diabetes Database, Cleveland Heart Disease dataset, etc.")*

## Disclaimer

This application provides predictions based on machine learning models trained on historical data. **It is not a substitute for professional medical advice, diagnosis, or treatment.** Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or seen in this application.
