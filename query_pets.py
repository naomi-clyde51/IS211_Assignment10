import sqlite3

def query_person_and_pets(person_id):
# Connect to the database in pets.db
    con = sqlite3.connect("pets.db")
    cur = con.cursor()

cur.execute()

    

if __name__ == "__main__":
    print("Running query_pets.py")

    while True:
    #Prompt: Ask the user for a person’s ID number
        person_id = input("Enter person's ID number or enter '1' to cancel: ")
    
    #User input to exit the program
        if person_id == "1":
            break
    '''
    Attempt to read if user input a whole number. If it's a whole number,
    then search and fetch the user's data in joined table
    '''
        try:
            person_id=int(person_id)
            person_data, pets_data = query_person_and_pets(person_id)
            
    # If that user exists...
        if person_data:
            # First name, last name, age years old
            print(f"{person_data[0]}, {person_data[1]}, {person_data[2]} years old")
            for pet in pets_data:
            # Owned Pet name, a pet breed, that is age years old
                print(f"Owned {pet[0]}, a {pet[1]}, that is {pet[2]} years old")
    # If that user does not exist...
        else:
            print("Error: User doesn't exist in system.")
        
    
