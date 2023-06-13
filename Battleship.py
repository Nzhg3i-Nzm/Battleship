'''
Nzhg3i_Nzm
Battleship program
May 2023
'''

p1_ships={ }
p2_ships={ }
ship_list=[]
validplace=False
used=[]

def check_used(length, direction, let, num):
    '''
checks to see if a spot is already being used
'''
    global validplace
    global ship_list
    global used
    if direction=="r":
        validplace=True
        i=0
        while i<length:
            plot=let+str(num+i)
            if plot in used:
                validplace=False
                break
            ship_list.append(plot)
            used.append(plot)
            i+=1
    elif direction=="l":
        validplace=True
        i=0
        while i<length:
            plot=let+str(num-i)
            if plot in used:
                validplace=False
                break
            ship_list.append(plot)
            used.append(plot)
            i+=1
    elif direction=="u":
        validplace=True
        i=0
        while i<length:
            plot=chr(ord(let)-i)+str(num)
            if plot in used:
                validplace=False
                break
            ship_list.append(plot)
            used.append(plot)
            i+=1
    elif direction=="d":
        validplace=True
        i=0
        while i<length:
            plot=chr(ord(let)+i)+str(num)
            if plot in used:
                validplace=False
                break
            ship_list.append(plot)
            used.append(plot)
            i+=1

def check_dir(start, direction, ship):
    '''
checks the ship placement and adds the rest of the points
'''
    global ship_list
    global validplace
    global used
    let=start[0]
    num=start[1:]
    num=int(num)
    ship_list=[]
    if ship=="cv":
        if ((num<5) and (direction=="l")):
            validplace=False
        elif ((num>6) and (direction=="r")):
            validplace=False
        elif ((let<"e") and (direction=="u")):
            validplace=False
        elif ((let>"f") and (direction=="d")):
            validplace=False
        elif direction=="r":
            check_used(5, direction, let, num)
        elif direction=="l":
            check_used(5, direction, let, num)
        elif direction=="u":
            check_used(5, direction, let, num)
        elif direction=="d":
            check_used(5, direction, let, num)
    elif ship=="bb":
        if ((num<4) and (direction=="l")):
            validplace=False
        elif ((num>7) and (direction=="r")):
            validplace=False
        elif ((let<"d") and (direction=="u")):
            validplace=False
        elif ((let>"g") and (direction=="d")):
            validplace=False
        elif direction=="r":
            check_used(4, direction, let, num)
        elif direction=="l":
            check_used(4, direction, let, num)
        elif direction=="u":
            check_used(4, direction, let, num)
        elif direction=="d":
            check_used(4, direction, let, num)
    elif ship=="ca":
        if ((num<3) and (direction=="l")):
            validplace=False
        elif ((num>8) and (direction=="r")):
            validplace=False
        elif ((let<"c") and (direction=="u")):
            validplace=False
        elif ((let>"h") and (direction=="d")):
            validplace=False
        elif direction=="r":
            check_used(3, direction, let, num)
        elif direction=="l":
            check_used(3, direction, let, num)
        elif direction=="u":
            check_used(3, direction, let, num)
        elif direction=="d":
            check_used(3, direction, let, num)
    elif ship=="ss":
        if ((num<3) and (direction=="l")):
            validplace=False
        elif ((num>8) and (direction=="r")):
            validplace=False
        elif ((let<"c") and (direction=="u")):
            validplace=False
        elif ((let>"h") and (direction=="d")):
            validplace=False
        elif direction=="r":
            check_used(3, direction, let, num)
        elif direction=="l":
            check_used(3, direction, let, num)
        elif direction=="u":
            check_used(3, direction, let, num)
        elif direction=="d":
            check_used(3, direction, let, num)
    elif ship=="dd":
        if ((num<2) and (direction=="l")):
            validplace=False
        elif ((num>9) and (direction=="r")):
            validplace=False
        elif ((let<"b") and (direction=="u")):
            validplace=False
        elif ((let>"i") and (direction=="d")):
            validplace=False
        elif direction=="r":
            check_used(2, direction, let, num)
        elif direction=="l":
            check_used(2, direction, let, num)
        elif direction=="u":
            check_used(2, direction, let, num)
        elif direction=="d":
           check_used(2, direction, let, num)

def place_ships(ships):
    '''
places a player's ships
'''
    ships.clear()
    ship_types=["cv", "bb", "ca", "ss", "dd"]
    global validplace
    global used
    for shipp in ship_types:
        validplace=False
        while validplace==False:
            print(used)
            print("where do you want your", shipp, "to start?")
            place=input()
            place=place.strip()
            place=place.lower()
            print("what direction do you want your", shipp, "to go? (R=right L=left U=up D=down)")
            direction=input()
            direction=direction.lower()
            direction=direction.strip()
            check_dir(place, direction, shipp)
            ships[shipp]=ship_list
            if validplace==True:
                break
    used=[]

def prepare():
    '''
makes an empty player board
'''
    brd = { }
    for letter in "abcdefghij":
        row = [ ]
        for i in range(10):
            row.append("   ")
        brd[letter]=row
    return brd

def print_board(brd):
    '''
prints the board
'''
    print("      1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |")
    for key in brd:
        print(key.upper(), " | ", end="")
        for value in brd[key]:
            print(value, "|", end="")
        print("\n",end="")
        print("   ===================================================",end="\n")

def check_shot(sh, let, num, brd, ships):
    '''
checks to see hit/miss/hit_and_sunk
updates board and ships
'''
    res="miss"
    brd[let][num-1]=" O "
    ships2=[]
    for key in ships:
        ships2.append(key)
    for key in ships2:
        cur_ship=ships[key]
        if sh in cur_ship:
            res="hit"
            brd[let][num-1]=" X "
            cur_ship.remove(sh)
            if len(cur_ship)==0:
                res+= " and sunk"
                del ships[key]
    return res

def main():
    '''
plays battlehsip with text based grids
'''
    place_ships(p1_ships)
    place_ships(p2_ships)
    p1_grid=prepare()
    p2_grid=prepare()
    currentB=p1_grid
    currentS=p2_ships
    while True:
        print_board(currentB)
        while True:
            shot=input("where do you want to shoot?\n")
            shot=shot.strip()
            shot=shot.lower()
            good = True
            letter=shot[0]
            number=shot[1:]
            number=int(number)
            if letter<'a':
                good=False
            elif letter>'j':
                good=False
            elif number<1:
                good=False
            elif number>10:
                good=False
            elif currentB[letter][number-1] != "   ":
                good=False
            if good:
                break
        ans=check_shot(shot,letter,number,currentB,currentS)
        print(ans)
        if len(currentS)==0:
            print("you win!")
            ans=input("do you want to play again?")
            ans=ans.strip()
            ans=ans.lower()
            if ans[0]=="y":
                main()
                break
            else:
                break
        if currentB is p1_grid:
            currentB=p2_grid
            currentS=p1_ships
        else:
            currentB=p1_grid
            currentS=p2_ships


main()
