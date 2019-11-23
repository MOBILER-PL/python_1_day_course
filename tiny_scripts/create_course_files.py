import os
import re

course_title = "Python: Code, Test, Deploy"

with open('sections.txt','r') as infile:
    sections = [a.strip().split(";") for a in infile.readlines()if a]
    for count, section in enumerate(sections):
        if section:
            file_name = section[0]
            clean_file = re.sub("[^A-Za-z\s]"," ", file_name).replace(" ","_")
            path = f"{count}_{clean_file}.md"
            contents = f"## Python: Code, Test, Deploy\n\n# {file_name}\n ---\n\n# Synopsis\n\n"
            os.system(f"touch {path}")
            with open(path, 'w') as infile:
                infile.write(contents)