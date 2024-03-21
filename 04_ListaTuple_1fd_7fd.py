#==============================================================
# 04_1fd.
#==============================================================
# 1.	Készítsen programot, amelyik egy szavakból álló listánál azokat a szavakat adja vissza, 
# amelyeknek a hossza éppen 5!  A szavakat egy sorban kapjuk, szóközzel elválasztva!
# a.	Adjuk meg, hogy hányadik szó a “fagyi”, ha köztük van! (index())
# b.	A megoldását módosítsa úgy, hogy használja a list comprehension szintaxist!


words = input("Kérem, adjon meg szavakat szóközzel elválasztva: ")

# Az input stringet feldaraboljuk szavakra
word_list = words.split()

# Üres lista inicializálása a 5 betűs szavak számára
five_letter_words = []

# Minden szóra ciklussal iterálunk
for word in word_list:
    # Ellenőrizzük, hogy a szó hossza éppen 5 karakter-e
    if len(word) == 5:
        # Ha igen, hozzáadjuk a five_letter_words listához
        five_letter_words.append(word)

# Az összes 5 betűs szó kiírása
print("Az 5 betűs szavak:", five_letter_words)


# a rész megoldása
def words_with_length_five(words):
    five_letter_words = [word for word in words.split() if len(word) == 5]
    return five_letter_words

def word_index(word, word_list):
    if word in word_list:
        return word_list.index(word)
    else:
        return None

# b rész megoldása
def words_with_length_five(words):
    return [word for word in words.split() if len(word) == 5]

def word_index(word, word_list):
    return word_list.index(word) if word in word_list else None


word_list = input("Kérem, adjon meg szavakat szóközzel elválasztva: ")
words_five_letters = words_with_length_five(word_list)
print("Az 5 betűs szavak:", words_five_letters)


search_word = "fagyi"
index = word_index(search_word, words_five_letters)
if index is not None:
    print(f"A(z) '{search_word}' szó a(z) {index+1}. helyen található.")
else:
    print(f"A(z) '{search_word}' szó nem található a listában.")


#==============================================================
# 04_2fd.
#==============================================================
# 2.	Készítsen programot, amelyik egyetlen sorban vár egész számokat
# (egymástól vesszővel elválasztva) és az egészeknek megfelelően létrehoz egy-egy szót,
# amelyikben a * karaktert ismétlődik a számszor! Írja ki ezeket!
# a.	Módosítsa a megoldását úgy, hogy függvényt használ a beolvasáshoz és a generáláshoz is!


#a rész megoldása
def generate_words(numbers):
    words = [str("*" * num) for num in numbers]
    return words

# b rész megoldása
def read_numbers():
    numbers = input("Kérem, adjon meg egész számokat vesszővel elválasztva: ").split(",")
    return [int(num.strip()) for num in numbers] 

def generate_words(numbers):
    return [str("*" * num) for num in numbers] 


    # a) Megoldás
numbers = [3, 5, 2, 7, 4]
words = generate_words(numbers)
print("Az egész számoknak megfelelő szavak:", words)

    # b) Megoldás
numbers = read_numbers()
words = generate_words(numbers)
print("Az egész számoknak megfelelő szavak:", words)



#==============================================================
# 04_3fd.
#==============================================================
# 3.	Készítsen programot, 
# amelyik az 1 és 100 közé eső számok közül kiválasztja azokat, 
#  amelyek hárommal nem oszthatóak és nem tartalmazzák a 3-as számjegyet! 
# a.	Adja össze az eredményül kapott számokat! (sum())
# b.	Adjuk meg a legnagyobbat! (max())
# c.	Használjon list comprehension megoldást!
# d.	Módosítsa úgy, hogy a 3-as számjegyet vagy 3-mal osztható számok helyett a bumm szót írja ki! 


# a) és b) rész megoldása
numbers = [x for x in range(1, 101) if x % 3 != 0 and '3' not in str(x)]
result_sum = sum(numbers)
max_number = max(numbers)

print("Az eredményül kapott számok összege:", result_sum)
print("A legnagyobb szám:", max_number)

# c) és d) rész megoldása
numbers_or_bumm = ['bumm' if x % 3 == 0 or '3' in str(x) else x for x in range(1, 101)]
print(numbers_or_bumm) 





#==============================================================
# 04_4fd.
#==============================================================

# 4.	Készítsen programot, amelyik beolvas N darab szót, listában tárolja ezeket és rendre kiírja a hosszukat! 
# a.	A megoldását módosítsa úgy, hogy használja a list comprehension szintaxist!
# b.	A megoldását módosítsa úgy, hogy hozzon létre egy szóból és hosszból álló tuple listát!
# c.	A megoldását módosítsa úgy, hogy a beolvasáshoz és a feldolgozáshoz is használjon függvényeket


# a) rész megoldása
def read_words(n):
    words = [input(f"Kérem, adjon meg egy szót ({i+1}/{n}): ") for i in range(n)]
    return words

def print_word_lengths(words):
    word_lengths = [len(word) for word in words]
    for i, length in enumerate(word_lengths):
        print(f"A(z) '{words[i]}' szó hossza: {length}")


n = int(input("Kérem, adjon meg a szavak számát: "))
words = read_words(n)
print_word_lengths(words)


# b) rész megoldása
def create_word_length_tuples(words):
    tuples = [(word, len(word)) for word in words]
    return tuples

def print_word_length_tuples(tuples):
    for word, length in tuples:
        print(f"A(z) '{word}' szó hossza: {length}")

print("================= b.fd ==========================================")
n = int(input("Kérem, adjon meg a szavak számát: "))
words = read_words(n)
tuples = create_word_length_tuples(words)
print_word_length_tuples(tuples)

# c) rész megoldása
def read_words():
    n = int(input("Kérem, adjon meg a szavak számát: "))
    words = [input(f"Kérem, adjon meg egy szót ({i+1}/{n}): ") for i in range(n)]
    return words

def calculate_word_lengths(words):
    lengths = [len(word) for word in words]
    return lengths

def display_word_lengths(words, lengths):
    for i, word in enumerate(words):
        print(f"A(z) '{word}' szó hossza: {lengths[i]}")

print("================= c.fd ==========================================")

words = read_words()
lengths = calculate_word_lengths(words)
display_word_lengths(words, lengths)



#==============================================================
# 04_5fd.
#==============================================================
# 5.	Készítsen programot, amelyik beolvas N darab koordináta párt és megszámolja, hány került az I. síknegyedbe! 
# A koordináta párokat soronként vesszővel elválasztva kapjuk!
# Tároljuk a koordinátákat tuple listában! Használjunk, a beolvasáshoz és megszámoláshoz függvényeket! 


def read_coordinates(n):
    coordinates = []
    for i in range(n):
        print(" koordináta párokat soronként vesszővel elválasztva ad meg: pl. 2,3 !")
        coordinate = input(f"Kérem, adjon meg egy koordináta párt ({i+1}/{n}): ").split(",")
        coordinates.append((int(coordinate[0]), int(coordinate[1])))
    return coordinates


def count_points_in_first_quadrant(coordinates):
    count = 0
    for x, y in coordinates:
        if x > 0 and y > 0:
            count += 1
    return count


n = int(input("Kérem, adjon meg a koordináta párok számát: "))
coordinates = read_coordinates(n)
count = count_points_in_first_quadrant(coordinates)
print(f"Az I. síknegyedbe került koordináta párok száma: {count}")




#==============================================================
# 04_6fd.
#==============================================================
# 6.	Készítsen programot, amelyik beolvas két szavakból álló listát! 
# (Egy sorban, szóközzel elválasztva.) 
# Hozza létre azt a listát, amelyik tartalmazza az összes lehetséges szavakból álló párt! 
# a.	Módosítsa úgy, hogy használja a list comprehension megoldást!
# b.	Használjon a beolvasáshoz és feldolgozáshoz függvényeket!




# a) rész megoldása
def create_word_pairs(words):
    word_pairs = [(word1, word2) for word1 in words[0] for word2 in words[1]]
    return word_pairs

# b) rész megoldása
def read_word_list():
    words = input("Kérem, adjon meg két szavakból álló listát szóközzel elválasztva: ").split()
    return words

def create_word_pairs(words):
    word_pairs = []
    for word1 in words[0]:
        for word2 in words[1]:
            word_pairs.append((word1, word2))
    return word_pairs

    # b) rész
words = read_word_list()
word_pairs = create_word_pairs(words)
print("Az összes lehetséges szavakból álló pár:")
print(word_pairs)


#==============================================================
# 04_7fd.
#==============================================================
# 7.	Készítsen programot, amelyik eldönti, hogy egy szavakból álló listában mindegyik szó palindrom-e! 
# (Palindrom, ha visszafele olvasva is ugyanaz!).
# Hozzunk létre függvényt a beolvasáshoz, a palindrom tulajdonság meghatározásához és az eldöntéshez!


def read_word_list():
    words = input("Kérem, adjon meg egy szavakból álló listát szóközzel elválasztva: ").split()
    return words

def is_palindrome(word):
    return word == word[::-1]

def are_all_palindromes(words):
    for word in words:
        if not is_palindrome(word):
            return False
    return True

words = read_word_list()
if are_all_palindromes(words):
    print("Az összes szó palindrom.")
else:
    print("Nem mindegyik szó palindrom.")




































