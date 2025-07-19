import random

def ask_questions():
    questions = {
        "name": "What is your name? ",
        "age": "How old are you? ",
        "color": "What is your favorite color? ",
        "food": "What is your favorite food? ",
        "city": "Which city do you live in? ",
        "shs": "Which SHS did you attend? ",
        "team": "What is your favorite soccer team? "
    }

    user_data = {}

    # Randomize question order
    question_keys = list(questions.keys())
    random.shuffle(question_keys)

    for key in question_keys:
        user_data[key] = input(questions[key])

    return user_data

def show_summary(data):
    print("\n--- 🎉 Here is your personalized summary! 🎉 ---\n")
    print(f"Hello, {data['name']}!")
    print(f"You are {data['age']} years old, love the color {data['color']}, and enjoy eating {data['food']}.")
    print(f"Life must be awesome in {data['city']}!")
    print(f"You attended {data['shs']} and support {data['team']} in football.")
    print("\n---------------------------------------------\n")

def save_to_file(data, rating):
    filename = f"{data['name']}.txt"
    with open(filename, 'w') as f:
        f.write(f"Name: {data['name']}\n")
        f.write(f"Age: {data['age']}\n")
        f.write(f"Favorite Color: {data['color']}\n")
        f.write(f"Favorite Food: {data['food']}\n")
        f.write(f"City: {data['city']}\n")
        f.write(f"SHS Attended: {data['shs']}\n")
        f.write(f"Favourite Team: {data['team']}\n")
        f.write(f"Rating: {rating}/5 stars\n")
    print(f"✔ Summary saved as '{filename}'")

def main():
    while True:
        data = ask_questions()
        show_summary(data)

        save_choice = input("Would you like to save this summary to a file? (yes/no): ").strip().lower()
        if save_choice == 'yes':
            while True:
                try:
                    rating = int(input("How would you rate this assistant? (1-5 stars): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                except ValueError:
                    print("Please enter a valid number.")
            save_to_file(data, rating)

        restart = input("\nWould you like to restart the process? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
