# File: main.py
from user import User
from post import Post
from comment import Comment

class InstaMimicApp:

    def __init__(self):
        self.users = []
        self.posts = []
    
    def reset(self):
        self.users = []
        self.posts = []

    def create_user(self, username, email):
        # Check if a user with the given username already exists
        if any(user._username == username for user in self.users):
            raise ValueError(f"Username '{username}' is already taken.")
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, user, content, tags=None):
        if not Post.is_valid_content(content):  # 确保调用的是正确的方法
            raise ValueError("Invalid post content.")
        if len(content) > 2200:
            raise ValueError("Content exceeds the maximum length of 2200 characters.")
        post = Post(user, content, tags)
        self.posts.append(post)
        user._posts.append(post)
        return post

    def delete_post(self, user, post):
        if post in user._posts:
            # Remove the post from the user's posts
            user._posts.remove(post)
            
            # Remove the post from the global posts list
            self.posts.remove(post)
            
            # Remove likes on this post
            for liker in post._liked_by:
                liker._liked_posts.remove(post)
            
            # Remove comments on this post
            for comment in post._comments:
                # Remove the comment from the author's comments
                comment._author._comments.remove(comment)
                
                # Remove likes on this comment
                for comment_liker in comment._liked_by:
                    comment_liker._liked_comments.remove(comment)
                
                # Decrease the comment count
                Comment.comment_count -= 1
            
            # Decrease the post count
            Post.post_count -= 1

    def like_post(self, user, post):
        if post not in user._posts and post not in user._liked_posts:
            user._liked_posts.append(post)
            post._liked_by.append(user)

    def unlike_post(self, user, post):
        if post in user._liked_posts:
            user._liked_posts.remove(post)
            post._liked_by.remove(user)

    def comment_on_post(self, user, post, content, tags=None):
        comment = Comment(user, content, tags)
        post._comments.append(comment)
        user._comments.append(comment)
        return comment

    def delete_comment(self, user, post, comment):
        if comment in user._comments and comment in post._comments:
            # Remove the comment from the user's comments
            user._comments.remove(comment)
            
            # Remove the comment from the post's comments
            post._comments.remove(comment)
            
            # Remove likes on this comment
            for liker in comment._liked_by:
                liker._liked_comments.remove(comment)
            
            # Decrease the comment count
            Comment.comment_count -= 1

    def like_comment(self, user, comment):
        if comment not in user._comments and comment not in user._liked_comments:
            user._liked_comments.append(comment)
            comment._liked_by.append(user)

    def unlike_comment(self, user, comment):
        if comment in user._liked_comments:
            user._liked_comments.remove(comment)
            comment._liked_by.remove(user)

    def follow_user(self, follower, followee):
        if follower != followee and followee not in follower.following:
            follower.following.append(followee)
            followee.followers.append(follower)

    def unfollow_user(self, follower, followee):
        if followee in follower.following:
            follower.following.remove(followee)
            followee.followers.remove(follower)
    
    def test_create_post_invalid_content(self):
        with self.assertRaises(ValueError):
            self.app.create_post(self.user1, "a" * 2201)  # 确保这是超过 2200 的内容
    def test_create_post_invalid_content(self):
        try:
            self.app.create_post(self.user1, "a" * 2201)
        except ValueError as e:
            print(f"Caught ValueError as expected: {e}")
            return
        self.fail("ValueError not raised")


if __name__ == "__main__":
    
    # Testing the app
    app = InstaMimicApp()
    
    # Create a user
    user1 = app.create_user("user1", "user1@example.com")
    
    # Create a post
    post1 = app.create_post(user1, "My first post", tags=["fun", "coding"])
    
    # Add a comment to the post
    comment1 = app.comment_on_post(user1, post1, "Nice post!")
    
    # Like the post
    app.like_post(user1, post1)
    
    # Like the comment
    app.like_comment(user1, comment1)
    # Create users
    alice = app.create_user("alice", "alice@example.com")
    bob = app.create_user("bob", "bob@example.com")

    # Create posts
    alice_post = app.create_post(alice, "Hello, Instagram!", ["firstpost", "excited"])
    bob_post = app.create_post(bob, "Python is awesome!", ["python", "coding"])
    # Print number of posts and post details
    print(f"Number of posts: {Post.get_post_count()}")
    print(f"Alice's post content: {alice_post.content}")
    print(f"Alice's post tags: {alice_post.tags}")
    print("Testing completed.")

