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
    times = club['times']
    str = ''.join(formatMeetingInfo(info) for info in times)
    return str

def compactTimesHTML(club):
    return "".join([f" <span class='compact-time'>{info['day']}</span>" for info in club['times']])

def formatMeetingInfo(info):
    return f"<p>{info['day']} &#149; {info['time']} { ' &#149; Room ' + str(info['room']) if 'room' in info else ''} { ' &#149; <a href=' + str(info['url']) + '>Join online meeting</a>' if 'url' in info else ''}</p>"

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
            output += f"\n\t<a href='/{club['shortName'].replace(' ','').lower()}/{page['name'].replace(' ','').lower() if page['name'] != 'Home' else '.'}/'>{page['name']}</a>"
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
<input type="search" id="search" placeholder="Search clubs, or weekdays">
</header>
"""

def catalogHTML(clubs):
    output = ""
    for club in clubs:
        clubInfoHTML = f"<a class='club-item' href='{club['shortName'].replace(' ','').lower()}'><h3>{club['name']}</h3><p>{club['description']}{compactTimesHTML(club)}</p><a>"
        output += clubInfoHTML
    return output + searchScriptHTML()

def searchScriptHTML():
    return """
<script>
function search() {
    var input, filter, clubs, club, a, i, txtValue;
    input = document.getElementById('search');
    filter = input.value.toUpperCase();
    clubs = document.getElementsByClassName('club-item');
    for (i = 0; i < clubs.length; i++) {
        club = clubs[i];
        txtValue = club.textContent || clubs.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            club.style.display = '';
        } else {
            club.style.display = 'none';
        }
    }
}
document.getElementById('search').addEventListener('keyup', search);
</script>
"""
