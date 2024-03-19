# Django Project: InterviewProject

Welcome to InterviewProject, a Django project for managing interviews with categories, questions, answers, and comments.

## Setup Instructions

1. Clone the repository:
   ```
    git clone git@github.com:Kabhishek18/interviewproject.git
    ```

2. Navigate to the project directory:
   ```
   cd InterviewProject
   ```
   
3. Create a virtual environment:
    ```
    python3 -m venv venv
    ```


4. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install dependencies:
  ```
    pip install -r requirements.txt
  ```

6. Migrate the database:
  ```
    python manage.py migrate
  ```

7. Create a superuser:
  ```
    python manage.py createsuperuser
  ```

8. Run the development server:
  ```
    python manage.py runserver
  ```

9. Access the admin interface:

  Navigate to `http://127.0.0.1:8000/admin` in your web browser and log in with the superuser credentials created earlier.



## Project Structure
```
InterviewProject/
│
├── interviewproject/ # Django project directory
│ ├── settings.py # Project settings
│ ├── urls.py # Project URL configuration
│ └── ...
│
├── core/ # Core Django app for main functionality
│ ├── migrations/ # Database migrations
│ ├── models.py # Database models (Subject, Question, Answer, Comment)
│ ├── views.py # Views for handling HTTP requests
│ └── ...
│
├── venv/ # Virtual environment directory
│
├── README.md # Project README file (you're here!)
└── requirements.txt # List of project dependencies
```

## Models

### Subject
- Represents a category or subject for interviews.

### Question
- Represents a question posted within a subject.

### Answer
- Represents an answer to a question.

### Comment
- Represents a comment on either a question or an answer.

## Usage

- Visit the admin interface (`http://127.0.0.1:8000/admin`) to manage subjects, questions, answers, and comments.
- Use Django ORM to interact with the database programmatically.
- Implement frontend views to display interviews, questions, answers, and comments.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


 
