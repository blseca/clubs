def rootHTML(club,content, opts = {}):
    return f"""<!DOCTYPE html>
<html class="{opts['site-class'] if 'site-class' in opts else ''}">
<head>
    <title>{club['name']}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1"> 
    <link rel="stylesheet" href="/style.css">
    <style>
        :root {{
            --background-color: {club['theme']['background-color'] if 'theme' in club else '#f9f4ff'};
            --primary-color: {club['theme']['primary-color'] if 'theme' in club else '#000000'};
            --accent-color: {club['theme']['accent-color'] if 'theme' in club else '#6D2BC1'};
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
    return "".join([f" <span class='compact-time {info['day']}'>{info['day']}</span>" for info in club['times']])

def formatMeetingInfo(info):
    return f"<p class={info['day']}>{info['day']} &#149; {info['time']} { ' &#149; Room ' + str(info['room']) if 'room' in info else ''} { ' &#149; <a href=' + str(info['url']) + '>Join online meeting</a>' if 'url' in info else ''}</p>"

def clubLinkHTML(club):
    for link in club['links']:
        return f"<p><a href='{link['url']}' title='{link['description']}'>{link['name']}</a></p>"
    return ""

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
    if 'images' in page:
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
<h1>Boston Latin School Club Catalog</h1>
<br>
<input type="search" id="search" placeholder="Search clubs, or weekdays">
</header>
"""

def catalogHTML(clubs, externalClubs = []):
    output = ""
    allClubs = clubs + externalClubs
    allClubs.sort(key=lambda club: club['name'])
    for club in allClubs:
        url = club['externalLink'] if 'externalLink' in club else club['shortName'].replace(' ','').lower()
        clubInfoHTML = f"<a class='club-item' href='{url}'><h3>{club['name']}</h3><p>{club['description']}</p><p>{compactTimesHTML(club)}</p><a>"
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
