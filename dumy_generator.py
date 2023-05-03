import random

month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

kode_telp = ["+62812", "+62813", "+62822", "+62823", "+62831", "+62857"]

gender_list = ["unknown", "male", "female"]

type_list = ["seller", "buyyer"]

filedata = open("users.sql", "a")

def date():
    year = random.randrange(1970, 2004)
    month = random.randrange(1, 12)
    if month == 2:
        day = random.randrange(1, 29)
    else :
        day = random.randrange(1, 30)
        
    return f'{year}-{month}-{day}'

def noTelp():
    return random.choice(kode_telp)+str(random.randrange(11111111, 99999999))

for i in range(100000):
    username = "user"+str(i + 8000000)
    email = username+"@mail.com"
    gender = random.choice(gender_list)
    city_id = random.randrange(1, 475)
    user_type = random.choice(type_list)
    filedata.write(f"INSERT INTO users (user_id, user_name, gender, birth, phone, email, city_id, user_type) VALUES({i+1}, '{username}', '{gender}', '{date()}', '{noTelp()}', '{email}', {city_id}, '{user_type}');\n")

filedata.close()

"""
user tables

user_id, user_name, user_gender, birth, phone, email, city_id, type
"""