##################################
#    Sesli Harf Bulma Projesi    #
#          Yazar: Babat          #
##################################

print(
    "##################################\n" + "#    Sesli Harf Bulma Projesi    #\n" + "#          Yazar: Babat          #\n" + "##################################",
    sep="")

while True:
    sesli_harfler = 'AEIİOÖUÜaeıioöuü'
    sayac = 0

    kelime = input('Bir kelime giriniz: ')


    def seslidir(harf):
        # print("sayac değişkeninin değeri şu anda: ", sayac)
        return harf in sesli_harfler


    def artir():
        global sayac
        for harf in kelime:
            if seslidir(harf):
                sayac += 1
        return sayac


    mesaj = "{} kelimesinde {} sesli harf vardır."
    print(mesaj.format(kelime, artir()))
