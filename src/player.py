# Write a class to hold player information, e.g. what room they are in
# currently.

# Class Player Encapsulation
class Player:
    # init function: takes in name and a current_room; current_room
    # will initialize to the "outside" room
    def __init__(self, name, current_room="outside"):
        # Player's name (type: String)
        self.name = name
        # Player's current_room (type: Room Object)
        self.current_room = current_room
        