import os
file_dir ="txt_files"


lines_list = []
with open("poem.txt.txt","r", encoding="utf-8") as file:
    for line in file.readlines():
        print(line, end="")
        if line.endswith(",\n") or line.endswith(",") :
            new_line = line.replace(",","")
            lines_list.append(new_line)
        else:

            lines_list.append(line)

print(lines_list)

with open("new_poem.txt", "w", encoding="utf-8") as file:

    poem = "".join(lines_list)
    file.write(poem)

with open("new_poem.txt", "a", encoding="utf-8") as file:

    file.write("\nВ.Б")


