# E-Learning Site with Django

## Overview
This is a simple E-learning web application built with Django that offers user authentication (sign-up, login, logout), a dashboard for users, and a contact form. The website allows users to register an account, log in, and access their dashboard. It also has a contact page for users to submit inquiries.

## Features
- **User Authentication**:
  - Sign up for a new account
  - Login with existing account
  - Logout functionality
- **Dashboard**:
  - Personalized user dashboard with navigation links
  - Display of user information and various features
- **Contact Us**:
  - A contact form for users to send messages
  - Email notification upon form submission

## Technologies Used
- **Django 4.x**
- **HTML5, CSS3** for responsive UI
- **Python 3.x**
- **Email System** for contact form submissions

## Setup

### Prerequisites
Ensure you have Python 3.x and Django installed. You can install Django and other necessary dependencies using the following commands:

### 1. Install Dependencies
Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
Then, install the required dependencies:
```python
pip install django djangorestframework
```

### 2. Database Setup
Make sure your database is set up by running migrations:
```bash
python manage.py migrate
```

### 3. Create a Superuser
Create a superuser to access the Django admin panel:
```bash
python manage.py migrate
```

### 4. Running the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

## Email Configuration:
Ensure you set up email settings in settings.py for the send_mail function to work. Example configuration:

``` python

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
NOTIFY_EMAIL = 'admin-email@gmail.com'
```

## File Structure

Below is the structure of the project directory:

```bash
.
├── app/                     # Main application directory
│   ├── migrations/          # Database migration files
│   ├── static/              # Static files (CSS, JS, Images)
│   ├── templates/           # HTML templates
│   │   ├── auth/            # Templates related to authentication
│   │   │   ├── login.html   # Login page template
│   │   │   └── register.html # Registration page template
│   │   ├── contact.html     # Contact form template
│   │   └── dashboard.html   # User dashboard template
│   ├── __init__.py          # Marks the directory as a Python package
│   ├── admin.py             # Admin configurations
│   ├── apps.py              # Application configuration
│   ├── forms.py             # Form classes for handling user inputs
│   ├── models.py            # Database models
│   ├── views.py             # Views for handling HTTP requests
│   └── urls.py              # URL routing for the app
├── manage.py                # Django management script
├── requirements.txt         # List of required Python packages
└── settings.py              # Django project settings



This project demonstrates the foundational aspects of building a Django web site, including user authentication, a dashboard, and a contact form. It is designed to be beginner-friendly while offering room for further enhancements and feature additions.

We hope this project serves as a valuable starting point for your Django development journey. Feel free to explore, modify, and expand upon the features to suit your specific needs. Contributions and feedback are always welcome to improve this project further.

Happy coding!
