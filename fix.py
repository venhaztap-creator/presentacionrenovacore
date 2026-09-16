import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(',550', '$2,550')
content = content.replace(',315', '$3,315')
content = content.replace('un sobrecargo de por prioridad', 'un sobrecargo de $765 por prioridad')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed")
