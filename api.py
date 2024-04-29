import requests

def get_posts():
    """
    Fetches posts from the JSONPlaceholder API.

    Returns:
    list: A list of dictionaries, each containing a post.

    200 todo bien
    300 redirección
    400 error de usuario
    500 error del servidor
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Returns the JSON response as a list of posts
    else:
        return {'error': 'Failed to fetch data', 'status_code': response.status_code}

def create_post():
    """Creates a new post."""
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'New Post',
        'body': 'This is the content of the post.',
        'userId': 1
    }
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return {'error': 'Failed to create data', 'status_code': response.status_code}

def update_post(post_id):
    """Updates an existing post."""
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    data = {
        'id': post_id,
        'title': 'Updated Post',
        'body': 'This is the updated content of the post.',
        'userId': 1
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Failed to update data', 'status_code': response.status_code}

def delete_post(post_id):
    """Deletes a post."""
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.delete(url)
    if response.status_code == 200:
        return {'success': f'Post with id {post_id} has been deleted.'}
    else:
        return {'error': 'Failed to delete data', 'status_code': response.status_code}

if __name__ == "__main__":
    # Create a new post
    new_post = create_post()
    print('Created Post:', new_post)

    # Update the newly created post
    if 'id' in new_post:
        updated_post = update_post(new_post['id'])
        print('Updated Post:', updated_post)

    # Delete the updated post
    if 'id' in new_post:
        result = delete_post(new_post['id'])
        print('Delete Result:', result)
    # https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums
    posts = get_posts()
    print(posts)
    for post in posts[:5]:  # Print the first 5 posts
        print(post['title'], post['userId'])
