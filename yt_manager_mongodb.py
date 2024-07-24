from pymongo import MongoClient 
from getpass import getpass 
from bson import ObjectId

try:
    u_name = input("Enter user name : ")
    password = getpass("Enter password : ")
    # u_name = "youtube_python"
    # password = "bansi636363"
    conn_str = f"mongodb+srv://{u_name}:{password}@cluster0.w4hnfhd.mongodb.net/"
    client = MongoClient(conn_str)
    print("Connection established succesfully...")
    print("-" * 50)
except Exception as e:
    print("Connection is not Established....",e)
    print("-" * 50)

try:
    db = client["ytmanager"]
    # print(db)
    # print(type(db))
    collection = db["youtube_videos"]
    # print(collection)
except Exception as e:
    print("Error....",e)


def Display():
    try:
        for i in collection.find():
            print( f"ID :{i['_id']} ,Name : {i['name']} , Time :{i['time']}")
    except Exception as e:
        print("Display error..." , e)

def update(no, new_name, new_time):
    try:
        collection.update_one({'_id' : ObjectId(no)},{"$set" : {'name' : new_name , 'time' : new_time}})
    except Exception as e:
        print("Update error..." , e)


def insert(name , time):
    try:
        collection.insert_one({"name" : name , "time" : time })
    except Exception as e:
        print("Insert error..." , e)

def delete(no):
    try:
        collection.delete_one({'_id' : ObjectId(no)})
    except Exception as e:
        print("Delete error..." , e)



def main():
     while True:
        print("*" * 50)
        print("Select any one option from below ")
        print("1. Display all Data ")        
        print("2. Add video ")
        print("3. Update video ")
        print("4. Delete video ")
        print("5. Exit")
        print("*" * 50)
        ch = int(input("Enter any one choice : "))
        print("=" * 50)

        match ch:
            case 1:
                Display()
        
            case 2:
                name = input("Enter name of video : ")
                time = input("Enter time for video : ")
                insert(name , time)
            
            case 3:
                no = input("enter id number which want to update :")
                name = input("Enter new name for video : ")
                time = input("Enter new time for video : ")
                update(no , name , time)

            case 4:
                no = input("Enter no for delete video : ")
                delete(no)
            case 5:
                print("******* Exiting***********")
                break

            case _:
                print("---------Invalid choice--------")

if __name__ == "__main__":
    main()

