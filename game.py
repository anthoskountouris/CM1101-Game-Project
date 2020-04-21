from map import rooms
from player import *
from items import *
from gameparser import *
from condexit import *
import winsound
import time
from combat import *

def character_creation():

    winsound.PlaySound("game_intro.wav",winsound.SND_ASYNC)
    time.sleep(5)
    print("Introduce yourself!!")
    time.sleep(1)
    player_firstname,player_lastname="",""
    while True:
        player_firstname = input("\n\nWhat's your Firstname?")
        time.sleep(1)
        player_lastname = input("What's your Lastname?")
        time.sleep(1)
        if player_firstname!="" or player_lastname!="":
            break
        else:
            print("\nPlease enter a name!")
    print("\n\nYOUR MISSION'S BRIEFING:", '\n')
    
    print("\nYou are part of a rebel group,")
    time.sleep(3)
    print("\nWorking to fight against Ab.bee, an evil coopertion which has taken over your city")
    time.sleep(2)
    print("\nTonight's the only night when this facility is least guarded")
    time.sleep(2)
    print("\nThis is your only chance to save them.")
    time.sleep(3)
    print("\n\nMake.")
    time.sleep(2)
    print("\n\nIt.")
    time.sleep(2)
    print("\n\nCount!")
    time.sleep(3)
    print("\n\nGood luck, Officer ",player_lastname,", we're counting on you!")
    time.sleep(0.5)
    winsound.PlaySound("gong.wav",winsound.SND_ASYNC)
    print('\n' * 10)
    time.sleep(2)
    print("A WICKED HEISTY RESCUE\n\n\n\n")
    time.sleep(0.5)


def sounds(item):
    if item == "wrench":
        winsound.PlaySound("wrench.wav",winsound.SND_ASYNC)
    elif item == "key":
        winsound.PlaySound("key.wav",winsound.SND_ASYNC)
    elif item == "smoke":
        winsound.PlaySound("smoke.wav",winsound.SND_ASYNC)
    elif item == "mirror":
        winsound.PlaySound("mirror.wav",winsound.SND_ASYNC)
    elif item == "rope":
        winsound.PlaySound("rope.wav",winsound.SND_ASYNC)
    elif item == "acid":
        winsound.PlaySound("acid.wav",winsound.SND_ASYNC)


def list_of_items(items):
    """Takes a list of items and returns a comma-seperated list of item names"""
    list_items=""
    for x in items:
        if x == items[-1]:
            list_items =list_items + x["name"]
        else:
            list_items =list_items + x["name"]+", "
    return list_items
    

def print_inventory(items):
    """Takes a list of items from inventory and displays them"""
    if list_of_items(items) != "":
        print("You have",list_of_items(items),end="")
        print('.','\n')

def print_room_items(room):
    """Takes a room(dictionary) as an argument and displays the
        items available in the room"""
    if room["items"]!=[]:
        print("There is",list_of_items(room['items']),'here.')

def print_room(room):
    """Takes a room and displays its name and description.
        room is a dictionary"""
    print('\n\n\n',room['name'].upper())
    if room["check"]>0 and len(room["items"])<2:
        print('\n',room['alt description'],'\n')
    else:
        print('\n',room['description'],'\n')
    print_room_items(room)

    
def exit_leads_to(exits,direction):
    """Takes a dictionary of exits and a direction and
       returns the name of the room into which the exit leads"""
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """Prints a line for the menu of exits"""
    print("GO ",direction.upper(),"to",leads_to+".")

    
def print_menu(exits,room_items,inv_items):
    """Displays the list of possible actions"""
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits,direction))
    for item in room_items:
        if room_items!=[]:
            print("TAKE",item['id'],"to take",item["name"])
    for item in inv_items:
        if inv_items!=[]:
            print("EXAMINE",item['id'],"to examine",item["name"])

def is_valid_exit(exits,chosen_exit):
    """Checks if the chosen exit is a valid exit"""
    return chosen_exit in exits

def execute_go(direction):
    """Updates the current room based on the direction given"""
    global curr_room
    if is_valid_exit(curr_room["exits"], direction):
        curr_room["check"]+=1
        #print("\n'")
        #time.sleep(0.4)
        #print(" '")
        #time.sleep(0.4)
        #print("'")
        #time.sleep(0.4)
        #print(" '")
        #time.sleep(0.4)
        #print("------------------------")
        curr_room=rooms[curr_room["exits"][direction]]
        return curr_room
    else:
        print("You cannot go there.")

def execute_take(item):
    """Takes an item and moves it from list of items in curr room
       and moves it to the inventory"""
    global curr_room, inventory
    i,f=0,0
    while i<len(curr_room["items"]):
        if curr_room["items"][i]["id"]==item:
            f+=1
            inventory.append(curr_room["items"][i])
            sounds(curr_room["items"][i]["id"]) #sound of item-
            curr_room["items"].remove(curr_room["items"][i])
            print("You take the " + item + ".")
        i+=1
    if f==0:
        print("You cannot take that.")

    
def execute_examine(item):
    """Takes an item and displays its description"""
    global inventory
    f=0
    for stuff in inventory:
        if stuff["id"]==item:
            print(stuff["description"])
            f+=1
    if f==0:
        print("You don't have that item in your inventory.")


def execute_command(command):
    """Takes a command and executes the action requested by the user"""
    if len(command)==0:
        return
    if command[0]=="go":
        if len(command)>1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0]=="take":
        if len(command)>1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0]=="examine":
        if len(command)>1:
            execute_examine(command[1])
        else:
            print("Examine what?")

    else:
        print("What is that?! Follow the instructions!")
        
def menu(exits,room_items,inv_items):
    """Takes a dictionary of possible exits, current room items,
       and inventory items and displays the menu of possible actions and exits,
       then asks player to type an action."""
    print_menu(exits, room_items, inv_items)
    user_input=input("\nWhat would you like to do? >")
    normalised=normalise_input(user_input)
    return normalised
       
def main():
    character_creation()
    while True:
        if curr_room['name']=='Roof' and item_treasure in inventory:
            print("\n\nYou and the hostages use the rope to escape from the roof")
            time.sleep(2)
            print("\n\nCongratulations! You have successfully completed the mission!")
            break
            quit()
        print_room(curr_room)
        print_inventory(inventory)
        cond_exit(curr_room,inventory)
        command=menu(curr_room['exits'],curr_room['items'],inventory)
        comstart(curr_room, inventory)
        execute_command(command)

if __name__ == "__main__":
    main()
