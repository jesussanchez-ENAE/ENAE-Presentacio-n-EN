import re

def add_font():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for </head>
    if "Open+Sans" not in content:
        link_tag = '<link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">\n'
        content = content.replace('</head>', link_tag + '</head>')
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Added Open Sans")
    else:
        print("Already has Open Sans")

add_font()
