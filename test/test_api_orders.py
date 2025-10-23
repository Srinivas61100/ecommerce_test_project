# Databricks notebook source
import requests

def test_create_order():
    url = "https://fakestoreapi.com/carts"
    payload = {
        "userId": 1,
        "date": "2025-10-23",
        "products": [
            {"productId": 1, "quantity": 2},
            {"productId": 3, "quantity": 1}
        ]
    }
    response = requests.post(url, json=payload)
    
    # Validate response
    assert response.status_code in [200, 201]
    data = response.json()
    assert "id" in data
    print(f"Order Created with ID: {data['id']}")