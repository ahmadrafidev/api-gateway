# API Gateway Project

This project demonstrates the implementation of an API Gateway using Flask. 

## Project Structure

- `/client`: Contains the client-side code or frontend scripts that interact with the API Gateway.
- `/server`: Hosts the Flask application which acts as the API Gateway, routing incoming API requests to the designated service.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework, ideal for handling requests in a simple and extensible manner.
- **Python**: The primary programming language used in this project.
- **Libraries**: Essential libraries such as `requests` for HTTP requests.

## Getting Started

### Prerequisites

- Python 3.6 or later
- pip for installing Python packages

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmadrafidev/api-gateway.git
   
2. Navigate to the project directory:
    ```bash
    cd api-gateway

3. Navigate to client-side directory:
   ```bash
    cd client
    python3 -m venv env
    source env/bin/activate 
    pip3 install Flask requests
    flask --app app run --port=8000

4. Navigate to server-side directory:
   ```bash
    cd server
    python3 -m venv env
    source env/bin/activate 
    pip3 install Flask requests
    flask --app app run --port=5000