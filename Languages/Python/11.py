temp = 50
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The party is cancelled :(")
else:
    print("The party is still in schedule!")

temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It's HOT outside!")
    print("It's sunny!")
elif temp <= 0 and is_sunny:
    print("It's CHILLY outside!")
    print("At least it's sunny!")
elif temp < 28 and temp > 0 and is_sunny:
    print("It's WARM outside!")
    print("Perfect weather and it's sunny!")
if temp >= 28 and not is_sunny:
    print("It's HOT outside!")
    print("It's cloudy but at least the temperature's nice!")
elif temp <= 0 and not is_sunny:
    print("It's CHILLY outside!")
    print("...and cloudy :(")
elif temp < 28 and temp > 0 and not is_sunny:
    print("It's WARM outside!")
    print("It's cloudy but the weather is still alright!")
