# user.py

from post import Post
from comment import Comment
from datetime import datetime
import re
class User:
    user_count = 0  
    
    @property
    def joined_on(self):
        return self._joined_on
    
    def __init__(self, username, email):
        if not self.is_valid_username(username):
            raise ValueError("Invalid username.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email.")
        self._username = username
        self._email = email
        self._joined_on = datetime.now() 
        self.bio = ""  
        User.user_count += 1  
        self._posts = []
        self._comments = []
        self._liked_posts = []
        self._liked_comments = []
        self.followers = []
        self.following = []

    @property
    def username(self):
        return self._username
   
    @property
    def posts(self):
        return self._posts  # Public property to access the user's posts
    
    @property
    def email(self):
        return self._email

    @property
    def bio(self):
        return self._bio
    
    @bio.setter
    def bio(self, value):
        if len(value) > 150:
            raise ValueError("Bio cannot be longer than 150 characters.")
        self._bio = value

    def add_post(self, post):
        self._posts.append(post)

    def add_comment(self, comment):
        self._comments.append(comment)


    @classmethod
    def get_user_count(cls):
        return cls.user_count 
    
    def create_post(self, content, tags=None):
        post = Post(self, content, tags)
        self.posts.append(post) 
        return post

    def delete_post(self, post):
        if post in self.posts:
            self.posts.remove(post) 
            Post.post_count -= 1 

    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag")
        self._tags.add(tag)

    def remove_tag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)

    @classmethod
    def is_valid_content(cls, content):
        return isinstance(content, str) and len(content) > 0
    
    @classmethod
    def is_valid_username(cls, username):
        # Username must be alphanumeric and between 3 and 20 characters
        return isinstance(username, str) and 3 <= len(username) <= 30 and bool(re.match("^[a-zA-Z0-9_.]*$", username))
    @classmethod
    def is_valid_email(cls, email):
        # Simple regex for email validation
        return isinstance(email, str) and re.match(r"[^@]+@[^@]+\.[^@]+", email)