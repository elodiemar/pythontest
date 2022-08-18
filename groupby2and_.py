def solution(s):
    arrayp = []
    if len(s) %2 == 1:
        s = s +"_"
    while s:
            arrayp.append(s[:2])
            s = s[2:]
    return arrayp
