## User Management Microservice (FastAPI + PostgreSQL + JWT + Docker)
A production‑ready microservice for user authentication and account management.
Built with FastAPI, PostgreSQL, SQLAlchemy, JWT, and fully containerized using Docker Compose.

This service provides:

User registration

Secure login

JWT access tokens

Persistent database storage

Clean architecture

Easy local development with Docker

Perfect for real‑world backend systems, microservice architectures, and cloud deployments.

- Features
- Authentication
Register new users

Login with email + password

Secure password hashing (bcrypt)

JWT access tokens with expiration

## Database
PostgreSQL

SQLAlchemy ORM

Auto‑generated tables

## Architecture
Modular FastAPI application

Separation of concerns (models, schemas, CRUD, auth, utils)

Dependency‑injected DB sessions

## Docker
Dockerfile for API

Docker Compose for API + PostgreSQL

One‑command startup

Setup Instructions
1. Clone the repository
Code
git clone https://github.com/<your-username>/ai-portfolio.git
cd ai-portfolio/backend/microservices/user_service

2. Start the microservice using Docker Compose
Code
docker-compose up --build
This will:

- Start PostgreSQL

- Build the FastAPI container

- Run the API on http://localhost:8000

3. Access API documentation
Open your browser:

- http://localhost:8000/docs

You’ll see interactive Swagger UI where you can test all endpoints.

## Environment Variables (Optional)
If you want to customize:

Variable	Description
POSTGRES_PASSWORD	DB password
POSTGRES_DB	Database name
SECRET_KEY	JWT secret
ALGORITHM	JWT algorithm
ACCESS_TOKEN_EXPIRE_HOURS	Token lifetime


## API Endpoints
POST /register
Create a new user.

Request Body:
{
  "email": "user@example.com",
  "password": "mypassword",
  "full_name": "John Doe"
}
Response:
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe"
}

POST /login
Authenticate user and return JWT token.

Request Body:
{
  "email": "user@example.com",
  "password": "mypassword"
}
Response:
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}

Testing the API
Using Swagger UI
Visit:

## http://localhost:8000/docs

You can test:

Register

Login

JWT token validation

Using cURL
curl -X POST http://localhost:8000/register \
-H "Content-Type: application/json" \
-d '{"email":"test@test.com","password":"123","full_name":"Test User"}'


## Development Without Docker
Install dependencies:
pip install -r requirements.txt

Run FastAPI:
uvicorn app.main:app --reload

## JWT Authentication Flow
User logs in

Password is verified

JWT token is generated

Token includes expiration

Client uses token in Authorization: Bearer <token>


------------------------------------------------

## MICROSERVICE: User Management Service (FastAPI + PostgreSQL + JWT)
A production‑style microservice that handles:

- User registration

- Login

- JWT authentication

- User profile retrieval

- Database persistence

- Dockerized deployment

## Architecture Overview

FastAPI (REST API)
│
├── PostgreSQL (persistent DB)
│
├── SQLAlchemy ORM
│
├── JWT Authentication
│
└── Docker (containerized service)


## Folder Structure
backend/microservices/user_service/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── crud.py
│   └── utils.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

## Database Schema (PostgreSQL)

Table: users

| Column | Type | Notes |
| --- | --- | --- |
| id | int (PK) | auto‑increment |
| email | text | unique |
| password | text | hashed |
| full_name | text | optional |
| created_at | timestamp | default NOW() |

