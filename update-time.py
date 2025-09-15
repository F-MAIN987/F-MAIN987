from datetime import datetime, timezone


now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


with open('README.md', 'r', encoding='utf-8') as f:
txt = f.read()


new = txt.replace('<!--TIME-->', now)


with open('README.md', 'w', encoding='utf-8') as f:
f.write(new)


print('Updated README timestamp to', now)
