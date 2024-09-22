# Main file for reading json from clubs/ directory and generating html files

import os
import json
import templates

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

def generate_page(club, pageNum):
    return templates.rootHTML(club,
                    templates.headerHTML(club) + 
                    templates.navbarHTML(club, pageNum) +
                    templates.bodyHTML(club, pageNum)
                    )

def generate_officer_page(club, pageNum):
    return templates.rootHTML(club,
                    templates.headerHTML(club) + 
                    templates.navbarHTML(club, pageNum) +
                    templates.officerHTML(club, pageNum)
                    )

def generate_club_pages():
    # loop through clubs and generate subdirectories with index.html files
    for club in clubs:
        club_dir = 'output/' + club['name'].replace(' ','_')
        if not os.path.exists(club_dir):
            os.makedirs(club_dir)

        for pageNum in range(len(club['pages'])):
            page = club['pages'][pageNum]
            with open(club_dir + '/' + page['name'] + '.html','w') as file:
                if page['name'] == 'Officers': # Officers need different page generation
                    file.write(generate_officer_page(club, pageNum))
                    continue
                file.write(generate_page(club, pageNum))

generate_club_pages()