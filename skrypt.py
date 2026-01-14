import subprocess
import time
import matplotlib.pyplot as plt
import os

# Nazwa pliku wykonywalnego (zalezy od systemu)
# Dla Windows uzywamy calka.exe
sciezka_do_exe = "calka.exe" 

# Parametry testu
liczb_podzialow = 100000000  # 100 milionow
maks_watkow = 30             # Przetestujemy od 1 do 30 watkow

wyniki_watki = []
wyniki_czasy = []

print(f"--- Rozpoczynam automatyczne testy programu: {sciezka_do_exe} ---")

if not os.path.exists(sciezka_do_exe):
    print("BLAD: Nie widze pliku calka.exe. Czy na pewno skompilowales kod C++?")
    exit()

for watki in range(1, maks_watkow + 1):
    print(f"Testuje dla {watki} watkow...", end=" ")
    
    # Przygotowanie danych wejsciowych: "liczba_podzialow\nliczba_watkow\n"
    dane_wejsciowe = f"{liczb_podzialow}\n{watki}\n"
    
    try:
        # Uruchomienie procesu C++
        proces = subprocess.Popen(
            [sciezka_do_exe],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wyslanie danych i odebranie wyniku
        stdout, stderr = proces.communicate(input=dane_wejsciowe)
        
        # Szukamy czasu w wynikach programu
        czas = 0.0
        for linia in stdout.splitlines():
            if "Czas obliczen:" in linia:
                czas = float(linia.split()[2]) # Pobranie liczby z linii
                break
        
        if czas > 0:
            wyniki_watki.append(watki)
            wyniki_czasy.append(czas)
            print(f"-> Czas: {czas:.4f} s")
        else:
            print("-> BLAD: Nie udalo sie odczytac czasu.")
            
    except Exception as e:
        print(f"\nBlad uruchomienia: {e}")

# Rysowanie wykresu
print("\nGeneruje wykres...")
plt.figure(figsize=(10, 6))
plt.plot(wyniki_watki, wyniki_czasy, marker='o', color='b', label='Czas obliczen')
plt.title(f"Zaleznosc czasu od liczby watkow (N={liczb_podzialow})")
plt.xlabel("Liczba watkow")
plt.ylabel("Czas [s]")
plt.grid(True)
plt.legend()

# Zapisanie wykresu
plik_wykresu = "wykres_wydajnosci.png"
plt.savefig(plik_wykresu)
print(f"Gotowe! Wykres zapisano w pliku: {plik_wykresu}")
# plt.show() # Odkomentuj jesli chcesz zobaczyc okienko z wykresem