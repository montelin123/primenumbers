from graphics import *
import json
with open('listaliczb.py','r') as f:
     listaLiczb= json.load(f)
with open('modul.py', 'r') as file:
     pierwsze10000 = json.load(file)

class Start():
    x=800
    y=400
    z = 0
    b = 0
def gora():
    Start.y -= 10
    Start.x -= 5
def dol():
    Start.y += 10
    Start.x += 5
def prawo():
    Start.x += 10
    Start.y -= 5
def lewo():
    Start.x -= 10
    Start.y += 5

def main():
    win = GraphWin("r", 1600, 800)
    a=0
    licznik = 0
    licznikList = [0]
    for e in listaLiczb:
        try:
            if licznik > len(licznikList)-1:
                licznikList.append(licznik)
            for item in licznikList:
                gora()
                c = Text(Point(Start.x, Start.y), str(listaLiczb[a]))#str(listaLiczb[a])
                if a in pierwsze10000:
                    c.setTextColor('red')
                    c.draw(win).setSize(5)
                    a += 1
                # elif e % 2 != 0:
                #     c.setTextColor('white')
                #     c.draw(win).setSize(5)
                #     a += 1
                else:
                    c.setTextColor('black')
                    c.draw(win).setSize(5)

                    a += 1
            if licznik > len(licznikList)-1:
                licznikList.append(licznik)
            for item in licznikList:
                prawo()
                c = Text(Point(Start.x, Start.y), str(listaLiczb[a]))
                if a in pierwsze10000:
                    c.setTextColor('red')
                    c.draw(win).setSize(5)
                    a += 1
                # elif item % 2 != 0:
                #     c.setTextColor('white')
                #     c.draw(win).setSize(5)
                #     a += 1
                else:
                    c.setTextColor('black')
                    c.draw(win).setSize(5)
                    a += 1
            licznik +=1
            if licznik > len(licznikList)-1:
                licznikList.append(licznik)
            for item in licznikList:
                dol()
                c = Text(Point(Start.x, Start.y), str(listaLiczb[a]))
                if a in pierwsze10000:
                    c.setTextColor('red')
                    c.draw(win).setSize(5)
                    a += 1
                # elif e % 2 != 0:
                    # c.setTextColor('white')
                    # c.draw(win).setSize(5)
                    # a += 1
                else:
                    c.setTextColor('black')
                    c.draw(win).setSize(5)
                    a += 1
            if licznik > len(licznikList)-1:
                licznikList.append(licznik)
            for item in licznikList:
                lewo()
                c = Text(Point(Start.x, Start.y), str(listaLiczb[a]))
                if a in pierwsze10000:
                    c.setTextColor('red')
                    c.draw(win).setSize(5)
                    a += 1
                # elif e % 2 != 0:
                    # c.setTextColor('white')
                    # c.draw(win).setSize(5)
                    # a += 1
                else:
                    c.setTextColor('black')
                    c.draw(win).setSize(5)
                    a += 1
            licznik += 1
        except IndexError:
            pass
    win.getMouse()  # Pause to view result
    win.close()
main()
