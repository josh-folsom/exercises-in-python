n = 4
for k in range(n):
    for j in range(n):
        print ('*' if j+k >= n-1 else ' ', end='')
    print ()
