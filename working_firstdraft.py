import random
from operator import itemgetter
from googlesearch import search

meals = ['Aglio e Olio', 'Cacio e Pepe', 'Bouef Bourginon', 'Chicken Cordon Bleu', 'General Tsos Chicken', 'Carne Asada','Raviolo al Ouvo', 'Chicken Parmigana', 'Pork Katsu', 'Pho', 'Salmon Picata', 'Vitello Barese', 'NY Strip w Garlic Butter']
hearty_meals = itemgetter(2, 7, 8, 12)(meals)
light_meals = itemgetter(0, 9, 10)(meals)
classic_meals = itemgetter(1, 3, 7, 11, 12)(meals)
fun_meals = itemgetter(4, 5, 6, 8, 9)(meals)
#update the food lists to use item getter, easier and cleaner for larger lists


wines = ['Washington Pinot Noir', 'Gamay', 'Napa Cabernet Sauv', 'Alexander Valley Cabernet Sauv', 'Malbec', 'Cabernet Franc', 'Valpolicella', 'Sancerre', 'Sauvignon Blanc', 'Chablis', 'Chardonnay', 'Bourginon Blanc', 'Albarino', 'Champagne', 'Vermentina', 'Gavi', 'Riesling']
acidic_white_wines = itemgetter(7, 8, 9, 12, 13, 15)(wines)
light_red_wines = itemgetter(0,1,5)(wines)
bold_red_wines = itemgetter(1, 2, 3,4, 6)(wines)
fruity_oaky_white_wines = itemgetter(16, 13, 11, 10, 8, 14, 7)(wines)
#itemgetter grabs specific items from a list to create a new string type var, that acts as list?


user_input = input("What are you feeling tonight?(Something hearty, light, fun & new, or a classic) ")

# options for input are: hearty, light, fun & new, or classic
# build loops that choose the food based off of input

if user_input == "hearty":
    #food
    print("The program chose this as your meal:", )
    hearty_random = random.choice(hearty_meals)
    print(hearty_random)
    print("Google searches for your meal below: ")
    query = hearty_random
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print(i)
    print(" ") #breathing room
    #wine
    print("The program chose this as your wine pairing: ",)
    hearty_wine = random.choice(acidic_white_wines)
    print(hearty_wine)
    print("Google searches for your wine pairing below: ")
    query = hearty_wine
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print(i)
    
if user_input == "light":
    #food
    print("The program chose this as your meal:", )
    light_random = random.choice(light_meals)
    print (light_random)
    print ("Google searches for your meal below: ")
    query = light_random
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print (i)
    print(" ") #breathing room
    #wine
    print("The program chose this as your wine pairing: ",)
    light_wine = random.choice(fruity_oaky_white_wines)
    print(light_wine)
    print("Google searches for your wine pairing below: ")
    query = light_wine
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print(i)

if user_input == "classic":
    #food
    print("The program chose this as your meal: ", )
    classic_random = random.choice(classic_meals)
    print (classic_random)
    print("Google searches for your meal below:")
    query = classic_random
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print (i)
    print(" ") #breathing room
    #wine
    print("The program chose this as your wine pairing: ", )
    classic_wine = random.choice(bold_red_wines)
    print(classic_wine)
    print("Google searches for your wine pairing below: ")
    query = classic_wine
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print(i)

if user_input == "fun":
    #food
    print("The program chose this as your meal: ")
    fun_food = random.choice(fun_meals)
    print(fun_food)
    print("Google searches for your meal below:")
    query = fun_food
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print(i)
    print(" ") #breathing room
    #wine
    print("The program chose this as your wine pairing: ") 
    fun_wine = random.choice(light_red_wines)
    print(fun_wine)
    print("Google searches for your wine pairing below: ")
    query = fun_wine
    for i in search(query, tld = "co.in", num = 10, stop = 2, pause = 2):
        print(i)
#this google searches the variable i created for the random.choice, and returns the searches in the
#terminal


