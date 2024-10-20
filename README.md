# Blood Bank Management System API

This project is a REST API for managing a Blood Bank system, built using Django and Django REST Framework (DRF). The API provides functionality for managing blood donors, blood inventory, and blood requests, along with user authentication using JWT tokens.


## Features

- **User Registration**: Register new users and issue JWT tokens for authentication.
- **Donor Management**: Admin users can create, retrieve, update, and delete donor records.
- **Blood Inventory Management**: Admin users can manage blood inventory records, including adding and updating available blood units.
- **Blood Request Management**: Users can request blood, and admin users can approve or reject blood requests.
- **JWT Authentication**: Secure the API using JSON Web Tokens for authenticated access.

## Requirements

- Python 3.8+
- Django 4.0+
- Django REST Framework 3.12+
- SQLite (default) or any other database like PostgreSQL or MySQL
- Django Simple JWT for authentication

## Installation

 Clone the repository:
   ```bash
   git clone 
   cd blood-bank-management
   python3 -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

  NOTE : USE POSTMAN OR THUNDERCLIENT TO CHECK API

##API URLS

Blood Bank Management System API Documentation
Base URL: http://127.0.0.1:8000/
Authentication:
The API uses JWT (JSON Web Token) for authentication. Obtain tokens via the
following endpoints:
1. Obtain Token
Endpoint: /api/token/
Method: POST
Payload:
{
 "username": "your-username",
 "password": "your-password"
}
Response:
{
 "access": "your-access-token",
 "refresh": "your-refresh-token"
}
2. Refresh Token
Endpoint: /api/token/refresh/
Method: POST
Payload:
{
 "refresh": "your-refresh-token"
}
Response:
{
 "access": "new-access-token"
}
User Registration:
Register New User
Endpoint: /register/
Method: POST
Payload:
{
 "username": "Thomas",
 "password": "Thomas@123",
 "email": "Thomas@gmail.com"
}
Response:
{
 "message": "User registered successfully"
}
Donor Management:
1. List All Donors (Admin)
Endpoint: /admin/donors/
Method: GET
Response:
[
 {
 "id": 1,
 "name": "Thomas",
 "blood_group": "O+",
 "contact": "1234567890"
 },
 ...
]
2. Get Single Donor by ID (Admin)
Endpoint: /admin/donors/<int:id>/
Method: GET
Response:
{
 "id": 1,
 "name": "Thomas",
 "blood_group": "O+",
 "contact": "1234567890"
}
Blood Inventory Management:
1. Get All Inventory (Public)
Endpoint: /allinventory/
Method: GET
Response:
[
 {
 "id": 1,
 "blood_group": "A+",
 "quantity": 5
 },
 ...
]
2. Get Inventory by ID (Admin)
Endpoint: /admin/inventory/<int:id>/
Method: GET
Response:
{
 "id": 1,
 "blood_group": "A+",
 "quantity": 5
}
Blood Request Management:
1. Create New Blood Request
Endpoint: /request/
Method: POST
Payload:
{
 "blood_group": "A-",
 "requester_name": "Thomas",
 "contact": "1234567890"
}
Response:
{
 "message": "Blood request created successfully"
}
Error Handling:
- 200 OK: The request was successful.
- 201 Created: A resource was successfully created.
- 400 Bad Request: The request was invalid or missing required fields.
- 401 Unauthorized: Authentication credentials were missing or invalid.
- 404 Not Found: The requested resource does not exist.
- 500 Internal Server Error: An error occurred on the server.
Technologies Used:
- Django
- Django REST Framework
- JWT Authentication
- SQLite

