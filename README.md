# SketchubScraper

Sketchubscraper is a Python script for scraping data from the Sketchub website (https://web.sketchub.in). It provides functions to retrieve information about apps and users.

## Example Usage

```python
from sketchubscraper import recent, editor_choice, trending, most_liked, user_info

# Get recent apps
recent_apps = recent()
print(recent_apps)

# returns : {"status": True, "link": "", "app_icon": "", "app_name": "", "likes": "", "comments": ""}

# Get editor's choice apps
editor_apps = editor_choice()
print(editor_apps)

# returns : {"status": True, "link": "", "app_icon": "", "app_name": "", "likes": "", "comments": ""}

# Get trending apps
trending_apps = trending()
print(trending_apps)

# returns : {"status": True, "link": "", "app_icon": "", "app_name": "", "likes": "", "comments": ""}

# Get most liked apps
liked_apps = most_liked()
print(liked_apps)

# returns : {"status": True, "link": "", "app_icon": "", "app_name": "", "likes": "", "comments": ""}

# Get user information
user_information = user_info('username')
print(user_information)

# returns : {"status": True, "username": "", "profile_pic": "", "role": "", "projects": "0", "likes": "0", "downloads": "0", "about": ""}

# Get app information 
app_information = app_info('app_id')
print(app_information)

# returns : {"status": True, "app_name": '', "author": '', "app_icon": '', "categories": [], "about": '', "whatsnew": ''}
```

## Functions

- `recent()`: Get recent apps.
- `editor_choice()`: Get editor's choice apps.
- `trending()`: Get trending apps.
- `most_liked()`: Get most liked apps.
- `user_info(username)`: Get information about a specific user.
- `app_info(app_id)`: Get information about the app.
## Dependencies

- BeautifulSoup (`bs4`)
- Requests (`requests`)
- JSON (`json`)
