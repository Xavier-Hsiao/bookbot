def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = count_words(text)
  chars_dict = count_chars(text)
  chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} was found")
  print()

  for item in chars_sorted_list:
    if not item["char"].isalpha():
      continue
    print(f"The {item['char']} character was found {item['num']} times")
  
  print("--- End report ---")

# Read the file
def get_book_text(path):
  with open(path) as f:
    return f.read()

# Count the words of a text
def count_words(text):
  # Split the text into a list of words
  words = text.split()
  return len(words)

# Count the characters of a text
def count_chars(text):
  lowered_string = text.lower()
  chars_count = {}

  for char in lowered_string:
    # Check if the character is already in the dictionnary
    if char in chars_count:
      chars_count[char] += 1
    else:
      chars_count[char] = 1

  return chars_count

def sort_on(dict):
  return dict["num"]

# Sort the dict alphabatically
def chars_dict_to_sorted_list(char_dict):
  sorted_list = []

  for char in char_dict:
    sorted_list.append({"char": char, "num": char_dict[char]})

  sorted_list.sort(reverse=True, key=sort_on)

  return sorted_list

main()

