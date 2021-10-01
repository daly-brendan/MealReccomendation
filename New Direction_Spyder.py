import random

meals = ["Aglio e Olio", "Cacio e Pepe", "Bouef Bourginon"]
hearty_meals = [meals[2]]
light_meals = [meals[0]]
classic_meals = [meals[1]]

wines = ['Washington Pinot Noir', 'Gamay', 'Napa Cabernet Sauv', 'Alexander Valley Cabernet Sauv', 'Malbec', 'Cabernet Franc', 'Valpolicella', 'Sancerre', 'Sauvignon Blanc', 'Chablis', 'Chardonnay', 'Bourginon Blanc' 'Albarino', 'Champagne', 'Vermentina', 'Gavi', 'Super Tuscan', 'Riesling']

user_input = input("What are you feeling tonight?(Something hearty, light, fun & new, or a classic) ")

#options for input are: hearty, light, fun & new, or classic
# build loops that choose the food based off of input

if user_input == "hearty":
    print("The program chose this as your meal:", (random.choice(hearty_meals)))
    
if user_input == "light":
    print("The program chose this as your meal:", (random.choice(light_meals)))

if user_input == "classic":
    print("The program chose this as your meal: ", (random.choice(classic_meals)))