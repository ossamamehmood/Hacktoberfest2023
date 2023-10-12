"""
Question : 
The aim is to make a diet planner, which tells what foods can you eat in a day, taking into consideration some
constraints on the amount of intake of different nutrients.
Carbohydrates: Lesser than 300
Fats:          Lesser than 150
Proteins:      Greater than 80 and lesser than 500
Vitamins:      Greater than 10 and lesser than 100
Minerals:      Greater than 10 and lesser than 50

The foods list is also given:
Food                Carbohydrates   Fats    Proteins    Vitamins    Minerals
Rice                195             12      12          5           7
Veg Curry           50              36      42          23          3
Cheeseburger        203             95      150         63          27
Potato Chips        78              78      25          14          12
Roti                76              20      34          14          6
Soft Drink          98              7       8           9           21
"""

# Firstly, I am assuming the fact that the repetition of food items is not allowed.
# I am defining a class Food, which is used to represent each meal and also the nutritional value of each meal.
class Food:
    # Any object of the Food class is to be initialized with its item name and nutritional value.
    def __init__(self, item, carbs, fats, proteins, vitamins, minerals):
        self.item = item
        self.carbs = carbs
        self.fats = fats
        self.proteins = proteins
        self.vitamins = vitamins
        self.minerals = minerals
    
    # This method is to add the nutritional value of another Food object to the current Food object.
    def add(self, other):
        self.item = self.item + "," + other.item if self.item != '' else other.item
        self.carbs = self.carbs + other.carbs
        self.fats = self.fats + other.fats
        self.proteins = self.proteins + other.proteins
        self.vitamins = self.vitamins + other.vitamins
        self.minerals = self.minerals + other.minerals
    
    # This method is to check if the current Food object's nutrition values satisfy the nutritional requirements of dietician.
    def valid(self):
        if(self.carbs>300):
            return False
        if(self.fats>150):
            return False
        if(self.proteins<=80 or self.proteins>500):
            return False
        if(self.vitamins<=10 or self.vitamins>100):
            return False
        if(self.minerals<=10 or self.minerals>50):
            return False
        return True
    
# diet_planner is the function that is finding all the possible combinations of meals that satisfy
# the nutrient requirements.
def diet_planner():
    possible_combinations = []
    checker = Food('', 0, 0, 0, 0, 0)
    diet_finder(all_food, n, 0, checker, possible_combinations)

    # Hereby, we have the possible_combinations as a list of lists containing the various
    # combinations of meals. We need to convert it into the desired format of output, i.e.,
    # tuple of tuples.
    for i in range(len(possible_combinations)):
        possible_combinations[i] = tuple(possible_combinations[i])

    possible_combinations = tuple(possible_combinations)
    print(possible_combinations)

# Sorting the strings array using Selection Sort algorithm
def selection_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if(arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# A recursive function, which evaluates the different combinations of meals against the valid conditions.
# Also, we are looking for combinations of meals and not permutations, i.e.,
# (("Rice"), ("Roti"), ("Soft Drink")) is equal to (("Roti"), ("Rice"), ("Soft Drink"))
def diet_finder(all_food, n, i, checker, possible_combinations):
    
    # If a certain combinations yields valid=True, we check if already the set of meals exists
    # in the possible_combinations list or not. If not, we add it to the list.
    if(checker.valid()):
        item_array = checker.item.split(',')
        item_array = selection_sort(item_array)
        
        if item_array not in possible_combinations:
            possible_combinations.append(item_array)
    
    # If i reaches n, terminate the particular instance of recursion.
    if(i==n):
        return
    
    # Iterating over all the meals to taking into account the repetition as well as non-repetition cases.
    for k in range(n):
        new_checker = Food(checker.item, checker.carbs, checker.fats, checker.proteins, checker.vitamins, checker.minerals)
        new_checker.add(all_food[k])
        diet_finder(all_food, n, i+1, new_checker, possible_combinations)
    
# Create objects of Food class for every meal described in the menu.
rice = Food("Rice", 195, 12, 12, 5, 7)
veg_curry = Food("Veg Curry", 50, 36, 42, 23, 3)
cheeseburger = Food("Cheeseburger", 203, 95, 150, 63, 27)
potato_chips = Food("Potato Chips", 78, 78, 25, 14, 12)
roti = Food("Roti", 76, 20, 34, 14, 6)
soft_drink = Food("Soft Drink", 98, 7, 8, 9, 21)

# all_food is a list of all meals, each of which is an object.
all_food = [rice, veg_curry, cheeseburger, potato_chips, roti, soft_drink]
n = len(all_food)

# Call the diet_planner function.
diet_planner()