def count_words(text):
    words = text.split()
    return len(words)

def count_char_occurence(text):
    char_occurence = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_occurence:
            char_occurence[lower_char] += 1
        else:
            char_occurence[lower_char] = 1
    return char_occurence

def dict_to_list(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "count": value})
    return dict_list

def sort_on(dict):
    return dict["count"]

def main():
    book_file_name = "books/frankenstein.txt"
    with open(book_file_name) as f:
      file_contents = f.read()
      
      book_stats = dict_to_list(count_char_occurence(file_contents))
      book_stats.sort(reverse=True, key=sort_on)

      print(f"Begin report of {book_file_name}")
      print(f"Number of words: {count_words(file_contents)}")
      for stat in book_stats:
          if stat["char"].isalpha():
              print(f"Character '{stat["char"]}' appears {stat["count"]} times")

      print("End of report")

main()
