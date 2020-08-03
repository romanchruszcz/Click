import pyautogui
import webbrowser
from datetime import datetime
import time
import os
import schedule
print("otworz przegladarke i ustaw  myszkę w odpowiednim miejscu:")
print("program uruchomi się po 5 sekundach od teraz")
i = 5
while i > 0:
    time.sleep(1)
    print(i)
    i -=1
print("start")

currentMouseX, currentMouseY = pyautogui.position()
print("Twoje koordynaty to: ", currentMouseX,currentMouseY)

c = input("podaj adres strony: ")
x = input('wprowadz "minutę" dla każdej godziny w której ma otworzyć się strona \n przykład: jeśli wpiszesz 05 to co godzinę tj. 06:05, 07:05 program będzie uruchamiał przeglądarkę: ')
a = ":" + x

opening = int(input("wprowadź ilość sekund na włączenie przeglądarki, im mniej RAMu tym dłuższy czas: "))
loading = int(input("wprowadz ilość sekund na wczytywanie strony, im wolniejsze łącze tym dłuższy czas: "))
def job():
    webbrowser.open(c)
    time.sleep(opening)
    pyautogui.moveTo(currentMouseX, currentMouseY) # przesuwa kursor do wybranego miejsca 
    
    time.sleep(3)
    pyautogui.click() # klika w miejsce ktore wybierze
    time.sleep(loading)
    print("za 30 sekund przeglądarka się wyłączy")
    time.sleep(30)
    
    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im opera.exe /f")
schedule.every().hour.at(a).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    