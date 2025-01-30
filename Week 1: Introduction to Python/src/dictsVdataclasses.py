import requests
import json

from dataclasses import dataclass

@dataclass
class Post:
    userId: int
    id: int
    title: str
    body: str
    def __str__(self):
        return f"Post {self.id}:\n    User ID: {self.userId}\n    ID: {self.id}\n    Title: {self.title}\n    Body: {self.body}"


posts = []
# Decode the JSON response into a Post instance
for post_id in range(1, 4):
    # URL: https://jsonplaceholder.typicode.com/posts/{post_id}
    # post_id is a number from 1 to max number of posts
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    post_data = json.loads(response.content)

    post = Post(userId=post_data["userId"], id=post_data["id"], title=post_data["title"], body=post_data["body"])
    posts.append(post)

# NOTE: post.userId to access the userId of the post
print(posts)