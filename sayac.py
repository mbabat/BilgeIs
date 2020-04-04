# -*- coding: utf-8 -*-

######################################
# Sesli ve Sessiz Harf Bulma Projesi #
#          Yazar: Babat              #
######################################

# OOP kurallarına uyacak şekilde düzenlendi. Class formatına getirildi.

print("Sayaç version = 1.2")
print("######################################\n" + "# Sesli ve Sessiz Harf Bulma Projesi #\n" + "#          Yazar: Babat              #\n" + "######################################", sep="")


class HarfSayaci:

    @staticmethod
    def kelime_sor():
        return input(str("Bir kelime giriniz: "))

    def __init__(self):
        self.sesli_harfler = "AEIİOÖUÜaeıioöuü"
        self.sessiz_harfler = "BCÇDFGĞHJKLMNPRSŞTVYZbcçdfgğhjklmnprsştvyz"
        self.sayac_sesli = 0
        self.sayac_sessiz = 0

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self,harf):
        return harf in self.sessiz_harfler

    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac_sesli += 1
            if self.sessizdir(harf):
                self.sayac_sessiz += 1
        return self.sayac_sesli, self.sayac_sessiz

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf, {} sessiz harf vardır."
        sesli, sessiz = self.artir()
        print(mesaj.format(self.kelime, sesli, sessiz))

    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()


if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()