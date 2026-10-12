s = input()
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

res = ''
words = s.split(' ')

for word in words:
    count = 0
    for symbol in word:
        if symbol.isalpha():
            count += 1
            
    k = count
    
    for symbol in word:
        if symbol in alphabet_lower:
            index = alphabet_lower.index(symbol)
            new_index = (index + k) % 26
            res += alphabet_lower[new_index]
        elif symbol in alphabet_upper:
            index = alphabet_upper.index(symbol)
            new_index = (index + k) % 26
            res += alphabet_upper[new_index]
        else:
            res += symbol
            
    res += ' '

print(res.strip())


