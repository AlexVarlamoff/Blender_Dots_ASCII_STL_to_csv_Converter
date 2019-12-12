import os

#last row deleting
with open("salesforce.txt", "r") as f:
    data = f.readlines()
data = filter(lambda line: "endsolid" not in line, data)
with open("text.txt", "w") as f:
    f.write("".join(data))

#replacement
replacements = {'outer loop' :'', 'endloop' :'', 'endfacet' :'', 'solid Exported from Blender-2.81 (sub 16)' :'x y z', 'vertex ' :'' , ' ' :' '}

with open('text.txt') as infile, open('text1.txt', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)

#empty rows deleting
with open('text1.txt', 'r') as inf, open('text.txt', 'w') as out:
    for line in inf:
        if line.strip():
            out.write(line)

with open("text.txt", "r") as f:
    data = f.readlines()
#deleting rows
data = filter(lambda line: "facet" not in line, data)
with open("text1.txt", "w") as f:
    f.write("".join(data))

#string numbers
with open('text1.txt', 'r') as read_object, open('text.txt', 'w') as write_object:
    for idx, line in enumerate(read_object, start=0):
        write_object.write('{} {}'. format(idx, line))

#remove 2nd file
os.remove('text1.txt')
