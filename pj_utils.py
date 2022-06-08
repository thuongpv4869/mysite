
import environ

env = environ.Env()

DOT_ENV_FILE = env.str("DOT_ENV_FILE", default='.env')
if DOT_ENV_FILE:
    env.read_env(DOT_ENV_FILE, overwrite=False)
