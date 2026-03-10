# Chatbot Caregiver Web App

A Flask web app that provides a caregiver support chat experience powered by the OpenAI API.

## Tech Stack

- Python 3.9+
- Flask
- Gunicorn (for production-style local run)
- OpenAI Python SDK

## Project Structure

```text
website-main/
  main.py
  Procfile
  requirements.txt
  FlaskWebApp/
    __init__.py
    views.py
    templates/
    static/
```

## Prerequisites

- Python 3.9 or newer
- `pip`
- An OpenAI API key

## Local Setup

From the `website-main` directory:

```bash
cd website-main
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in `website-main`:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Run the App

Development mode:

```bash
python3 main.py
```

Open: `http://127.0.0.1:5000`

Production-style (Gunicorn):

```bash
gunicorn main:app --bind 127.0.0.1:8000 --reload
```

Open: `http://127.0.0.1:8000`

Important: run Gunicorn from inside `website-main`.  
If you run from the repo root, you may see `ModuleNotFoundError: No module named 'main'`.

## Current Routes

- `GET /`: renders `question.html`
- `GET /question`: renders the chat UI and existing session chat history
- `POST /question`:
  - with `message-input`: sends user message to OpenAI and returns JSON response
  - with `action=end_interview`: clears session data for that participant and renders `thanks.html`

## Configuration Notes

- The OpenAI key is loaded via `python-dotenv` from `.env`.
- Flask session secret is currently set in code (`SECRET_KEY = 'secretkey'`).
- Mail settings are currently hardcoded in `FlaskWebApp/__init__.py`.

For safer deployment, move `SECRET_KEY` and mail credentials into environment variables.

## Dependencies

Dependencies are listed in `requirements.txt`.

## Troubleshooting

- `ModuleNotFoundError: No module named 'main'`:
  - Start from `website-main`, not the parent folder.
- `ModuleNotFoundError: No module named 'flask'`:
  - Activate your virtual environment and reinstall requirements.
- `API key not found... OPENAI_API_KEY`:
  - Ensure `.env` exists in `website-main` and contains `OPENAI_API_KEY=...`.

## Citation

If you use this project, please cite:

```bibtex
@article{shi2026mapping,
title={Mapping Caregiver Needs to AI Chatbot Design: Strengths and Gaps in Mental Health Support for Alzheimer's and Dementia Caregivers},
author={Shi, Jiayue Melissa and Yoo, Dong Whi and Wang, Keran and Rodriguez, Violeta J. and Karkar, Ravi and Saha, Koustuv},
journal={ACM Transactions on Computing for Healthcare},
year={2026}
}

```
```bibtex
@article{shi2025balancing,
  title={Balancing Caregiving and Self-Care: Exploring Mental Health Needs of Alzheimer's and Dementia Caregivers},
  author={Shi, Jiayue Melissa and Wang, Keran and Yoo, Dong Whi and Karkar, Ravi and Saha, Koustuv},
  journal={Proceedings of the ACM on Human-Computer Interaction},
  volume={9},
  number={7},
  pages={1--36},
  year={2025},
  publisher={ACM New York, NY, USA}
}
```
