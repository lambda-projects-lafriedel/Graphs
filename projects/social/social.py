import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        # self.users is a dict where keys are the userIDs and value is a User class instance that is fed the user's name
        self.users = {}
        # self.friendships is a dict where keys are the userIDs and the value is a set of IDs that user is friends with
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)
            return True

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        hint: average_friendships_per_user = total_friendships / total_users
        so
        total_friendships = average_friendships_per_user * total_users
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        #for i in range numUsers, call addUser and implement a random name
        # add their ID to a list, for building friendhips
        for i in range(1, numUsers + 1):
            self.addUser("Bob")        
        # Create friendships
        possible_friends = []

        total_friendships = numUsers * avgFriendships
        num_friendships = 0
        while num_friendships < total_friendships:
            userID = random.randint(1, self.lastID)
            friendID = random.randint(1, self.lastID)
            if self.addFriendship(userID, friendID):
                num_friendships += 2
        '''  
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possible_friends.append((userID, friendID))

        print(possible_friends)
        num_friendships = (numUsers * avgFriendships) // 2
        random.shuffle(possible_friends)
        friendships_to_create = possible_friends[:num_friendships]
        # or could use   friendships_to_create = random.sample(possibleFriendships, (numUsers * avgFriendships) // 2)

        for friendship in friendships_to_create:
            self.addFriendship(friendship[0], friendship[1])

            '''

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        # use a queue
        q = []
        q.append([userID])
        # add userID as its own key and value to visited
        visited[userID] = [userID]

        while len(q) > 0:
            path = q.pop(0)
            curr_friend = path[-1]

            # for all the userID keys inside self.friendships
            for friend in self.friendships[curr_friend]:
                # add neighbor as a key, if not visited, in visited with an empty list as value
                if friend not in visited:
                    visited[friend] = list()
                # break out of loop if already in visited
                else: 
                    continue
                
                # create a new list that holds the path from userID to friend
                friend_path = list(path)
                # add the friend onto the end of the list
                friend_path.append(friend)
                # also add path to the queue
                q.append(friend_path) 
                # add path as the value to the friend
                visited[friend].extend(friend_path)
                
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
