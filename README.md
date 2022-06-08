### 1. Run project at local
1. Install docker, docker-compose
2. Create file `.env`, `envs/local/*.env`, `config/settings/local.py` as example.
3. Build: `./app.sh build`
4. Run: `./app.sh up`
5. Check api doc at: `http://localhost:8000/api/schema/redoc/`

### 2. Setup dev
1. Install python and create venv, activate venv
1. Setup dev tools: `./app.sh setup-devtool`


### 3. Run test
1. Run test: `./app.sh test`
