def rootHTML(club,content):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{club['name']}</title>
    <link rel="stylesheet" href="/style.css">
    <style>
        :root {{
            {'--background-color:'+club['theme']['background-color'] if 'theme' in club else ''};
            {'--primary-color:'+club['theme']['primary-color'] if 'theme' in club else ''};
            {'--accent-color:'+club['theme']['accent-color'] if 'theme' in club else ''};
        }}
    </style>
</head>
<body>{content}
</body>
</html>"""

def headerHTML(club):
    return f"""
<header>
    <h1>{club['name']}</h1>
    <a id="all-clubs" href='/' title='BLS Clubs'>ALL CLUBS</a>
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

def compactTimesHTML(club):
    return "".join([f" <span class='compact-time'>{day}</span>" for day,info in club['times']['weekly'].items() if info['meet']])

def formatMeetingInfo(day,time):
    if not time['meet']: 
        return ''
    return f"<p>{day} &#149; {time['time']} { ' &#149; Room ' + str(time['room']) if 'room' in time else ''} { ' &#149; <a href=' + str(time['url']) + '>Join online meeting</a>' if 'url' in time else ''}</p>"

def clubLinkHTML(club):
    for link in club['links']:
        return f"<p><a href='{link['url']}' title='{link['description']}'>{link['name']}</a></p>"

def navbarHTML(club, pageNum):
    output = ""
    for i in range(len(club['pages'])):
        page = club['pages'][i]
        if i == pageNum:
            output += f"\n\t<a href='./' class='currentPage'>{page['name']}</a>"
        else:
            output += f"\n\t<a href='/{club['name'].replace(' ','_')}/{page['name'] if page['name'] != 'Home' else '.'}/index.html'>{page['name']}</a>"
    return "\n<nav>" + output + "\n</nav>"

def bodyHTML(club, pageNum):
    page = club['pages'][pageNum]
    output = f"""
<main>
<h1>{page['title']}</h1>
<p>{page['body']}</p>
"""
    for image in page['images']:
        output += f"<img src='{image['url']}' alt='{image['alt']}'>\n"
    return output + "\n</main>"

def officerHTML(club, pageNum):
    page = club['pages'][pageNum]
    output = f"""
<main>
<p>{page['description']}</p>
"""
    for category in page['categories']:
        output += f"\n<h3>{category['name']}</h3>"
        for member in category['members']:
            output += f"\n\t<p>{member['name']} - {member['position']}</p>"

    return output + "\n</main>"


def catalogHeaderHTML():
    return """
<header>
<h1>Boston Latin School Clubs</h1>
<p>Search here for a list of all clubs at blsclubs.org</p>
</header>
"""

def catalogHTML(clubs):
    output = ""
    for club in clubs:
        name = club['name']
        clubInfoHTML = f"<a class='club-item' href='{name}'><h3>{name}</h3><p>{club['description']}{compactTimesHTML(club)}</p><a>"
        output += clubInfoHTML
    return output
