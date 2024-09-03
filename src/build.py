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



def rootHTML(title,content):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    {content}
</body>
</html>"""

def generate_club_page(club):
    title = club['name']
    content = f"""<h1>{club['name']}</h1>
    <p>{club['description']}</p>"""
    return rootHTML(title,content)

# loop through clubs and generate subdirectories with index.html files
for club in clubs:
    club_dir = 'output/' + club['name'].replace(' ','_')
    if not os.path.exists(club_dir):
        os.makedirs(club_dir)
    with open(club_dir + '/index.html','w') as file:
        file.write(generate_club_page(club))


