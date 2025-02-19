# Milk Quality Prediction

A machine learning-based web application for predicting the quality of milk using various parameters such as pH, Temperature, Taste, Odor, Fat, Turbidity, and Colour. The app uses a pre-trained logistic regression model and provides a user-friendly interface through Streamlit.

---

## Features
- Predicts milk quality as "Good" or "Bad" based on input parameters.
- Interactive web-based interface using Streamlit.
- Lightweight and deployable using Docker.

---

## Directory Structure
sarathi7777-milk-quality-prediction/ ├── data.pkl # Pre-trained model file ├── dockerfile # Dockerfile for containerized deployment ├── ml2.py # Main application script ├── requirements.txt # List of dependencies

---

## Installation and Usage

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)

1. Clone the Repository

    ```bash
    git clone https://github.com/Sarathi7777/milk-quality-prediction.git
    cd milk-quality-prediction

2. Install Dependencies

    Use pip to install the required packages:

    ```bash
    pip install -r requirements.txt

3. Run the Application
    Run the Streamlit app:

    ```bash
    streamlit run ml2.py

    Deployment Using Docker
    
    Build and run the application using Docker:

4. Build the Docker image:
    
    ```bash
    docker build -t milk-quality-prediction .

5. Run the Docker container:

    ```bash
    docker run -p 8501:8501 milk-quality-prediction
    Access the app at http://localhost:8501.

### Input Parameters:

        pH: Acidity or alkalinity of the milk.
        Temperature: Temperature of the milk.
        Taste: Numeric encoding of milk taste quality.
        Odor: Numeric encoding of milk odor quality.
        Fat: Fat content of the milk.
        Turbidity: Turbidity level of the milk.
        Colour: Colour level of the milk.

### How It Works:
        Users input the values for the milk parameters.
        The app uses a logistic regression model to calculate the probability of the milk being "Good".
        If the probability > 0.5, the app indicates that the milk is "Good"; otherwise, it is "Bad".

### Technologies Used:

        Python
        Streamlit
        scikit-learn
        Docker
        Requirements
        Flask
        pandas
        numpy
        matplotlib
        streamlit
        gunicorn
        scikit-learn==1.2.2

### License

This project is licensed under the MIT License.

### Author
[Sarathi] (sarathiff777@gmail.com)
Sarathi7777 GitHub: Sarathi7777 


