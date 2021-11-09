with open('text.txt') as file:
    line_chr = ['-', ',', '.', '!', '?']
    line = file.readline().strip()
    i = 0
    while line:
        if i % 2 == 0:
            if i % 2 == 0:
                for chr in line_chr:
                    line = line.replace(chr, '@')
                print(" ".join(line.split()[::-1]))
        i += 1
        line = file.readline()


