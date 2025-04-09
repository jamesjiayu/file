# Chapter 11: Testing Your Code
# Name: James W.
# Date: 04/9/2025

# 11-2. Population:

from city_functions import city_country_population


def test_city_country_population():
    actual_res = city_country_population("santiago", "chile", 5000000)
    assert actual_res == "Santiago, Chile - population 5000000"
