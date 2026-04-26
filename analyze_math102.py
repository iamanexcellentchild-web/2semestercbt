with open('app.py', 'r') as f:
    lines = f.readlines()

# Find Math 102
for i, line in enumerate(lines):
    if '"Math 102": [' in line and i < 200:
        print(f'Math 102 starts at line {i+1}')
        # Find where it ends
        for j in range(i, min(i+4500, len(lines))):
            if lines[j].strip() == '],' and j > i + 100:
                # Check if this is really the end
                # Look ahead for next section
                next_section = None
                for k in range(j, min(j+10, len(lines))):
                    if '"' in lines[k] and ':' in lines[k] and '[' in lines[k]:
                        next_section = k
                        break
                if next_section:
                    print(f'Math 102 ends at line {j+1} (closing bracket)')
                    print(f'Next section at line {next_section+1}: {lines[next_section][:50]}')
                    
                    # Now count questions with and without solutions
                    with_solutions = 0
                    without_solutions = 0
                    missing_ids = []
                    for idx in range(i, j):
                        if '"id":' in lines[idx]:
                            has_solution = False
                            for jdx in range(idx, min(idx+25, j)):
                                if '"solution":' in lines[jdx]:
                                    has_solution = True
                                    break
                            if has_solution:
                                with_solutions += 1
                            else:
                                without_solutions += 1
                                # Extract ID
                                import re
                                match = re.search(r'"id":\s*(\d+)', lines[idx])
                                if match:
                                    missing_ids.append(int(match.group(1)))
                    
                    print(f'\nWith solutions: {with_solutions}')
                    print(f'Without solutions: {without_solutions}')
                    print(f'Missing solution IDs: {sorted(missing_ids)[:50]}')
                    break
        break
