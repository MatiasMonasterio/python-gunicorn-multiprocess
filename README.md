## Get Started
### Prerequisites
You need to be using:

- Git - [Download & Install Git](https://git-scm.com/downloads)
- Python - [Download & Install Python](https://www.python.org/downloads/)
- Venv - [Dowload & Install Venv](https://docs.python.org/es/3/library/venv.html)
- Docker - [Dowload & Install Docker](https://docs.docker.com/get-docker/)

### Run locally
Copy the `env.example` file to an `.env` file and fill in the necessary environment variables.
```bash
cp .env.example .env
```

Init a virtual env
```bash
virtualenv .venv
```

Enable the virtual env
```bash
source ./venv/bin/activate
```

Install the required libraries and packages dependencies
```bash
python -m pip install -r requirements.txt
```

Run the project
```bash
gunicorn run:app
```


