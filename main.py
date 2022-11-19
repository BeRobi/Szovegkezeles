'''
szoveg = input(str(f'Írj be egy szöveget!'))
szoveg = szoveg.upper()
print(szoveg)
if len(szoveg) > 10:
    print(len(szoveg))
else:
    print(f'A szöveg 10 karakternél rövidebb!')


szoveg_jo = False
while not szoveg_jo:
    szoveg = input("Adj meg egy legalább három betűs szót!")
    if len(szoveg) >= 3:
        szoveg_jo = True



szoveg_jo = False
while len(szoveg) >= 3:
    szoveg = input("Adj meg egy legalább három betűs szót!")
    szoveg_jo = True

szoveg = input('Adj meg egy szót, megmondom hányadik karaktere \"a\"!')
i = 0
while i < len(szoveg) and szoveg[i].upper() != 'A':
    i += 1


if i < len(szoveg):
    print(f'Van a betű \"a\" szövegben a {i + 1}. karakteren.')
else:
    print('Nincs a szövegben \"a\" betű')

'''


nevsor = []

nev = input(str(f'Írj be egy nevet!'))

nev = nev.capitalize()
    if nev != '@':
    nevsor.append(nev)
    print(nev)
    else:
    input(str(f'Írj be egy nevet!'))



