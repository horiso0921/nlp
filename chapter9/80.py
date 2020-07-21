fname = "enwiki-20150112-400-r100-10576.txt"
out_fname = "80_out"

def _80():
    with open(fname, "r", encoding="utf-8") as target, open(out_fname,"w") as out_target:
        for line in target:
            tokens = line.split()
            for token in tokens:
                token = token.strip(".,!?;:()[]'\"")
                token = token.strip()
                if token:
                    print(token, end=" ", file=out_target)
            print("",file=out_target)

if __name__ == "__main__":
    _80()

"""
Anarchism 

Anarchism is a political philosophy that advocates stateless societies often defined as self-governed voluntary institutions but that several authors have defined as more specific institutions based on non-hierarchical free associations Anarchism holds the state to be undesirable unnecessary or harmful While anti-statism is central anarchism entails opposing authority or hierarchical organisation in the conduct of human relations including but not limited to the state system 
As a subtle and anti-dogmatic philosophy anarchism draws on many currents of thought and strategy Anarchism does not offer a fixed body of doctrine from a single particular world view instead fluxing and flowing as a philosophy There are many types and traditions of anarchism not all of which are mutually exclusive Anarchist schools of thought can differ fundamentally supporting anything from extreme individualism to complete collectivism Strains of anarchism have often been divided into the categories of social and individualist anarchism or similar dual classifications Anarchism is usually considered a radical left-wing ideology and much of anarchist economics and anarchist legal philosophy reflect anti-authoritarian interpretations of communism collectivism syndicalism mutualism or participatory economics 
The central tendency of anarchism as a social movement has been represented by anarcho-communism and anarcho-syndicalism with individualist anarchism being primarily a literary phenomenon which nevertheless did have an impact on the bigger currents and individualists have also participated in large anarchist organisations Many anarchists oppose all forms of aggression supporting self-defense or non-violence anarcho-pacifism while others have supported the use of some coercive measures including violent revolution and propaganda of the deed as means to achieve anarchist ends 
Etymology and terminology 
The term anarchism is a compound word composed from the word anarchy and the suffix -ism themselves derived respectively from the Greek i.e anarchy from anarchos meaning one without rulers from the privative prefix ἀν- an- i.e without and archos i.e leader ruler cf archon or arkhē i.e authority sovereignty realm magistracy and the suffix or -ismos -isma from the verbal infinitive suffix -ίζειν -izein The first known use of this word was in 1539."Anarchist was the term adopted by Maximilien de Robespierre to attack those on the left whom he had used for his own ends during the French Revolution but was determined to get rid of though among these anarchists there were few who exhibited the social revolt characteristics of later anarchists There would be many revolutionaries of the early nineteenth century who contributed to the anarchist doctrines of the next generation such as William Godwin and Wilhelm Weitling but they did not use the word anarchist or anarchism in describing themselves or their beliefs Pierre-Joseph Proudhon was the first political philosopher to call himself an anarchist marking the formal birth of anarchism in the mid-nineteenth century Since the 1890s from France the term libertarianism has often been used as a synonym for anarchism and was used almost exclusively in this sense until the 1950s in the United States its use as a synonym is still common outside the United States On the other hand some use libertarianism to refer to individualistic free-market philosophy only referring to free-market anarchism as libertarian anarchism 
History 
Origins 
"""