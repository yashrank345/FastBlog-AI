# FastBlog-AI

FastBlog-AI is a modern blog backend application built using **FastAPI**, **MySQL** (via XAMPP), and **JWT-based authentication**. It allows users to create, update, delete, and view blogs, along with AI-powered blog generation using **LangChain Groq** with the **LLaMA 3.1 8B Instant** model.

---

## Features

### Authentication
- Login using OAuth2 and JWT tokens
- Secure authentication for users

### Blog Management
- **Get all blogs** – `GET /blog/`
- **Create blog** – `POST /blog/`
- **Update blog** – `PUT /blog/{id}`
- **Delete blog** – `DELETE /blog/{id}`
- **View single blog** – `GET /blog/{id}`

### User Management
- **Create user** – `POST /user/`
- **Get user by ID** – `GET /user/{id}`

### AI Blog Generator
- Generate AI-written blogs using LangChain Groq
- **Endpoint:** `POST /ai_blog/`

---

## Tech Stack
- **Backend:** FastAPI
- **Database:** MySQL (via XAMPP)
- **Authentication:** OAuth2 + JWT Tokens
- **AI Blog Generator:** LangChain Groq, LLaMA 3.1 8B Instant
- **Environment:** Python 3.11+

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yashrank345/FastBlog-AI.git
cd FastBlog-AI
```
## Setup & Installation

2. **Create `.env` file** in the project root and add your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

3. **Create a virtual environment and activate it**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```
4. **Install dependencies**

```bash
pip install -r requirements.txt
```
5. **Run the application**

```bash
uvicorn blog.main:app --reload
```

6. **Access the API Open your browser or API client (like Postman) at:**

```bash
http://127.0.0.1:8000/docs
```
---

**Image**
<img width="1000" height="635" alt="Screenshot 2025-12-11 190627" src="https://github.com/user-attachments/assets/7be3a906-46d6-4483-9543-77fdb9cf46ac" />

## Author
**Created by @Yash**

If you found this useful, consider leaving a ⭐ on the repository!

---


