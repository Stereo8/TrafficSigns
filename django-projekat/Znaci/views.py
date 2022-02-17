from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse, JsonResponse
import pandas as pd
from Znaci.models import Pitanje
import os
import json



def index(request: HttpRequest):
    return render(request, 'base.html')

def pojediExcel(request: HttpRequest):
    module_dir = os.path.dirname(__file__)
    excel_path = os.path.join(module_dir, 'data/Srbija2008.xlsx')
    workbook = pd.read_excel(excel_path)

    imena_slika = workbook["TAČAN"]
    tacni_odg = workbook["Tačni"]
    netacni_odg1 = workbook["Netačni 1"]
    netacni_odg2 = workbook["Netačni 2"]
    opis = workbook["Opis"]

    pitanja = []
    unos = []

    for i in range(508):
        pitanje = {
            "slika": 'znak' + str(imena_slika[i]) + '.webp',
            "tacan_odg": tacni_odg[i],
            "netacan_odg1": netacni_odg1[i],
            "netacan_odg2": netacni_odg2[i],
            "opis": opis[i]
        }
        pitanja.append(pitanje)

    for pitanje in pitanja:
        unos.append(Pitanje(
            znak = pitanje['slika'],
            tacan_odg = pitanje['tacan_odg'],
            netacni_odg1 = pitanje['netacan_odg1'],
            netacni_odg2 = pitanje['netacan_odg2'],
            opis = pitanje['opis']))

    Pitanje.objects.bulk_create(unos)

def prikazi_pitanje(request: HttpRequest, pitanje_id: int):
    pitanje = get_object_or_404(Pitanje, pk=pitanje_id)
    pitanje_dict = {
        'znak': pitanje.znak,
        'opis': pitanje.opis,
        'tacan_odg': pitanje.tacan_odg,
        'netacni_odg1': pitanje.netacni_odg1,
        'netacni_odg2': pitanje.netacni_odg2
    }
    return JsonResponse(pitanje_dict)