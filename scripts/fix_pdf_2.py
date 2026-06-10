import re

def fix():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_logic = """    // Position printContainer off-screen to not mess up viewport
    printContainer.style.position = 'absolute';
    printContainer.style.top = '0';
    printContainer.style.left = '-9999px';"""

    # We will just change it to absolute, zIndex -1 to be safe and avoid bounding box bugs
    new_logic = """    // Position printContainer behind everything to avoid html2canvas bounding box bugs with -9999px
    printContainer.style.position = 'absolute';
    printContainer.style.top = '0';
    printContainer.style.left = '0';
    printContainer.style.zIndex = '-9999';
"""

    if old_logic in content:
        content = content.replace(old_logic, new_logic)
        with open('ENAE_Presentation_v3.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed 2")
    else:
        print("Not found 2")

fix()
