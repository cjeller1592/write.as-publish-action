import writeas
import os

# Grab variables
blog = os.env.get('INPUT_BLOG')
token = os.env.get('INPUT_TOKEN')
draft = os.env.get('INPUT_DRAFT')

# Instanciate Write.as client with auth token
c = writeas.client()
c.setToken(token)

# Pull title & body from draft post
draft = c.retrievePost(draft)
title = draft['title']
body = draft['body']

# Create post on my blog
p = c.createCPost(blog, body, title)
slug = p['slug']
url = f'https://blog.cjeller.site/{slug}'

# Show published url
print(f'Post published! Here is the url: {url}')


