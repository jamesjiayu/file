# Chapter 10: Files and Exceptions
# Name: James Wang
# Date: 04/07/2025
import json
# 10-3. Guest
filename = "name.txt"
try:
    name = input("Please enter your name: ")

    with open(filename, "w") as file:
        file.write(name + "\n")

except Exception as e:
    print(f"An error occurred: {e}")


# 10-4. Guest Book:
def guest_book():

    filename = "guest_book.txt"

    try:
        with open(filename, "a") as file:
            while True:
                name = input("Please enter your name (or 'quit' to exit): ")

                if name.lower() == "quit":
                    print("Exiting guest book.")
                    break

                print(f"Hello, {name}!")
                file.write(f"{name} visited \n")

    except Exception as e:
        print(f"An error occurred: {e}")


guest_book()


# 10-6. Addition:
def addition():
    try:
        num1 = int(input("Please enter a number: "))
        num2 = int(input("Please enter another number: "))

    except ValueError as e:
        print(f"An error occurred: {e} ")
    else:
        print(f"number 1 + number 2 = {num1+ num2}")
    finally:
        print("execution done")


addition()

# 10-8. Cats and Dogs:


def cats_dogs():
    filename_cats = "cats.txt"
    filename_dogs = "dogs.txt"
    try:
        with open("cats.txt", "r") as f:
            content = f.read()
            print(content)
        with open("dogs.txt", "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError as e:
        print(f"File Is Not Found Error: {e}")

    finally:
        print("execution done")


cats_dogs()

# 10-11. Favorite Number:

def store_fav_number():
    filename = "fav_num.json"
    try:
        num1 = int(input("Please enter your favorite number: "))
        with open(filename, "w") as f:
            json.dump(num1, f)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("execution done")


store_fav_number()


def read_fav_number():
    filename = "fav_num.json"
    try:
        with open(filename, "r") as f:
            fav_num = json.load(f)
            print(f"I know your favorite number! It’s {fav_num}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("execution done")


read_fav_number()


# 10-12. Favorite Number Remembered:
def fav_number():
    filename = "fav_num.json"
    try:
        with open(filename, "r") as f:
            fav_num = json.load(f)
            print(f"I know your favorite number! It's {fav_num}")
    except Exception as e:
        try:
            fav_num = int(input("Please enter your favorite number: "))
            with open(filename, "w") as f:
                json.dump(fav_num, f)
        except Exception as e:
            print(f"Error: {e}")
    finally:
        print("execution done")


fav_number()
