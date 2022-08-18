def sort_array(source_array):
    # Return a sorted array.
    new_array=[]
    odd_numbers= sorted(number for number in source_array if number %2 ==1)
   # j'itaire sur mon tableau intitial si c'est pair ca bouge pas sinon j'insère le premier élément (trié) puis je le supprime
    for num in source_array:
        if num%2 ==0:
            new_array.append(num)
        else:
            new_array.append(odd_numbers[0])
            odd_numbers.pop(0)
    return new_array
