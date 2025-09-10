#entry_point.py
"""Entry point for the U_Think_U_know_Islam quiz"""
from quiz_logic import Player, MAX_LEVEL

while True:
    print("Welcome to the 'U Think U know Islam' quiz!")
    print("1. Start Quiz")
    print("2. Exit")
    choice = input("Please Enter your option (1 or 2): ")
    if choice == '2':
        print("Thank you for visiting! Goodbye!")
        break
    elif choice == '1':
        player_name = input("Enter your name: ")
        new_player = Player(player_name)
        new_player.start_quiz()
        for q in new_player.quiz.questions:
            while True:
                print(f"{q.content}")
                for option in q.options.values():
                    print(option)
                player_answer = input("Enter your answer code 'a, b, c, or d': ")
                if player_answer.lower() == q.right_answer and q.level != MAX_LEVEL:
                    new_player.answer_right()
                    break
                elif player_answer.lower() == q.right_answer and q.level == MAX_LEVEL:
                    new_player.won()
                    break
                # make sure after the player says he want to continue, the right question is displayed
                elif player_answer.lower() in ['exit', 'quit']:
                    player_conf = new_player.end_quiz()
                    if player_conf in ['yes', 'y']:
                        break
                    else:
                        continue
                else:
                    new_player.answer_wrong()
                    break

    else:
        print("Invalid option. Please try again.")
        continue
