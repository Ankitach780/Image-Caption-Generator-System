import os

# Load Google OAuth credentials from environment variables
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "")

# Add other settings here, for example:
DEBUG = True
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///default.db")

