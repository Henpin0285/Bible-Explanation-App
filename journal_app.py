import json
import os

# Path to the JSON file
json_file_path = "C:/Users/henry/OneDrive/Desktop/Project Foster Farm Family House/Journal Project JSON(Personal)/bible_explanations.json"

# Check if the JSON file exists
if os.path.exists(json_file_path):
    # If it exists, load data from the file
    with open(json_file_path, "r") as file:
        bible_explanations = json.load(file)
else:
    # If it doesn't exist, initialize an empty list
    bible_explanations = []

def add_explanation():
    book = input("Enter the book of the gospel: ")
    chapter = input("Enter the chapter of the gospel: ")
    verse = input("Enter the verse of the gospel: ")
    message1 = input("Enter message 1: ")
    message2 = input("Enter message 2: ")
    message3 = input("Enter message 3: ")

    # Check if a similar explanation already exists based on Book, Chapter, Verse, and Messages
    existing_explanation_indices = [
        idx + 1 for idx, expl in enumerate(bible_explanations)
        if expl["book"] == book and expl["chapter"] == chapter and expl["verse"] == verse
        and expl["message1"] == message1 and expl["message2"] == message2 and expl["message3"] == message3
    ]

    if existing_explanation_indices:
        print("Similar explanation already exists:")
        for idx in existing_explanation_indices:
            print(f"Index: {idx}, Date: {bible_explanations[idx-1]['date']}")

        # Allow user to add the similar explanation with a different date
        while True:
            date = input("Enter a different date for the new explanation (e.g., YYYY-MM-DD): ")
            if any(expl["date"] == date for expl in bible_explanations):
                print("An explanation with the same date already exists. Please choose a different date.")
            else:
                break

        # Find the index of the existing explanation and update the date
        existing_index = existing_explanation_indices[0] - 1
        existing_explanation = bible_explanations[existing_index]
        existing_explanation_copy = existing_explanation.copy()  # Create a copy of the existing entry
        existing_explanation_copy["date"] = date
        bible_explanations.append(existing_explanation_copy)
        print("New date added successfully!")

    else:
        # Check if the date is already used
        while True:
            date = input("Enter the date (e.g., YYYY-MM-DD): ")
            if any(expl["date"] == date for expl in bible_explanations):
                print("An explanation with the same date already exists. Please choose a different date.")
            else:
                break

        explanation = {
            "date": date,
            "book": book,
            "chapter": chapter,
            "verse": verse,
            "headline": input("Enter a headline for the explanation: "),
            "message1": message1,
            "message2": message2,
            "message3": message3,
            "bodymessage1": input("Enter the explanation for message1:\n"),
            "bodymessage2": input("Enter the explanation for message2:\n"),
            "bodymessage3": input("Enter the explanation for message3:\n")
        }

        bible_explanations.append(explanation)
        print("Explanation added successfully!")

    # Save data immediately after each operation
    save_to_file()

def save_to_file():
    with open(json_file_path, "w") as file:
        json.dump(bible_explanations, file)
    print("Explanations saved to file.")
    

def view_explanations():
    if not bible_explanations:
        print("No explanations available.")
    else:
        print("\n*** Bible Explanations ***")
        for idx, explanation in enumerate(bible_explanations, start=1):
            print(f"{idx}. Date: {explanation.get('date', 'N/A')}")
            print(f"   Book: {explanation.get('book', 'N/A')}, Chapter: {explanation.get('chapter', 'N/A')}, "
                  f"Verse: {explanation.get('verse', 'N/A')}")
            print(f"   Headline: {explanation.get('headline', 'N/A')}")

            # Print messages and their bodies with checks
            print(f"   Message 1: {explanation.get('message1', 'N/A')}")
            print(f"   Body for Message 1: {explanation.get('bodymessage1', 'N/A')}")

            print(f"   Message 2: {explanation.get('message2', 'N/A')}")
            print(f"   Body for Message 2: {explanation.get('bodymessage2', 'N/A')}")

            print(f"   Message 3: {explanation.get('message3', 'N/A')}")
            print(f"   Body for Message 3: {explanation.get('bodymessage3', 'N/A')}")

            print()


def save_explanations():
    save_to_file()
    print("Explanations saved to file.")

    
def load_explanations():
    try:
        with open(json_file_path, "r") as file:
            data = json.load(file)

            # Check if an explanation with the same date already exists in memory
            existing_dates = {expl["date"] for expl in bible_explanations}
            new_data = [expl for expl in data if expl["date"] not in existing_dates]

            bible_explanations.extend(new_data)

        print("Explanations loaded from file.")
    except FileNotFoundError:
        print("No saved explanations found.")

def delete_explanation():
    view_explanations()  # Display explanations for user reference
    if not bible_explanations:
        print("No explanations available to delete.")
        return

    try:
        index_to_delete = int(input("Enter the index of the explanation to delete: "))
        if 1 <= index_to_delete <= len(bible_explanations):
            deleted_explanation = bible_explanations.pop(index_to_delete - 1)
            print(f"Deleted the following explanation:\n{deleted_explanation}")
            save_to_file()  # Save changes after deletion
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


# Load explanations from file (if any) when the program starts
load_explanations()

# Create Main Menu and Integrate Functions
while True:
    print("1. Add Explanation")
    print("2. View Explanations")
    print("3. Save Explanations to file")
    print("4. Delete Explanation")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_explanation()
    elif choice == "2":
        view_explanations()
    elif choice == "3":
        save_explanations()
    elif choice == "4":
        delete_explanation()
    elif choice == "5":
        print("Exiting the Bible explanation application.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")