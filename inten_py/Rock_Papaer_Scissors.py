import random
import tkinter as tk

game_schema = {
    "Rock": {"Rock": "Draw", "Paper": "Computer", "Scissor": "Player"},
    "Paper": {"Rock": "Player", "Paper": "Draw", "Scissor": "Computer"},
    "Scissor": {"Rock": "Computer", "Paper": "Player", "Scissor": "Draw"}
}

computer_score = 0
player_score = 0

def handle_outcome(player_choice):
    global computer_score, player_score
    
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(choices)
    
    result = game_schema[player_choice][computer_choice]
    
    player_choice_label.config(fg="#2e8b57", text="Player Choice: " + player_choice)
    computer_choice_label.config(fg="#8b0000", text="Computer Choice: " + computer_choice)
    
    if result == "Player":
        player_score += 1
        player_score_label.config(text="Player Score: " + str(player_score))
        outcome_label.config(fg="#1e90ff", text="Outcome: Player Won")
    elif result == "Computer":
        computer_score += 1
        computer_score_label.config(text="Computer Score: " + str(computer_score))
        outcome_label.config(fg="#1e90ff", text="Outcome: Computer Won")
    else:
        outcome_label.config(fg="#1e90ff", text="Outcome: Draw")

app = tk.Tk()
app.title("Rock Paper Scissors Game")
app.geometry("450x400")
app.resizable(False, False)

tk.Label(app, text="Rock, Paper, Scissors", font="Arial 16 bold", bg="#f0f8ff").pack(pady=20)

frame_scores = tk.Frame(app, bg="#f0f8ff")
frame_scores.pack(pady=10)

player_score_label = tk.Label(frame_scores, text="Player Score: 0", font="Arial 12", bg="#e6e6fa")
player_score_label.grid(row=0, column=0, padx=20, pady=5)

computer_score_label = tk.Label(frame_scores, text="Computer Score: 0", font="Arial 12", bg="#ffe4e1")
computer_score_label.grid(row=0, column=1, padx=20, pady=5)

frame_choices = tk.Frame(app, bg="#f0f8ff")
frame_choices.pack(pady=10)

player_choice_label = tk.Label(frame_choices, text="Player Choice: ", font="Arial 12", bg="#fafad2")
player_choice_label.grid(row=0, column=0, padx=20, pady=5)

computer_choice_label = tk.Label(frame_choices, text="Computer Choice: ", font="Arial 12", bg="#fafad2")
computer_choice_label.grid(row=0, column=1, padx=20, pady=5)

outcome_label = tk.Label(app, text="Outcome: ", font="Arial 12", bg="#d3d3d3")
outcome_label.pack(pady=10)
tk.Label(app, text="Select an option:", font="Arial 12", bg="#f0f8ff").pack(pady=10)

frame_buttons = tk.Frame(app, bg="#f0f8ff")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Rock", width=15, command=lambda: handle_outcome("Rock"), bg="#b0e0e6").grid(row=0, column=0, padx=10, pady=5)
tk.Button(frame_buttons, text="Paper", width=15, command=lambda: handle_outcome("Paper"), bg="#ffb6c1").grid(row=0, column=1, padx=10, pady=5)
tk.Button(frame_buttons, text="Scissor", width=15, command=lambda: handle_outcome("Scissor"), bg="#98fb98").grid(row=0, column=2, padx=10, pady=5)

app.configure(bg="#f0f8ff")

app.mainloop()
