import os 
directory = "Labs/Lab_3/4/texts"
files = sorted(
    os.listdir(directory)
)
with open("merged.txt", "w") as outfile:
    for filename in files:
        if filename.endswith(".txt"):
            filepath = os.path.join(
                directory, filename
            )
            with open(filepath, "r") as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write("==== end of file ====\n")
print("Files merged into merged.txt")