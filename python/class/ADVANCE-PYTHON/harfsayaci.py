class HarfSayaci:
    def __init__(self):
        self.sesli_harfler = "aeıioöuü"
        self.sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
        self.sesli_sayac = 0
        self.sessiz_sayac = 0

    def kelime_sor(self):
        return input("Bir kelime giriniz: ").lower()

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sesli_sayac += 1
            elif self.sessizdir(harf):
                self.sessiz_sayac += 1
        return self.sesli_sayac, self.sessiz_sayac

    def ekrana_goster(self):
        sesli_harf_sayisi, sessiz_harf_sayisi = self.artir()
        mesaj = f"{self.kelime} kelimesinde {sesli_harf_sayisi} sesli harf vardır"
        mesaj2 = f"{self.kelime} kelimesinde {sessiz_harf_sayisi} sessiz harf vardır"
        print(mesaj)
        print(mesaj2)

    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_goster()


if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()
