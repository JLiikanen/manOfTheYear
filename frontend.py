import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import dataToPandas as source

# SETTING UP DATA

st.set_page_config(page_title="Person's of the Year", page_icon=":mortar_board:", layout="wide")

# TOP WORDS


# THE INTRO CHAPTER

lmargin, center, rmargin = st.columns([0.5, 1, 0.5])

with center:
    st.header("The Most Influential People In History: What made them so extraordinary?")
    st.write("4.12.2022")

    st.write("**The questions that sparked this project:** ")
    st.write(
        "> What traits do these influential people have in common?  \n>What sets them apart?  \n>What are the pratical "
        "takeaways we can get by observing them?"
    )

    st.write("The Time paper chooses yearly one person, group, or object or institute that has for better or for "
             "worse ... "
             "done the most to influence the events of the year. "
             "The [list of the winners]("
             "https://en.wikipedia.org/wiki/Time_Person_of_the_Year) of The Person Of The Year award seemed like a "
             "justified starting point "
             "for "
             "this study, as I now already had a sample of "
             "influential people that can be analyzed. (Though their list can be disagreed with, and might be a "
             "little skewed towards americans.)")

    st.write("Despite that, it remains a reliable source for finding answers to our questions.  \n\nWhat factors "
             "contribute to their influence?  \n\n"
             " What careers have they pursued?  \n\nIn what "
             "circumstances did they make their breakthrough?")

    st.write("##### Most importantly, could you become like them and replicate their success?")
    st.write("What if our school system trained students to be like the people on [The Time List...]("
             "https://en.wikipedia.org/wiki/Time_Person_of_the_Year)  \n\nWould our society be more " +
             "advanced if everyone aspired to be like them to the best of their abilities?  \n\nOr yikes, would it end "
             "up "
             "being "
             "even…  Worse?")

    st.write("Good questions. ")

    st.write("**My hypothesis:** I believed most of them would have a business, military and political background. "
             "However, as it turned out, the 'weight' between the categories wasn't what I was expecting.")

    st.write("**Project Execution with The DAD Framework:**")

    st.write("**Data:** I decided to count all the words that occurred in their wikipedia summaries* (The first "
             "paragraph.) and see if there would be some words occurring more often, which would reveal underlying "
             "patterns. "
             "The data was collected through Python Text mining with the pandas library and wikipedia api.")

    st.write("**Analyze:** Once data mining was completed, I had to manually categorize* similar nouns and adjectives "
             "into categories, for example, a word might belong to the 'Military' or 'Politics' category. On a side "
             "note, I later "
             "found out about the [NLTK "
             "python library](https://www.nltk.org/), which would have "
             "saved me some time processing the words. Might refactor the code with NLTK soon. "
             " Anyway, I ended up keeping little under 90 different words/bundles out of all the 3303 words "
             "found. ")

    st.write("You may ask, what bundles??")

    st.write(
        "Some words "
        "were closely "
        "related, so I decided to count them together as a bundle. Here's the logic: (Eg. “Politician” occurred 7 "
        "times + "
        "“Statesman” was "
        "found 5 "
        "times, "
        "so in total “Politician” occurred 12 times. The word “Politician” belongs to the Politics word category.")

    st.write(
        "**Display:** Based on the word categories, I formed Plotly bar charts displayed on this Streamlit website. "
        "For transparency, the data used for the current chart is shown under the chart. The raw dataset "
        "is also publicly available in “The Source Data” -tab.")

    st.caption("> *1. (A summary is counted from the beginning until the first line break.  \n"
               "> *2. This was done "
               "purely according "
               "to my judgment. You may have bundled different words together, which would change the scores for "
               "certain "
               "words, but not significantly enough. The main patterns won’t change no matter what.")

    st.markdown("Libraries used:  \n"
                "- Streamlit  \n"
                "- Plotly  \n"
                "- Pandas  \n"
                "- [Wikipedia api](https://wikipedia.readthedocs.io/en/latest/code.html)  \n")

# DATA READY FOR DISPLAY - MAKING CHARTS

cats, trends, data = st.tabs(["Main", "Trends", "Source Data"])

with cats:
    lpad, middle, rpad = st.columns([0.5, 1, 0.5])

    with middle:
        st.write()
        colors = ["#4274F5", "#5A86F6", "#819EE9", "#99B6FF", "#ADC2FB", "#CBD8FB"]

        topwordsfig = go.Figure(go.Bar(x=source.topwords["Words"], y=source.topwords["Count"],
                                       texttemplate="<b>%{y}</b>", hovertemplate="Word: %{x} <br> Count: %{y}",
                                       name=" ", insidetextanchor="end", width=0.8, marker=dict(color=colors)))

        topwordsfig.update_layout(
            xaxis=dict(fixedrange=True, title=go.layout.xaxis.Title(), linecolor="#002140", linewidth=2.4,
                       showgrid=False, tickfont=dict(color="#002140", size=13.5)),
            yaxis=dict(fixedrange=True, linecolor="#002140", linewidth=1.5, showgrid=False,
                       title=dict(font=dict(color="#002140", size=16), text="Count"),
                       tickfont=dict(color="#002140", size=13.5)
                       ), plot_bgcolor="#FFFFFF",
            title=dict(text="Top Words", xref="container", yref="container", x=0.09, y=0.87,
                       font=dict(size=24, color="#002140"))
        )
        st.plotly_chart(topwordsfig, use_container_width=True, config={"displayModeBar": False})

        st.write("This chart includes the most frequently found individual words. "
                 "Should you be a courageous politician and do something new during war time?")

        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Politician: 21 + politician.: 2 + politicians: 1 + political: 15 + statesman: 7 + + statesman.: "
                     "1 = 47  \n" +
                     "President: 44  \n" +
                     "Leader: 26  +  leaders: 6 + leadership: 4 + leader.: 2 + leadership.: 1 = 39  \n" +
                     "American: 35"
                     "First: 30 + first-ever: 1 = 31  \n" +
                     "War: 24, +  war.: 4 = 28  \n"
                     )


    # ---- Helper Function ---
    def barChart(dataframe, color, name, total=0, tickanglevalue=0, needsTotal=True):
        barFig = go.Figure(go.Bar(x=dataframe["Words"], y=dataframe["Count"],
                                  texttemplate="<b>%{y}</b>", hovertemplate="Word: %{x} <br> Count: %{y}",
                                  name=" ", insidetextanchor="end", width=0.8, marker=dict(color=color)))
        if needsTotal:
            barFig.update_layout(
                xaxis=dict(fixedrange=True, linecolor="#002140", linewidth=2.4,
                           showgrid=False, tickfont=dict(color="#002140", size=13.5), tickangle=tickanglevalue),
                yaxis=dict(fixedrange=True, linecolor="#002140", linewidth=1.5, showgrid=False,
                           title=dict(font=dict(color="#002140", size=16), text="Count"),
                           tickfont=dict(color="#002140", size=13.5), ),
                title=dict(text=name, xref="container", yref="container", x=0.09, y=0.87,
                           font=dict(size=24, color="#002140"))
                , plot_bgcolor="#FFFFFF",
                annotations=(
                    go.layout.Annotation(text=f"Total: {total}", xref="paper", yref="paper", x=0.99, y=0.99,
                                         showarrow=False,
                                         font=dict(size=16)),)
            )
        else:
            barFig.update_layout(
                xaxis=dict(fixedrange=True, linecolor="#002140", linewidth=2.4,
                           showgrid=False, tickfont=dict(color="#002140", size=13.5), tickangle=tickanglevalue),
                yaxis=dict(fixedrange=True, linecolor="#002140", linewidth=1.5, showgrid=False,
                           title=dict(font=dict(color="#002140", size=16), text="Count"),
                           tickfont=dict(color="#002140", size=13.5)),
                title=dict(text=name, xref="container", yref="container", x=0.09, y=0.87,
                           font=dict(size=24, color="#002140"))
                , plot_bgcolor="#FFFFFF",
            )

        st.plotly_chart(barFig, use_container_width=True, config={"displayModeBar": False})  # total annotation


    # CHART CREATION
    # ---

    adjs, pols = st.columns(2)
    with adjs:
        barChart(source.adjectives, "#40C391", "Adjectives", 185, tickanglevalue=45)
        st.write("Bold Leadership and superlatives.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("First:49 + first-ever:1 = 50  \n"
                     "Leader:34 + leadership:6 + leader.:4 + leadership.:1= 45  \n"
                     "New: 29  \n"
                     "Most: 21  \n"
                     "Known: 14  \n"
                     "Revolutionary: 8  \n"
                     "Prominent: 6  \n"
                     "Largest: 6  \n"
                     "Female:6  \n"
                     )

    # -----
    with pols:
        barChart(source.politics, "#E073E9", "Politics", 228, tickanglevalue=45)
        st.write("Politcs is an interesting game... Of influence.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Politician:35 + political: 24 + politician.:2  + statesman:11 + statesman.:2 = 74  \n"
                     "Party: 43 + party’s:5 = 48  \n"
                     "Government: 18  + government.:5  = 23  \n"
                     "Democratic: 20  \n"
                     "National: 16  \n"
                     "Federal: 16  \n"
                     "Republican:14  \n"
                     "Presidential: 11  \n"
                     "Politics: 4 + politics.:2 = 6  \n"

                     )

    # -----
    eventChart, positions = st.columns(2)

    with eventChart:
        barChart(source.events, "#07C3CF", "Events", 99)
        st.write("Leadership during an era of crisis... Hard but rewarding?")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("War: 44 + war.:7 = 51  \n"
                     "Death:19 + death.:2 = 21  \n"
                     "Revolution:10 + 'revolutions': 1 = 11  \n"
                     "Election: 7 + election.:4 = 11  \n"
                     "Crisis: 5  \n")

    # ---
    with positions:
        barChart(source.positionOfPower, "#EBAA4E", "Positions Of Power", 278, tickanglevalue=45)
        st.write("Just pointing out that they usually are in a position of power inside the government.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("President: 78  \n"
                     "Secretary: 22  \n"
                     "Chairman: 18  \n"
                     "Marshall: 18  \n"
                     "Minister': 16, +  minister): 1  = 17  \n"
                     "General: 16  \n"
                     "Senator: 15  \n"
                     "Commander': 9 + Commander-in-chief:2 = 11  \n"
                     "King: 11  \n"
                     "Chancellor: 9 + vice-chancellor: 1 = 10  \n"
                     "Pope: 10  \n"
                     "Governor: 9  \n"
                     "Head: 8  \n"
                     "Chief': 8  \n"
                     "Mayor': 5 + mayor'.: 1 = 6  \n"
                     "Queen': 4 + Queen’s:1 = 5  \n"
                     "Emperor': 3 + King-emperor: 1 = 4  \n"
                     "Dictator: 3 + Dictatorship:1 = 4  \n"

                     )
    # ---
    coljobs, colcountries = st.columns(2)
    with coljobs:
        barChart(source.jobs, "#E01E5A", "Occupations", 69)

        st.write("Common occupation they have. I'm surprised how many times the word lawyer was found!")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Businessman: 6 + entrepreneur: 4 + founder: 8 + co-founder:1  = 19  \n"
                     "Lawyer: 8 + attorney:11 = 19  \n"
                     "Executive: 8 + ceo: 6  = 14  \n"
                     "Activist: 5, + activist.:1 = 6  \n"
                     "Author': 3 +  Writer: 4 +  Columnist.: 1 + Columnist:1 + Journalist: 4 = 6  \n"
                     "Diplomat: 5"
                     )

    # ---
    with colcountries:
        barChart(source.countries, "#ECB22E", "Countries", 283, tickanglevalue=45)
        st.write("Well.. The list was made from an american perspective. I guess it helps if your nation is powerful.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("American': 57, + U.S.: 35 + america: 5, + america\'s:1 +  america.: 2 = 100  \n"
                     "China': 18 + chinese: 12 +china.: 3 + china'.: 2 + china's: 2 +  (chinese: 1 = 38  \n"
                     "Soviet: 31  \n"
                     "Germany': 11, +  german: 8 + (german: 4 +  germany.: 1 + germany's: 1 = 25  \n"
                     "French: 5 +  france: 7, + france.: 3 +  (french: 1  = 16  \n"
                     "Hungary:3 + hungarian:11 + hungarians:1 = 15  \n"
                     "Poland: 5, +  poland's: 1 +  polish: 7 = 13  \n"
                     "Iran: 4, + 'iranian: 8 = 12  \n"
                     "Africa: 8 + african: 2 + africa.:1  = 11  \n"
                     "Saudi: 9  \n"
                     "British: 7  \n"
                     "Russia:4 + russian:1 + russia.:1 = 6  \n"
                     )

    # ---

    colmil, colreligion = st.columns(2)

    with colmil:
        barChart(source.military, "#5D6728", "Military", 123)
        st.write("Not surprised by this.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Military: 24  \n"
                     "Army: 21 + army.: 2 = 23  \n"
                     "Marshall: 18  \n"
                     "General: 16  \n"
                     "Forces:13  \n"
                     "Commander: 9 + Commander-in-chief:2 =   \n"
                     "Officer:10  \n"
                     "Chief: 8  \n"
                     )
    # ---
    with colreligion:
        barChart(source.religion, "#EAEAEA", "Religion", 26)
        st.write("The head of the Catholic Church has a huge following and an audience that listens to "
                 "him.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Pope: 10  \n"
                     "Church: 3 + church.:1 = 4  \n"
                     "Vatican: 4  \n"
                     "Catholic: 4  \n"
                     "Religious: 4  \n"
                     )
    # ---

    leftouter, inner, rightouter = st.columns([0.5, 1, 0.5])

    with inner:
        barChart(source.other, "#2D3C4E", "Other - Non Categorized, But Worth Mention", 263, tickanglevalue=45)
        st.write("Miscellaneous. But the words are still somewhat related to the categories above.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("World:30 + world.:4 + world's:5 = 39  \n"
                     "During:35   \n"
                     "Member:31  \n"
                     "Climate: 6 + climate): 1 + environment: 3 + nature: 1 + environmentalism: 3 + "
                     "environmentalism.: 1 + environmentalism: 6 = 21  \n"
                     "Civil: 17   \n"
                     "Social: 16  \n"
                     "Against: 15  \n"
                     "Power: 14  \n"
                     "Economic: 14  \n"
                     "Communist: 14  \n"
                     "Company: 13  \n"
                     "University: 12 + university.:1 = 13  \n"
                     "Following: 12  \n"
                     "Peace: 9  \n"
                     )

with trends:
    leftmargin, core, rightmargin = st.columns([0.5, 1, 0.5])
    with core:
        st.header("Word Trends")

        st.write("This section demonstrates the fluctuations in the popularity of words used in the articles of the "
                 "honorees between the timeframes.")

        st.write("To do this, I scraped only the honorees selected during the specified timeframe (Eg. The winners "
                 "between 1927 - 1945) and picked the top "
                 "10 "
                 "nouns "
                 "and/or adjectives that occurred in the first paragraphs of their wikipedia articles. "
                 "No word bundles were made.")

    first, second = st.columns(2)
    with first:
        barChart(source.firstPeriod1927, "#A96B38", "1927-1945", needsTotal=False, tickanglevalue=45)
    with second:
        barChart(source.secondPeriod1946, "#BFAA69", "1946-1964", needsTotal=False, tickanglevalue=45)

    third, fourth = st.columns(2)

    with third:
        barChart(source.thirdPeriod1965, "#4D6E67", "1965-1983", needsTotal=False, tickanglevalue=45)

    with fourth:
        barChart(source.fourthPeriod1984, "#DF9D4F", "1984-2002", needsTotal=False, tickanglevalue=45)

    leftm, central, rightm = st.columns([0.5, 1, 0.5])

    with central:
        barChart(source.fifthPeriod2003, "#748FFB", "2003-2021", needsTotal=False, tickanglevalue=45)
        st.write("**There seems to be a general trend of**  \n1. An important event. (The context in which they "
                 "became important.)  \n2. Politics and the position "
                 "of power achieved "
                 "through "
                 "politics in a powerful/relevant country. Other paths to power, such as a military career is also "
                 "present. "
                 " And even if not mentioned, businesses have always been a channel for making an impact. "
                 "\n3. Doing something new.")

with data:
    st.write("##### Want to see the raw source data that contains all the words found?")

    with open("allWordsFound", encoding="utf-8") as f:
        st.download_button("Download Source Data in CSV", f, mime="text/csv", file_name="allWordsFound.csv")

    st.write("##### Periodic Data")
    first, second, thrid, fourth, fifth, emptySpace = st.columns([0.5, 0.5, 0.5, 0.5, 0.5, 2.2])

    with first:
        with open("Trending Data, 1927-1945", encoding="utf-8") as f:
            st.download_button("1927 - 1945", f, mime="text/csv", file_name="Trending Data, 1927-1945.csv")
    with second:
        with open("Trending Data, 1946 - 1964", encoding="utf-8") as f:
            st.download_button("1946 - 1964", f, mime="text/csv", file_name="Trending Data, 1946 - 1964.csv")

    with thrid:
        with open("Trending Data, 1965 - 1983", encoding="utf-8") as f:
            st.download_button("1965 - 1983", f, mime="text/csv", file_name="Trending Data, 1965 - 1983.csv")

    with fourth:
        with open("Trending Data, 1984 - 2002", encoding="utf-8") as f:
            st.download_button("1984 - 2002", f, mime="text/csv", file_name="Trending Data, 1984 - 2002.csv")

    with fifth:
        with open("Trending Data, 2003 - 2021", encoding="utf-8") as f:
            st.download_button("2003 - 2021", f, mime="text/csv", file_name="Trending Data, 2003 - 2021.csv")

