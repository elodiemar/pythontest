def filter_list(l):
    'return a new list with the strings filtered out'
    new_list=[]
    for element in l:
        if type(element) == int:
            new_list.append(element)
    return new_list


#other method
def filter_list2(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]
