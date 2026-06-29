# Simple FastAPI Cloud Project

A minimal FastAPI application designed for deployment to cloud platforms (like AWS ECS, Azure Container Instances, Google Cloud Run, etc.) or any Docker-compatible environment.

## Features

- Health check endpoint (`/health`)
- Info endpoint (`/info`) showing application and environment details
- Minimal dependencies (FastAPI and Uvicorn)
- Dockerized for easy deployment
- Ready for cloud deployment

## Running Locally

### Prerequisites

- Python 3.12+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```
   or
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

4. Open your browser to `http://localhost:8000/docs` for the API documentation (Swagger UI) or visit:
   - Health check: `http://localhost:8000/health`
   - Info: `http://localhost:8000/info`

## Running with Docker

### Build the Docker image

```bash
docker build -t simple-fastapi-cloud .
```

### Run the container

```bash
docker run -p 8000:8000 --env ENVIRONMENT=development simple-fastapi-cloud
```

### Access the application

- Health check: `http://localhost:8000/health`
- Info: `http://localhost:8000/info`
- API docs: `http://localhost:8000/docs`

## Deployment to Cloud Platforms

This project is ready for deployment to any cloud platform that supports Docker containers. Here are some examples:

### Google Cloud Run
```bash
gcloud run deploy --image gcr.io/<project-id>/simple-fastapi-cloud --platform managed
```

### AWS ECS (Fargate)
1. Push image to ECR
2. Create task definition and service

### Azure Container Instances
```bash
az container create --resource-group <group> --name <name> --image <acr-login-server>/simple-fastapi-cloud --dns-name-label <dns-name> --ports 8000
```

## API Endpoints

### GET `/health`
Returns a simple health check response.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-06-29T20:05:00.123456"
}
```

### GET `/info`
Returns application and environment information.

**Response:**
```json
{
  "app_name": "Simple FastAPI Cloud Project",
  "app_version": "0.1.0",
  "python_version": "3.12.0",
  "platform": "Linux-5.15.0-105-generic-x86_64-with-glibc2.35",
  "environment": "production",
  "timestamp": "2024-06-29T20:05:00.123456"
}
```

## Project Structure

```
.
├── Dockerfile          # Dockerfile for containerization
├── main.py             # Main FastAPI application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
