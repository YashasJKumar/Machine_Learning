import matplotlib.pyplot as plt
import json
from datetime import datetime

# File to store the data
data_file = 'dsa_progress.json'


def load_data():
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file)


def update_progress(solved_problems):
    data = load_data()
    current_date = datetime.now().strftime('%Y-%m-%d')
    data.append({'date': current_date, 'solved': solved_problems})
    save_data(data)


def plot_progress():
    data = load_data()
    if not data:
        print("No data to plot.")
        return

    dates = [entry['date'] for entry in data]
    solved = [entry['solved'] for entry in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, solved, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Number of Problems Solved')
    plt.title('DSA Problems Solved Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    while True:
        choice = input("Enter 'u' to update progress, 'p' to plot progress, or 'q' to quit: ").lower()
        if choice == 'u':
            solved_problems = int(input("Enter the number of problems solved: "))
            update_progress(solved_problems)
        elif choice == 'p':
            plot_progress()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please enter 'u', 'p', or 'q'.")