import re
import os

files = [
    ("gallery.html", "gnome/"),
    ("gallery1.html", "memory_bear/")
]

for file, prefix in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace src="X.png" or src="X.jpg" with src="prefix/X.png"
    # only if the image doesn't start with http, gnome/, memory_bear/, c1.png, tmxk.png
    def replacer(m):
        filename = m.group(1)
        if filename.startswith('http') or filename.startswith('gnome/') or filename.startswith('memory_bear/') or filename in ['c1.png', 'tmxk.png']:
            return m.group(0)
        return f'src="{prefix}{filename}"'
        
    content = re.sub(r'src="([^"]+\.(?:png|jpg|jpeg))"', replacer, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# For index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="dd1.png"', 'src="gnome/dd1.png"')
content = content.replace('src="kk2.png"', 'src="gnome/kk2.png"')
content = content.replace('src="kk3.png"', 'src="memory_bear/kk3.png"')
content = content.replace('src="kk4.png"', 'src="memory_bear/kk4.png"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
