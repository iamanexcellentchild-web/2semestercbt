import json
import re

# Read the file
with open(r'c:\Users\HP\OneDrive\Desktop\cbt2semester\chm102.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove comments (lines starting with #)
lines = content.split('\n')
cleaned_lines = []
for line in lines:
    # Skip comment lines
    stripped = line.lstrip()
    if stripped.startswith('#'):
        continue
    # Replace 'questions = [' with just '['
    if 'questions = [' in line:
        cleaned_lines.append('[')
    else:
        cleaned_lines.append(line)

content = '\n'.join(cleaned_lines)

# Replace 'explanation' with 'solution'
content = content.replace('"explanation":', '"solution":')

# Debug: print first 500 characters
print("First 500 chars of cleaned content:")
print(repr(content[:500]))
print("\n---\n")

try:
    data = json.loads(content)
    print(f'✓ Successfully parsed! Total questions: {len(data)}')
    
    # Write the converted data back to the file
    with open(r'c:\Users\HP\OneDrive\Desktop\cbt2semester\chm102.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f'✓ Successfully wrote converted CHM102 file with {len(data)} questions!')
    
except json.JSONDecodeError as e:
    print(f'✗ JSON Error at position {e.pos}: {e.msg}')
    print(f'Context: ...{content[max(0, e.pos-80):e.pos+80]}...')
