import re
from bs4 import BeautifulSoup
import sys

html_file = sys.argv[1]
output_file = sys.argv[2]

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

results = []

# Try to find elements that contain onion links
# Looking for typical structures like lists or paragraphs containing links
for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if '.onion' in href:
        link_text = a_tag.get_text(strip=True)
        # Try to find the description and status which are usually in the same parent element (li, p, tr, etc.)
        parent = a_tag.parent
        # Go up a bit if parent is too specific (like strong, span)
        while parent and parent.name not in ['li', 'p', 'td', 'div']:
            parent = parent.parent
            if parent is None:
                break
        
        description = ""
        if parent:
            description = parent.get_text(" ", strip=True)
            # Remove the link itself from the description if it's there
            description = description.replace(link_text, "").strip()
            
            # Simple check for online/offline status in the text
            status = "Unknown"
            text_lower = description.lower()
            if "online" in text_lower or "aktywna" in text_lower or "działa" in text_lower:
                status = "Online"
            elif "offline" in text_lower or "nieaktywna" in text_lower or "nie działa" in text_lower:
                status = "Offline"
            
            results.append(f"Link: {href}\nDescription: {description}\nStatus: {status}\n")

if not results:
    # Fallback to regex if beautifulsoup doesn't catch them easily
    onion_pattern = re.compile(r'([a-zA-Z0-9]{16,56}\.onion)')
    for match in onion_pattern.finditer(html_content):
        results.append(f"Link: {match.group(1)}\nDescription: (Fallback extracted)\nStatus: Unknown\n")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write("\n".join(results))

print(f"Extracted {len(results)} links to {output_file}")
