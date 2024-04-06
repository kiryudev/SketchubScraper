from bs4 import BeautifulSoup as bs
import requests, json

# github.com/kiryudev

site = 'https://web.sketchub.in'
ses = requests.Session()

def get_data(scope):
    soup = bs(ses.get(f'{site}/all?scope={scope}').text, 'html.parser')
    value = soup.find_all('a', class_=lambda x: x and 'appCard' in str(x))
    result = []
    if value:
        for card in value:
            link = site + card.get('href')
            icon = card.find('img', class_='appIcon')['src']
            name = card.find('p', class_='appCard__appname').text.strip()
            likes = card.find_all('p', class_='text text-b3')[0].text.strip()
            comments = card.find_all('p', class_='text text-b3')[1].text.strip()
            result.append({
                'status': True,
                'link': link,
                'app_icon': icon,
                'app_name': name,
                'likes': likes,
                'comments': comments
            })
    return result

def recent():
    data = get_data('recent')
    if not data:
        data = e_msg
    return data

def editor_choice():
    data = get_data('editor_choice')
    if not data:
        data = e_msg
    return data

def trending():
    data = get_data('trending')
    if not data:
        data = e_msg
    return data

def most_liked():
    data = get_data('most_liked')
    if not data:
        data = e_msg
    return data

e_msg = {'status': False, 'message': 'found 0'}

def app_info(pid):
    soup = bs(ses.get(f'{site}/p/{pid}').text, 'html.parser')
    value = soup.find('div', class_='project')
    if value:
        name = value.find('h2', class_='project__name').text.strip()
        author = value.find('a', class_='project__author').text.strip()
        icon = value.find('img', class_='appIcon')['src']
        categories = [button.text.strip() for button in value.find_all('button', class_='sk-chips')]
        val1 = soup.find('div', class_='project-about')
        val2 = soup.find('div', class_='project-whatsnew')
        about = val1.find('p', class_='text text-b1').get_text(strip=True) if val1 else 'N/A'
        whatsnew = val2.find('p').get_text(strip=True) if val2 else 'N/A'
        return {
            'status': True,
            'app_name': name,
            'author': author,
            'app_icon': icon,
            'categories': categories,
            'about': about,
            'whatsnew': whatsnew if whatsnew else None
        }
    else:
        return e_msg      
        
def user_info(username):
    soup = bs(ses.get(f'{site}/u/{username}').text, 'html.parser')
    
    val1 = soup.find('h2', class_='profile__name text text-h2')
    val2 = soup.find('img', class_='appIcon')
    val3 = soup.find('div', class_='lcd-stats__item')
    val4 = val3.find_next_sibling('div') if val1 else None
    val5 = val4.find_next_sibling('div') if val2 else None
    val6 = soup.find('div', class_='profile-about')
    
    name = val1.text.strip() if val1 else None    
    icon = val2['src'] if val2 else 'N/A'
    role = soup.find('button', class_='sk-chips text text-b2').text.strip() if soup.find('button', class_='sk-chips text text-b2') else 'N/A'
    
    if name:
        projects = val3.find_all('span')[1].text  if val1 else 'N/A'
        likes = val4.find_all('span')[1].text     if val2 else 'N/A'
        downloads = val5.find_all('span')[1].text if val3 else 'N/A'
        about = val6.find('p', class_='text text-b1').text.strip() if val4 else 'N/A'
        
        return {
            'status': True,
            'username': name,
            'profile_pic': icon,
            'role': role,
            'projects': projects,
            'likes': likes,
            'downloads': downloads,
            'about': about
        }
    else:
        return {'status': False, 'message': 'user not found'}
