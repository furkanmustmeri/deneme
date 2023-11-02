print('''    _                       __
              /   \                  /      *
             '      \              /          *
            |       |Oo          o|            |
            `    \  |OOOo......oOO|   /        |
             `    \OOOOOOOOOOOOOOO\//        /
               \ _o\OOOOOOOOOOOOOOOO//. ___ /
           ______OOOOOOOOOOOOOOOOOOOOOOOo.___
            --- OO'* `OOOOOOOOOO'*  `OOOOO--
                OO.   OOOOOOOOO'    .OOOOO o
                `OOOooOOOOOOOOOooooOOOOOO'OOOo
              .OO "OOOOOOOOOOOOOOOOOOOO"OOOOOOOo
          __ OOOOOO`OOOOOOOOOOOOOOOO"OOOOOOOOOOOOo
         ___OOOOOOOO_"OOOOOOOOOOO"_OOOOOOOOOOOOOOOO
           OOOOO^OOOO0`(____)/"OOOOOOOOOOOOO^OOOOOO
           OOOOO OO000/00||00000000OOOOOOOO OOOOOO
           OOOOO O0000000000000000 ppppoooooOOOOOO
           `OOOOO 0000000000000000 QQQQ "OOOOOOO"
            o"OOOO 000000000000000oooooOOoooooooO'
            OOo"OOOO.00000000000000000000OOOOOOOO'
           OOOOOO QQQQ 0000000000000000000OOOOOOO
          OOOOOO00eeee00000000000000000000OOOOOOOO.
         OOOOOOOO000000000000000000000000OOOOOOOOOO
         OOOOOOOOO00000000000000000000000OOOOOOOOOO
         `OOOOOOOOO000000000000000000000OOOOOOOOOOO
           "OOOOOOOO0000000000000000000OOOOOOOOOOO'
             "OOOOOOO00000000000000000OOOOOOOOOO"
  .ooooOOOOOOOo"OOOOOOO000000000000OOOOOOOOOOO"
.OOO"""""""""".oOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
OOO         QQQQO"'                     `"QQQQ
OOO
`OOo.
  `"OOOOOOOOOOOOoooooooo....''')


print(f"Welcome to the MAZE!\nYour Mission is to help mice to find the cheese!")

choice1 = input("You don't know where you are right now. You need to find the kitchen. Would you like to explore the world around you? Type yes, or no\n")

if choice1 == "yes":
    print(f"You are an explorer woow!")
    
    choice2 = input("Let's see...Should mice go to left or right? There are sounds coming from the right..Write left or right\n")

    if choice2 == "left":
        choice3 = input("You found yourself in a weird room, but good news is that there is a little cheese on a small rectangular platform. Do you want to take it? yes or no?\n")
        if choice3 == "yes":
            print(f"You are dead as hell!!!")
        else:
            choice4=input("You are smart to not touch it. There are two doors in front of you. Would you like to choose the left on or right one?\n")
            if choice4 == "right":
                print('''    _--"-.
      .-"      "-.
     |""--..      '-.
     |      ""--..   '-.
     |.-. .-".    ""--..".
     |'./  -_'  .-.      |
     |      .-. '.-'   .-'
     '--..  '.'    .-  -.
          ""--..   '_'   :
                ""--..   |
                      ""-'\nYou have found the treasure and you can eat as much cheese as you want!!!''')
            else:
                print(f"Homeowners found you and you are dead now :(((")
    else:
        print(f"Homeowners found you and you are dead now :(((")

else:
    print("Mice is so sad...:((")