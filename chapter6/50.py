import re
def _50():
    with open("nlp.txt") as f:
        contents = []
        for line in f:
            line = line.rstrip()
            if line:
                lines = re.sub(r"([.;:?!]) ([A-Z])",r"\1\n\2",line)
                contents.append(lines)
        print("\n".join(contents))

if __name__ == "__main__":
    _50()

"""
Natural language processing
From Wikipedia, the free encyclopedia
Natural language processing (NLP) is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human (natural) languages.
As such, NLP is related to the area of humani-computer interaction.
Many challenges in NLP involve natural language understanding, that is, enabling computers to derive meaning from human or natural language input, and others involve natural language generation.
History
The history of NLP generally starts in the 1950s, although work can be found from earlier periods.
In 1950, Alan Turing published an article titled "Computing Machinery and Intelligence" which proposed what is now called the Turing test as a criterion of intelligence.
The Georgetown experiment in 1954 involved fully automatic translation of more than sixty Russian sentences into English.
The authors claimed that within three or five years, machine translation would be a solved problem.
However, real progress was much slower, and after the ALPAC report in 1966, which found that ten year long research had failed to fulfill the expectations, funding for machine translation was dramatically reduced.
Little further research in machine translation was conducted until the late 1980s, when the first statistical machine translation systems were developed.
Some notably successful NLP systems developed in the 1960s were SHRDLU, a natural language system working in restricted "blocks worlds" with restricted vocabularies, and ELIZA, a simulation of a Rogerian psychotherapist, written by Joseph Weizenbaum between 1964 to 1966.
Using almost no information about human thought or emotion, ELIZA sometimes provided a startlingly human-like interaction.
When the "patient" exceeded the very small knowledge base, ELIZA might provide a generic response, for example, responding to "My head hurts" with "Why do you say your head hurts?".
During the 1970s many programmers began to write 'conceptual ontologies', which structured real-world information into computer-understandable data.
Examples are MARGIE (Schank, 1975), SAM (Cullingford, 1978), PAM (Wilensky, 1978), TaleSpin (Meehan, 1976), QUALM (Lehnert, 1977), Politics (Carbonell, 1979), and Plot Units (Lehnert 1981).
During this time, many chatterbots were written including PARRY, Racter, and Jabberwacky.
.....
"""