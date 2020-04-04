# OOP kurallarına uyacak şekilde düzenlendi. Class formatına getirildi.

print("Sayaç version = 1.2")
print("##################################\n" + "#    Sesli Harf Bulma Projesi    #\n" + "#          Yazar: Babat "
      "  #\n" + "##################################", sep="")


class HarfSayaci:

    def kelime_sor(self):
        return input(str("Bir kelime giriniz: "))

    def __init__(self):
        self.sesli_harfler = "AEIİOÖUÜaeıioöuü"
        self.sayac = 0

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac += 1
        return self.sayac

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesli_harf_sayisi = self.artir()
        print(mesaj.format(self.kelime, sesli_harf_sayisi))

    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()


if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()