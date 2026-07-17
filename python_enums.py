from enum import Enum

#class Color(Enum):
    #RED = "R"
    #GREEN = "G"
    #BLUE = "B"

# here in python enums attribute can have various datatype as value unlike in c it can have only integer

Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

print(Color.RED.name)
print(Color.GREEN.value)
