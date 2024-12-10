import random  # Import modulu random pro zamíchání pole

array = [42, 10, 78, 54, 23, 7, 85, 92, 31, 67]  # Základní pole

# Bubble sort
# Řadí pole pomocí bubble sort algoritmu.
# Porovnává sousední prvky a vyměňuje je, pokud nejsou ve správném pořadí.
def bubble_sort(array):
    n = len(array)  # Délka pole
    for i in range(n):  # Opakování pro každý prvek v poli
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:  # Porovnání dvou prvků
                array[j], array[j+1] = array[j+1], array[j]  # Výměna prvků
    return array

# Bogo sort
# Řadí pole pomocí bogo sort algoritmu.
# Náhodně míchá prvky, dokud nejsou ve správném pořadí.

def is_sorted(array): #    Kontroluje, zda je pole seřazeno v neklesajícím pořadí.
    return all(array[i] <= array[i+1] for i in range(len(array)-1))

def bogo_sort(array):
    while not is_sorted(array):  # Dokud není pole seřazeno
        random.shuffle(array)  # Náhodné promíchání pole
    return array

# Selection sort
# Řadí pole pomocí selection sort algoritmu.
# Vyhledává nejmenší prvek v nevyřešené části a umisťuje ho na správné místo.

def selection_sort(array):
    n = len(array)  # Délka pole
    for i in range(n):
        min_idx = i  # Index nejmenšího prvku
        for j in range(i+1, n):  # Hledání nejmenšího prvku
            if array[j] < array[min_idx]:  # Porovnání aktuálního prvku s minimálním
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]  # Výměna prvků
    return array

# Insertion sort
#    Řadí pole pomocí insertion sort algoritmu.
#    Postupně umisťuje prvky na jejich správné místo v již seřazené části pole.

def insertion_sort(array):
    for i in range(1, len(array)):  # Iterace přes každý prvek kromě prvního
        key = array[i]  # Prvek, který má být vložen
        j = i - 1  # Index předchozího prvku
        while j >= 0 and key < array[j]:  # Pročištění velkých prvků o pozici doprava
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key  # Vložení aktuálního prvku na správnou pozici
    return array

print("Základní pole:", array)  # Původní pole
print("Bubble sort:", bubble_sort(array.copy()))  # Vypsání bubble sort
print("Bogo sort:", bogo_sort(array.copy()))  # Vypsání bogo sort
print("Selection sort:", selection_sort(array.copy()))  # Vypsání selection sort
print("Insertion sort:", insertion_sort(array.copy()))  # Vypsání insertion sort