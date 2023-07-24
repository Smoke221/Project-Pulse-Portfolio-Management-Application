# Import necessary modules
from pymongo import MongoClient
import os

# Retrieve the MongoDB connection URL from environment variables
url = os.environ.get('MONGO')

# Set up MongoDB connection and select the database
client = MongoClient(url)
db = client['Project-Pulse']

# Define collections to interact with different types of data
managers = db['Manager']       # Collection for storing manager-related data
projects = db['project']       # Collection for storing project-related data
tasks = db['Task']             # Collection for storing task-related data
resources = db['Resource']     # Collection for storing resource-related data
user = db['user']              # Collection for storing user-related data
auth = db['auth']              # Collection for storing authentication-related data
