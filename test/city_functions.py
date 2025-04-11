# Chapter 11: Testing Your Code
# Name: James W.
# Date: 04/9/2025


def city_country(city, country, population=None):
    res = f"{city.title()}, {country.title()}"
    if population:
        res += f" - population {population}"
    # print(res)
    return res


# city_country("beijing" , "china")
# City, Country – population xxx


def city_country_population(city, country, population=6):
    res = f"{city.title()}, {country.title()} - population {population}"
    return res
