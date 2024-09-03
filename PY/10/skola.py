# skola.py

skupina1 = {'Jan', 'Anna', 'Leoš', 'Kuba', 'Lena', 'Oto'}
skupina2 = {'Kuba', 'Marta', 'Marek', 'Leo', 'Jana', 'Anna'}
skupina3 = {'Dita', 'Nina', 'Alex', 'Kuba', 'Marek', 'Oto'}

vsichni_studenti = skupina1 | skupina2 | skupina3
top_studenti = skupina1 & skupina2 & skupina3
studenti_1 = vsichni_studenti - (skupina1 & skupina2 | skupina2 & skupina3 | skupina1 & skupina3)

print(vsichni_studenti)
print(top_studenti)
print(studenti_1)

