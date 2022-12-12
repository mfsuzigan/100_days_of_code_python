## should be run on http://reeborg.ca, field MAZE

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def face_east():
    while not is_facing_north():
        turn_left()
    turn_right()
    
sound(True)
face_east()
    
while not at_goal():
    
    if right_is_clear():
        turn_right()
        move()
   
    elif front_is_clear():
        move()
        
    else:
        turn_left()

done()