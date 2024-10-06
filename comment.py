# comment.py
from datetime import datetime

class Comment:
    comment_count = 0

    def __init__(self, author, content, tags=None):
        if not self.is_valid_content(content):
            raise ValueError("Invalid comment content.")
    
        if tags is not None:
            for tag in tags:
                if not self.is_valid_tag(tag):
                    raise ValueError(f"Invalid tag: {tag}")
    
        self._author = author
        self._content = content
        self._tags = set(tags) if tags is not None else set()
        self._created_on = datetime.now()
        self._liked_by = []
        Comment.comment_count += 1
   
    @property
    def tags(self):
        return frozenset(self._tags)  
   
    @property
    def content(self):
        return self._content  
    
    @staticmethod
    def is_valid_content(content):
        return 3 <= len(content) <= 2200

    def add_like(self, user):
        if user not in self._liked_by:
            self._liked_by.append(user)
    
    @classmethod
    def get_comment_count(cls):
        return cls.comment_count  

    def add_tag(self, tag):
        if not self.is_valid_tag(tag):
            raise ValueError("Invalid tag.")
        self._tags.add(tag)

    def remove_tag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)

    @property
    def created_on(self):
        return self._created_on

    @staticmethod
    def is_valid_tag(tag):
        return isinstance(tag, str) and 1 <= len(tag) <= 30 and ' ' not in tag and all(c.isalnum() for c in tag)
