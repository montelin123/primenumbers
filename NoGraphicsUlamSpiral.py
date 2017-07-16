listPrimes=[2,3,5] #with open file , json etc
listNumbers= [0,1,2,3] #with open file , json etc
class Start(): #starting coord. 
    x=0
    y=0
def up():
    Start.y -= 10
def down():
    Start.y += 10
def right():
    Start.x += 10
def left():
    Start.x -= 10
def main():
    a=0 # counts how many numbers
    counter = 0
    counterList = [0]
    for e in listNumbers:
        try:
            if counter > len(counterList)-1:
                counterList.append(counter)
            for item in counterList:
                up()
                if item in listPrimes:
                    #setTextColor('red')
                    a += 1
                else:
                    a += 1
            if counter > len(counterList)-1:
                counterList.append(counter)
            for item in counterList:
                right()
                if item in listPrimes:
                    #setTextColor('red')
                    a += 1
                else:
                    a += 1
            counter +=1
            if counter > len(counterList)-1:
                counterList.append(counter)
            for item in counterList:
                down()
                if item in listPrimes:
                    #setTextColor('red')
                    a += 1
                else:
                    a += 1
            if counter > len(counterList)-1:
                counterList.append(counter)
            for item in counterList:
                left()
                if item in listPrimes:
                    #setTextColor('red')
                    a += 1
                else:
                    a += 1
            counter += 1
        except IndexError:
            pass