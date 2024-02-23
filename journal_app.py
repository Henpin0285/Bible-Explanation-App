import json
import os

# Path to the JSON file
json_file_path = "C:/Users/henry/Documents/Project Foster Farm Family House/Journal Project JSON(Personal)/bible_explanations.json"

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

    # Sort the list by date before saving
    bible_explanations.sort(key=lambda x: x.get('date', ''))

    # Save data immediately after each operation
    save_to_file()

def modify_explanation():
    view_explanations()  # Display explanations for user reference
    if not bible_explanations:
        print("No explanations available to modify.")
        return
    
    try:
        index_to_modify = int(input("Enter the index of the explanation to modify: "))
        if 1 <= index_to_modify <= len(bible_explanations):
            explanation_to_modify = bible_explanations[index_to_modify - 1]

            print("Current explanation:")
            print(explanation_to_modify)

            # Get new values for the explanation
            explanation_to_modify["book"] = input("Enter the new book of the gospel (press enter to keep current value): ") or explanation_to_modify["book"]
            explanation_to_modify["chapter"] = input("Enter the new chapter of the gospel (press enter to keep current value): ") or explanation_to_modify["chapter"]
            explanation_to_modify["verse"] = input("Enter the new verse of the gospel (press enter to keep current value): ") or explanation_to_modify["verse"]
            explanation_to_modify["headline"] = input("Enter a new headline for the explanation (press enter to keep current value): ") or explanation_to_modify["headline"]
            explanation_to_modify["message1"] = input("Enter new message 1 (press enter to keep current value): ") or explanation_to_modify["message1"]
            explanation_to_modify["bodymessage1"] = input("Enter the new explanation for message 1 (press enter to keep current value): ") or explanation_to_modify["bodymessage1"]
            explanation_to_modify["message2"] = input("Enter new message 2 (press enter to keep current value): ") or explanation_to_modify["message2"]
            explanation_to_modify["bodymessage2"] = input("Enter the new explanation for message 2 (press enter to keep current value): ") or explanation_to_modify["bodymessage2"]
            explanation_to_modify["message3"] = input("Enter new message 3 (press enter to keep current value): ") or explanation_to_modify["message3"]
            explanation_to_modify["bodymessage3"] = input("Enter the new explanation for message 3 (press enter to keep current value): ") or explanation_to_modify["bodymessage3"]
            explanation_to_modify["date"] = input("Enter the new date (press enter to keep current value): ") or explanation_to_modify["date"]

            print("Explanation modified successfully.")
            save_to_file()  # Save changes after modification
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Print modified explanation
    print("Modified explanation:")
    print(explanation_to_modify)

    # Save changes to file
    save_to_file()
    print("Explanation modified successfully.")

def save_to_file():
    with open(json_file_path, "w") as file:
        # Sort explanations by date before saving
        sorted_explanations = sorted(bible_explanations, key=lambda x: x.get('date', ''))
        json.dump(sorted_explanations, file)

    print("Explanations saved to file.")    

def view_explanations():
    if not bible_explanations:
        print("No explanations available.")
    else:
        # Sort explanations by date
        sorted_explanations = sorted(bible_explanations, key=lambda x: x.get('date', ''))
        
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

def search_explanations():
    keyword = input("Enter keyword, book, chapter, or verse to search: ").lower()
    matching_explanations = []

    for explanation in bible_explanations:
        if (
            keyword in explanation["book"].lower() or
            keyword in explanation["chapter"].lower() or
            keyword in explanation["verse"].lower() or
            any(keyword in msg.lower() for msg in [explanation["message1"], explanation["message2"], explanation["message3"]]) or
            any(keyword in body_msg.lower() for body_msg in [explanation["bodymessage1"], explanation["bodymessage2"], explanation["bodymessage3"]])
        ):
            matching_explanations.append(explanation)

    if not matching_explanations:
        print("No matching explanations found.")
        return

    print("\n*** Matching Explanations ***")
    for idx, explanation in enumerate(matching_explanations, start=1):
        print(f"{idx}. Date: {explanation.get('date', 'N/A')}")
        print(f"   Book: {highlight_keyword(explanation.get('book', 'N/A'), keyword)}, "
              f"Chapter: {highlight_keyword(explanation.get('chapter', 'N/A'), keyword)}, "
              f"Verse: {highlight_keyword(explanation.get('verse', 'N/A'), keyword)}")
        print(f"   Headline: {highlight_keyword(explanation.get('headline', 'N/A'), keyword)}")

        # Print messages and their bodies with checks
        print(f"   Message 1: {highlight_keyword(explanation.get('message1', 'N/A'), keyword)}")
        print(f"   Body for Message 1: {highlight_keyword(explanation.get('bodymessage1', 'N/A'), keyword)}")

        print(f"   Message 2: {highlight_keyword(explanation.get('message2', 'N/A'), keyword)}")
        print(f"   Body for Message 2: {highlight_keyword(explanation.get('bodymessage2', 'N/A'), keyword)}")

        print(f"   Message 3: {highlight_keyword(explanation.get('message3', 'N/A'), keyword)}")
        print(f"   Body for Message 3: {highlight_keyword(explanation.get('bodymessage3', 'N/A'), keyword)}")

        print()
        
def highlight_keyword(text, keyword):
    highlighted_text = "\033[1;31m"  # ANSI escape code for bold red text
    reset_format = "\033[0m"  # ANSI escape code to reset text formatting

    # Use case-insensitive search for highlighting
    keyword_lower = keyword.lower()
    index = text.lower().find(keyword_lower)

    if index != -1:
        return text[:index] + highlighted_text + text[index:index + len(keyword)] + reset_format + text[index + len(keyword):]

    return text

# Load explanations from file (if any) when the program starts
load_explanations()

# Create Main Menu and Integrate Functions
while True:
    print("1. Add Explanation")
    print("2. View Explanations")
    print("3. Save Explanations to file")
    print("4. Delete Explanation")
    print("5. Modify Explanation")
    print("6. Search Explanations")
    print("7. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6/7): ")
    
    if choice == "1":
        add_explanation()
    elif choice == "2":
        view_explanations()
    elif choice == "3":
        save_explanations()
    elif choice == "4":
        delete_explanation()
    elif choice == "5":
        modify_explanation()
    elif choice == "6":
        search_explanations()
    elif choice == "7":
        print("Exiting the Bible explanation application.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, 6, or 7.")