

#==============================================================
# 03_1fd.
#==============================================================


# Készítsen programot, amelyik beolvas egy szót és meghatározza, hogy ez a szó milyen hosszú!

# Szó beolvasása a felhasználótól
szo = input("Kérem, adjon meg egy szót: ")

# Szó hosszának meghatározása
hossz = len(szo)

# Eredmény kiírása
print(f"A(z) '{szo}' szó hossza: {hossz}")


#==============================================================
# 03_2fd.
#==============================================================

# Készítsen programot, amelyik két szöveget olvas be. Írja ki a hosszabbikat!

# Első szöveg beolvasása
szoveg1 = input("Kérem, adjon meg egy szöveget: ")

# Második szöveg beolvasása
szoveg2 = input("Kérem, adjon meg még egy szöveget: ")

# Első és második szöveg hosszának meghatározása
hossz1 = len(szoveg1)
hossz2 = len(szoveg2)

    # Hosszabb szöveg meghatározása
if hossz1 > hossz2:
    hosszabb_szoveg = szoveg1
elif hossz2 > hossz1:
    hosszabb_szoveg = szoveg2
else:
    hosszabb_szoveg = "Mindkét szöveg egyforma hosszú."

# Hosszabb szöveg kiírása
print("A hosszabbik szöveg:")
print(hosszabb_szoveg)

#==============================================================
# 03_3fd.
#==============================================================

# Készítsen programot, amelyik beolvas egy mondatot! Írja ki, hogy kijelentő, felkiáltó vagy kérdő mondat volt-e. (utolsó karakter)

#VOLT ÓRÁN !!!

# Mondat beolvasása a felhasználótól
mondat = input("Kérem, adjon meg egy mondatot: ")

# Utolsó karakter meghatározása
utolso_karakter = mondat[-1]

# Kijelentő, felkiáltó vagy kérdő mondat ellenőrzése az utolsó karakter alapján
if utolso_karakter == ".":
    print("A megadott mondat kijelentő.")
elif utolso_karakter == "!":
    print("A megadott mondat felkiáltó.")
elif utolso_karakter == "?":
    print("A megadott mondat kérdő.")
else:
    print("A megadott mondat más típusú.")


#==============================================================
# 03_4fd.
#==============================================================

# Készítsen programot, amelyik beolvas egy szót és kiírja, 
# hogy az első és utolsó karaktere ugyanaz-e! Ellenőrizzük függvénnyel, 
# hogy tényleg egy szó-e! (Nincs benne szóköz.)

# VOLT oran 


def is_word(word):
    # Ellenőrizzük, hogy a szó csak betűket tartalmaz-e
    if word.isalpha():
        return True
    else:
        return False
    
# Szó beolvasása a felhasználótól
szo = input("Kérem, adjon meg egy szót: ")

# Ellenőrizzük, hogy a beolvasott szó tényleg egy szó-e
if ' ' in szo:
    print("A megadott input nem egy szó, mert tartalmaz szóközt.")

# Ellenőrizzük, hogy a beolvasott szó csak betűket tartalmaz-e
if not is_word(szo):
    print("A megadott input nem egy szó, mert tartalmaz nem betű karaktereket.")


    # Ellenőrizzük, hogy az első és utolsó karakter ugyanaz-e
if szo[0] == szo[-1]:
    print("Az első és az utolsó karakter ugyanaz.")
else:
    print("Az első és az utolsó karakter nem azonos.")
    
#==============================================================
# 03_5fd.
#==============================================================

# Készítsünk programot, amelyik beolvas egy szót és ritkítva írja ki! pl. fagylalt => f a g y l a l t

# Szó beolvasása a felhasználótól
szo = input("Kérem, adjon meg egy szót: ")

# Ritkított verzió létrehozása
ritkított_szo = " ".join(szo)

# Ritkított szó kiírása
print("A ritkított szó:", ritkított_szo)


#==============================================================
# 03_6fd.
#==============================================================

# Készítsen programot, 
# amelyik beolvassa a születési hónap sorszámát és adja meg, 
# hogy télen született-e! Ellenőrizze, 
# hogy helyes értéket kapott-e 1..12 (biztos egészet kapott).
# Az ellenőrzéshez használjon függvényt!


def validate_month(month):
    try:
        month = int(month)
        if 1 <= month <= 12:
            return True, month
        else:
            return False, None
    except ValueError:
        return False, None

def is_winter(month):
    winter_months = [12, 1, 2]
    if month in winter_months:
        return True
    else:
        return False

# Születési hónap beolvasása és ellenőrzése
while True:
    month_input = input("Kérem, adjon meg a születési hónap sorszámát (1-12): ")
    is_valid, month = validate_month(month_input)
    if is_valid:
        break
    else:
        print("Hibás input! Kérem, adjon meg egy érvényes hónapsorszámot.")

    # Télen született-e ellenőrzése
if is_winter(month):
    print("Télen született.")
else:
    print("Nem télen született.")


#==============================================================
# 03_7fd.
#==============================================================

# Készítsen egy programot, amelyik beolvas egy szót és megadja, hogy van-e benne e betű!

# Szó beolvasása a felhasználótól
szo = input("Kérem, adjon meg egy szót: ")

# 'e' betű jelenlétének ellenőrzése
if 'e' in szo:
    print("A megadott szó tartalmaz 'e' betűt.")
else:
    print("A megadott szó nem tartalmaz 'e' betűt.")

#==============================================================
# 03_8fd.
#==============================================================
# Készítsen egy programot, amelyik beolvas egy szót és megadja, hogy hány darab e betű van benne!

    # Szó beolvasása a felhasználótól
szo = input("Kérem, adjon meg egy szót: ")

    # 'e' betűk számolása
e_betuk_szama = szo.count('e')

    # Eredmény kiírása
print(f"A(z) '{szo}' szóban {e_betuk_szama} darab 'e' betű van.")


#==============================================================
# 03_9fd.
#==============================================================
# Készítsen programot, amelyik beolvas egy szót és megadja, hogy palindrom-e! (ugyanaz előről és hátulról olvasva. (pl. görög


def is_palindrome(word):
    return word == word[::-1]


    # Szó beolvasása a felhasználótól
szo = input("Kérem, adjon meg egy szót: ")

    # Palindrom ellenőrzése
if is_palindrome(szo):
    print(f"A(z) '{szo}' szó palindrom.")
else:
    print(f"A(z) '{szo}' szó nem palindrom.")

# Az [::-1] rész ténylegesen egy szintaxis a Pythonban, amely egy slice operátor. A slice operátor használható a szekvenciák (pl. stringek, listák) részét vagy alhalmazát kiválasztására. A szintaxis általában a következőképpen néz ki: [start:stop:step].

# start: A kivágás kezdete, alapértelmezés szerint az adott szekvencia elejétől kezdődik.
# stop: A kivágás vége, alapértelmezés szerint az adott szekvencia végénél áll meg.
# step: A lépésköz, alapértelmezés szerint 1, ami azt jelenti, hogy minden elemet kiválaszt.


#==============================================================
# 03_10fd.
#==============================================================
# Készítsen programot, amelyik beolvas egy pozitív egész számot és a rákövetkezők közül írjon ki 5 darabot, 
# amelyik nem osztható 3-mal! (pl. induló érték 5, rákövetkező 5db: 7,8,10,11,13


while True:
    try:
            # Pozitív egész szám beolvasása a felhasználótól
        start_number = int(input("Kérem, adjon meg egy pozitív egész számot: "))
        if start_number > 0:
            break
        else:
            print("Hibás input! Kérem, adjon meg egy pozitív egész számot.")
    except ValueError:
        print("Hibás input! Kérem, adjon meg egy számot.")

print("Az első 5 olyan szám, amely nem osztható 3-mal:")
count = 0
number = start_number + 1
while count < 5:
    if number % 3 != 0:
        print(number, end=" ")
        count += 1
    number += 1
    
    
#==============================================================
# 03_11fd.
#==============================================================
# Készítsen programot, amelyik beolvas egy egész számot és megadja, hogy prím-e!

def is_prime_trial_division(n):
    # Check if the number is less than
    # or equal to 1, return False if it is
    if n <= 1:
        return False
    # Loop through all numbers from 2 to
    # the square root of n (rounded down to the nearest integer)
    for i in range(2, int(n/2)+1):
        # If n is divisible by any of these numbers, return False
        if n % i == 0:
            return False
    # If n is not divisible by any of these numbers, return True
    return True

try:
        # Egész szám beolvasása a felhasználótól
    szam = int(input("Kérem, adjon meg egy egész számot: "))
        
    if is_prime_trial_division(szam):
        print(f"A(z) {szam} szám prím.")
    else:
        print(f"A(z) {szam} szám nem prím.")
except ValueError:
    print("Hibás input! Kérem, adjon meg egy egész számot.")

#==============================================================
# 03_12fd.
#==============================================================
# Készítsen programot, amelyik beolvas két egész számot és megadja, 
# hogy a kettő között melyek a prímszámok! 
# Használjon függvényt! Ellenőrizze, hogy pozitív számokat kapott-e!


def is_prime(n):
    # Check if the number is less than
    # or equal to 1, return False if it is
    if n <= 1:
        return False
    # Loop through all numbers from 2 to
    # the square root of n (rounded down to the nearest integer)
    for i in range(2, int(n/2)+1):
        # If n is divisible by any of these numbers, return False
        if n % i == 0:
            return False
    # If n is not divisible by any of these numbers, return True
    return True
 




def find_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes

while True:
    try:
            # Két egész szám beolvasása a felhasználótól
        start_number = int(input("Kérem, adjon meg egy kezdő egész számot: "))
        end_number = int(input("Kérem, adjon meg egy végződő egész számot: "))

        if start_number <= 0 or end_number <= 0:
            print("Hibás input! Mindkét számnak pozitívnak kell lennie.")
            continue
        break
    except ValueError:
        print("Hibás input! Kérem, adjon meg két egész számot.")

    # Prímszámok meghatározása és kiírása
primes = find_primes(start_number, end_number)
if primes:
    print(f"A {start_number} és {end_number} közötti prímszámok:")
    print(primes)
else:
    print(f"A(z) {start_number} és {end_number} között nincsenek prímszámok.")


#==============================================================
# 03_13fd.
#==============================================================
# Készítsen programot, amely meghatározza, hogy a beolvasott pozitív egész szám tökéletes-
# e! Tökéletes, ha az osztói összege a számmal azonosak. Használjon függvényt (pl. 6=1+2+3)


def is_perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number




while True:
    try:
            # Pozitív egész szám beolvasása a felhasználótól
        szam = int(input("Kérem, adjon meg egy pozitív egész számot: "))
        if szam > 0:
            break
        else:
            print("Hibás input! Kérem, adjon meg egy pozitív egész számot.")
    except ValueError:
        print("Hibás input! Kérem, adjon meg egy számot.")

if is_perfect_number(szam):
    print(f"A(z) {szam} szám tökéletes.")
else:
    print(f"A(z) {szam} szám nem tökéletes.")

#==============================================================
# 03_14fd.
#==============================================================
# Készítsen programot, amelyik beolvas egy programozási nyelvet! 
# Írja ki, hogyha az első 5 TIOBE indexű nyelv között van-e 2023-ban, hogy hányadik. 
# (sorrendben: Python, C, C++, Java, C#), egyébként írja ki sokadik. 
# (elif és match használatával)


    # Programozási nyelv beolvasása a felhasználótól
language = input("Kérem, adjon meg egy programozási nyelvet: ")

    # Első 5 TIOBE indexű nyelvek 2023-ban
top_languages_2023 = ["Python", "C", "C++", "Java", "C#"]

    # Nyelv ellenőrzése és helyének meghatározása
if language in top_languages_2023:
    position = top_languages_2023.index(language) + 1
    print(f"A(z) {language} a(z) {position}. helyen van a 2023-as TIOBE indexben.")
else:
    print(f"A(z) {language} nem szerepel az első 5 TIOBE indexű nyelv között 2023-ban.")



#==============================================================
# 03_15fd.
#==============================================================

# Készítsen programot, amelyik beolvas egy szót és megadja, hogy hány magánhangzó van benne! 
# Használjon függvényt, amelyik két paramétert kap, az aktuális magánhangzót és a szót! 
# A magánhangzókat írjuk be egy „konstans szóba” „aeiuo”.

#VOLT gyakon

def count_vowels(vowel, word):
    count = 0
    for char in word:
        if char in vowel:
            count += 1
    return count



vowels = "aeiuo"
word = input("Kérem, adjon meg egy szót: ")

vowel_count = count_vowels(vowels, word)

print(f"A(z) '{word}' szóban {vowel_count} darab magánhangzó van.")

#==============================================================
# 03_16fd.
#==============================================================
# Készítsen programot, amelyik beolvas egy szót és kicseréli a magánhangzókat X betűre! 
# Használjon függvényt, amelyik két paramétert kap, a magánhangzókat tartalmazó szót és a beolvasott szót!

#volt gyakon

def replace_vowels(vowels, word):
    for char in vowels:
        word = word.replace(char, 'X')
    return word


# word="alma"

# word.replace

vowels = "aeiuo"
word = input("Kérem, adjon meg egy szót: ")

new_word = replace_vowels(vowels, word)

print(f"A(z) '{word}' szót kicseréltük a magánhangzókat tartalmazó betűket X-re: '{new_word}'.")




















