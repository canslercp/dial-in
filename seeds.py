from app.models import User, Coffee, Recipe
from app.config import get_database

# Not sure if this is the correct way to connect to the database
db = get_database()

userSeed = [
    { 'email': 'canslercp@gmail.com', 'username': 'canslercp', 'password': 'imakecoffee123'},
    { 'email': 'nimmynam@gmail.com', 'username': 'nimmyNam', 'password': 'squirrel123' },
    { 'email': 'mrpeanut@gmail.com', 'username': 'mrpeanut', 'password': 'carrots123'}
]

User.insert_many(userSeed)

coffeeSeed = [
    {'roaster': 'Madcap', 'name': 'Vista Hermosa', 'originCountry': 'Colombia', 'regionCountry': 'Tolima', 'processMethod': 'washed', 'roastLevel': 'medium', 'roastDate': '10/31/2022'},
    {'roaster': 'Onyx', 'name': 'Wush Wush', 'originCountry': 'Ethiopia', 'regionCountry': 'Keffa', 'processMethod': 'washed', 'roastLevel': 'light', 'roastDate': '10/29/2022' },
    {'roaster': 'Counter Culture Coffee', 'name': 'Kamavindi', 'originCountry': 'Kenya', 'regionCountry': 'Embu', 'elevation': '1600', 'processMethod': 'washed', 'roastLevel': 'light', 'roastDate': '10/31/2022'}
]

Coffee.insert_many(coffeeSeed)

recipeSeed = [
    {'amountCoffee': '30', 'amountWater': '480', 'grindSize': '28', 'waterTemp': '205', 'brewer': 'kalita'},
    {'amountCoffee': '30', 'amountWater': '480', 'grindSize': '29', 'waterTemp': '207', 'brewer': 'v60'},
    {'amountCoffee': '30', 'amountWater': '480', 'grindSize': '29', 'waterTemp': '207', 'brewer': 'v60'}
]

Recipe.insert_many(recipeSeed)

print('data seeded!!')