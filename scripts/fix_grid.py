file_path = 'ENAE_Presentation_v3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the grid with a flexbox
old_grid = 'display:grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 1400px; margin: 0 auto; flex:1;'
new_grid = 'display:flex; flex-wrap: wrap; justify-content: center; gap: 24px; max-width: 1200px; margin: 0 auto; flex:1; align-content: flex-start; padding-top: 20px;'

content = content.replace(old_grid, new_grid)

# Remove the weird grid-column and margins from card 4 and 5
content = content.replace('grid-column: span 1.5; margin-left: 50%;', '')
content = content.replace('grid-column: span 1.5; margin-right: 50%;', '')

# Make all cards roughly 1/3 width using flex-basis
old_card = 'background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px);'
new_card = 'flex: 1 1 calc(33.333% - 24px); min-width: 300px; max-width: 360px; background:rgba(255,255,255,.05); border:1px solid rgba(255,255,255,.1); border-radius:16px; padding:32px; backdrop-filter:blur(12px);'

content = content.replace(old_card, new_card)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done fix grid")
