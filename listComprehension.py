# Zad 1
# wyprintowanie wszytskich nazw
my_train = ['pływanie', 'rower', 'bieg']

[print(name) for name in my_train]

print('---')

# Zad 2
# Zamiana na duzę litery
items = ['kawa', 'herbata', 'Energy-drink']

itemUpper = [item.upper() for item in items]

print(itemUpper)

print('---')

# Zad 3
# Zamiana na 0 lub 1
bits = [False, True, True, False, True, True]

new_bits = [0 if item is False else 1 for item in bits]

print(new_bits)

print('---')

# Zad 4
# Wczytaj zawartość tego pliku,
# usuń wszystkie znaki nowej linii oraz usuń linie, które nie zawierają żadnego znaku
with open('gaming.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

print(lines)

print('---')

# zad 5
# list comprehension - obliczyć cenę brutto dla każdego produktu. 
# Cenę zaokrąglij do drugiego miejsca po przecinku
tax_rate = 0.23
net_prices = [5.5, 4.0, 9.0, 10.0]

new_prices = [round((item +item * tax_rate), 2) for item in net_prices]

print(new_prices)

print('---')
# zad 6 
# Zamiana st. Celciusza na Fahrenheit
celsius = [2, 10, 4, 16, 30]

fahrenheit = [(2* item + 32) for item in celsius]
print(fahrenheit)

print('---')

# zad 7
# Czy Ukończył 18 lat
age = [19, 10, 14, 34, 50, 16, 9]

check_age = [True if ageHuman > 18 else False for ageHuman in age]

print(check_age)