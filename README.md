# Remind Me Later - README  

This project is a simple Python application for managing reminders using Flask and SQLite. Below are the steps to set up and run the application.  

## Setting Up the Environment  

1. **Create a Python Virtual Environment**  
    ```
    python -m venv venv
    ```  

2. **Activate the Virtual Environment**  
    ```
    venv\Scripts\activate  
    ```

3. **Install Required Packages**  
    ```
    pip install -r requirements.txt  
    ```  

## Running the Application  

1. Run the Flask application:  
    ```
    python app.py  
    ```  

2. The application will start on `http://127.0.0.1:5000/`.  

## About `app.py`  

- The `app.py` file is a Flask application that provides an API for managing reminders.  
- It supports two endpoints:  
  - `GET /api/reminder`: Fetches all saved reminders.  
  - `POST /api/reminder`: Allows users to create a new reminder with fields like date, time, message, and type (SMS or email).  
- The application validates input data and ensures proper date and time formats.  
