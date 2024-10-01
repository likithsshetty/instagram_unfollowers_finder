import json
from time import sleep

with open("followers_1.json") as file:
    followersFile = json.load(file)
    file.close()

with open("following.json") as file:
    followingFile = json.load(file)
    file.close()



totalFollowing = (len(followingFile["relationships_following"]))
totalFollowers = (len(followersFile))
followers = list()
following = list()

for i in range(totalFollowing):
    person = str(followingFile["relationships_following"][i]['string_list_data'][0]['value'])
    # person = person.replace("_","")
    # person = person.replace(".","")
    following.append(person)

for i in range(totalFollowers):
    person = followersFile[i]['string_list_data'][0]['value']
    # person = person.replace("_","")
    # person = person.replace(".","")
    followers.append(person)


followers = sorted(followers)
following = sorted(following)

def showConnections():
    print("\nAll Conections:")
    for person in following:
        if person in followers:
            print("✅  :", person)
        else:
            print("❌  :", person)

def showUnfollowers():
    print("\nPeople not following you: ")
    for person in following:
        if person not in followers:
            print("❌  :", person)

if __name__ == "__main__":
    try:
        choice = int(input("1. Show all connections\n2. Show Non Followers\nEnter Your Choice:"))
    except Exception as e:
        print("invalid Input!!")
    else:
        if choice == 1:
            showConnections()
        elif choice == 2:
            showUnfollowers()
        else:
            print("invalid Choice!!")