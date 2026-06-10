import re

def check():
    with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find s3 block
    match = re.search(r'(<div class="s[^>]*id="s3".*?)(<!-- ══════════════════════════════════════\n     S5 ·)', content, re.DOTALL)
    if not match:
        # maybe S4?
        match = re.search(r'(<div class="s[^>]*id="s3".*?)(<!-- ══════════════════════════════════════\n     S4 ·)', content, re.DOTALL)

    if match:
        print("S3 found.")
    else:
        print("S3 not found.")

check()
