import markdown

with open("website.md", "r") as input_file:
    html = markdown.markdown(input_file.read())
    print(html)

with open('website.html', 'w') as output_file:
    output_file.write(html)