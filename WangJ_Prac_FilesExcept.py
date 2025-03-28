# Chapter 10: Files and Exceptions
# Name: James Wong
# Date: 03/28/2025

# 10-3. Guest
filename = "name.txt"
try:
    name = input("Please enter your name: ")

    with open(filename, "w") as file:
        file.write(name + "\n"
                   )



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


# guest_book()
