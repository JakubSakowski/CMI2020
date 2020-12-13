import random

ZABAWKI = ['Auto','Gra','Lalka','Maskotka','Rakieta']
print('1. Lista ZABAWKI to: ')
print(*ZABAWKI, sep = ", ")

print('')
print('2. Losowanie zabawek do listy DANE')
print('')

DANE = []
for x in range(1000):
    DANE.append(ZABAWKI[random.randrange(5)])
print('3. Lista DANE to: ')
print(*DANE, sep = ", ")

print('')
print('4. Wśród wylosowanych zabawek mamy zatem:')
print('')

licznikAuto=0
licznikGra=0
licznikLalka=0
licznikMaskotka=0
licznikRakieta=0

for x in range(len(DANE)):
    if DANE[x] == 'Auto':
        licznikAuto += 1
    if DANE[x] == 'Gra':
        licznikGra += 1
    if DANE[x] == 'Lalka':
        licznikLalka += 1
    if DANE[x] == 'Maskotka':
        licznikMaskotka += 1
    if DANE[x] == 'Rakieta':
        licznikRakieta += 1

print('Auto:'),
print(licznikAuto)
print('Gra:'),
print(licznikGra)
print('Lalka:'),
print(licznikLalka)
print('Maskotka:'),
print(licznikMaskotka)
print('Rakieta:'),
print(licznikRakieta)
