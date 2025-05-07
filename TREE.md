(venv) wsl@win-hcoco1:~/code/gym-tracker-backend$ tree -L 3
.
├── Dockerfile
├── ENDPOINTS.md
├── TREE.md
├── alembic
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-310.pyc
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── __pycache__
│       ├── a048bef4686a_initial_setup.py
│       ├── b5fce00ce06d_initial_supabase2.py
│       └── c70e32f7ce79_initial_supabase.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── config.cpython-310.pyc
│   │   └── main.cpython-310.pyc
│   ├── api
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── v1
│   ├── config.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── security.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── dependencies.py
│   ├── main.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── auth.py
│   │   └── workouts.py
│   ├── test
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       ├── __pycache__
│       └── helpers.py
├── requirements.txt
├── schema
├── venv
│   ├── bin
│   │   ├── Activate.ps1
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── alembic
│   │   ├── dotenv
│   │   ├── email_validator
│   │   ├── fastapi
│   │   ├── mako-render
│   │   ├── pip
│   │   ├── pip3
│   │   ├── pip3.10
│   │   ├── pyrsa-decrypt
│   │   ├── pyrsa-encrypt
│   │   ├── pyrsa-keygen
│   │   ├── pyrsa-priv2pub
│   │   ├── pyrsa-sign
│   │   ├── pyrsa-verify
│   │   ├── python -> python3
│   │   ├── python3 -> /usr/bin/python3
│   │   ├── python3.10 -> python3
│   │   └── uvicorn
│   ├── include
│   │   └── site
│   ├── lib
│   │   └── python3.10
│   ├── lib64 -> lib
│   └── pyvenv.cfg
└── workouts.db