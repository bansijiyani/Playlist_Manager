import sqlite3 
# import Error

try:
    con = sqlite3.connect("youtube_data_sql.db")
    cursor = con.cursor()
    table_create = 'CREATE TABLE IF NOT EXISTS youtube_data (no  int primary key, name  varchar , time  varchar)'
    cursor.execute(table_create)
    # con.close()
except sqlite3.Error as e:
    print(e)

def Display():
    qry = 'SELECT * FROM youtube_data'
    result = cursor.execute(qry)
    for i in result:
        print(i)

def insert(id_no ,nm , tm):
    try:
        qry = 'INSERT INTO youtube_data (no , name , time ) values (? , ? , ? )'
        cursor.execute(qry,(id_no,nm,tm))
        con.commit()
    except sqlite3.Error as e:
        print(e)


def update(no , name , time):
    try:
        qry = 'UPDATE youtube_data SET name = ? , time = ? WHERE no = ? '
        values = (name , time , no)
        cursor.execute(qry,values)
        con.commit()
    except sqlite3.Error as e:
        print(e)

def delete(no):
    try:
        qry = 'Delete from youtube_data WHERE no = ?'
        cursor.execute(qry , (no,))
        con.commit()
    except sqlite3.Error as e:
        print(e)



def main():
    while True:
        print("*" * 50)
        print("Select any one option from below ")
        print("1. Display all Data ")        
        print("2. Insert Data ")
        print("3. Update Data ")
        print("4. Delete Data ")
        print("5. Exit")
        print("*" * 50)
        ch = int(input("Enter any one choice : "))
        print("=" * 50)

        match ch:
            case 1:
                Display()
        
            case 2:
                no = int(input("enter number :"))
                name = input("Enter name of video : ")
                time = input("Enter time for video : ")
                insert(no , name , time)
            
            case 3:
                no = int(input("enter number :"))
                name = input("Enter name of video : ")
                time = input("Enter time for video : ")
                update(no , name , time)

            case 4:
                no = int(input("Enter no for delete video : "))
                delete(no)
            case 5:
                break

            case _:
                print("Invalid choice")
            
    con.close()

main()

