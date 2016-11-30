pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def pirate_sorter_woodenleg_gold(pirates_input):
    pirates_with_gold = []
    for i in pirates_input:
        # print(i)
        if i['gold'] > 15 and i['has_wooden_leg'] == True:
            print(i['Name'])
            pirates_with_gold.append(i['Name'])
    return pirates_with_gold

piratess = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
  {'Name': 'Rook', 'has_wooden_leg': True, 'gold': 20},
  {'Name': 'Took', 'has_wooden_leg': True, 'gold': 27},
]
print(pirate_sorter_woodenleg_gold(piratess))
