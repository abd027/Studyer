
# 📚 Studyer – Study Group Web App

**Studyer** is a full-featured Django-based web application that enables users to create and join study rooms categorized by topics. It provides an engaging, community-driven platform for learners and developers to collaborate, communicate, and grow together.

---

## 🧠 Key Features

- **👤 Custom User System**  
  Email-based login system with user profiles, bios, and avatar support.

- **🧵 Topic Categorization**  
  Browse or filter study rooms based on subjects (e.g., Python, Django, JavaScript).

- **📌 Room Creation & Participation**  
  Users can create, join, or leave study rooms and engage in topic-specific conversations.

- **💬 Real-Time Messaging**  
  Fully functional message board in each room to discuss and collaborate.

- **📊 Activity Dashboard**  
  Shows recent room activity, trending topics, and most active users.

- **🌐 RESTful API Support**  
  Built with Django REST Framework (DRF) to allow integration with mobile apps or frontend frameworks.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL  
- **Authentication:** Custom `AbstractUser` model  
- **Media:** Image uploads via `Pillow`

---

## 📂 Project Structure

```

Studyer/
├── static/              # CSS, JS, images
├── templates/           # Jinja2 HTML templates
├── studyer/             # Core Django app (models, views, API, URLs)
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation

````

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/studyer.git
   cd studyer
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations and run the server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Configure MySQL Database**

Make sure MySQL is installed and a database is created (e.g., `studyer_db`).  
Update your `settings.py` like so:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studyer_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
---

## 🧪 API Preview (DRF)

Once running, you can access API endpoints such as:

```
GET /api/rooms/
POST /api/messages/
GET /api/users/
```

Browsable API interface: `http://127.0.0.1:8000/api/`

---

## 👨‍💻 Developed By

**Abdullah**
📌 Software Engineering @ NUST
🌐 [GitHub](https://github.com/abd027) | [LinkedIn](https://www.linkedin.com/in/abdullah-3940471b9)

---

## 📃 License

This project is open-source and free to use for educational and non-commercial purposes.

```

