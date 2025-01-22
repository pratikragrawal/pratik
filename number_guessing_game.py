import tkinter as tk
from tkinter import messagebox, ttk
import random

class NumberGuessingGame:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.best_score = None  # To track the best score
        
        # Game state variables
        self.target_number = None
        self.attempts = 0
        
        # Create UI components
        self.create_start_screen()
    
    def create_start_screen(self):
        """Display the start screen with game options."""
        self.clear_window()
        tk.Label(self.root, text="Welcome to the Number Guessing Game!", 
                 font=("Arial", 16, "bold")).pack(pady=20)
        
        tk.Label(self.root, text="Choose a difficulty level to start:", font=("Arial", 14)).pack(pady=10)
        
        # Difficulty level buttons
        tk.Button(self.root, text="Easy (1-50)", font=("Arial", 12), command=lambda: self.start_game(50)).pack(pady=5)
        tk.Button(self.root, text="Medium (1-100)", font=("Arial", 12), command=lambda: self.start_game(100)).pack(pady=5)
        tk.Button(self.root, text="Hard (1-200)", font=("Arial", 12), command=lambda: self.start_game(200)).pack(pady=5)
        
        if self.best_score:
            tk.Label(self.root, text=f"Best Score: {self.best_score} attempts", font=("Arial", 12), fg="green").pack(pady=20)
    
    def start_game(self, max_number):
        """Start the game with the selected difficulty."""
        self.target_number = random.randint(1, max_number)
        self.max_number = max_number
        self.attempts = 0
        self.create_game_screen()
    
    def create_game_screen(self):
        """Display the main game screen."""
        self.clear_window()
        
        tk.Label(self.root, text=f"Guess a number between 1 and {self.max_number}", 
                 font=("Arial", 14)).pack(pady=20)
        
        self.entry = ttk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)
        
        tk.Button(self.root, text="Check", font=("Arial", 12), command=self.check_guess).pack(pady=10)
        
        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.feedback_label.pack(pady=10)
        
        self.attempt_label = tk.Label(self.root, text="Attempts: 0", font=("Arial", 12), fg="purple")
        self.attempt_label.pack(pady=10)
        
        tk.Button(self.root, text="Restart Game", font=("Arial", 12), command=self.create_start_screen).pack(pady=20)
    
    def check_guess(self):
        """Handle user guess and provide feedback."""
        try:
            guess = int(self.entry.get())
            
            if guess < 1 or guess > self.max_number:
                self.feedback_label.config(text=f"Please enter a number between 1 and {self.max_number}.", fg="red")
                return
            
            self.attempts += 1
            self.attempt_label.config(text=f"Attempts: {self.attempts}")
            
            if guess < self.target_number:
                self.feedback_label.config(text="Too Low! Try again.", fg="blue")
            elif guess > self.target_number:
                self.feedback_label.config(text="Too High! Try again.", fg="blue")
            else:
                self.feedback_label.config(text="Correct! You guessed it!", fg="green")
                self.end_game()
        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a number.", fg="red")
    
    def end_game(self):
        """Handle end-of-game logic and display results."""
        if self.best_score is None or self.attempts < self.best_score:
            self.best_score = self.attempts
        
        messagebox.showinfo("Congratulations!", 
                            f"You guessed the number in {self.attempts} attempts!")
        self.create_start_screen()
    
    def clear_window(self):
        """Clear all widgets from the current window."""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

