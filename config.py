from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['SQLITE_USER']
database = os.environ['SQLITE_DATABASE']

DATABASE_CONNECTION_URI = f'sqlite:///C:\\Users\\{user}\\Documents\\python-projects\\fweb-contacts\\{database}'

SECRET_KEY = os.environ['SECRET_KEY']