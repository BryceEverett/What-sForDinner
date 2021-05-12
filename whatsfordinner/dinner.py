import random
def food_selection():
    print('Food Types: Chinese, Japanese, Indian, Pizza, Random')
    food_type = input('What Type: ')
    if food_type == 'Chinese' or food_type == 'chinese':
        noms = ['Panda Express','P.F Changs','Pei Wei Asian Diner','Leean Chin']
        print(random.choice(noms))
    elif food_type =='Japanese' or food_type =='japanese':
        noms =['Ace Sushi','Gyu-Kaku','Hibachi-San','Todai']
        print(random.choice(noms))
    elif food_type =='Indian' or food_type =='indian':
        noms =['Choolaah','Curry Up Indian Grill','Indian Oven','Haveli Bistro']
        print(random.choice(noms))
    elif food_type =='Pizza' or food_type =='pizza':
        noms =['Pizza Hut','Dominos','Gioninos', 'Little Ceasers']
        print(random.choice(noms))
    elif food_type =='Random' or food_type =='random':
        noms =['Ace Sushi','Gyu-Kaku','Hibachi-San','Todai','Panda Express','P.F Changs','Pei Wei Asian Diner','Leean Chin','Choolaah','Curry Up Indian Grill','Indian Oven','Haveli Bistro','Pizza Hut','Dominos','Gioninos','Little Ceasers']
        print(random.choice(noms))
food_selection()