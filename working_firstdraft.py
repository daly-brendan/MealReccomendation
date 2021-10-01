import random
from operator import itemgetter

meals = ['Aglio e Olio', 'Cacio e Pepe', 'Bouef Bourginon', 'Chicken Cordon Bleu', 'General Tsos Chicken', 'Carne Asada','Raviolo al Ouvo', 'Chicken Parmigana', 'Pork Katsu', 'Pho', 'Salmon Picata', 'Vitello Barese', 'NY Strip w Garlic Butter']
hearty_meals = itemgetter(2, 7, 8, 12)(meals)
light_meals = itemgetter(0, 9, 10)(meals)
classic_meals = itemgetter(1, 3, 7, 11, 12)(meals)
fun_meals = itemgetter(4, 5, 6, 8, 9)(meals)
#update the food lists to use item getter, easier and cleaner for larger lists


wines = ['Washington Pinot Noir', 'Gamay', 'Napa Cabernet Sauv', 'Alexander Valley Cabernet Sauv', 'Malbec', 'Cabernet Franc', 'Valpolicella', 'Sancerre', 'Sauvignon Blanc', 'Chablis', 'Chardonnay', 'Bourginon Blanc', 'Albarino', 'Champagne', 'Vermentina', 'Gavi', 'Riesling']
acidic_white_wines = itemgetter(7, 8, 9, 12, 13, 15)(wines)
fruity_white_wines = itemgetter(8, 10, 11, 13, 16)(wines)
oaky_white_wines = itemgetter(7, 10, 14)(wines)
light_red_wines = itemgetter(0,1,5)(wines)
bold_red_wines = itemgetter(1, 2, 3,4, 6)(wines)
#itemgetter grabs specific items from a list to create a new string type var, that acts as list?


user_input = input("What are you feeling tonight?(Something hearty, light, fun & new, or a classic) ")

# options for input are: hearty, light, fun & new, or classic
# build loops that choose the food based off of input

if user_input == "hearty":
    print("The program chose this as your meal:", (random.choice(hearty_meals)))
    
if user_input == "light":
    print("The program chose this as your meal:", (random.choice(light_meals)))

if user_input == "classic":
    print("The program chose this as your meal: ", (random.choice(classic_meals)))

if user_input == "fun":
    print("The program chose this as your meal: ", random.choice(fun_meals))

#do the same thing above for the wines, how to make a list from existing lists
#