import re

def extract():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Financial Magazine logo (it's right after "FM + El Mundo")
    fm_pattern = r'alt="Financial Magazine".*?src="(data:image/png;base64,[^"]+)"'
    fm_match = re.search(r'src="(data:image/png;base64,[^"]+)".*?alt="Financial Magazine"', content)
    if not fm_match:
        # try the other way
        fm_match = re.search(r'alt="Financial Magazine".*?src="(data:image/png;base64,[^"]+)"', content)

    # Find El Mundo logo
    elmundo_match = re.search(r'alt="El Mundo".*?src="(data:image/png;base64,[^"]+)"', content)
    if not elmundo_match:
        elmundo_match = re.search(r'src="(data:image/png;base64,[^"]+)".*?alt="El Mundo"', content)

    # Find QS badges
    # Since QS is repeated or there's one main one, let's find one
    qs_match = re.search(r'src="(data:image/png;base64,[^"]+)".*?QS World University Rankings', content, re.DOTALL)
    if not qs_match:
        # just find any qs base64
        # In S4 it says "QS World University Rankings"
        qs_match = re.search(r'<img src="(data:image/png;base64,[a-zA-Z0-9+/=]+)"', content[content.find('QS World'):content.find('QS World')+2000])

    print("FM logo found:", bool(fm_match))
    print("El Mundo logo found:", bool(elmundo_match))
    print("QS logo found:", bool(qs_match))

extract()
