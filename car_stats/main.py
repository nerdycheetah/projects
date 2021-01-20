import requests
from bs4 import BeautifulSoup

# Get the webpage
request = requests.get("https://www.roadandtrack.com/car-culture/entertainment/a23062590/these-are-all-the-vehicles-in-forza-horizon-4/")

# Convert to soup where we can find things
soup = BeautifulSoup(request.text, 'html.parser')

data_list = soup.findAll('td')
data_row = soup.findAll('tr')
car_list = []

# Parse the list and separate the information for each car respectively, for this first example, we know that every 3 items in the list contains information of ONE car.
# for i in data_list[:3]:
#     print(i.text)
for i in data_row:
    columns = i.findAll('td')
    if (len(columns) == 3):
        year = columns[0].text
        make = columns[1].text
        model = columns[2].text
        individual_car = {}
        individual_car['year'] = year
        individual_car['make'] = make
        individual_car['model'] = model
        car_list.append(individual_car)
    #print('--------------')
#print(car_list)
#print(len(car_list))
sorted_year_desc = sorted(car_list, key = lambda i: i['year'],reverse=True)
newest_car = sorted_year_desc[1]
oldest_car = sorted_year_desc[-1]
# print('Total number of cars -->', len(car_list))
# print('Newest_car -->', newest_car)
# print('Oldest_car -->', oldest_car)

'''
There are a couple questions you must answer AFTER you parse and store your data.

1: How many cars are in your dataset?

There are 459 cars in the dataset.

2: What is the oldest car?

The oldest car (in this list at least) is the Bugatti Type 35 C (the actual oldest car is the Quartz Regalia / Quartz Regalia Type D

3: What is the newest car?

Hyundai Veloster N (this list was the original car list, so it didn't include newer cars from newer updates, like the Rimac C_2 or the Volkswagen IDR Pikes Peak.)

You must do these programatically and not just by looking at the information

9/19/20

1: Create a function that uses your current dataset/datastructure to query cars by their year. 
    For example, if I put in the year 1970 into the function, it should return all cars that were made that year, return the same datastructure as the original dataset
2: Do the same for make and model
'''

def search_by_year(year_input:int, car_list:list=car_list) -> list:
    """Searches the list of cars by year"""
    res = []
    list_of_years = [] 
    pretty_car = []
    for i in car_list:
        list_of_years.append(i['year'])
        if i['year'] == str(year_input):
            res.append(i)
    if len(res):
        # print(res)
        for i in res:
           print(f"{i['year']} {i['make']} {i['model']}")
    else:
        print('**Car not found**')
        print('Here are some of the years of all the cars you can choose from: ')
        print(list_of_years[:10])
# print(sort_by_year(2015))

def search_by_make(make_input:str, car_list:list=car_list) -> list:
    """Searches the list of cars alphabetically"""
    res = []
    list_of_makes = []
    for i in car_list:
        list_of_makes.append(i['make'])
        if i['make'].lower() == make_input.lower():
            res.append(i)
    if len(res):
        for i in res:
            print(f"{i['year']} {i['make']} {i['model']}")
            # theres a new formula drift car in forza this week :P 
    else: 
        print('**Car not found**')
        print('Here are some of the makes you can choose from: ')
        print(list_of_makes[:10])
# print(sort_by_make('Porsche'))

def search_by_model(model_input:str, car_list:list=car_list) -> list:
    """Searches the list of cars by model"""
    # print(car_list)
    res = []
    list_of_models = []
    for i in car_list:
        list_of_models.append(i['model'])
        if i['model'].lower() == model_input.lower():
            res.append(i)
    if len(res):
        for i in res:
            print(f"{i['year']} {i['make']} {i['model']}")
    else:
        print('**Car not found**')
        print('Here are some of the models of the cars you can choose from: ')
        print(list_of_models[:10])
# print(sort_by_model('FF'))

'''
Now we finished the main search functions for our dataset! Yay! Now the next goal is to turn this into a prettyier application that users can use to query Forza Horizon 4 cars!

Think about the flow of your application, we want users to choose their lookup method, and then query for that. 

Example
Welcome to the Forza car lookup! You can search by:

1: YEAR
2: MAKE
3: MODEL

Enter a number.... :

'''
def get_user_input_year():
    year = input('Enter the year --> ')
    search_by_year(year)

def get_user_input_make():
    make = input('Enter the make --> ')
    search_by_make(make)

def get_user_input_model():
    model = input('Enter the model --> ')
    search_by_model(model)

def greeter_func():
    print('''Hello user! Welcome to the Forza Horizon 4 car lookup database! You can search for any car in the base game, either by year, make, or model.
    To search a car(s) by year, type in 1.
    To search a car(s) by make, type in 2.
    To search a car(s) by model, type in 3. 
    ''')
    choice_input = input('Type in your input. --> ')
    
    if choice_input == '1':
        get_user_input_year()
    elif choice_input == '2':
        get_user_input_make()
    elif choice_input == '3':
        get_user_input_model()
    else:
        print('Please type in a number from 1 to 3. ')


greeter_func()






