# -*- coding: utf-8 -*-
##################################
#    Sesli Harf Bulma Projesi    #
#          Yazar: Babat          #
##################################

print(
    "##################################\n" + "#    Sesli Harf Bulma Projesi    #\n" + "#          Yazar: Babat        "
                                                                                      "  #\n" +
    "##################################",
    sep="")

sesli_harfler = "AEIİOÖUÜaeıioöuü"
sayac = 0


# Sesli harf sayımı
def seslidir(harf):
    return harf in sesli_harfler


# Kelime girişi
def kelime_sor():
    return input(str("Bir kelime giriniz: "))


# Girilen kelimedeki sesli harf sayısı
def artir(n, kelime):
    for h in kelime:
        if seslidir(h):
            n += 1
    return n


# Ekrana verilecek mesaj
def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} tane sesli harf vardır."
    print(mesaj.format(kelime, artir(sayac, kelime)))


# Çalıştırma fonsiyonu
def calistir():
    kelime = kelime_sor()
    ekrana_bas(kelime)


if __name__ == '__main__':
    calistir()
