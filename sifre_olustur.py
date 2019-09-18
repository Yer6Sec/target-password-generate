#!/usr/bin/env python
# -*- coding: utf-8 -*-
#YER6SEC.ORG GELECEK BİZİZ!
import itertools
from collections import Counter
from datetime import datetime
import os.path
print("""                               Yer6Sec.Org | Yaşlı Kurtlar

                                Şifre oluşturucu V1.3""")
anahtar_kelimeler = input("Lütfen kurban hakkında anahtar kelimeleri girin!(Anahtar kelimeleri ',' ile ayırın!): ")
kelimeler = anahtar_kelimeler.split(",")
kelime_uzunlugu = len(kelimeler)

if (kelime_uzunlugu <= 0 or len(anahtar_kelimeler.strip()) <= 0):
    print("\n\tLütfen en az 1 kelime giriniz.\n")
    exit()

sayi_uzunlugu = 0
sayi_gir = input("Lütfen kurban ile alakalı sayıları girin!(Sayıları ',' ile ayırın): ")
sayi = sayi_gir.split(",")
sayi_uzunlugu = len(sayi)

ozelkarakter_uzunlugu = 0
ozelkarakter_gir = input("Kurbanın kullanabileceğini düşündüğünüz özel karakterleri girin!(Karakterleri boşluk ile ayırın. Örnek özel karakterler: '. , ? - _ ! +'): ")
ozelkarakter = ozelkarakter_gir.split(" ")
ozelkarakter_uzunlugu = len(ozelkarakter)

karakter_limit = None
try:
    karakter_limit = int(input("Girdiğiniz değerlere göre en fazla kaç şifre oluşturulsun? (Örnek: 15): "))
except ValueError:
    print("\n\tLütfen geçerli bir sayı girin!\n")
    try:
        karakter_limit = int(input("Girdiğiniz değerlere göre en fazla kaç şifre oluşturulsun? (Örnek: 15): "))
    except ValueError:
        print("\n\tUygulama kapatılıyor!")
        exit()

kelime_listesi = []
kelime_listesi_sayi = []
karmasik_kelimeler = []
karmasik_kelimeler_removed = []
tum_kelimeler = []

for counter in range(0, kelime_uzunlugu):
    kelime_listesi.append([])

for counter in range(0, kelime_uzunlugu):
    kelime_listesi_sayi.append([])

print("\n\tKelime(ler):{}\n\tÖzel karakter(ler):{}\n\tSayı(lar):{}\n".format(kelime_uzunlugu, ozelkarakter_uzunlugu or None,
                                                                     sayi_uzunlugu or None))


def kelime_uret(kelimeler, min, max):
    for i in range(int(min), int(max) + 1):
        for j in itertools.product(kelimeler, repeat=i):
            counter_for_join_word = len(j)
            counter_list = Counter(j)
            for element in j:
                if (counter_list[element] < 3):
                    if not ''.join(j) in kelime_listesi[counter_for_join_word - 1]:
                        kelime_listesi[counter_for_join_word - 1].append(''.join(j))
                        ekle_sayi(''.join(j), counter_for_join_word - 1) if sayi_uzunlugu > 0 else False

                    if (ozelkarakter_uzunlugu > 0 and len(j) == 1):
                        for stabil_bey in ozelkarakter:
                            if not j[0] + stabil_bey in kelime_listesi[0]:
                                kelime_listesi[0].append(j[0] + stabil_bey)
                                ekle_sayi(j[0] + stabil_bey, 0) if sayi_uzunlugu > 0 else False
                            if not stabil_bey + j[0] in kelime_listesi[0]:
                                kelime_listesi[0].append(stabil_bey + j[0])
                                ekle_sayi(stabil_bey + j[0], 0) if sayi_uzunlugu > 0 else False

                    if (ozelkarakter_uzunlugu > 0 and len(j) > 1):
                        for stabil_bey in ozelkarakter:
                            if not stabil_bey.join(j) in kelime_listesi[counter_for_join_word - 1]:
                                kelime_listesi[counter_for_join_word - 1].append(stabil_bey.join(j))
                                ekle_sayi(stabil_bey.join(j), counter_for_join_word - 1) if sayi_uzunlugu > 0 else False
    tum_kelimeler.append(kelime_listesi)


def ekle_sayi(kelime_eklereis, kac_kelime):
    for sayilar_buraya in sayi:
        if not sayilar_buraya + kelime_eklereis in kelime_listesi[kac_kelime]:
            kelime_listesi_sayi[kac_kelime].append(sayilar_buraya + kelime_eklereis)
        if not kelime_eklereis + sayilar_buraya in kelime_listesi[kac_kelime]:
            kelime_listesi_sayi[kac_kelime].append(kelime_eklereis + sayilar_buraya)
    tum_kelimeler.append(kelime_listesi_sayi)


def ozelkarakter_uret_reisss():
    for kelimeler_list in kelime_listesi:
        for word in kelimeler_list:
            for kelimeler_list_with_sayilar_buraya in kelime_listesi_sayi:
                for reis_sayilar_buraya in kelimeler_list_with_sayilar_buraya:
                    karmasik_kelimeler.append(word + reis_sayilar_buraya)

    for ozel_karakter_kelime in karmasik_kelimeler:
        for kelime_ayirici in kelimeler:
            if (ozel_karakter_kelime.count(kelime_ayirici) > 1):
                karmasik_kelimeler_removed.append(ozel_karakter_kelime)

    karmasik_kelimeler_finally = list(set(karmasik_kelimeler).difference(karmasik_kelimeler_removed))
    tum_kelimeler.append(karmasik_kelimeler_finally)


kelime_uret(kelimeler, 1, kelime_uzunlugu)
ozelkarakter_uret_reisss()

file_existed_kontrolet = 0

dosyaadi_ = None

karakter_sayacccc = 0

kelime_ekle_haci = []


def yazustad_kelimeler(tum_kelimeler_list):
    global file_existed_kontrolet
    global dosyaadi_
    global karakter_sayacccc
    global karakter_limit
    global kelime_ekle_haci

    if (file_existed_kontrolet == 0):
        dosyaadi_ = "yer6secorg_sifre-{}.txt".format(datetime.now().strftime('%H-%M'))
        dosyaadi_ = file_existed(dosyaadi_)
        file_existed_kontrolet = 1

    sifre_listesi = open(dosyaadi_, mode='a')

    for item in tum_kelimeler_list:
        if (type(item) == list):
            yazustad_kelimeler(item)
        elif (type(item) == str):
            if (karakter_limit is not None):
                if (len(item) <= karakter_limit):
                    if (item not in kelime_ekle_haci):
                        sifre_listesi.write("{}\n".format(item))
                        kelime_ekle_haci.append(item)
                        karakter_sayacccc += 1
            else:
                if (item not in kelime_ekle_haci):
                    sifre_listesi.write("{}\n".format(item))
                    kelime_ekle_haci.append(item)
                    karakter_sayacccc += 1
        else:
            print("Bilinmeyen dosya tipi: ", item)

    sifre_listesi.close()


def file_existed(dosyaadi_kontrol, counter=0):
    global dosyaadi_
    if (os.path.isfile(dosyaadi_kontrol)):
        yeni_sayac = counter + 1
        new_dosyaadi_ = "yer6secorg_sifre-{}({}).txt".format(datetime.now().strftime('%H-%M'), yeni_sayac)
        return file_existed(new_dosyaadi_, yeni_sayac)
    else:
        dosyaadi_ = dosyaadi_kontrol
        return dosyaadi_


yazustad_kelimeler(tum_kelimeler)
print("\t{} Kelimeler üretildi. Bu kelimeleri görebilirsiniz {}\n".format(karakter_sayacccc, dosyaadi_))
