# Author Rico Magnucki

from enum import Enum, unique
import os


@unique
class State(Enum):
    NONE = 0
    VALID = 1
    INVALID = 2
    QUESTION = 3
    ANSWER = 4
    SECTION = 5
    SUBSECTION = 6


# INPUT_FILE = "sampleinput.md"
INPUT_FILE = "/Users/Rico/Dev/python/MDTTF/sampleinput.md"
OUTPUT_FILE = ""

QUESTION_START = "\\begin{karte}{"
QUESTION_END = "\n\end{karte}\n"
USEPACKAGE = "\\usepackage{"
USEPACKAGE_PARAMETER = "\\usepackage["
PARAMETER_PACKAGE_DIVIDER = "]{"
BEGIN_DOCUMENT = "\\begin{document}\n"
END_DOCUMENT = "\end{document}\n"
CONTENT = ''
CLOSING_BRACE = "}\n"
BEGIN_FIGURE = "\\begin{figure}\n\centering\n"
PICTURE_INCLUDE = "\includegraphics[width=0.8\pagewidth]{"
END_FIGURE = "\\end{figure}\n"
CURRENT_STATE = State.NONE
LAST_STATE = State.NONE

QUESTION_TAG = "### "
ANSWER_TAG = "_"
SECTION_TAG = "# "
SUBSECTION_TAG = "## "
PICTURE_TAG = "[img] "

SECTION = "\section*{"
SUBSECTION = "\subsection*{"

PACKAGES = [("inputenc", "utf8"), ("fontenc", "T1"),
            ("libertine", ""), ("babel", "ngerman"), ("graphicx", "")]

DOCUMENTCLASS = "\documentclass[a7paper,grid=rear]{kartei}\n"

TEX_FILE = open("flashcards.tex", "w+")


def init_tex():
    TEX_FILE.write(DOCUMENTCLASS)
    load_packages()
    TEX_FILE.write(BEGIN_DOCUMENT)


def close_tex():
    TEX_FILE.write(QUESTION_END)
    TEX_FILE.write(END_DOCUMENT)
    TEX_FILE.close()


def load_packages():
    for package in PACKAGES:
        TEX_FILE.write(build_package_statement(package[1], package[0]))


def build_package_statement(parameter, packagename):
    if parameter:
        return USEPACKAGE_PARAMETER + parameter + PARAMETER_PACKAGE_DIVIDER + packagename + CLOSING_BRACE
    else:
        return USEPACKAGE + packagename + CLOSING_BRACE


def process_file():
    with open(INPUT_FILE) as INPUT:
        print("Zeilen gelesen - parse Input")
        parse_markdown(INPUT.readlines())


def parse_markdown(text_input):
    question = False

    for string in text_input:
        string.rstrip(' ')
        #Create Questions
        if string.startswith(QUESTION_TAG):
            if question:
                TEX_FILE.write(QUESTION_END)
                question = False
            TEX_FILE.write(QUESTION_START + string.strip(QUESTION_TAG + "\n") + CLOSING_BRACE)
            question = True
        elif (string.endswith(ANSWER_TAG + "\n")):
            TEX_FILE.write(string.strip('_\n') + QUESTION_END)
        elif string.startswith(SECTION_TAG):
            TEX_FILE.write(
                SECTION + string.strip('# \n') + CLOSING_BRACE)
        elif string.startswith(SUBSECTION_TAG):
            TEX_FILE.write(
                SUBSECTION + string.strip('# \n') + CLOSING_BRACE)
        elif string.startswith(PICTURE_TAG):
            TEX_FILE.write(
                BEGIN_FIGURE + PICTURE_INCLUDE + string.strip(PICTURE_TAG + '\n') + CLOSING_BRACE + END_FIGURE)
        else:
            TEX_FILE.write(string.strip('\n'))


def set_current_state(prefix):
    if prefix is QUESTION_TAG:
        currentState = State.QUESTION
    elif prefix is ANSWER_TAG:
        currentState = State.ANSWER
    elif prefix is SECTION_TAG:
        currentState = State.SECTION
    elif prefix is SUBSECTION_TAG:
        currentState = State.SUBSECTION


def validate_input(linePrefix):
    lastState = CURRENT_STATE
    set_current_state(linePrefix)
    if CURRENT_STATE is State.QUESTION and (
                        lastState is State.SECTION or lastState is State.SUBSECTION or lastState is State.ANSWER):
        return True
    elif CURRENT_STATE is State.ANSWER and lastState is State.QUESTION:
        return True
    elif CURRENT_STATE is State.SECTION and (
                    lastState is State.SUBSECTION or lastState.ANSWER):
        return True


def clean_tex_files():
    os.system("rm flashcards*")


init_tex()
process_file()
close_tex()
#clean_tex_files()

# Run pdflatex to create pdf files
os.system("pdflatex flashcards.tex")
