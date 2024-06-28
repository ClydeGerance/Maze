# Clyde Lester Gerance
# 185503
# October 11, 2022

##I hereby certify that the submission described in this document abides by the
##principles stipulated in the DISCS Academic Integrity Policy document.

##I further certify that I am the author of this submission and that any
##assistance I received in its preparation is fully acknowledged and
##disclosed in the documentation.

##I have also cited all sources from which I obtained data,
##ideas, or words that are directly copied or paraphrased
##in this document. Sources are properly credited according to accepted
##standards for professional publication.

## Strings
## --------------------------------------------------
Intro = "Welcome to the Maze!   \nSelect a level: 1, 2, or 3"
Choices = "Available Directions: "
Question = "Which direction will you take?"
Wrong = "Please choose an available direction."
Quit = "Try again next time. \nGoodbye."
Finish = "Found the exit! \nGoodbye."
Start = "Please choose your starting location."
End = "Please choose the exit location."
## --------------------------------------------------

## MAZE Illustrations and Directions
## --------------------------------------------------
I = '██'
O = '  '

m1 = [[I,I,I,I,I,I,I],
      [I,O,I,O,O,O,I],
      [I,O,I,O,I,I,I],
      [I,O,O,O,O,O,I],
      [I,O,I,O,I,I,I],
      [I,O,I,O,O,O,I],
      [I,I,I,I,I,I,I]]

D1 = [['South','East South','West'],['North East South','North East West South','West'],['North','North East','West']]

m2 = [[I,I,I,I,I,I,I,I,I],
      [I,O,O,O,O,O,O,O,I],
      [I,O,I,I,I,I,I,O,I],
      [I,O,O,O,O,O,I,O,I],
      [I,O,I,I,I,O,I,I,I],
      [I,O,I,O,I,O,O,O,I],
      [I,O,I,O,I,O,I,O,I],
      [I,O,O,O,I,O,I,O,I],
      [I,I,I,I,I,I,I,I,I],]

D2 = [['East South','East West','East West','West South'],['North East South','East West','West','North'],['North South','South','North East South','West'],['North East','North West','North','North']]

m3 = [[I,I,I,I,I,I,I,I,I,I,I],
      [I,O,O,O,O,O,O,O,I,O,I],
      [I,O,I,I,I,O,I,O,I,O,I],
      [I,O,O,O,I,O,I,O,O,O,I],
      [I,I,I,O,I,O,I,O,I,I,I],
      [I,O,O,O,O,O,I,O,O,O,I],
      [I,O,I,O,I,I,I,I,I,O,I],
      [I,O,I,O,O,O,I,O,I,O,I],
      [I,O,I,I,I,O,I,O,I,O,I],
      [I,O,O,O,I,O,I,O,O,O,I],
      [I,I,I,I,I,I,I,I,I,I,I]]

D3 = [['East South','East West','East West South','West South','South'],['North East','West South','North South','North East South','North West'],['East South','North East West South','North West','North East','West South'],['North South','North East','West South','East South','North South'],['North East','West','North','North East','North West']]

## --------------------------------------------------

## FUNCTIONS
def Locate(D,Z,m):
    print(Start)
    P = int(input())
    Y = P // Z
    X = P % Z
    print(End)
    E = int(input())
    EY = E // Z
    EX = E % Z
    p = ':)'
    e = '><'
    J = (2*(Y))+1
    K = (2*(X))+1
    L = (2*(EY))+1
    M = (2*(EX))+1
    m[J][K] = p
    m[L][M] = e
    def maze(m):
        y = ''
        i = 0
        while i < len(m):
            for x in m[i]:
                y += x 
            y += '\n'
            i += 1
        return y
    print(maze(m))
    print(Choices + D[Y][X])
    print(Question)
    answer = str(input()).casefold()## https://www.journaldev.com/23610/python-string-equals
    while answer != 'Quit'.casefold():
        if D[Y][X] == 'North':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'South':
            m[J][K] = O
            if answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'East South':
            m[J][K] = O
            if answer == 'East'.casefold():
                X += 1
                K += 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'West':
            m[J][K] = O
            if answer == 'West'.casefold():
                X -= 1
                K -= 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North East South':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'East'.casefold():
                X += 1
                K += 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North East West':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'East'.casefold():
                X += 1
                K += 2
            elif answer == 'West'.casefold():
                X -= 1
                K -= 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'West South':
            m[J][K] = O
            if answer == 'West'.casefold():
                X -= 1
                K -= 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'East':
            m[J][K] = O
            if answer == 'East'.casefold():
                X += 1
                K += 2 
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North West':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'West'.casefold():
                X -= 1
                K -= 2 
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'East West':
            m[J][K] = O
            if answer == 'East'.casefold():
                X += 1
                K += 2
            elif answer == 'West'.casefold():
                X -= 1
                K -= 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North South':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North West South':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'West'.casefold():
                X -= 1
                K -= 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North East':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'East'.casefold():
                X += 1
                K += 2             
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'East West South':
            m[J][K] = O
            if answer == 'East'.casefold():
                X += 1
                K += 2
            elif answer == 'West'.casefold():
                X -= 1
                K -= 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        elif D[Y][X] == 'North East West South':
            m[J][K] = O
            if answer == 'North'.casefold():
                Y -= 1
                J -= 2
            elif answer == 'East'.casefold():
                X += 1
                K += 2
            elif answer == 'West'.casefold():
                X -= 1
                K -= 2
            elif answer == 'South'.casefold():
                Y += 1
                J += 2
            else:
                print(Wrong)
                answer = str(input()).casefold()
                continue
        if (Y==EY)and(X==EX):
            break
        else:
            m[J][K] = p
            print(maze(m))
            print(Choices + D[Y][X])
            print(Question)
            answer = str(input()).casefold()
    if (Y==EY)and(X==EX):
        print(Finish)
    else:
        print(Quit)

# -----------------
# PROCESS
# -----------------
print(Intro)
Level=int(input())

if Level == 1:
    Locate(D1,3,m1)
if Level == 2:
    Locate(D2,4,m2)
if Level == 3:
    Locate(D3,5,m3)

