#X values
x_old = ["F", "R", "B", "L"]
x_new = ["", "", "", ""]

#Y Values
y_old = ["F", "D", "B", "U"]
y_new = ["", "", "", ""]

#State
state = ""

file1 = open("/tmp/rubiks-cube-NxNxN-solver/solution.txt","r")
solution = file1.read()
solve = solution.split()
changed = [ ]
for q in range(len(solve)):
    changed.append('')

while(True):

    for q in range(len(solve)):
        changed[q] = ''
    
    #Rotation 0 = 0deg || 1 = 90 deg || 2 = 180 deg || 3 = 270 deg #    
    x_rot = 0
    y_rot = 0
    x_new = ["", "", "", ""]
    y_new = ["", "", "", ""]

    
    direction = input("X or Y: ")
    rotate = input("Degree: ")
    move = input("Move: ")
    direction = direction.upper()
    if (direction == "X"):
        x_rot = rotate
        y_rot = 0          
    elif (direction == "Y"):
        x_rot = 0
        y_rot = rotate
    else:
        break
    
    if (x_rot == '1'):
        x_new[0] = x_old[3]
        x_new[1] = x_old[0]
        x_new[2] = x_old[1]
        x_new[3] = x_old[2]
        
    if (x_rot == '2'):
        x_new[0] = x_old[2]
        x_new[1] = x_old[3]
        x_new[2] = x_old[0]
        x_new[3] = x_old[1]

    if (x_rot == '3'):
        x_new[0] = x_old[1]
        x_new[1] = x_old[2]
        x_new[2] = x_old[3]
        x_new[3] = x_old[0]

    if (y_rot == '1'):

        y_new[0] = y_old[3]
        y_new[1] = y_old[0]
        y_new[2] = y_old[1]
        y_new[3] = y_old[2]

    if (y_rot == '2'):
        y_new[0] = y_old[2]
        y_new[1] = y_old[3]
        y_new[2] = y_old[0]
        y_new[3] = y_old[1]

    if (y_rot == '3'):
        y_new[0] = y_old[1]
        y_new[1] = y_old[2]
        y_new[2] = y_old[3]
        y_new[3] = y_old[0]

    x_rot = int(x_rot)
    y_rot = int(y_rot)

    
    if (x_rot == 0 and (y_rot != 0)):
        state = y_old
        state_new = y_new
    elif (x_rot != 0 and (y_rot == 0)):
        state = x_old
        state_new = x_new

    if ( (x_rot == 0) and (y_rot ==0) ):
        print(solve)
        print("Do:", solve[int(move)])  
        x_new = x_old
        y_new = y_old
        continue
    else:
        for k in range(len(state)):
            for i in range(len(solve)):
                if(state[k] in solve[i]):
                    if (changed[i] != "ok"):
                        text = solve[i]
                        text = text[:0] + state_new[k] + text[1:]
                        solve[i] = text
                        changed[i] = "ok"

    if (x_rot == 0 and (y_rot != 0)):
        y_old = y_new
    elif (x_rot != 0 and (y_rot == 0)):
        x_old = x_new

    print(solve)
        
    print("Do:", solve[int(move)])    
    #########################################################
print("Solved")
