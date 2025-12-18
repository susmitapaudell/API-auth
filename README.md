# Auth Backend Service

## Project Overview
This project is a **backend-only authentication and user management system** built with **Python** and **FastAPI**.  
It is designed as a standalone service that can be reused by any application requiring secure user authentication.

The system focuses on real-world backend engineering concepts rather than frontend development. All interactions are done through API calls via **Swagger UI**.

---

## Why This Project Matters
Authentication is one of the most critical components of any software system.

By completing this project, I demonstrate:
- Security awareness
- Backend architecture thinking
- Practical FastAPI knowledge
- Database modeling skills
- Ability to design production-oriented systems


## High-Level System Flow
1. User registers with email and password.
2. Backend validates input and hashes the password.
3. User data is stored securely in the database.
4. User logs in with credentials.
5. Backend verifies password and issues JWT tokens (access + refresh).
6. User accesses protected routes using tokens.
7. Backend authorizes or rejects requests.
8. Refresh token endpoint handles expired access tokens securely.

---

## Tech Stack
- **Language:** Python 3.10+
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Password Security:** Bcrypt / Passlib
- **Environment Config:** python-dotenv
- **API Testing:** Swagger UI / Postman
- **Version Control:** Git

---

## Project Structure
