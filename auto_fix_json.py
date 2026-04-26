import json
import re

# Read the file
with open('mth103.json', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix solution lines that have unescaped quotes
fixed_lines = []
for i, line in enumerate(lines):
    if '"solution":' in line and '"' in line[line.find('"solution":'):]:
        # Extract the solution field and escape internal quotes
        match = re.search(r'"solution":\s*"(.+)"(?:\s*[},])', line)
        if match:
            solution_text = match.group(1)
            # Replace problematic quote patterns
            solution_text = solution_text.replace('"', '\\"')
            # But unescape the outer quotes
            line = line[:match.start()] + '"solution": "' + solution_text + '"' + line[match.end()-1:]
    fixed_lines.append(line)

# Try to parse the fixed content
fixed_content = ''.join(fixed_lines)
try:
    data = json.loads(fixed_content)
    print(f"Successfully fixed! Valid JSON with {len(data)} questions.")
    # Write back the fixed content
    with open('mth103.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("File saved successfully.")
except json.JSONDecodeError as e:
    print(f"Still has errors at line {e.lineno}: {e.msg}")
