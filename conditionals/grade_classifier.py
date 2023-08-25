# dictionary of student_id -> score

student_score = {
    "1" : 80,
    "2" : 50,
    "3" : 92,
    "4" : 70,
    "5" : 74,
    "6" : 68,
    "7" : 80,
    "8" : 82,
}

MIN_PASSING_SCORE = 70

def is_passing_score(score):
    """Returns True if the score is passing"""
    return score >= MIN_PASSING_SCORE

def build_pass_fail_dictionary(scores):
    """Build dictionary of passing and failing id lists"""

    pass_fail_dictionary = {
        "passing": [],
        "failing": []
    }
    for student_id in scores:
        if is_passing_score(scores[student_id]):
            pass_fail_dictionary['passing'].append(student_id)
        else:
            pass_fail_dictionary['failing'].append(student_id)
    
    return pass_fail_dictionary

report = build_pass_fail_dictionary(student_score)
print(report)