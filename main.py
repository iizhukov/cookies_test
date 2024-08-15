import uvicorn
import os

from dotenv import load_dotenv

from cookies_test import app


load_dotenv()

HOST = os.getenv("HOST") or "127.0.0.1"
PORT = os.getenv("PORT") or 8000

if isinstance(PORT, str):
    PORT = int(PORT)


def main():
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
