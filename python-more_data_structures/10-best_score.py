def best_score(a_dictionary):
    if a_dictionary:
        max_value = max(a_dictionary.values())
        for key in a_dictionary:
            if a_dictionary[key] == max_value:
                return key
    return None
