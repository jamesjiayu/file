# Chapter 11: Testing Your Code
# Name: James W.
# Date: 04/9/2025

# 11-1. City, Country

from city_functions import city_country
from city_functions import city_country_population


def test_city_country():
    formatted_location = city_country("santiago", "chile")
    assert formatted_location == "Santiago, Chile"


def test_city_country_with_pop():
    formatted_location = city_country("santiago", "chile", 5000000)
    assert formatted_location == "Santiago, Chile - population 5000000"


def test_city_country_population():
    actual_res = city_country_population("santiago", "chile", 5000000)
    assert actual_res == "Santiago, Chile - population 5000000"
