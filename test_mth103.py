#!/usr/bin/env python3
import json
import os

# Test loading mth103.json
mth103_path = os.path.join(os.path.dirname(__file__), 'mth103.json')
print(f"Looking for file at: {mth103_path}")
print(f"File exists: {os.path.isfile(mth103_path)}")

if os.path.isfile(mth103_path):
    try:
        with open(mth103_path, encoding='utf-8') as f:
            data = json.load(f)
        print(f"Successfully loaded JSON")
        print(f"Data type: {type(data)}")
        print(f"Is list: {isinstance(data, list)}")
        if isinstance(data, list):
            print(f"Number of questions: {len(data)}")
            if len(data) > 0:
                print(f"First question: {data[0]}")
    except Exception as e:
        print(f"Exception: {e}")
        import traceback
        traceback.print_exc()
else:
    print("File not found!")
