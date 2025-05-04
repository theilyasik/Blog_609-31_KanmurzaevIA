# MyBlog

> A simple Django-based blog application to write, edit and browse articles.

![Python Version](https://img.shields.io/pypi/pyversions/Django)  
![License](https://img.shields.io/github/license/theilyasik/Blog_609-31_KanmurzaevIA)

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Prerequisites](#prerequisites)  
4. [Installation](#installation)  
5. [Running the App](#running-the-app)  
6. [Project Structure](#project-structure)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Author & Contact](#author--contact)  

---

## Features

- ✍️ Create, read, update, delete (CRUD) articles  
- 📸 Upload and display images per article  
- 🔐 User authentication (Sign Up / Login / Logout)  
- ⚡ Responsive, clean UI with modern CSS  
- 🖼️ Media files served correctly in development  

---

## Tech Stack

- **Backend:** Django 4.x  
- **Frontend:** Django Templates, plain CSS  
- **Database:** SQLite (default)  
- **Python:** 3.10+  

---

## Prerequisites

- Python 3.10 or higher  
- `pip` (comes with Python)  
- (Optional) `virtualenv` or `venv`  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```
2. **Create & activate a virtual environment**
   ```bash
    python -m venv .venv
    ```
    # Windows
    ```
    .venv\Scripts\activate
    ```

    # macOS / Linux
    ```
    source .venv/bin/activate
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
4. **Apply database migrations**
    ```bash
    python manage.py migrate
5. **Create a superuser (for admin access)**
    ```bash
    python manage.py createsuperuser

---

## Running the App

```bash
python manage.py runserver
```
Open your browser at http://127.0.0.1:8000/ to view the site.

---

## Project Structure
```bash

├── myblog/             # project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── articles/           # articles app
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── templates/articles/
│       ├── article_list.html
│       └── article_item.html
├── accounts/           # auth app
│   ├── views.py
│   ├── urls.py
│   └── templates/accounts/
│       ├── login.html
│       └── signup.html
├── static/             # CSS, images, JS
│   └── css/
│       └── style.css
├── templates/          # base layouts
│   └── base_layout.html
├── media/              # uploaded images
├── manage.py
└── requirements.txt
```

---

## Contributing
1. **Fork the repository**
2. **Create your feature branch:**
```bash
git checkout -b feature/YourFeature
```
3. **Commit your changes:**
```
git commit -am "Add some feature"
```
4. **Push to your branch**:
```
git push origin feature/YourFeature
```
Open a Pull Request

**Please follow the existing code style and include meaningful commit messages.**

---

# Author & Contact
Kanmurzaev Ilyas

Email: theilyasik@gmail.com