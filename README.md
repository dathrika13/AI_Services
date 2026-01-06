# AI Services

A Python-based AI services platform with AWS Lambda deployment, containerization support, and CI/CD integration.

---

## Overview

This project provides a scalable AI services backend featuring:

- Modular source code architecture
- AWS Lambda serverless functions
- Docker containerization for local development and deployment
- Automated CI/CD workflows via GitHub Actions
- Comprehensive test suite

---

## Project Structure

```
AI_Services_sep27/
├── .github/
│   └── workflows/          # CI/CD pipeline configurations
├── aws_lambda/             # AWS Lambda function handlers
├── data/                   # Data files and datasets
├── src/                    # Core source code modules
├── tests/                  # Unit and integration tests
├── backend.py              # Backend server implementation
├── main.py                 # Main application entry point
├── Dockerfile              # Docker image configuration
├── docker-compose.yaml     # Multi-container orchestration
├── requirements.txt        # Python dependencies
└── README.md
```

---

## Tech Stack

- **Python 3.x** — Core programming language
- **AWS Lambda** — Serverless compute
- **Docker** — Containerization
- **Docker Compose** — Multi-container orchestration
- **GitHub Actions** — CI/CD automation

---

## Getting Started

### Prerequisites

- Python 3.8+
- Docker & Docker Compose
- AWS CLI (for Lambda deployment)

### Local Development

```bash
# Clone the repository
git clone https://github.com/dathrika13/AI_Services_sep27.git
cd AI_Services_sep27

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up --build

# Or build manually
docker build -t ai-services .
docker run -p 8000:8000 ai-services
```

---

## AWS Lambda Deployment

The `aws_lambda/` directory contains serverless function handlers for AWS deployment.

```bash
# Deploy using AWS CLI or SAM
cd aws_lambda
# Follow your preferred deployment method (SAM, Serverless Framework, etc.)
```

---

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src
```

---

## CI/CD

GitHub Actions workflows are configured in `.github/workflows/` for:

- Automated testing on push/PR
- Code quality checks
- Deployment pipelines

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/service` | Main AI service endpoint |
| GET | `/health` | Health check |

*Note: Update this section based on actual endpoints in `backend.py`*

---

## Configuration

Environment variables and configuration options:

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | `8000` |
| `DEBUG` | Debug mode | `False` |
| `AWS_REGION` | AWS region for Lambda | `us-east-1` |

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

## Contributors

This project has 5 contributors.

---

## License

This project is for internal use and educational purposes.

Minor update for PR test.

Another minor update for YOLO.
