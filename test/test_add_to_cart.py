# Databricks notebook source
from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_add_to_cart(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    home_page = HomePage(browser)
    home_page.add_to_cart()
    home_page.open_cart()

    assert "cart" in browser.current_url