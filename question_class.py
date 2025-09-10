# question_class.py
"""handles the Question class to avoid circular import error"""

class Question:
    """Class representing a quiz question"""
    def __init__(self, level, content, options, right_answer):
        self.level = level
        self.content = content
        self.options = options
        self.right_answer = right_answer

    def __repr__(self):
        return f"""
        This question is for level {self.level} and
        """
