import random
import time
"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Tibor Nešpor
email: tibornespor97@gmail.com"""

# Uvítací text
print("Hi there !")
print("-" * 47)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print("-" * 47)
#Generátor náhodného čísla
def generate_unique_number():
    """Generuje náhodné(tajné) 4 místné číslo které má 
    každé číslo jiné a nezačíná 0"""
    cisla = random.sample(range(10), 4)
    if cisla[0] == 0:
        cisla[0], cisla[1] = cisla[1], cisla[0]
    unique_number = "".join(map(str, cisla))
    return unique_number


#Vstup od uživatele + kontrola
def cislo():
    """Zajišťuje, aby uživatel zadal validní čtyřmístné číslo bez duplicitních číslic."""
    while True:
        user_number = input("Vložte číslo: ")
        if user_number.isalpha():
            print("Musíte vložit 4 místné číslo")
            
        elif not user_number.isdigit():
            print("Číslo nesmí obsahovat písmena")
            
        elif user_number.startswith("0"):
            print("Číslo nesmí začínat 0")
            
        elif len(user_number) != 4:
            print("Vyberte číslo od 1000 do 9999")
            
        elif not len(set(user_number)) == 4:
            print("Číslo nesmí obsahovat duplicity")
            
        else:
            print("-" * 47)
            return user_number

#Bulls and Cows funkce
def bulls_and_cows(secret, guess):
    """Vyhodnotí počet "bulls" (shod na správné pozici) a "cows" (shod na nesprávné pozici) 
    ve hře Bulls and Cows.

    Funkce porovnává dva řetězce stejných délek:
    - `secret`: tajné čtyřmístné číslo (bez opakujících se číslic), které se hádá.
    - `guess`: tip hráče (také čtyřmístné číslo bez opakujících se číslic).

    Pravidla:
    1. **Bulls** (býci): Počet číslic, které jsou na správné pozici v obou řetězcích.
    2. **Cows** (krávy): Počet číslic, které se vyskytují v obou řetězcích, ale na jiné pozici.
       - Číslice započítané jako "bull" se do "cows" nezapočítávají."""
    bulls = 0  
    for i in range(len(secret)):  
        if secret[i] == guess[i]:  
            bulls += 1  
    cows = 0  
    for g in guess:  
        if g in secret:  
            cows += 1  

    
    cows -= bulls  
    return bulls, cows

# Hra
def main():
    """   Hlavní funkce pro hru Bulls and Cows. 

    Tato funkce řídí celý průběh hry:
    1. Generuje tajné čtyřmístné číslo bez duplicitní číslice.
    2. Požaduje od uživatele zadání čtyřmístného čísla.
    3. Vyhodnocuje počet býků (bulls) a krav (cows), které uživatel uhádne.
    4. Zobrazuje zpětnou vazbu o počtu býků a krav.
    5. Pokračuje v cyklu, dokud uživatel neuhádne všechny býky (bulls = 4).
    6. Po uhodnutí tajného čísla zobrazí gratulaci, počet pokusů a čas potřebný pro uhodnutí.

    Funkce využívá:
    - `time.time()` pro měření času.
    - `generate_unique_number()` pro generování tajného čísla.
    - `cislo()` pro získání uživatelského vstupu.
    - `bulls_and_cows()` pro vyhodnocení býků a krav."""
    time_start = time.time()
    tajne_cislo = generate_unique_number()
    #print(f"Tajné číslo (pro kontrolu): {tajne_cislo}") Tajné číslo pro rychlejší kontrolu
    pokusy = 0
    while True:
        uzivatel_cislo = cislo()
        pokusy += 1 
        bulls, cows = bulls_and_cows(tajne_cislo, uzivatel_cislo)
        
        bull_text = "bull" if bulls == 1 else "bulls"
        cow_text = "cow" if cows == 1 else "cows"
        print(f"Bulls: {bulls} {bull_text}, Cows: {cows} {cow_text}")
        if bulls == 4:
            time_stop = time.time()
            ubehly_cas = time_stop - time_start
            print(f"Gratuluji, uhádl jsi tajné číslo {tajne_cislo} a potřeboval jsi {pokusy} pokusů a trvalo ti to {ubehly_cas:.2f} sekund")
            break
if __name__ == "__main__":
    main()
