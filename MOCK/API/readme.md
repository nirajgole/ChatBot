### API

1. create project folder
2. (optional) create readme.md
   1. `ni readme.md`
3. create virtual environment
   1. `python -m venv .venv`
4. Activate virtual env
   1. `.venv/Scripts/activate`
5. create requirements.txt and
   1. `ni requirements.txt`
6. install required libraries
   1. `python -m pip install -r requirements.txt`
7. if requirements not found
   1. `pip install fastapi uvicorn`
   2. `pip list --not-required`
   3. `pip freeze > requirements.txt`
8. `setup .venv kernel for Jupyter Notebook`
9.  Create .env file for credentials/secrets
   1. `ni .env`
   2. store OPEN_AI_API key in .env file
10. Run App
    1.  `uvicorn fa_orders:app --reload --port 8001`
    2.  Test `http://localhost:8001/order/status?order_id=123`