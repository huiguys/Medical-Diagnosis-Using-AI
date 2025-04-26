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
