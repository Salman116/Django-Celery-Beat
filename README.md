# Django app Creation

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
    ```

3. Install required packages:
    ```bash
    pip install Django django-cors-headers djangorestframework
    ```

4. Create a new Django project:
    ```bash
    django-admin startproject django_celery_project .
    ```

5. Create a new app:
    ```bash
    python manage.py startapp django_celery_app
    ```

6. Add `'django_celery_app'`, `'rest_framework'`, `'corsheaders'` to your `INSTALLED_APPS` in `settings.py`.

7. Add `.gitignore` file (make sure you ignore unnecessary files like `db.sqlite3`, `migrations/`, etc.).

8. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9. Start the server:
    ```bash
    python manage.py runserver
    ```

---

## To include Celery

1. Install Celery and Redis:
    ```bash
    pip install celery redis
    ```

2. Ensure Redis is installed and running on your machine.

3. Add `'celery'` to `INSTALLED_APPS` in `settings.py`.

4. Create a `celery.py` file in the project directory (where `settings.py` is located) and add the following:

    ```python
    import os
    from celery import Celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

    app = Celery('django_celery_project')

    app.config_from_object('django.conf:settings', namespace='CELERY')

    app.autodiscover_tasks()
    ```

5. Update the `__init__.py` file in the project directory to include:

    ```python
    from .celery import app as celery_app

    __all__ = ('celery_app',)
    ```

6. Add the following Celery settings to `settings.py`:

    ```python
    # Celery Settings
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = 'UTC'
    ```

---

## Create Your First Celery Task

1. In your app directory (`django_celery_app`), create a `tasks.py` file and add:

    ```python
    from celery import shared_task

    @shared_task
    def my_task():
        print('Hello from Celery!')
        return "task ended"
    ```

2. In your views, you can call the task asynchronously:

    ```python
    my_task.delay()
    ```

---

## Commands to Run Celery

1. Open another terminal and start the Celery worker:

    ```bash
    celery -A django_celery_project worker -l INFO
    ```

    - **If on Windows**, use the following command:
      ```bash
      celery -A django_celery_project worker -l INFO --pool=solo
      ```

---

**Note**: Make sure Redis is running before starting the Celery worker.
