from app.app import app
from requests import get, post

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
