# Author Rico Magnucki

import os

input_file = "sampleinput.md"

question_start = "\\begin{karte}{"
question_end = "\n\end{karte}\n"
usepackage = "\\usepackage{"
usepackage_parameter =  "\\usepackage["
parameter_package_divider = "]{"

closing_brace = "}\n"

packages = [("inputenc", "utf8"), ("fontenc", "T1"), ("libertine","")]

documentclass = "\documentclass[a7paper,grid=rear]{Kartei/kartei}\n"

tex_file = open("flashcards.tex", "w")
input_file = "sampleinput.md"


def init_tex():
    tex_file.write(documentclass)
    load_packages()
    tex_file.write("\\begin{document}\n")


def close_tex():
    tex_file.write("\end{document}")
    tex_file.close()

def load_packages():
     for package in packages:
         tex_file.write(build_package_statement(package[1],package[0]))

def build_package_statement(parameter, packagename):
    if parameter:
        return usepackage_parameter + parameter + parameter_package_divider + packagename + closing_brace
    else:
        return usepackage + packagename + closing_brace


init_tex()
with open(input_file) as input:
    content = input.readlines()

    for string in content:
        if (string.startswith("* ")):
            tex_file.write(question_start + string.strip('* \n') + closing_brace)
        if (string.startswith("_")):
            tex_file.write(string.strip('_\n') + question_end)
        if (string.startswith("# ")):
            tex_file.write("\section{" + string.strip('# \n') + closing_brace)







close_tex()

#Run pdflatex to create pdf files
os.system("pdflatex flashcards.tex")

# \setcardpagelayout
# \begin{karte}[Fach]
# {Frage}
# [Kommentar]
# Antwort
# \end{karte}