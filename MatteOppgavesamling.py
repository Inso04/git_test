'''
Oppgave 6.2a
i = 1
n = 1

for i in range (50):
    n = n + i
    print(n)
    i = i + 1
'''
'''Oppgave 6.2b'''
i = 1
n = 1

for i in range (50):
    d = (n + i) - n + 1
    n = n + i
    print(n)
    print("Differansen er: ", d)
    i = i + 1
