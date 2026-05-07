import json

# Read the file
with open('mth103.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define comprehensive topic consolidation mapping
topic_mapping = {
    # ============= VECTORS - FUNDAMENTALS =============
    "Vectors - Component Form": "Vectors - Fundamentals",
    "Vectors - Magnitude and Unit Vectors": "Vectors - Fundamentals",
    "Vectors - Direction Cosines": "Vectors - Fundamentals",
    "Vectors - Basic Concepts": "Vectors - Fundamentals",
    "Vectors - Magnitude": "Vectors - Fundamentals",
    "Vectors - Unit Vector": "Vectors - Fundamentals",
    "Vectors - Unit Vector along Sum": "Vectors - Fundamentals",
    "Vectors - Direction Angles": "Vectors - Fundamentals",
    "Vectors - Resolution": "Vectors - Fundamentals",
    "Vectors - Component along a Direction": "Vectors - Fundamentals",
    
    # ============= VECTORS - OPERATIONS =============
    "Vector Algebra - Addition": "Vectors - Operations",
    "Vectors - Addition of three vectors": "Vectors - Operations",
    "Vectors - Triangle Law": "Vectors - Operations",
    "Vector Algebra - Triangle Law": "Vectors - Operations",
    "Vectors - Parallelogram Law": "Vectors - Operations",
    "Vectors - Subtraction": "Vectors - Operations",
    "Vectors - Linear Combination": "Vectors - Operations",
    "Vectors - Angle Between Vectors": "Vectors - Operations",
    "Vectors - Angle Between Two Forces": "Vectors - Operations",
    "Vectors - Direction of Resultant": "Vectors - Operations",
    "Vectors - Resultant Force": "Vectors - Operations",
    "Vectors - Parallel Vectors": "Vectors - Operations",
    
    # ============= VECTORS - DOT PRODUCT =============
    "Dot Product": "Vectors - Dot Product",
    "Dot Product - Work Done": "Vectors - Dot Product",
    "Dot Product - Angle": "Vectors - Dot Product",
    "Dot Product - Perpendicular": "Vectors - Dot Product",
    "Vectors - Dot Product": "Vectors - Dot Product",
    "Vectors - Dot Product Perpendicular": "Vectors - Dot Product",
    "Vectors - Dot Product for Perpendicularity": "Vectors - Dot Product",
    "Vectors - Scalar Projection": "Vectors - Dot Product",
    "Vectors - Work Done": "Vectors - Dot Product",
    
    # ============= VECTORS - CROSS PRODUCT =============
    "Cross Product": "Vectors - Cross Product",
    "Cross Product - Area": "Vectors - Cross Product",
    "Cross Product - Volume": "Vectors - Cross Product",
    "Cross Product - Area of Triangle": "Vectors - Cross Product",
    "Cross Product - Shortest Distance": "Vectors - Cross Product",
    "Cross Product - Volume of Parallelepiped": "Vectors - Cross Product",
    "Vectors - Cross Product": "Vectors - Cross Product",
    "Vectors - Cross Product Area": "Vectors - Cross Product",
    "Vectors - Cross Product of Perpendicular Vectors": "Vectors - Cross Product",
    "Vectors - Magnitude of Cross Product": "Vectors - Cross Product",
    "Vectors - Scalar Triple Product": "Vectors - Cross Product",
    
    # ============= VECTORS - GEOMETRY & POSITION =============
    "Vector Algebra - Lines in 3D": "Vectors - Geometry",
    "Vector Algebra - Position Vectors": "Vectors - Geometry",
    "Lines in 3D - Intersection": "Vectors - Geometry",
    "Lines in 3D - Intersection with Plane": "Vectors - Geometry",
    "Lines in 3D - Shortest Distance": "Vectors - Geometry",
    "Lines and Planes - Intersection": "Vectors - Geometry",
    "Vectors - Geometry": "Vectors - Geometry",
    "Vectors - Position Vectors": "Vectors - Geometry",
    "Vectors - Velocity Components": "Vectors - Geometry",
    
    # ============= VECTORS - ADVANCED =============
    "Vector Algebra - Perpendicularity": "Vectors - Advanced",
    "Vector Algebra - Linear Independence": "Vectors - Advanced",
    "Vector Algebra - Coplanarity": "Vectors - Advanced",
    "Vector Algebra - Orthogonality": "Vectors - Advanced",
    "Vectors - Properties": "Vectors - Advanced",
    "Vectors - Linear Independence": "Vectors - Advanced",
    
    # ============= VECTOR CALCULUS =============
    "Vector Calculus - Differentiation": "Vector Calculus",
    "Vector Calculus - Integration": "Vector Calculus",
    "Vector Calculus - Definite Integral": "Vector Calculus",
    "Vector Calculus - Relative Velocity": "Vector Calculus",
    "Vector Calculus - Speed": "Vector Calculus",
    
    # ============= KINEMATICS =============
    "Kinematics - River Crossing": "Kinematics - Applications",
    "Kinematics - River Crossing with Drift": "Kinematics - Applications",
    
    # ============= MISCELLANEOUS =============
    "Lines and Planes - Angle": "Geometry - Lines & Planes",
    "Vectors - Projection": "Vectors - Advanced",
}

# Apply mapping to all questions
for question in data:
    old_topic = question.get("topic")
    if old_topic in topic_mapping:
        question["topic"] = topic_mapping[old_topic]

# Get unique topics after mapping
unique_topics_after = sorted(set(q.get("topic") for q in data if q.get("topic")))

# Count vector-related topics
vector_topics = [t for t in unique_topics_after if t.startswith('Vectors') or 'Vector Calculus' in t or 'Kinematics' in t]

print("VECTOR-RELATED TOPICS (CONSOLIDATED):")
print("=" * 60)
for topic in sorted(vector_topics):
    count = sum(1 for q in data if q.get("topic") == topic)
    print(f"  {topic}: {count:2d} questions")

# Save the reorganized file
with open('mth103.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Topics reorganized successfully!")
print(f"   Total unique topics in file: {len(unique_topics_after)}")
