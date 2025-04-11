# Chapter 11: Testing Your Code
# Name: James W.
# Date: 04/11/2025

def add(x, y):
    try:
        return float(x) + float(y)
    except Exception as e:
        # raise Exception("something wrong") # not graceful
        print(f"Error: {e}")


def subtract(x, y):
    try:
        return float(x) - float(y)
    except Exception as e:
        print(f"Error: {e}")


def multiply(x, y):
    try:
        return float(x) * float(y)
    except Exception as e:
        print(f"Error: {e}")


def divide(x, y):
    try:
        return float(x) / float(y)
    except Exception as e:
        print(f"Error: {e}")


# add(4,"j")
# divide(2, 0)
print(subtract(1, 1))
