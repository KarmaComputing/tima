# Tima - Example SaaS Stopwatch app

Configure
```
cp .env.example .env # change values in .env file
```

Install
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python src/tima/manage.py migrate
python src/tima/manage.py createsuperuser
```

Run
```
. venv/bin/activate
python src/tima/manage.py runserver
```

Visit: http://127.0.0.1:8000/
