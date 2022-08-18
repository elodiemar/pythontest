def remove_values_from_list(list, val):
    return [value for value in list if value != val]

def array_diff(a, b):
    #your code here
    for elementa in a:
        for elementb in b:
            if elementa == elementb:
                a = remove_values_from_list(a, elementb)
    return a
