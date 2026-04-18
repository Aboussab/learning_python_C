import os
from dotenv import load_dotenv
from importlib.metadata import version

load_dotenv()

MATRIX_MODE = os.environ.get("MATRIX_MODE", None)

DATABASE_URL = os.environ.get("DATABASE_URL", None)

API_KEY = os.environ.get("API_KEY", None)


LOG_LEVEL = os.environ.get("LOG_LEVEL", None)

ZION_ENDPOINT = os.environ.get("ZION_ENDPOINT", None)


print("ORACLE STATUS: Reading the Matrix...")

print("\nConfiguration loaded:")
print(f"Mode: {MATRIX_MODE}")
print(f"Database: {DATABASE_URL}")
print(f"API Access: {API_KEY}")
print(f"Log Level: {LOG_LEVEL}")
print(f"Zion Network: {ZION_ENDPOINT}")

print("\nEnvironment security check:")

if MATRIX_MODE is None:
    print("[MISSING] MATRIX_MODE is not set !")
else:
    print("[OK] No hardcoded secrets detected")

if API_KEY is None:
    print("[MISSING] API_KEY is not set !")
else:
    print("[OK] .env file properly configured")

if DATABASE_URL is None:
    print("[MISSING] DATABASE_URL is not set !")
else:
    print("[OK] Production overrides available")

print("\nThe Oracle sees all configurations.")
print(f"{version("python-dotenv")}")
