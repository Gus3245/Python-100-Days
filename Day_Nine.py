#The Python Dictionary: Deep Dive
from reprlib import clear

Dic = {
    "Key": "Value to the key",
    "Another key": "Other Value",
    "Another key": "Other Value"
        }

print(Dic["Key"]) #Retrieving items from dictionary

#Adding new items to dictionary
Dic["Loop"] = "This is a Loop"

print(Dic)

#Create an empty dictionary
empyt_Dic = {}

#Loop a Dictionary

for thing in Dic:
    print(thing) #print Keys
    print(Dic[thing]) #print Values

#Nestling List and Dictionary

Nestling_Dic = {"Key": ["Hello", "World", "!"], 
                "total_visits": 12,
                "Another Key": {"Keys": ["Hello", "World", "!"]}
                }

#Nestling Dictionary on List

List = [{"Key": "Value",
         "Key2": "Value2"},
        
        {"Key": "Value",
         "Key2": "Value2"}
        ]

#challenge 0.1 
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
def add_new_country(init_country, init_visits, init_list):
  new_country = {}
  new_country["country"] = init_country
  new_country["visits"] = init_visits
  new_country["cities"] = init_list
  travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")