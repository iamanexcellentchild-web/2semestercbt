import json
import re

# Read the file
with open('mth103.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Try to parse and find the issue
try:
    data = json.loads(content)
    print("JSON is valid!")
except json.JSONDecodeError as e:
    print(f"JSON Error at line {e.lineno}, column {e.colno}: {e.msg}")
    # Get lines around the error
    lines = content.split('\n')
    start = max(0, e.lineno - 5)
    end = min(len(lines), e.lineno + 5)
    print(f"\nContext (lines {start+1}-{end}):")
    for i in range(start, end):
        marker = ">>>" if i == e.lineno - 1 else "   "
        print(f"{marker} {i+1:4d}: {lines[i]}")
