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
        matches = [word for word in words 
                  if current_letters in word.lower() and word not in used_words]
        if matches:
            print("Matches found:")
            print(", ".join(matches[:10]))  # Show first 10 matches
            if len(matches) > 10:
                print(f"...and {len(matches)-10} more")
        else:
            print("No matches found")