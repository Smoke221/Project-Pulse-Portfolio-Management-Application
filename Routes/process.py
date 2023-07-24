from flask import Flask, jsonify, request
from bson.objectid import ObjectId
from datetime import datetime
from Configs.db import user,managers

def welcome():
    return 'Sample route is working'


# Get all managers.
def get_managers():
    result = []
    for manager in managers.find():
        result.append({
            'id': str(manager['_id']),
            'name': manager['name'],
            'email': manager['email'],
            'status': manager['status'],
            'role': manager['role'],
            'bio': manager['bio'],
            'start_date': manager['start_date'],
        })
    return jsonify(result), 200


# Get a manager by ID.
def get_manager(manager_id):
    manager = managers.find_one({'_id': ObjectId(manager_id)})
    if manager:
        result = {
            'id': str(manager['_id']),
            'name': manager['name'],
            'email': manager['email'],
            'status': manager['status'],
            'role': manager['role'],
            'bio': manager['bio'],
            'start_date': manager['start_date'],
            'password': manager['password'],
        }
        return jsonify(result), 200
    return jsonify({'message': 'Manager not found'}), 404

# Create a new manager.
def create_manager():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    status = data.get('status')
    role = data.get('role')
    bio = data.get('bio')
    if 'start_date' in data and data['start_date'] is not None:
        start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    else:
        start_date = ""
    
    password = data.get('password')

    manager_id = managers.insert_one({
        'name': name,
        'email': email,
        'status': status,
        'role': role,
        'bio': bio,
        'start_date': start_date,
        'password': password,
    }).inserted_id

    return jsonify({'message': 'Manager created', 'id': str(manager_id)}), 201

#Update the manager
def update_manager(manager_id):
    data = request.json
    update_data = {}

    name = data.get('name')
    email = data.get('email')
    status = data.get('status')
    role = data.get('role')
    bio = data.get('bio')
    start_date_str = data.get('start_date')
    password = data.get('password')

    if name is not None:
        update_data['name'] = name
    if email is not None:
        update_data['email'] = email
    if status is not None:
        update_data['status'] = status
    if role is not None:
        update_data['role'] = role
    if bio is not None:
        update_data['bio'] = bio
    if start_date_str is not None:
        update_data['start_date'] = start_date_str
    if password is not None:
        update_data['password'] = password

    if update_data:
        result = managers.update_one({'_id': ObjectId(manager_id)}, {'$set': update_data})
        if result.matched_count > 0:
            return jsonify({'message': 'Manager updated'}), 200

    return jsonify({'message': 'Manager not found or no fields to update'}), 404


# Delete a manager.
def delete_manager(manager_id):
    result = managers.delete_one({'_id': ObjectId(manager_id)})
    if result.deleted_count > 0:
        return jsonify({'message': 'Manager deleted'}), 200
    return jsonify({'message': 'Manager not found'}), 404

