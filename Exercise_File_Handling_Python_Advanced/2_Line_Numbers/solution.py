with open("text.txt") as file, open("output.txt", 'w') as result:
    set_chr = {'!', '?', ',', '.', 45, '_', "'", ';', ':', '"'}
    count_line = 0
    for line in file:
        count_line += 1
        character_count = 0
        punctuation_count = 0
        for chr in line:
            if chr in set_chr or ord(chr) in set_chr: punctuation_count += 1
            elif 65 <= ord(chr) <= 90 or 97 <= ord(chr) <= 122: character_count += 1

        result.write(f"Line {count_line}: {line.strip()} ({character_count})({punctuation_count})")
        result.write('\n')
