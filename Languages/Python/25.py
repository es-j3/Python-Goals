capitals = {"USA": "Washington D.C.",
            "China": "Beijing",
            "Kazakhstan": "Almaty",
            "Poland": "Warsaw"}

# print(dir(capitals))
# print(help(capitals))

#print(capitals.get(Kyrgystan))

# if capitals.get("Poland"):
#    print("Capital Exists")
# else:
#    print("Capital doesn't compute!")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Roanoke"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

#keys = capitals.keys()

#for key in capitals.keys():
#    print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value, in capitals.items():
    print(f"{key}: {value}")