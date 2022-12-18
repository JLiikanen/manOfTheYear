import pandas as pd
import wikipedia

df = pd.read_html("https://en.wikipedia.org/wiki/Time_Person_of_the_Year")[1]
base = "https://en.wikipedia.org"

specialcases = {"The American fighting-man": "United_States_Armed_Forces",
                "The Hungarian freedom fighter": "Hungarian Revolution of 1956",
                "U.S. Scientists": "Science and technology in the United States",
                "The Inheritor": "Baby boomers",
                "The Apollo 8 astronauts": "Apollo 8",
                "The Middle Americans": "Middle America (United States)",
                "American women": "Women_in_the_United_States",
                "The Computer": "Personal Computer",
                "The Endangered Earth": "Environmentalism",
                "The Whistleblowers": "Whistleblower",
                "The American soldier ": "United_States_Armed_Forces",  # the space matters!
                "You": "You_(Time_Person_of_the_Year)",
                "Francis": "Pope_Francis",
                "Faisal": "Faisal of Saudi Arabia"
                }

noLinkCases = {"The Guardians": 1, "The Silence Breakers": 2, "Ebola fighters": 3, "The Protester": 3,
               "The Good Samaritans": 4, "The Peacemakers": 5}


def nameCleaner(name):
    for char in name:
        if char == "(" or char == "[":
            pos = name.index(char)

            n = len(name) - (len(name) - pos)
            return name[:n]
    else:
        return name


def wordParser(namelst):
    p_wiki = ""
    wordsCounted = dict()
    for dude in namelst:
        cleanedDude = nameCleaner(dude)
        if cleanedDude in specialcases:
            p_wiki = wikipedia.WikipediaPage(specialcases[cleanedDude]).content
        elif cleanedDude in noLinkCases:  # if no link take the notes connected to that person.
            i = df[df["Choice"] == dude].index
            p_wiki = df.loc[i, "Notes"].values[0]
            summaryParagraph = p_wiki.lower().replace(",", " ").replace(":", " ").split(" ")
            for word in summaryParagraph:
                wordsCounted[word] = wordsCounted.get(word, 0) + 1
            continue
        else:
            try:
                p_wiki = wikipedia.WikipediaPage(cleanedDude).content
            except (wikipedia.exceptions.PageError, wikipedia.exceptions.DisambiguationError):
                    print(f"ERROR ERROR - NOT FOUND {cleanedDude}")

        print(cleanedDude)
        summaryParagraph = p_wiki.split("\n")[0].lower().replace(",", " ").replace(":", " ").split(" ")
        # its line break vs summary <- line break is a better separator, it basically eliminates overly-long summaries
        # while keeping most summaries as it is already a common separator there
        for word in summaryParagraph:
            wordsCounted[word] = wordsCounted.get(word, 0) + 1

    return wordsCounted


allWords = wordParser(df["Choice"])
allWords = dict(sorted(allWords.items(), key=lambda item: item[1], reverse=True))

print(allWords)

csv = pd.DataFrame(columns=["Word", "Count"])
csv["Word"] = allWords.keys()
csv["Count"] = allWords.values()

csv.to_csv("worddata", index=False, )



# --- TRENDING VALUES ---


sectionNames = {1: "1927 - 1945", 2: "1946 - 1964", 3: "1965 - 1983", 4: "1984 - 2002", 5: "2003 - 2021"}
sectionIndex = 1

lst1 = df[(df['Year'] >= 1927) & (df['Year'] <= 1945)]["Choice"]
lst2 = df[(df['Year'] >= 1946) & (df['Year'] <= 1964)]["Choice"]
lst3 = df[(df['Year'] >= 1965) & (df['Year'] <= 1983)]["Choice"]
lst4 = df[(df['Year'] >= 1984) & (df['Year'] <= 2002)]["Choice"]
lst5 = df[(df['Year'] >= 2003) & (df['Year'] <= 2021)]["Choice"]

allPeriods = [lst1, lst2, lst3, lst4, lst5]

for period in allPeriods:
    wordsFoundInThatPeriod = wordParser(period)

    dataframe = pd.DataFrame(wordsFoundInThatPeriod, columns=["Word", "Count"])
    dataframe["Word"] = wordsFoundInThatPeriod.keys()
    dataframe["Count"] = wordsFoundInThatPeriod.values()

    filename = f"Trending Data, {sectionNames[sectionIndex]}"
    dataframe.sort_values(by="Count", inplace=True, ascending=False)
    dataframe.to_csv(filename, index=False)

    sectionIndex += 1
