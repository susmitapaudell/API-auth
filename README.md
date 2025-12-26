## Auth Backend Service
## Overview

A FastAPI-based authentication backend for secure user registration and login.
Implements JWT-based authentication with access and refresh tokens, allowing applications to authenticate users and issue tokens for session management.

---

## Features Implemented

User Registration: Stores email and hashed password securely.

Login: Verifies credentials and issues JWT access and refresh tokens.

Refresh Tokens: Exchange valid refresh tokens for new access tokens.


## High-Level System Flow
1. User registers with email and password.
2. Backend validates input and hashes the password.
3. User data is stored securely in the database.
4. User logs in with credentials.
5. Backend verifies password and issues JWT tokens (access + refresh).
6. Refresh token endpoint handles expired access tokens securely.

---

## Tech Stack
- **Language:** Python 3.10+
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT (JSON Web Tokens)
- **Password Security:** Argon2
- **Environment Config:** python-dotenv
- **API Testing:** Swagger UI / Postman
- **Version Control:** Git

---

## Project Structure
