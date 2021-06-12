import instaloader
import numpy as np

class InstagramScrapper:

    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.profile = None
        self.followers_list = []
        self.following_list = []

    def create_session(self):

        L = instaloader.Instaloader()
        L.login(self.username, self.password) # Login or load session
        self.profile = instaloader.Profile.from_username(L.context, self.username) # Obtain profile metadata

    def scrape_followers(self):
       
        for follower in self.profile.get_followers():
            self.followers_list.append(follower.username)

    def scrape_following(self):

        for followee in self.profile.get_followees():
            self.following_list.append(followee.username)

    def generate_unfollowers_list(self):

        unfollow_list = np.setdiff1d(self.following_list, self.followers_list) # unfollow people who are only in following list and not in followers list
        print("People to unfollow: ", unfollow_list)
        filename = "unfollowers_" + self.username + ".txt"
        file = open(filename, "w")
        for person in unfollow_list:
            file.write(person + "\n")
        file.close()


