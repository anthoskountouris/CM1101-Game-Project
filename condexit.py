from map import *
from game import *
from player import *
import time
def item_check(itemid, inventory):
    a=0
    for item in inventory:
        if itemid in item['id']:
            a+=1
    return a

def item_remove(itemid, inventory):
    for x in inventory:
        if itemid == x["id"]:
            inventory.remove(x)

def cond_exit(room, inventory):
    roomlist=[room_bathroom,room_roof,room_trappedRoom,room_vault_locked,room_research,room_security,room_vault_unlocked]
    if room in roomlist:
        if room==room_security and room_security["check"]>0:
            if item_check("device", inventory) == 1:
                print("""\n\n\nYou use the hacking device on the security cameras to turn
                         all footage into loops. Nobody will catch you now.\n\n\n""")
                time.sleep(2)
                item_remove("device",inventory)
        if room==room_bathroom:
            if item_check("wrench", inventory) == 1:
                print("""\n\n\nYou notice the vent and use your wrench to open it.
                         Your wrench breaks in the process.\n\n\n""")
                time.sleep(2)
                room_bathroom["exits"]["up"] = "Vents"
                item_remove("wrench", inventory)
                return 
            else:
                return
        elif room==room_roof: 
                if item_check("rope",inventory) == 1:
                    global exit_open
                    print("\n\n\nYou use your rope to prepare your escape.\n\n\n")
                    time.sleep(2)
                else:
                    print("\n\n\nYou enjoy the breeze on the roof.\n\n\n")
                    time.sleep(2)
        elif room==room_trappedRoom:
                if item_check("smoke", inventory) == 1:
                    print("""\n\n\nYou use the can of smoke in your inventory.
                                 The lasers suddenly are visible.\n\n\n""")
                    time.sleep(2)
                    item_remove("smoke", inventory)
                    room_trappedRoom["exits"]["forward"] = "Vault locked"
                else:
                    return
        elif room==room_vault_locked:
                if item_check("acid", inventory) == 1:
                    print("""\n\n\nYou set the acid to bore through the doors.
                          The fumes are getting thick. You should GO BACK for a moment.\n\n\n""")
                    time.sleep(2)
                    curr_room = rooms["Vault unlocked"]
                    room_trappedRoom["exits"]["forward"]="Vault unlocked"
                    item_remove("acid", inventory)
                else:
                    print("The vault is locked.")
                    return
        elif room==room_research:
            if item_check("key", inventory) == 1:
                print("\n\n\nYou try the key in the lock. It creaks open - you're in.\n\n\n")
                time.sleep(2)
                room_research["exits"]["forward"] = "Main Corridor"
                room_maincorridor["exits"]["back"] = "Main Entrance to the Research Facility"
                item_remove("key", inventory)
                
        elif room==room_vault_unlocked:
            if item_check("hostages",inventory)==1:
                print("\n\n\nYou also pick up the rope for your escape.\n\n\n")
                inventory.append(item_rope)
                time.sleep(2)
    else:
        return
