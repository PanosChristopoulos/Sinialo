import mysql.connector
from getpass import getpass

database = mysql.connector.connect(
user='root',
password='Aekjim1998@',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = database.cursor()


def addFriend(username,friend):
    if checkFriendship(username,friend) == True:
        print("Friendship already Exists")
    elif checkFriendRequest(username,friend) == True:
        print("Request has already been made")
    elif checkUsers(username,friend) == False:
        print("User",friend,"does not exist in database")
    else:
        sql = "INSERT INTO requests (requestfrom, requestto) VALUES (%s, %s)"
        val = (username,friend)
        mycursor.execute(sql, val)
        database.commit()
        print("You have made a friend request to user",friend)
    makeFriendship()


def checkFriendship(user1,user2):
    mycursor.execute("SELECT friend1,friend2 FROM friends")
    friendships = mycursor.fetchall()
    #print(friendships)
    friendshipExists = False
    for x in range(len(friendships)):
        if friendships[x][0] == user1 and friendships[x][1] == user2:
            friendshipExists=True
        elif friendships[x][1] == user1 and friendships[x][0] == user2:
            friendshipExists=True
        else:
             friendshipExists=False
    return friendshipExists

def checkFriendRequest(user1,user2):
    mycursor.execute("SELECT requestfrom,requestto FROM requests")
    requests = mycursor.fetchall()
    #print(friendships)
    requestExists = False
    for x in range(len(requests)):
        if requests[x][0] == user1 and requests[x][1] == user2:
            requestExists=True
        #elif requests[x][1] == user1 and requests[x][0] == user2:
         #   requestExists=True
        else:
             requestExists=False
    return requestExists

def checkUsers(user1,user2):
    mycursor.execute("SELECT username FROM users")
    usernameResults = mycursor.fetchall()
    exists1 = False
    exists2 = False
    usersExist = False
    for x in usernameResults:
        if user1 == x[0]:
            exists1 = True
    for x in usernameResults:
        if user2 == x[0]:
            exists2 = True
    if exists1 == True and exists2 == True:
        usersExist = True
    return usersExist

def Reverse(tuples): 
    new_tup = tuples[::-1] 
    return new_tup 

def makeFriendship():
    mycursor.execute("SELECT requestfrom,requestto FROM requests")
    requests = mycursor.fetchall()
    requests1 = [t[::-1] for t in requests]
    #print(requests)
    for x in requests:
        item = x
        if item in requests1:
            print(item)
            sql = "DELETE FROM requests WHERE requestfrom = %s and requestto = %s"
            val = (item[0],item[1])
            mycursor.execute(sql, val)
            database.commit()
            sql = "INSERT INTO friends (friend1,friend2) VALUES (%s, %s)"
            val = (item[0],item[1])
            mycursor.execute(sql, val)
            database.commit()
            requests.remove(item)
            requests.remove(Reverse(item))
            print("Friend Added")
            #print(requests)
            #print("Item",x," removed")

def viewFriends(user):
    mycursor.execute("SELECT friend1,friend2 FROM friends")
    requests = mycursor.fetchall()
    friends = []
    for x in range(len(requests)):
        if requests[x][0] == user:
            friends.append(requests[x][1])
        elif requests[x][1] == user:
            friends.append(requests[x][0])
    return friends
print(viewFriends("fitsoulas"))