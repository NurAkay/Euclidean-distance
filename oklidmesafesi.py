# Noktaların Tanımlanması
noktalar = [(1, 2), (4, 6), (5, 9), (8, 8)]  # Örnek noktalar, kendi noktalarınızı ekleyebilirsiniz

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def oklidMesafesi(nokta1, nokta2):
    x_farki = nokta2[0] - nokta1[0]
    y_farki = nokta2[1] - nokta1[1]
    return (x_farki * x_farki + y_farki * y_farki) ** 0.5

# Mesafelerin Hesaplanması
mesafeler = []
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Minimum Mesafenin Bulunması
min_mesafe = min(mesafeler)

# Sonuçları Yazdırma
print("Mesafeler:", mesafeler)
print("Minimum Mesafe:", min_mesafe)
