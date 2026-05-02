"""
Thirteen-Trial Learning System (TTLS)
======================================
A structured repetition system where all questions are completely loaded
within exactly 13 trials. The system ensures spaced repetition with strategic
progression and guaranteed full coverage by trial 13.

Features:
- Structured question introduction (new questions each trial)
- Spaced repetition of previously seen questions
- Guaranteed complete loading by trial 13
- Difficulty progression option
- Performance-based repetition
- Session tracking and persistence
"""

import json
import random
from datetime import datetime
from math import ceil


class ThirteenTrialLearningSystem:
    """
    Main system class for managing 13-trial learning.
    """
    
    MAX_TRIALS = 13
    MASTERY_THRESHOLD = 0.8  # 80% to consider a question mastered
    
    def __init__(self, subject, total_questions):
        """
        Initialize the TTLS.
        
        Args:
            subject: Subject name (e.g., "Math 102")
            total_questions: Total number of unique questions to load
        """
        self.subject = subject
        self.total_questions = total_questions
        self.questions_per_trial = ceil(total_questions / self.MAX_TRIALS)
        
    def generate_trial_plan(self):
        """
        Generate a complete 13-trial plan ensuring all questions are loaded.
        
        Returns:
            dict: Trial plan with question indices for each trial
        """
        trial_plan = {
            "metadata": {
                "subject": self.subject,
                "total_questions": self.total_questions,
                "total_trials": self.MAX_TRIALS,
                "questions_per_trial": self.questions_per_trial,
                "strategy": "Structured Spaced Repetition with Guaranteed Coverage"
            },
            "trials": {}
        }
        
        # Distribute questions across trials
        all_question_indices = list(range(self.total_questions))
        
        # Trial structure:
        # Trials 1-3: Light introduction (NEW questions)
        # Trials 4-7: Moderate review with new questions
        # Trials 8-10: Intensive review + remaining new questions
        # Trials 11-13: Deep mastery + light new questions
        
        for trial_num in range(1, self.MAX_TRIALS + 1):
            trial_data = {
                "trial_number": trial_num,
                "new_questions": [],
                "review_questions": [],
                "total_questions_in_trial": 0,
                "repetition_count": self._calculate_repetition_for_trial(trial_num),
                "purpose": self._get_trial_purpose(trial_num)
            }
            
            trial_plan["trials"][trial_num] = trial_data
        
        # Distribute new questions
        new_questions_per_trial = max(1, self.questions_per_trial)
        question_idx = 0
        
        for trial_num in range(1, self.MAX_TRIALS + 1):
            # Add new questions
            questions_to_add = min(
                new_questions_per_trial,
                len(all_question_indices) - question_idx
            )
            
            for _ in range(questions_to_add):
                if question_idx < len(all_question_indices):
                    trial_plan["trials"][trial_num]["new_questions"].append(
                        all_question_indices[question_idx]
                    )
                    question_idx += 1
            
            # Add review questions (from previous trials)
            if trial_num > 1:
                review_questions = self._get_review_questions(
                    trial_plan, trial_num
                )
                trial_plan["trials"][trial_num]["review_questions"] = review_questions
            
            # Calculate total for this trial
            trial_plan["trials"][trial_num]["total_questions_in_trial"] = (
                len(trial_plan["trials"][trial_num]["new_questions"]) +
                len(trial_plan["trials"][trial_num]["review_questions"])
            )
        
        return trial_plan
    
    def _calculate_repetition_for_trial(self, trial_num):
        """Calculate how many times questions should be seen by this trial."""
        if trial_num <= 3:
            return 1
        elif trial_num <= 7:
            return 2
        elif trial_num <= 10:
            return 3
        else:  # Trials 11-13
            return 4
    
    def _get_trial_purpose(self, trial_num):
        """Get the learning purpose for each trial."""
        purposes = {
            1: "Initial exposure to first batch of questions",
            2: "Review first batch, introduce second batch",
            3: "Light review, introduce third batch",
            4: "Moderate review cycle begins",
            5: "Continue review, add new material",
            6: "Spaced repetition, more new material",
            7: "Comprehensive review checkpoint",
            8: "Intensive review of mastered concepts",
            9: "Deep learning, fine-tuning knowledge",
            10: "Consolidation of intermediate material",
            11: "Final review push, fill any gaps",
            12: "Mastery refinement, targeted review",
            13: "Complete mastery verification - ALL questions loaded"
        }
        return purposes.get(trial_num, "Review and consolidation")
    
    def _get_review_questions(self, trial_plan, current_trial):
        """Get questions that should be reviewed in current trial."""
        review_questions = []
        
        # Strategy: Increase review intensity as trials progress
        if current_trial <= 3:
            review_count = 0  # No review in early trials
        elif current_trial <= 5:
            review_count = len(trial_plan["trials"][current_trial - 1]["new_questions"])
        elif current_trial <= 7:
            # Mix of previous trials
            prev_new = trial_plan["trials"][current_trial - 1]["new_questions"]
            prev_prev = trial_plan["trials"][max(1, current_trial - 2)]["new_questions"]
            review_count = len(prev_new) + len(prev_prev) // 2
        else:
            # Heavy review in later trials
            for prev_trial in range(max(1, current_trial - 3), current_trial):
                review_questions.extend(
                    trial_plan["trials"][prev_trial]["new_questions"]
                )
        
        return review_questions[:review_count]
    
    def get_trial_questions(self, trial_num, all_questions):
        """
        Get questions for a specific trial.
        
        Args:
            trial_num: Trial number (1-13)
            all_questions: List of all available questions
            
        Returns:
            list: Questions for this trial
        """
        plan = self.generate_trial_plan()
        trial_data = plan["trials"][trial_num]
        
        questions = []
        
        # Add new questions
        for q_idx in trial_data["new_questions"]:
            if q_idx < len(all_questions):
                questions.append(all_questions[q_idx])
        
        # Add review questions
        for q_idx in trial_data["review_questions"]:
            if q_idx < len(all_questions):
                questions.append(all_questions[q_idx])
        
        return questions


class TrialProgressTracker:
    """Track user's progress through the 13-trial system."""
    
    def __init__(self, subject):
        self.subject = subject
        self.progress = {
            "subject": subject,
            "current_trial": 1,
            "trials_completed": [],
            "questions_seen": set(),
            "questions_mastered": set(),
            "trial_scores": {},
            "created_at": datetime.utcnow().isoformat(),
            "last_updated": datetime.utcnow().isoformat()
        }
    
    def start_trial(self, trial_num):
        """Record that user is starting a trial."""
        self.progress["current_trial"] = trial_num
        self.progress["last_updated"] = datetime.utcnow().isoformat()
    
    def complete_trial(self, trial_num, score, total, questions_in_trial):
        """Record trial completion."""
        self.progress["trials_completed"].append(trial_num)
        percentage = (score / total * 100) if total > 0 else 0
        
        self.progress["trial_scores"][str(trial_num)] = {
            "score": score,
            "total": total,
            "percentage": round(percentage, 2),
            "completed_at": datetime.utcnow().isoformat()
        }
        
        # Mark questions as seen
        for q in questions_in_trial:
            q_id = q.get("id", "")
            self.progress["questions_seen"].add(str(q_id))
            
            # Mark as mastered if scored well (simple heuristic)
            if percentage >= 75:
                self.progress["questions_mastered"].add(str(q_id))
        
        self.progress["current_trial"] = trial_num + 1
        self.progress["last_updated"] = datetime.utcnow().isoformat()
    
    def get_progress_percentage(self, total_questions):
        """Get % of questions that have been seen."""
        return (len(self.progress["questions_seen"]) / total_questions * 100) if total_questions > 0 else 0
    
    def is_system_complete(self):
        """Check if all 13 trials have been completed."""
        return len(self.progress["trials_completed"]) >= 13
    
    def to_dict(self):
        """Convert progress to dictionary (JSON-serializable)."""
        progress_copy = self.progress.copy()
        progress_copy["questions_seen"] = list(self.progress["questions_seen"])
        progress_copy["questions_mastered"] = list(self.progress["questions_mastered"])
        return progress_copy


def generate_13_trial_mode_quiz(subject, questions, trial_num=1, user_progress=None):
    """
    Generate a quiz for 13-trial mode.
    
    Args:
        subject: Subject name
        questions: All available questions
        trial_num: Current trial number (1-13)
        user_progress: User's current progress dict
        
    Returns:
        dict: Quiz data with questions for this trial
    """
    if not questions:
        return {"error": "No questions available"}
    
    system = ThirteenTrialLearningSystem(subject, len(questions))
    trial_questions = system.get_trial_questions(trial_num, questions)
    
    # Shuffle for variety
    random.shuffle(trial_questions)
    
    return {
        "trial_number": trial_num,
        "total_trials": 13,
        "subject": subject,
        "questions": trial_questions,
        "trial_purpose": system._get_trial_purpose(trial_num),
        "expected_questions": len(trial_questions),
        "repetition_intensity": system._calculate_repetition_for_trial(trial_num),
        "progress": {
            "trials_completed": len(user_progress.get("trials_completed", [])) if user_progress else 0,
            "questions_seen": len(user_progress.get("questions_seen", [])) if user_progress else 0,
            "total_questions": len(questions)
        }
    }


def calculate_trial_statistics(trial_result):
    """Calculate statistics for a completed trial."""
    stats = {
        "score": trial_result.get("score", 0),
        "total": trial_result.get("total", 0),
        "percentage": round(
            (trial_result.get("score", 0) / trial_result.get("total", 1) * 100),
            2
        ),
        "time_taken": trial_result.get("time_taken", 0),
        "questions_correct": trial_result.get("score", 0),
        "questions_incorrect": trial_result.get("total", 0) - trial_result.get("score", 0),
    }
    
    # Mastery determination
    if stats["percentage"] >= 90:
        stats["mastery_level"] = "Expert"
        stats["recommendation"] = "Ready for more advanced material"
    elif stats["percentage"] >= 75:
        stats["mastery_level"] = "Proficient"
        stats["recommendation"] = "Good progress; continue review"
    elif stats["percentage"] >= 60:
        stats["mastery_level"] = "Developing"
        stats["recommendation"] = "More practice needed on weak areas"
    else:
        stats["mastery_level"] = "Beginner"
        stats["recommendation"] = "Review fundamentals; repeat this trial"
    
    return stats


# Example usage:
if __name__ == "__main__":
    # Create a system for 100 questions
    system = ThirteenTrialLearningSystem("Math 102", 100)
    plan = system.generate_trial_plan()
    
    print("13-Trial Learning Plan Generated")
    print("=" * 50)
    print(json.dumps(plan["metadata"], indent=2))
    print("\nTrial Breakdown:")
    for trial_num, trial_data in plan["trials"].items():
        print(f"\nTrial {trial_num}: {trial_data['purpose']}")
        print(f"  New Questions: {len(trial_data['new_questions'])}")
        print(f"  Review Questions: {len(trial_data['review_questions'])}")
        print(f"  Total This Trial: {trial_data['total_questions_in_trial']}")
        print(f"  Repetition Intensity: {trial_data['repetition_count']}x")
