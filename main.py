from keyboard import read_event
from random import choice

# Load word list
def load_words():
    try:
        with open("./config/words.txt", "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        print("Error: words.txt not found in config folder")
        exit(1)

# Initialize
words = load_words()
used_words = set()
print("Type letters to find matches. Press ESC to clear, Ctrl+C to quit.")

current_letters = ""
while True:
    event = read_event()
    
    # Only process key down events to avoid double readings
    if event.event_type != 'down':
        continue
        
    if event.name == 'esc':  # Clear current input
        current_letters = ""
        print("\nCleared input")
    elif event.name == 'backspace':  # Allow deleting letters
        current_letters = current_letters[:-1]
        print(f"\nCurrent letters: {current_letters}")
    elif len(event.name) == 1 and event.name.isalpha():  # Only accept single letters
        current_letters += event.name.lower()
        print(f"\nCurrent letters: {current_letters}")
        
    # Find and display matches (if we have input)
    if current_letters:
        # Split matches into two groups: starts_with and contains
        starts_with = [word for word in words 
                      if word.lower().startswith(current_letters) and word not in used_words]
        # Check if letters appear as an exact sequence somewhere in the word
        contains = [word for word in words 
                   if current_letters in word.lower() 
                   and not word.lower().startswith(current_letters) 
                   and word not in used_words]
        
        if starts_with or contains:
            print("Matches found:")
            # Show starting matches first
            if starts_with:
                print("Starts with:", ", ".join(starts_with[:5]))
            # Then show other matches
            if contains:
                if starts_with:
                    print("Also contains:", ", ".join(contains[:5]))
                else:
                    print("Contains:", ", ".join(contains[:5]))
            
            total_matches = len(starts_with) + len(contains)
            shown_matches = min(5, len(starts_with)) + min(5, len(contains))
            if total_matches > shown_matches:
                print(f"...and {total_matches - shown_matches} more")
        else:
            print("No matches found")