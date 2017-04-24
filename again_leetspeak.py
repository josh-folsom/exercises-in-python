quote = "it was the best of times, it was the worst of times"
for char in quote:
    if char == 'a':
        quote = quote.replace('a', '4')
    elif char == 'e':
        quote = quote.replace('e', '3')
    elif char == 'g':
        quote = quote.replace('g', '6')
    elif char == 'i':
        quote = quote.replace('i', '1')
    elif char == 'o':
        quote = quote.replace('o', '0')
    elif char == 's':
        quote = quote.replace('s', '5')
    elif char == 't':
        quote = quote.replace('t', '7')
    else:
        pass

print(quote)
