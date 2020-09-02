# Implement a class to hold room information. This should have name and
# description attributes.

# Class Room Encapsulation
class Room:
    # init function: takes in name and description
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # cardinal directions: initiated to none,
        # will hold the full Room classes connected to this one
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    # Override __str___ method
    def __str__(self):
        return f"Room Name: {self.name}\n{self.description}"

# Testing functionality of Room class instantiation
r = Room("Name", "Description")

# Further testing with __str__ method
print(r)