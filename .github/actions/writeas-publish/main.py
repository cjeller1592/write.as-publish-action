import writeas
import os

# Grab variables
token = os.getenv('INPUT_WRTIEAS_TOKEN')

# Instanciate Write.as client with auth token
c = writeas.client()
c.setToken(token)

# Pull title & body from draft post
draft = c.retrievePost('e30m2wbxgsalir1g')
title = draft['title']
body = draft['body']

# Create post on my blog
p = c.createCPost('the-test-blog', body, title)

# Show published url
print(f'Post published! Here it is:\n\n{p}')


