import re

with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the FIRST line where Math 102 starts with questions data
math102_start = None
math102_end = None
for i, line in enumerate(lines):
    if '"Math 102": [' in line and i < 200:  # The actual data should be near the beginning
        math102_start = i
        print(f"Found Math 102 at line {i+1}: {line[:50]}")
        break

if math102_start is not None:
    # Search for the end of Math 102 section (look for the next key like "Physics 102")
    for i in range(math102_start + 100, min(math102_start + 4000, len(lines))):
        # Look for pattern like '  ],' which closes the Math 102 array
        if lines[i].strip() == '],' and not any('"' in lines[j] for j in range(max(0, i-30), i)):
            math102_end = i
            print(f"Math 102 ends around line {i+1}")
            break
    
    if math102_end:
        print(f"Math 102 section: lines {math102_start+1} to {math102_end+1}")
        
        # Look for questions without solutions
        missing_ids = []
        solution_count = 0
        no_solution_count = 0
        
        for i in range(math102_start, math102_end + 1):
            if '"id":' in lines[i]:
                # Extract ID
                id_match = re.search(r'"id":\s*(\d+)', lines[i])
                if id_match:
                    qid = id_match.group(1)
                    # Check next 25 lines for solution field
                    has_solution = False
                    for j in range(i, min(i+25, math102_end + 1)):
                        if '"solution":' in lines[j]:
                            has_solution = True
                            solution_count += 1
                            break
                    if not has_solution:
                        missing_ids.append(int(qid))
                        no_solution_count += 1
                        if no_solution_count <= 30:
                            print(f"ID {qid} - NO SOLUTION")
        
        print(f"\nTotal with solutions: {solution_count}")
        print(f"Total missing solutions: {no_solution_count}")
        print(f"Missing IDs: {sorted(missing_ids)[:30]}")
    else:
        print("Could not find end of Math 102 section")
else:
    print("Could not find Math 102 section")
