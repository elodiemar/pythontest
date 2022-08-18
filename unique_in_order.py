def unique_in_order(iterable):
    unique_list=[]
    for i in iterable:
        if unique_list ==[]:
             unique_list.append(i)
        elif unique_list[-1] != i:
            unique_list.append(i)
    return unique_list
