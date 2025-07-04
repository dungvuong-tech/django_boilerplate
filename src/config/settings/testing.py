from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Load testing environment variables
environ.Env.read_env(BASE_DIR.parent / ".envs" / "testing" / ".django")

# Use PostgreSQL for testing
DATABASES = {"default": env.db()}
