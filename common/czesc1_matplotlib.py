import czesc1_matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[10,15,13,20,17]
#
# # 1. Wykres liniowy
#
# plt.plot(
#     x,
#     y,
#     color="green",
#     linewidth=3,
#     marker="o",
#     markersize=10
# )
#
# plt.title("Wykres liniowy")
# plt.xlabel("Numer dnia")
# plt.ylabel("Wartość sprzedaży")
#
# plt.show() # przywolanie / aktywowanie wykresu

# 2.Wykres slupkowy
# produkty = ["A", "B", "C", "D"]
# wyniki = [12, 19, 7, 15]

# plt.bar(produkty, wyniki) vertical(pionowy)
# plt.barh(produkty, wyniki) #horizontal(poziomy)
# plt.title("Wykres słupkowy")
# plt.xlabel("Produkty")
# plt.ylabel("Liczba sztuk")
# plt.show()

# oceny = [1,2,3,4,5,6,5,4,4,4,1]
#
# plt.hist(oceny, bins=4)
# plt.title("Histogram ocen")
# plt.xlabel("Ocena")
# plt.ylabel("Liczba wystapien")
# plt.show()

# 3. WYkres kolowy
# etykiety = ["Py", "JS", "C++", "Java"]
# wartosci = [40,25,15,20]
#
# plt.pie(wartosci, labels=etykiety, autopct="%1.2f%%")
# plt.title("Udzial jezykow programowania")
# plt.show()

# 4.Wykres punktowy
# x = [1,2,3,4,5]
# y = [3,7,4,9,6]
#
# plt.scatter(x,y)
# plt.title("Wykres punktowy")
# plt.xlabel("Liczba godzin nauki")
# plt.ylabel("Ilość pkt. na teście")
# plt.show()

# dni = [1,2,3,4,5]
# sprzedaz = [10,12,15,14,18]
# koszty = [6,7,8,7,9]
#
# plt.plot(dni, sprzedaz, label="Sprzedaz")
# plt.plot(dni, koszty, label="Koszty")
# plt.title("Sprzedaż i koszty")
# plt.xlabel("Dzień")
# plt.ylabel("Kwota")
# plt.legend()
# plt.ylim(top=30, bottom=-30)
# plt.show()

#zadania
# Zadanie 1 Matplotlib
# Stwórz wykres liniowy, który pokaże sprzedaż sklepu w kolejnych dniach tygodnia.
# Na wykresie:
# dodaj tytuł
# opisz oś X i Y
# dodaj markery w punktach

dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
sprzedaz = [120, 150, 180, 160, 170, 210, 190]

plt.plot(
    dni,
         sprzedaz,
         marker="o",
         markersize=10
         )
plt.title("Sprzedaz sklepu")
plt.xlabel("Dni tygodnia")
plt.ylabel("Sprzedaz")
plt.show()
# --------------------------------------------------------------

# Zadanie 2 Matplotlib
# Stwórz wykres słupkowy, który pokaże sprzedaż czterech produktów.
# Na wykresie:
# dodaj tytuł
# opisz osie
produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
sprzedaz = [25, 18, 40, 12]

plt.bar(produkty, sprzedaz)
plt.title("Sprzedaz produktow")
plt.xlabel("Produkty")
plt.ylabel("Sprzedaz")
plt.show()

# --------------------------------------------------------------

# Zadanie 3 Matplotlib
# Oto wyniki testu studentów.
# Stwórz histogram, który pokaże rozkład wyników.

wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]

plt.hist(wyniki)
plt.title("Histogram wynikow studentow")
plt.show()

# --------------------------------------------------------------