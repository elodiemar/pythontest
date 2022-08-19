def remove_values_from_list(list, val):
    return [value for value in list if value != val]


def duplicate_count(text):
    # Your code goes here
    sum=0
    text = text.lower()
    for letter in text:
        if text.count(letter)>1:
            sum+=1
            text = remove_values_from_list(text, letter)
            print(text)

    return sum
