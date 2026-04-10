def analyze_text_file(filename):
    # 1. Read file
    file = open(filename, "r")
    content = file.read()
    file.close()

    
    words = []
    temp_word = ""
    for char in content:
        if char == " " or char == "\n" or char == "\t":
            if temp_word != "":
                words = words + [temp_word]
                temp_word = ""
        else:
            temp_word = temp_word + char
    if temp_word != "":
        words = words + [temp_word]

    # 2. total length
    total_chars = 0
    for char in content:
        total_chars = total_chars + 1

    word_counts = {}
    largest_word = ""
    max_len = 0

    for w in words:
        # Word Occurrence Count
        if w in word_counts:
            word_counts[w] = word_counts[w] + 1
        else:
            word_counts[w] = 1
        
        # Largest Word 
        curr_word_len = 0
        for char in w:
            curr_word_len = curr_word_len + 1
        
        if curr_word_len > max_len:
            max_len = curr_word_len
            largest_word = w

    # 3. Reverse Largest Word
    rev_word = ""
    for char in largest_word:
        rev_word = char + rev_word

    
    print("Total character length: " + str(total_chars))
    print("\nRepeated Words:")
    for w in word_counts:
        if word_counts[w] > 1:
            print(w + ": " + str(word_counts[w]) + " times")

    print("\nLargest word: " + largest_word)
    print("Reversed largest word: " + rev_word)
analyze_text_file("input.txt")
