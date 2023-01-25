def search_replace(my_list, search, replace):
    new_list = []
    if search and replace and my_list:
        for i in range(0, len(my_list)):
            if my_list[i] != search:
                new_list.append(my_list[i])
            else:
                new_list.append(replace)
        return new_list
