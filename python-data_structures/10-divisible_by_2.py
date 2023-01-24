def divisible_by_2(my_list=[]):
    bool_list = []
    if not my_list:
        return None
    else:
        for i in range(0, len(my_list)):
            if my_list[i] % 2 == 0:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
