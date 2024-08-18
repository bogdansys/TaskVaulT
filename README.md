# PMBackend

PMBackend is a minimalistic project management tool designed to provide essential functionalities for managing projects, tasks, and teams. It serves as a streamlined alternative to more complex tools like Jira and YouTrack, focusing on simplicity and ease of use. The backend is built using Django and SQLite, ensuring efficient project collaboration.

## Overview

The architecture of the PMBackend application is based on the Django framework with SQLite as the primary database. The backend handles user management, project management, task management, team management, logging and monitoring, notifications and alerts, and admin functionalities. The application follows a RESTful API design for client-server communication.

### Technologies Used

- **Python**: Programming language required to run Django.
- **SQLite**: Database for data storage.
- **Django**: High-level Python web framework for rapid development.
- **djangorestframework**: Toolkit for building Web APIs in Django.
- **django-cors-headers**: Django app for handling the server headers required for Cross-Origin Resource Sharing (CORS).
- **django-rest-knox**: Authentication module for Django REST Framework.

### Project Structure

- **PMBackend/settings.py**: Configuration file for the Django project.
- **users/models.py**: Defines a custom User model.
- **users/serializers.py**: Serializers for handling user data.
- **users/views.py**: API views for user registration and login functionalities.
- **users/urls.py**: URL patterns for the 'users' app.
- **projects/models.py**: Defines the Project model.
- **projects/serializers.py**: Serializer for the Project model.
- **projects/views.py**: API views for handling Project resources.
- **projects/urls.py**: URL patterns for the 'projects' app.
- **tasks/models.py**: Defines the Task model.
- **tasks/serializers.py**: Serializer for the Task model.
- **tasks/views.py**: API views for managing tasks.
- **tasks/urls.py**: URL patterns for the 'tasks' app.
- **teams/models.py**: Defines the Team model.
- **teams/serializers.py**: Serializer for the Team model.
- **teams/views.py**: API views for managing team members.
- **teams/urls.py**: URL patterns for the 'teams' app.
- **logs/models.py**: Defines the Log model.
- **logs/admin.py**: Configuration for the Django admin interface for logs.
- **logs/migrations/0001_initial.py**: Initial migration script for the 'Log' model.

## Features

- **User Management**
  - Registration and Authentication
  - Profile Management
  - Role-Based Access Control (RBAC)

- **Project Management**
  - Project Creation and Management
  - Instance-Based Project Handling
  - Project Sharing

- **Task Management**
  - Task Creation and Assignment
  - Task Status Tracking
  - Task Editing and Deletion

- **Team Management**
  - Team Collaboration
  - Admin-Specific Team Control

- **Admin Panel**
  - Comprehensive Management Interface
  - Global Controls

- **Logging and Monitoring**
  - User Action Logging
  - Log Viewing

- **Notifications and Alerts**
  - User Notifications
  - Admin Alerts
  - Notifications Tab

## Getting Started

### Requirements

- Python 3.x
- SQLite

### Quickstart

1. **Clone the repository**:
   ```sh
   git clone <repository-url>
   cd PMBackend
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply database migrations**:
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```sh
   python manage.py runserver
   ```

7. **Access the application**:
   - Admin Panel: `http://127.0.0.1:8000/admin/`
   - API Endpoints: `http://127.0.0.1:8000/api/`

### License

The project is proprietary. 

```
© 2024.
```
```
