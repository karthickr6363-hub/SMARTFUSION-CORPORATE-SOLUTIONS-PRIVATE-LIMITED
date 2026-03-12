import glob
import re

files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(
        r'(<a href="service\.html" class="nav-item nav-link(?: active)?">Services</a>)',
        r'\1\n                    <a href="how-it-works.html" class="nav-item nav-link">How It Works</a>',
        content
    )
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
print(f"Updated {len(files)} files.")
