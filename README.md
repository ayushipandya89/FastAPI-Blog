# FastAPI Blog App

A simple blog application built with FastAPI featuring CRUD operations for blogs and users, along with JWT authentication.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- JWT (JSON Web Tokens) for authentication

## Install Python

```bash
    sudo apt install python3
```

## Setup Instructions


1.Clone the Repository:

```bash
    git clone https://github.com/ayushipandya89/FastAPI-Blog.git
```

2.Create a Virtual Environment:

```bash
    python -m venv venv
    source venv/bin/activate   # Unix/macOS
    venv\Scripts\activate      # Windows
```

3.Install Dependencies:

```bash
    pip install -r requirements.txt
```

4.Run the Application:

```bash
uvicorn app.main:app --reload
```
