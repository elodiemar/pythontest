def tribonacci(signature, n):
    #your code here
    if n== 0:
        return []
    signature.append(sum(signature))
    for element in range(0, n-4):
        signature.append(sum(signature[-3:]))
    return signature[0:n]
