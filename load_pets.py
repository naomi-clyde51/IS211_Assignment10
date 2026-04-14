import sqlite3
#connect to the database in pets.db
con = sqlite3.connect("pets.db")
# database cursor to execute SQL statements and fetch results from SQL queries
cur = con.cursor()

'''
execute the CREATE TABLE statement and
insert data/values into table
'''
# insert data/values into person table
cur.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (1, 'James', 'Smith', 41)")
cur.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (2, 'Diana', 'Greene', 23)")
cur.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (3, 'Sara', 'White', 27)")
cur.execute("INSERT INTO person (id, first_name, last_name, age) VALUES (4, 'William', 'Gibson', 23)")

# insert data/values into pet table
cur.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (1, 'Rusty', 'Dalmatian', 4, 1)")
cur.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (2, 'Bella', 'Alaskan Malamute', 3, 0)")
cur.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (3, 'Max', 'Cocker Spaniel', 1, 0)")
cur.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (4, 'Rocky', 'Beagle', 7, 0)")
cur.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (5, 'Rufus', 'Cocker Spaniel', 1, 0)")
cur.execute("INSERT INTO pet (id, name, breed, age, dead) VALUES (6, 'Spot', 'Bloodhound', 2, 1)")

# insert data/values into person_pet table

cur.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (1, 1)")
cur.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (1, 2)")
cur.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (2, 3)")
cur.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (2, 4)")
cur.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (3, 5)")
cur.execute("INSERT INTO person_pet (person_id, pet_id) VALUES (4, 6)")

'''
The purpose of the person_pet table is to conjoin the data of
'person' and 'pet' tables into a single table
'''

#commit changes and close connection
con.commit() 
con.close()

if __name__ == "__main__":
    print("Running load_pets.py")
