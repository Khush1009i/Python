# dictionaries : a collection of {Key : values} pairs, ordered & changeable.
# No duplicates are allowed


capitals= { "Inida": "NEW DELHI",
            "USA": "WASHINGTON D.C.",
            "China": "Beijing",
            "Russia": "Moscow"       }

if capitals.get("japan"):
    print("That exist")
else:
    print("It doesn't exist")


capitals.update({"Germany" : "Berlin"})
capitals.update({"USA" : "LWDA"})
# x = capitals.get("USA")

capitals.pop("Russia") # pop to delete/ remove the given key wrord
print(capitals)