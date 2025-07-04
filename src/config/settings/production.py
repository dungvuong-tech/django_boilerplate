from .base import *

# Load production environment variables
environ.Env.read_env(BASE_DIR.parent / ".envs" / "production" / ".django")
environ.Env.read_env(BASE_DIR.parent / ".envs" / "production" / ".postgres")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Database
DATABASES = {"default": env.db()}

# Whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
