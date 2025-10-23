# Databricks notebook source
import requests

def test_get_products():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)

    # Basic validation
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "title" in data[0]
    print(f"Total Products Found: {len(data)}")