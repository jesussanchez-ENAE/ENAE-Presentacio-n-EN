import re
with open('ENAE_Presentation_v3.html', 'r', encoding='utf-8') as f:
    html = f.read()
css = re.search(r'<style>(.*?)</style>', html, re.DOTALL).group(1)
css = re.sub(r"url\('data:[^)]+'\)", "url('...')", css)
print(css[:3000])
