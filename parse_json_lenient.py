import json
import re

# Read the problematic JSON file with lenient parsing
with open('mth103.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Try multiple encoding/replacement strategies
attempts = [
    (content, "original"),
    (content.replace('"', '\\"').replace('\\"solution', '"solution').replace('\\"', '"'), "quote replacement"),
]

for attempt_content, attempt_name in attempts:
    try:
        data = json.loads(attempt_content)
        print(f"Successfully parsed with {attempt_name}!")
        print(f"Total questions: {len(data)}")
        break
    except json.JSONDecodeError as e:
        print(f"Failed with {attempt_name} at line {e.lineno}: {e.msg}")
        continue
else:
    print("\nTrying to use ast.literal_eval as fallback...")
    import ast
    try:
        # This won't work for JSON, but let's try regex extraction
        questions = re.findall(r'\{\s*"id":\s*(\d+)', content)
        print(f"Found {len(set(questions))} unique question IDs")
    except:
        pass
