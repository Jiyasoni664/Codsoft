import tkinter as tk
import random

def play(choice):
    choices = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(choices)

    computer_label.config(text=f"Computer: {computer_choice}")
    player_label.config(text=f"Player: {choice}")

    if choice == computer_choice:
        result_label.config(text="It's a Tie!",fg="blue")
    elif (choice == "Rock" and computer_choice == "Scissors") or \
        (choice == "Paper" and computer_choice == "Rock") or \
        (choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You Win!",fg="green")

    else:
        result_label.config(text="You Lose!",fg="red")

root = tk.Tk()
root.title("Rock paper Scissors")
root.geometry("400x400")
root.config(bg="lightyellow")

tk.Label(root,text="Rock paper Scissors",font=("Arial", 20, "bold"), bg="lightyellow").pack(pady=10)

player_label = tk.Label(root,text="Player: ",font=("Arial",14),bg="lightyellow")
player_label.pack()

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 14), bg="lightyellow")
computer_label.pack()

result_label = tk.Label(root,text="",font=("Arial",16,"bold"),bg="lightyellow")
result_label.pack(pady=10)

button_frame = tk.Frame(root,bg="lightyellow")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame,text="Rock",font=("Arial",14),width=10,command=lambda:play("Rock"))
rock_btn.grid(row=0,column=0,padx=5)

paper_btn = tk.Button(button_frame,text="Paper",font=("Arial",14),width=10,command=lambda:play("Paper"))
paper_btn.grid(row=0,column=1,padx=5)

scissors_btn = tk.Button(button_frame,text="Scissors",font=("Arial",14),width=10,command=lambda:play("Scissors"))
scissors_btn.grid(row=0,column=2,padx=5)

root.mainloop()
          
          
          