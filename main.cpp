/**
 * @file main.cpp
 * @brief Glowny plik projektu obliczajacego PI metoda calkowania.
 * @author Dominik Chrobak
 * @version 0.1 - Szkielet
 */

#include <iostream>
#include <vector>
#include <thread>
#include <mutex>
#include <functional>
#include <chrono>
#include <iomanip>

/**
 * @brief Funkcja matematyczna: f(x) = 4 / (1 + x^2).
 * * Calka z tej funkcji na przedziale [0,1] daje wartosc PI.
 * * @param x Punkt x.
 * @return double Wartosc f(x).
 */
inline double funkcja_podcalkowa(double x) {
    return 4.0 / (1.0 + x * x);
}

int main() {
   long long liczba_podzialow;
    int liczba_watkow;

    // Pobranie konfiguracji od uzytkownika
    std::cout << "Podaj liczbe podzialow (N): ";
    std::cin >> liczba_podzialow;
    std::cout << "Podaj liczbe watkow: ";
    std::cin >> liczba_watkow;

    // Prosta walidacja danych, aby uniknac bledow
    if (liczba_watkow < 1) liczba_watkow = 1;
    if (liczba_podzialow < 1) liczba_podzialow = 1000;

    std::cout << "Konfiguracja: " << liczba_podzialow << " podzialow na " 
              << liczba_watkow << " watkach." << std::endl;
    
    double szerokosc_prostokata = 1.0 / liczba_podzialow;
    double suma_globalna = 0.0;
    
    // Mutex bedzie potrzebny do bezpiecznego sumowania wynikow z watkow
    std::mutex mutex_sumy; 

    // Rozpoczecie pomiaru czasu
    auto start_czasu = std::chrono::high_resolution_clock::now();

    // Wektor przechowujacy obiekty watkow
    std::vector<std::thread> wektor_watkow;

    // Wyliczenie ile prostokatow przypada na jeden watek
    long long kroki_na_watek = liczba_podzialow / liczba_watkow;

    return 0;
}