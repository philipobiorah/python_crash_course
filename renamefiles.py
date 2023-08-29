## Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
#To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for file in filenames:
    
    if file.endswith(".hpp"):
        new = file.replace(".hpp", ".h")
        newfilenames.append(new)

    else:
        newfilenames.append(file)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
