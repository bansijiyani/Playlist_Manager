import json

# file = 'yt_data.txt'

def load_data():
    try:
        with open('yt_data.txt','r') as file:
            data = json.load(file)
            # print(data)
            # print(type(data))
            return data
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('yt_data.txt','w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("=" * 50)
    print("---------------- LIST OF ALL VIDEOS -----------------")
    print("=" * 50)
    for i, video in enumerate(videos,1):
        name = video.get('name')
        time = video.get('time')
        # print(f"{i}. Name : {video['name']} , Time : {video['time']}")
        print(f"{i} . Name : {name} , Time : {time}")
    print("=" * 50)


def add_videos(videos):
    nm = input("enter video name : ")
    time = input("enter time for video : ")
    videos.append({'name' : nm , 'time' : time})
    save_data_helper(videos)
    print("------- video added succesfully.....")


def update_videos(videos):
    print("*" * 50)
    print("choose any one option from beow and press number")
    print("1 . Update Video name and time")
    print("2 . Update only name")
    print("3 . Update Time")
    print("*" * 50)

    index = int(input("Enter the number of video for update the list : "))
    if index >= 1 and index <= len(videos) :
        ch = int(input("enter choice : "))
        print("-" * 50)
        if ch == 1:
            name = input("Enter name of video :")
            time = input("Enter new time of video :")
            videos[index - 1] = {'name' : name , 'time' : time}
        elif ch == 2:
            name = input("Enter name of video :")
            videos[index - 1]['name'] = name
        elif ch == 3:
            time = input("Enter new time of video :")
            videos[index - 1]['time'] = time
        else:
            print("invalid choice")
            ##
        ##
        save_data_helper(videos)
        print("------- video updated succesfully.....")
        ##
    else :
        print("Invalid index number")
    

def delete_videos(videos):
    list_all_videos(videos)
    print("Enter number of video which you want to delete ")
    print("-" * 50)
    index = int(input("Enter number for delete video :"))
    
    if index >=1 and index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("------- video deleted succesfully.....")
    else :
        print("Invalid number for deleting data")



def main():
    videos = load_data()
    while True:
        print("-----------------------------------------------------")
        print("You tube manager List (Choose any 1 option from below)")
        print("-----------------------------------------------------")
        print("1. list all videos")
        print("2. add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit the app")
        print("-----------------------------------------------------")
        # print(videos)
        ch = input("enter choice : ")
        match ch:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:  #also use default
                print("invalid choice...")

if __name__ == "__main__":
    main()
