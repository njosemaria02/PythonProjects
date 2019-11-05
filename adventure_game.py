# Update this text to match your story.

#Instructions: game file is adventure_game.py !!!
start = '''
/\/\/\/\You wake up one morning and find that you aren't in your bed; you aren't even in your room.
        You're in the middle of a giant maze.
        A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
        There is a hallway to your right and to your left.
'''

print(start)

path = "start"

while True:
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
    if user_input == "left":
        left1 = '''
        You decide to go left and you see a branch start moving and bending itself.
        As it mysteriously moves on its own, it forms an ominous shape, similar to that of a skull.
        It freaks you out so bad you die!
        '''
        print(left1)
        break
    elif user_input == "right":
        path = "right1"
        break
    else:
        print("That not an option!")
        continue

if path == "right1":
    while True:
        print("You see two paths. Select if you want or go 'left' or 'right'")
        user_input = input()
        if user_input == "left": #this is left2
            path = "left2"
            break
        elif user_input == "right": #this is right2
            path = "right2"
            break
        else:
            print("Not an option. Try again!")
            continue

if path == "left2":
    while True:
        print("You see two more paths. Do you go right or continue forward?")
        user_input = input()
        if user_input == "forward": #this is forward1
            path = "forward1"
            break
        elif user_input == "right": #this is right3
            path = "right3"
            break
        else:
            print("Not an option. Try again!")
            continue
if path == "forward1":
    print("There is nothing here. You have to go back.")
if path == "right3":
    right3 = '''
    As you turn the corner, a small poison spike grazed you shoulder.
    You start seeing visions and hallucinations and suddenly...
    '''
    print(right3)
if path == "right2":
    while True:
        print("You see two more paths. Do you go left or continue forward?")
        user_input = input()
        if user_input == "forward": #this is forward2
            path = "forward2"
            break
        elif user_input == "left": #this is left3
            path = "left3"
            break
        else:
            print("Not an option. Try again!")
            continue
if path == "forward2":
    forward2 = '''
    You walk forward and discover a hallway full of spikes and prongs.
    And before you knew it, your foot accidently steps on one of the spikes and
    it impales you...
    '''
    print(forward2)
if path == "left3":
    left3 = '''
    You look around the shrubbery of vines and poisonous plants and see a light.
    You decide to follow that light and see crowds of individuals each holding flashlights.
    You recognize these people as your friends and family that were worried for you.
    You feel loved and you go home....
    '''
    print(left3)
