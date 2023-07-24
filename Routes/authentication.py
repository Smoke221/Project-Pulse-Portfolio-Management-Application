from flask import Flask, jsonify, request
from bson.objectid import ObjectId
from Configs.db import auth,managers

def login():
    data = request.json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    existing_user = managers.find_one({'email': email})
    if existing_user is None:
        return jsonify({"message": "User not found. Please check your email"}), 404

    active_user = auth.find_one({'email': email})
    if active_user is not None:
        return jsonify({"message": "You are already logged in"}), 403

    if existing_user['password'] == password:
        auth.insert_one({'email': email})
        return jsonify({"message": "Logged in successfully!"}), 200
    else:
        return jsonify({"message": "Incorrect password. Please try again"}), 401

def logout():
    data = request.json()
    email = data.get('email')

    if not email:
        return jsonify({"message": "Email is required"}), 400

    active_user = auth.find_one({'email': email})
    if active_user is None:
        return jsonify({"message": "User not logged in"}), 404

    auth.delete_one({'email': email})
    return jsonify({"message": "Logged out successfully"}), 200