# questions.py
"""this file include all 15 question objects for the quiz"""
from question_class import Question

question_1 = Question(
    level=1,
    content="1. What is the holy book of Islam?",
    options={
        "a": "A) Bible",
        "b": "B) Torah",
        "c": "C) Quran",
        "d": "D) Zabur"
    },
    right_answer="c"
)
question_2 = Question(
    level=2,
    content="2. Who is the last prophet in Islam?",
    options={
        "a": "A) Prophet Musa (Moses)",
        "b": "B) Prophet Isa (Jesus)",
        "c": "C) Prophet Muhammad (PBUH)",
        "d": "D) Prophet Ibrahim (Abraham)"
    },
    right_answer="c"
)
question_3 = Question(
    level=3,
    content="3. In which city was Prophet Muhammad (PBUH) born?",
    options={
        "a": "A) Medina",
        "b": "B) Mecca",
        "c": "C) Jerusalem",
        "d": "D) Ta'if"
    },
    right_answer="b"
)
question_4 = Question(
    level=4,
    content="4. What is the name of the journey from Mecca to Medina?",
    options={
        "a": "A) Isra",
        "b": "B) Hijrah",
        "c": "C) Mi’raj",
        "d": "D) Umrah"
    },
    right_answer="b"
)
question_5 = Question(
    level=5,
    content="5. What is the name of Prophet Muhammad’s father?",
    options={
        "a": "A) Abu Talib",
        "b": "B) Abdullah",
        "c": "C) Abdul Muttalib",
        "d": "D) Hamza"
    },
    right_answer="b"
)
question_6 = Question(
    level=6,
    content="6. Who was the first person to accept Islam?",
    options={
        "a": "A) Abu Bakr (RA)",
        "b": "B) Khadijah (RA)",
        "c": "C) Ali ibn Abi Talib (RA)",
        "d": "D) Bilal ibn Rabah (RA)"
    },
    right_answer="b"
)
question_7 = Question(
    level=7,
    content="7. How old was Prophet Muhammad (PBUH) when he received the first revelation?",
    options={
        "a": "A) 25",
        "b": "B) 30",
        "c": "C) 35",
        "d": "D) 40"
    },
    right_answer="d"
)
question_8 = Question(
    level=8,
    content="8. Who was the Prophet’s uncle that supported him in Mecca?",
    options={
        "a": "A) Abu Lahab",
        "b": "B) Abu Talib",
        "c": "C) Hamza ibn Abdul Muttalib",
        "d": "D) Abbas ibn Abdul Muttalib"
    },
    right_answer="b"
)
question_9 = Question(
    level=9,
    content="9. Which angel brought the revelation to Prophet Muhammad (PBUH)?",
    options={
        "a": "A) Angel Israfil",
        "b": "B) Angel Mikail",
        "c": "C) Angel Jibreel (Gabriel)",
        "d": "D) Angel Malik"
    },
    right_answer="c"
)
question_10 = Question(
    level=10,
    content="10. What was the first word revealed to Prophet Muhammad (PBUH)?",
    options={
        "a": "A) Pray",
        "b": "B) Read (Iqra)",
        "c": "C) Believe",
        "d": "D) Worship"
    },
    right_answer="b"
)
question_11 = Question(
    level=11,
    content="11. What is the event of Isra and Mi’raj?",
    options={
        "a": "A) Prophet’s migration to Medina",
        "b": "B) Prophet’s night journey and ascension to the heavens",
        "c": "C) Prophet’s first revelation",
        "d": "D) Prophet’s last sermon"
    },
    right_answer="b"
)
question_12 = Question(
    level=12,
    content="12. Which battle was the first major battle fought by Muslims?",
    options={
        "a": "A) Battle of Uhud",
        "b": "B) Battle of the Trench",
        "c": "C) Battle of Badr",
        "d": "D) Battle of Hunayn"
    },
    right_answer="c"
)
question_13 = Question(
    level=13,
    content="13. What was the Prophet’s title given by the Quraysh before Prophethood?",
    options={
        "a": "A) Al-Mu’allim (The Teacher)",
        "b": "B) Al-Muhtadi (The Guided One)",
        "c": "C) Al-Ameen (The Trustworthy)",
        "d": "D) Al-Faruq (The One Who Distinguishes)"
    },
    right_answer="c"
)
question_14 = Question(
    level=14,
    content="14. What is the name of the treaty signed between Muslims and Quraysh in 628 CE?",
    options={
        "a": "A) Treaty of Hudaybiyyah",
        "b": "B) Treaty of Ta’if",
        "c": "C) Treaty of Medina",
        "d": "D) Treaty of Mecca"
    },
    right_answer="a"
)
question_15 = Question(
    level=15,
    content="15. In which year did Prophet Muhammad (PBUH) deliver his Farewell Sermon?",
    options={
        "a": "A) 5 AH",
        "b": "B) 8 AH",
        "c": "C) 10 AH",
        "d": "D) 12 AH"
    },
    right_answer="c"
)

quiz_questions = [
    question_1,
    question_2,
    question_3,
    question_4,
    question_5,
    question_6,
    question_7,
    question_8,
    question_9,
    question_10,
    question_11,
    question_12,
    question_13,
    question_14,
    question_15
    ]
