import re
import base64
import os

repo_dir = '/Users/jesus/Documents/GitHub/Plantilla-Dossiers-ENAE/src/Rankings/'
def get_b64(filename):
    path = os.path.join(repo_dir, filename)
    if not os.path.exists(path):
        return ""
    with open(path, 'rb') as f:
        return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"

# Images we need
badges = {
    'excellent': get_b64('0faf3965-9e4e-419c-a4cc-2ac0a6a48783.png'),
    'teaching': get_b64('e32d12cd-861d-4634-8b5d-ca1fbae0e4db.png'),
    'inclusiveness': get_b64('b3b7e495-1f79-4615-97b7-688792bd45fd.png'),
    'logistics_star': get_b64('6db43692-2cf3-407f-b674-75311166e7cf.png'),
    'arts': get_b64('2950d6d7-9af8-4583-9c77-d8240f953611.png'),
    
    'marketing': get_b64('e28e8b09-fbda-47c6-af43-34509a6d3dd8.png'), # Check if this is marketing? I need to guess or try e28...
    'data_science': get_b64('76e149bf-d0f1-4b5e-8cf5-9826206a5f62.png'),
    'logistics': get_b64('18c6ddab-e93d-4504-b5ad-ed2593881ba5.png'),
    'exec_mba': get_b64('QS Executive MBA Rankings - Europe - 2026 - Badge.png'),
    'finance': get_b64('99f03286-f60a-47a4-8774-bccf8abcbbdb.png'),
    'trade': get_b64('qs_international_trade.png'),
    'management': get_b64('1c465398-80d3-4b18-8bf8-deccb5a7d7af.png'),
    'global_mba': get_b64('68ad4500-612d-41e7-b2c3-f4266989e13f.png'),
    
    'fm': get_b64('FinancialMagazine.png'),
    'elmundo': get_b64('El_Mundo_logo.svg.png')
}

file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

s3_pattern = r'(<!-- ══════════════════════════════════════\n\s+S3 · RANKINGS.*?(?=<!-- ══════════════════════════════════════\n\s+S5 · PROGRAMAS EN INGLÉS))'
s3_match = re.search(s3_pattern, content, re.DOTALL)
if s3_match:
    s3_block = s3_match.group(1)
    
    # 1. FM and El Mundo
    s3_block = re.sub(r'<img src="[^"]*" class="w-32" alt="FM">', f'<img src="{badges["fm"]}" class="w-32" alt="FM">', s3_block)
    s3_block = re.sub(r'<img src="[^"]*" class="w-32" alt="El Mundo">', f'<img src="{badges["elmundo"]}" class="w-32" alt="El Mundo">', s3_block)
    
    # 2. QS Stars row
    # The HTML has:
    # <img src="..." class="h-24" alt="QS Star">
    # <img src="..." class="h-16 opacity-70" alt="QS Star"> x4
    stars_html = f"""<div class="flex gap-4 mb-2 justify-around bg-black/10 rounded-2xl p-6 border border-white/5 backdrop-blur-sm items-center">
        <img src="{badges['excellent']}" class="h-24" alt="QS Rated Excellent">
        <img src="{badges['teaching']}" class="h-16 opacity-70" alt="QS 5 Star">
        <img src="{badges['inclusiveness']}" class="h-16 opacity-70" alt="QS 5 Star">
        <img src="{badges['logistics_star']}" class="h-16 opacity-70" alt="QS 4 Star">
        <img src="{badges['arts']}" class="h-16 opacity-70" alt="QS 4 Star">
      </div>"""
    s3_block = re.sub(r'<div class="flex gap-4 mb-2 justify-around bg-black/10.*?</div>', stars_html, s3_block, flags=re.DOTALL)

    # 3. Big QS Card (Marketing)
    # The HTML has <img src="..." class="w-32 absolute top-8 left-8" alt="QS">
    s3_block = re.sub(r'<img src="[^"]*" class="w-32 absolute top-8 left-8" alt="QS">', f'<img src="{badges["marketing"]}" class="w-32 absolute top-8 left-8" alt="QS Marketing">', s3_block)
    
    # 4. Master Cards
    # We will just replace them one by one based on their name
    def replace_badge(name, b64):
        # find the card containing this name and replace its QS img
        pattern = r'(<div class="bg-white/5[^>]*>.*?<img src=")[^"]*(" class="w-16 mr-6 z-10" alt="QS">.*?<div class="font-bold text-\[16px\][^>]*>' + name + ')'
        nonlocal s3_block
        s3_block = re.sub(pattern, r'\1' + b64 + r'\2', s3_block, flags=re.DOTALL)

    replace_badge('Master in AI & Data Science', badges['data_science'])
    replace_badge('Logistics & Operations<br>Management', badges['logistics'])
    replace_badge('Global Executive MBA', badges['exec_mba'])
    replace_badge('Digital Marketing with AI', badges['marketing'])
    replace_badge('Finance, Fintech & Strategic<br>Control', badges['finance'])
    replace_badge('International Trade', badges['trade'])
    replace_badge('Risk Management in<br>Organizations', badges['management'])
    replace_badge('International MBA', badges['global_mba'])
    
    content = content.replace(s3_match.group(1), s3_block)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Badges mapped.")
