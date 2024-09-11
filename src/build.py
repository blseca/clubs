# Main file for reading json from clubs/ directory and generating html files

import os
import json

# Read json files from clubs/ directory
def read_json_files():
    clubs = []
    for filename in os.listdir('clubs'):
        if filename.endswith('.json'):
            with open('clubs/' + filename) as file:
                clubs.append(json.load(file))
    return clubs


# ensure existence of clubs/ and output/ directories
def ensure_directories():
    if not os.path.exists('clubs'):
        os.makedirs('clubs')
    if not os.path.exists('output'):
        os.makedirs('output')

ensure_directories()

clubs = read_json_files()

def generate_club_page(club):
    title = club['name']
    return rootHTML(title,headerHTML(club))

def generate_club_pages():
    # loop through clubs and generate subdirectories with index.html files
    for club in clubs:
        club_dir = 'output/' + club['name'].replace(' ','_')
        if not os.path.exists(club_dir):
            os.makedirs(club_dir)
            
        with open(club_dir + '/index.html','w') as file:
            file.write(generate_club_page(club))

def rootHTML(title,content):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>{content}
</body>
</html>"""

def headerHTML(club):
    return f"""
<header>
    <h1>{club['name']}</h1>
    <p class="description">{club['description']}</p>
    {clubTimesHTML(club)}
    {clubLinkHTML(club)}
</header>"""

def clubTimesHTML(club):
    weekly = club['times']['weekly']
    str = ''
    str += formatMeetingInfo('Monday',weekly['Monday'])
    str += formatMeetingInfo('Tuesday',weekly['Tuesday'])
    str += formatMeetingInfo('Wednesday',weekly['Wednesday'])
    str += formatMeetingInfo('Thursday',weekly['Thursday'])
    str += formatMeetingInfo('Friday',weekly['Friday'])
    str += formatMeetingInfo('Saturday',weekly['Saturday'])
    str += formatMeetingInfo('Sunday',weekly['Sunday'])
    return str

def formatMeetingInfo(day,time):
    if not time['meet']: 
        return ''
    return f"<p>{day} &#149; {time['time']} { ' &#149; Room ' + str(time['room']) if 'room' in time else ''} { ' &#149; <a href=' + str(time['url']) + '>Join meeting</a>' if 'url' in time else ''}</p>"

def clubLinkHTML(club):
    for link in club['links']:
        return f"<p><a href='{link['url']}' title='{link['description']}'>{link['name']}</a></p>"


generate_club_pages()