import requests
class JSONPlaceholderClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_posts(self):
        """Fetch all posts from the API."""
        url = f"{self.base_url}/posts"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
            return None

    def create_post(self, title, body, user_id):
        """Create a new post."""
        url = f"{self.base_url}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Failed to create post. Status code: {response.status_code}")
            return None


if __name__ == "__main__":
    client = JSONPlaceholderClient()

    posts = client.get_posts()
    if posts:
        print("Fetching Posts:")
        for post in posts[:5]:  # print first 5 posts
            print(f"Title: {post['title']}")

    new_post = client.create_post("My New Post", "This is the content of my new post", 1)
    if new_post:
        print("\nCreating a New Post:")
        print(f"Title: {new_post['title']}")
        print(f"Body: {new_post['body']}")
