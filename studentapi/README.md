
# Student Management API

This Django REST API enables users to manage student records through CSV uploads, providing functionalities for adding student records from a CSV file, retrieving all student records in a paginated format, and deleting all student records from the database.

## Features

- **Add Students**: Allows uploading a CSV file in various formats to add student records to the database.
- **Get All Students**: Retrieve all student records in a paginated response.
- **Delete All Students**: Clears all records from the student table.

## Setup

Follow these instructions to set up and run this project locally.

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Virtualenv (optional, recommended for creating an isolated Python environment)

### Cloning the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository_url>
cd <repository_directory>
```

Replace `<repository_url>` and `<repository_directory>` with the URL of the repository and the directory name, respectively.

### Installing Dependencies

Set up a virtual environment (recommended) and install the required Python packages:

```bash
# Optional: Create a virtual environment
python -m venv venv

# Activate the virtual environment (Unix-based systems)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### Running the Server

Start the development server with the following command:

```bash
python manage.py runserver
```

The API will then be accessible at `http://127.0.0.1:8000/`.

## API Usage

Use these `curl` commands to interact with the API:

### Get All Students

```bash
curl --location 'http://127.0.0.1:8000/student/getAll'
```

### Add Students from CSV

```bash
curl --location 'http://127.0.0.1:8000/student/addFromCSV' \
--form 'studentcsv=@"/path/to/your/csvfile.csv"'
```

Replace `/path/to/your/csvfile.csv` with the path to your CSV file.

### Delete All Students

```bash
curl --location --request DELETE 'http://127.0.0.1:8000/student/deleteAll'
```

## Running Tests

To ensure the functionality of the API, it is essential to run tests. Execute the following command to run all tests:

```bash
python manage.py test students.tests
```

This will run the tests defined in your Django app, verifying both the functionality of your views and the CSV processing logic.

## Note on CSV Uploads

The CSV upload feature supports various CSV formats. The API intelligently maps different CSV headers to the corresponding database fields, allowing flexibility in the CSV files you upload.

---

## Docker Support

This project includes a Dockerfile for building and running the application in a containerized environment.

### Building the Docker Image

```bash
docker build -t studentapi
```

## Setup and Running with Docker

Follow the instructions in the root `README.md` to build and run the application using Docker. 

Once the Docker containers are up, you may need to make and apply database migrations. You can do this by running:

```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

## Running without Docker

If you're not using Docker, follow these steps after setting up your virtual environment and installing dependencies:

1. Make migrations:

    ```bash
    python manage.py makemigrations
    ```

2. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

3. Start the development server:

    ```bash
    python manage.py runserver
    ```