def order(sentence):
  # code here
    arr= sentence.split()
    result=[]
    for word in arr:
        for number in word:
            if number.isdigit():
                result.append([int(number), word])

    return " ".join([x[1] for x in sorted(result)])
