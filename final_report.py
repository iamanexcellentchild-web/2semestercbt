import json

print("="*70)
print("FINAL REORGANIZATION REPORT")
print("="*70)

# Check PHY104
with open('phy104.json', encoding='utf-8') as f:
    phy104 = json.load(f)
phy_topics = sorted(set(q.get('topic', 'General Physics') for q in phy104))

print("\n✅ PHY104 (Physics):")
print(f"   Questions: {len(phy104)}")
print(f"   Topics: {len(phy_topics)}")
for i, t in enumerate(phy_topics, 1):
    count = len([q for q in phy104 if q.get('topic') == t])
    pct = (count / len(phy104)) * 100
    print(f"     {i:2d}. {t:<40} {count:3d} qs ({pct:5.1f}%)")

# Check MTH103
with open('mth103.json', encoding='utf-8') as f:
    mth103 = json.load(f)
mth_topics = sorted(set(q.get('topic', 'General') for q in mth103))

print("\n✅ MTH103 (Mathematics):")
print(f"   Questions: {len(mth103)}")
print(f"   Topics: {len(mth_topics)}")
for i, t in enumerate(mth_topics, 1):
    count = len([q for q in mth103 if q.get('topic') == t])
    pct = (count / len(mth103)) * 100
    print(f"     {i:2d}. {t:<40} {count:3d} qs ({pct:5.1f}%)")

# Check STA112
with open('sta112.json', encoding='utf-8') as f:
    sta112 = json.load(f)
sta_topics = sorted(set(q.get('topic', 'General') for q in sta112))

print("\n✅ STA112 (Statistics):")
print(f"   Questions: {len(sta112)}")
print(f"   Topics: {len(sta_topics)}")
for i, t in enumerate(sta_topics, 1):
    count = len([q for q in sta112 if q.get('topic') == t])
    pct = (count / len(sta112)) * 100
    print(f"     {i:2d}. {t:<40} {count:3d} qs ({pct:5.1f}%)")

print("\n" + "="*70)
print("IMPROVEMENTS MADE:")
print("="*70)
print("""
1. PHY104:
   - Reorganized from 217 scattered topics to 18 meaningful grouped topics
   - Used intelligent keyword-based topic inference from question content
   - Topics now logically grouped: Waves, Sound, Optics, Modern Physics, etc.

2. MTH103:
   - Kept original 20 topics (already well-organized)
   - Topics cover: Vectors, Kinematics, Dynamics, Collisions, Conics, Coordinate Geometry

3. STA112:
   - Reorganized from 4 overgrouped topics to 10 specific topics
   - New topics: Probability Basics, Conditional Probability, Descriptive Statistics, etc.
   - Better separation of statistical concepts

4. APP.PY Updates:
   - Increased questions per session limit from 40 to 150
   - Updated flash message from "40 questions" to "150 questions"
   - This allows users to see ALL topics, not just a subset

5. Field Standardization:
   - All files now use consistent fields: id, source, topic, question, options, answer, explanation
   - Renamed 'correct_answer' → 'answer' and 'solution' → 'explanation' in STA112
   - All files properly formatted as JSON arrays
""")

print("="*70)
print("✨ REORGANIZATION COMPLETE!")
print("="*70)
print("\nNow users can:")
print("  • See all topics (not limited to 40 questions)")
print("  • Better navigate through logically grouped content")
print("  • Access detailed topic breakdowns with meaningful names")
