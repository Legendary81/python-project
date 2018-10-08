# filename     : Marey_e1.py
# author       : Marey Klarize Sevilla
# description  : this is my 1st exercise python program that prints the content of a dictionary in a specific format

message = "I am {}.\n" + \
          "My spirit animal is {}.\n" + \
          "because {}.\n" +\
          "when not in school, I love to {}.\n" + \
          "I dream of a/an {} in the future"

data = {"name"          : "Marey Klarize M. Sevilla",
        "spirit_animal" : "goldfish",
        "reason"        : "I love to eat goldfish",
        "hobby"         : "sleep",
        "profession"    : "Chef" }

print (message.format ( \
    data["name"], \
    data["spirit_animal"], \
    data["reason"], \
    data["hobby"], \
    data["profession"] 
    ))