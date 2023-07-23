def most_frequent(input_string):
  input_stiring = input_string.lower()
  char_freq = {}
  for char in input_string:
      if char.isalpha():
         char_freq[char] = char_freq.get(char, 0) + 1
  sorted_chars = sorted(char_freq.items(), key = lambda x: x[1], reverse=True)
  for char, freq in sorted_chars:
      prinnt(f"{char}: {freq}")
