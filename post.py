# post.py
from datetime import datetime

class Post:
    post_count = 0

    def __init__(self, author, content, tags=None):
        if not self.is_valid_content(content):
            raise ValueError("Invalid content.")
        if tags is not None:
            for tag in tags:
                if not self.is_valid_tag(tag):
                    raise ValueError("Invalid tag.")
        self._author = author
        self._content = content
        self._tags = set(tags) if tags else set()
        self._created_on = datetime.now()
        self._liked_by = []
        self._comments = []
        Post.post_count += 1

    @property
    def content(self):
        return self._content

    @property
    def tags(self):
        return self._tags
    
    @property
    def liked_by(self):
        return self._liked_by
    
    @property
    def created_on(self):
        return self._created_on
    
    def add_like(self, user):
        if user not in self._liked_by:
            self._liked_by.append(user)

    def add_comment(self, comment):
        self._comments.append(comment)
    
    @classmethod
    def get_post_count(cls):
        return cls.post_count  
    
    def like_post(self, user):
        if user not in self._liked_by:
            self._liked_by.append(user)
    
    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag.")
        self._tags.add(tag)
        
    def remove_tag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)
        

    @staticmethod
    def is_valid_tag(tag):
        if not isinstance(tag, str):
            return False
        if not (1 <= len(tag) <= 30):
            return False
        if any(c.isspace() for c in tag):  
            return False
        return True
    
    @classmethod
    def is_valid_content(cls, content):
        return isinstance(content, str) and 3 <= len(content) <= 2200  

    def test_invalid_tags(self):
        invalid_tags = ["invalid tag", "tag!" * 16, "", "a" * 31]  
        for invalid_tag in invalid_tags:
            with self.assertRaises(ValueError):
                Post(self.user, self.valid_content, [invalid_tag]) 
