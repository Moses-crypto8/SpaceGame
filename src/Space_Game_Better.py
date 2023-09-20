#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Room import Room
from Player import Player
from Item import Item
import RoomIds
"""
Created on Tue Sep 12 13:42:11 2023

@author: moseshernandez
"""

# Create the player
player = Player("The Player", RoomIds.CLOSET_ID)

# Start game
print("Welcome to My Space Adventure")
print("\nYou wake up on a space station.")

while True:
    print("")
    print(player.get_current_room())
    print(player.get_current_room().get_name())
    print(player.get_current_room().get_description())
    print("\nHere are the exits: ")

    for exit in player.get_current_room().get_exits().values():
        print(exit.get_name())
    
    print("\nYou see the following: ")
    for item in player.get_current_room().get_items():
        print(item.get_name())
        
  
    command = input("\n> ")
        
    words = command.split()
    if len(words) > 0:
        verb = words[0]
    if len(words) > 1:
        noun = words[1]
    
    # Examine
    if verb == "examine":
        for item in player.location.items:
            if item.name == noun:
                print(item.description)
        for item in player.inventory:
            if item.name == noun:
                print(item.description)

    # Get
    if verb == "get":
        for item in player.location.items:
            if item.name == noun:
                # Check is it movable
                if item.is_movable:
                    print("You take the {}".format(item.name))
                    # Remove from room
                    player.location.items.remove(item)
                    # Add to player's inventory
                    player.inventory.append(item)
                
                else:
                    print("Sorry, you can't move that.")

    # Drop
    if verb == "drop":
       for item in player.inventory:
            print("You drop the {}.".format(item.name))
            player.inventory.remove(item)
            player.location.items.append(item)
        
    # Inventory
    if verb in ["inv", "inventory"]:
        print("You have the following: ")
        for item in player.inventory:
            print(item.name)

    # Movement
    if verb in ["n", "s", "e", "w", "u", "d"]:
        if verb in player.location.exits:
            player.location = player.location.exits[verb]
            print("You go {} and find yourself in a new room.".format(verb))

    # Room specific code
    # Control Room
    if player.location == control_room:
        if uniform not in player.inventory:
            print("The guard sees you. Without saying a word, he pulls his laser gun and kills you. Game over.")
            exit()
        else:
            print("The guard looks up, looks at the uniform, and turns his head back to the display.")

    if player.location == control_room:
        if verb == "open" and noun == "airlock":
            if credentailial in player.inventory:
                print("You swipe the credential and the airlock opens.")
                control_room.exits["e"] = airlock
                
            else:
                print("The airlock won't open. You must need some credential to open it.")

    # Airlock
    if player.location == airlock:
        if "w" in airlock.exits:
            del(airlock.exits["w"])
            print("The airlock door closes! You are trapped.  There is no lock on this scredentailiale.")
            
    if player.location == airlock:
        if verb == "press" and noun == "button":
            if spacesuit in player.inventory:
                print("You put on the spacesuit and push the red button.")
                print("The outer airlock door opens!")
                airlock.exits["n"] = outerspace
            else:
                print("The outer airlock door opens.  You are sucked into the vacuum of space and die.")
                exit()
    #Outerspace
    if player.location == outerspace:
        if verb == "get" and noun == "cord":
            if cord in player.inventory:
                print("You attach cord, and avocredential floating off into space")
            else:
                print("The cord floats out of reach and you die in the emptiness of space")
                exit()
            
            