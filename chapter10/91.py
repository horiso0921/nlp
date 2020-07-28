fname_input = "questions-words.txt"
fname_out = "family_91"
def _91():
    with open(fname_input, "r") as target, open(fname_out, "w") as out_target:
        contens = target.read()
        contens_splited = contens.split(": ")
        for session in contens_splited:
            session_list = session.split("\n")
            if session_list[0] == "family":
                out_target.write("\n".join(session_list[1:]))

if __name__ == "__main__":
    _91()