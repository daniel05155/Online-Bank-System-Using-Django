# Our Bank System 

A secure and user-friendly online banking system developed with Django Framework, featuring comprehensive account management capabilities.

## Features
- User Account Management
  - Account Registration
  - Authentication (Login/Logout)
  - Secure Password Storage
  - Session Management
  - User Profile Management

## Future Enhancements
- Implementation of transaction management
- Addition of account statement generation
- Integration of payment gateway
- Enhancement of security features

## Technical Architecture
- **Backend Framework**: Django 4.2
- **Database**: PostgreSQL
- **Authentication**: Django Authentication System
- **Frontend**: 
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5

## System Requirements
- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation Guide
1. Clone the repository
```bash
git clone https://github.com/your-username/Online-Bank-System-Using-Django.git
cd Online-Bank-System-Using-Django
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
# or
venv\Scripts\activate  # For Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env file with your configuration settings
```

5. Execute database migrations
```bash
python manage.py migrate
```

6. Launch development server
```bash
python manage.py runserver
```

The application will be accessible at http://localhost:8000

## Project Structure
```
Online-Bank-System-Using-Django/
├── manage.py
├── banking_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── static/
    ├── css/
    └── js/
```

## Database Schema

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

