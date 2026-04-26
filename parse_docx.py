from docx import Document
import json
import re

doc = Document('PHY102_PHS122_Question_Bank (1).docx')

questions = []
current_q = None
topic = ""

for para in doc.paragraphs:
    text = para.text.strip()
    if not text:
        continue
    
    # Check for topic
    if text.startswith("TOPIC"):
        topic_match = re.search(r'TOPIC \d+:\s*(.+)', text)
        if topic_match:
            topic = topic_match.group(1).strip()
        continue
    
    # Check for question start
    q_match = re.match(r'Q(\d+)\.\s*(.+)', text)
    if q_match:
        if current_q:
            questions.append(current_q)
        q_id = int(q_match.group(1))
        question = q_match.group(2)
        current_q = {
            "id": q_id,
            "source": "Past Questions Compilation",
            "topic": topic,
            "question": question,
            "options": {},
            "answer": "",
            "explanation": ""
        }
        continue
    
    if current_q:
        # Check for options
        opt_match = re.match(r'\s*([a-d])\.\s*(.+)', text, re.IGNORECASE)
        if opt_match:
            letter = opt_match.group(1).upper()
            option_text = opt_match.group(2)
            current_q["options"][letter] = option_text
            continue
        
        # Check for correct answer
        ans_match = re.match(r'✔ Correct Answer:\s*([a-d])\.\s*(.+)', text, re.IGNORECASE)
        if ans_match:
            current_q["answer"] = ans_match.group(1).upper()
            continue
        
        # Check for explanation
        exp_match = re.match(r'💡 Explanation:\s*(.+)', text)
        if exp_match:
            current_q["explanation"] = exp_match.group(1)
            continue

# Append last question
if current_q:
    questions.append(current_q)

# Assign unique ids
for i, q in enumerate(questions, start=1):
    q['id'] = i

with open('phy102.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(questions)} questions.")