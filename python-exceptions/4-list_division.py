#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    divition = 0.0
    for i in range(list_length):
        try:
            divition = my_list_1[i] / my_list_2[i]
            new_list[i] = divition
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except (IndexError, RuntimeError):
            print("out of range")
        finally:
            pass
    return new_list