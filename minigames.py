import random
import sys

def guess_number():
    print("\n=== Угадай число ===")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Угадай число от 1 до 100: "))
            attempts += 1
            
            if guess < number:
                print("Слишком маленькое!")
            elif guess > number:
                print("Слишком большое!")
            else:
                print(f"Поздравляю! Ты угадал за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, вводи только числа!")

def hangman():
    print("\n=== Виселица ===")
    words = ["питон", "программа", "виселица", "игра", "код"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []
    
    while attempts > 0 and "_" in guessed:
        print("\nСлово:", " ".join(guessed))
        print("Осталось попыток:", attempts)
        print("Использованные буквы:", ", ".join(used_letters))
        
        letter = input("Введи букву: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введи одну букву!")
            continue
            
        if letter in used_letters:
            print("Ты уже использовал эту букву!")
            continue
            
        used_letters.append(letter)
        
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
        else:
            print("Такой буквы нет!")
            attempts -= 1
    
    if "_" not in guessed:
        print("\nПоздравляю! Ты угадал слово:", word)
    else:
        print("\nТы проиграл! Загаданное слово было:", word)

def tic_tac_toe():
    print("\n=== Крестики-нолики ===")
    board = [" "] * 9
    players = ["X", "O"]
    current_player = 0
    
    def print_board():
        print("\n")
        for i in range(0, 9, 3):
            print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
            if i < 6:
                print("-----------")
    
    def check_winner():
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикали
            [0, 4, 8], [2, 4, 6]              # диагонали
        ]
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != " ":
                return True
        return False
    
    while True:
        print_board()
        print(f"\nХод игрока {players[current_player]}")
        
        try:
            move = int(input("Выбери клетку (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Пожалуйста, выбери число от 1 до 9!")
                continue
                
            if board[move] != " ":
                print("Эта клетка уже занята!")
                continue
                
            board[move] = players[current_player]
            
            if check_winner():
                print_board()
                print(f"\nИгрок {players[current_player]} победил!")
                break
                
            if " " not in board:
                print_board()
                print("\nНичья!")
                break
                
            current_player = 1 - current_player
        except ValueError:
            print("Пожалуйста, вводи только числа!")

def main():
    while True:
        print("\n=== Меню мини-игр ===")
        print("1. Угадай число")
        print("2. Виселица")
        print("3. Крестики-нолики")
        print("4. Выход")
        
        choice = input("Выбери игру (1-4): ")
        
        if choice == "1":
            guess_number()
        elif choice == "2":
            hangman()
        elif choice == "3":
            tic_tac_toe()
        elif choice == "4":
            print("До свидания!")
            sys.exit()
        else:
            print("Неверный выбор. Попробуй еще раз.")

if __name__ == "__main__":
    main()