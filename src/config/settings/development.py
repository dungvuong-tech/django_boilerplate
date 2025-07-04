from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Load development environment variables
environ.Env.read_env(BASE_DIR.parent / ".envs" / "development" / ".django")
environ.Env.read_env(BASE_DIR.parent / ".envs" / "development" / ".postgres")

DATABASES = {"default": env.db()}
