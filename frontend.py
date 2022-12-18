import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import dataInPandas as source

# SETTING UP DATA

st.set_page_config(page_title="Person's of the Year", page_icon=":mortar_board:", layout="wide")

# TOP WORDS

# todo trending barchart and rewrite the source data displayed.
# THE INTRO CHAPTER

lmargin, center, rmargin = st.columns([0.5, 1, 0.5])

with center:
    st.header("The Most Influential People In History: What made them so significant?")
    st.write("4.12.2022")

    st.write("**The questions that sparked this project:** ")
    st.write(
        "> What do the Persons of the Year have in common?  \n>What makes them special?  \n>What could I learn from them?")

    st.write("The time chooses yearly one person, group, or object or institute that has for better or for worse ...  "
             "done the most to influence the events of the year. "
             "This [list]("
             "https://en.wikipedia.org/wiki/Time_Person_of_the_Year) seemed like a good and justified starting point for "
             "this study, as I now already had a list of "
             "influential people. (Though their list can be disagreed with.)")

    st.write("But, what makes them influential? What backgrounds do they have? What achievements do they have? In what "
             "circumstances did they become influential? ")

    st.write("##### Could you become like them and replicate their success?")
    st.write("What if our school system trained people to be like the people on [The Time List...]("
             "https://en.wikipedia.org/wiki/Time_Person_of_the_Year) Would our society be more " +
             "advanced if everyone tried to be like them to the best of their abilities?  \n\nOr yikes, would it end "
             "up "
             "being "
             "even…  worse?")

    st.write("Good questions. ")

    st.write("**My hypothesis:** I believed most of them would have a business, military and political background. "
             "However, as it turned out, my hypothesis both underestimated and overestimated certain categories.")

    st.write("**Project Execution with The DAD Framework:**")

    st.write("**Data:** I decided to count all the words that occurred in their wikipedia summaries* (The first few "
             "paragraphs) and see if there would be some words occurring more often. I did this with python web "
             "scraping.")

    st.write("**Analyze:** After doing this, I had to manually categorize* similar nouns and adjectives into groups. "
             "I ended up keeping little under 90 different words/and/bundles out of all the unique 3303 words found. ")

    st.write("What bundles?")

    st.write(
        "Some words "
        "were closely "
        "related, so I decided to count them together. (Eg. “Politician” occurred 7 times + “Statesman” was "
        "found 5 "
        "times, "
        "so in total “Politician” occurred 12 times.")

    st.write(
        "**Display:** Based on the words & bundles, I formed Plotly bar charts displayed on this Streamlit website. "
        "For transparency, All the words that were bundled are shown under the barcharts and the original dataset "
        "scraped "
        "is also publicly available in “The Source Data”.")

    st.caption("> *1. (A summary is counted from the beginning until the first line break. (Line break in python))  \n"
               "> *2. This was done "
               "purely according "
               "to my judgment. You may have bundled different words together. Which would change some scores for "
               "certain "
               "words, but not significantly enough. The main patterns won’t change no matter what.")

    st.markdown("Libraries used:  \n"
                "- Streamlit  \n"
                "- Plotly  \n"
                "- Pandas (And its dependencies like Beautiful Soup 4)  \n"
                "- Wikipedia-api  \n")


# DATA READY FOR DISPLAY - MAKING CHARTS

cats, trends, data = st.tabs(["Categories", "Trends", "Source Data"])

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
        barChart(source.adjectives, "#40C391", "Adjectives", 114, tickanglevalue=45)
        st.write("Bold Leadership and superlatives.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Leader: 26  +  leaders: 6 + leadership: 4 + leader.: 2 + leadership.: 1 = 39  \n" +
                     "First: 30, + first-ever: 1 = 31  \n" +
                     "New: 20  \n" +
                     "Most: 15  \n" +
                     "Largest: 6  \n" +
                     "Revolutionary: 3  \n" +
                     "Total: 114"
                     )

    # -----
    with pols:
        barChart(source.politics, "#E073E9", "Politics", 76, tickanglevalue=45)
        st.write("Politcs is an interesting game... Of influence.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write(
                "Politician: 21 + politician.: 2 + politicians: 1 + statesman: 7 + statesman.: 1 + political: 15 = 47 "
                " \n" +
                "Government: 10  \npresidential: 8  \nfederal: 8  \n" +
                "Politics: 3  \n" +
                "Total: 76"
            )

    # -----
    eventChart, positions = st.columns(2)

    with eventChart:
        barChart(source.events, "#07C3CF", "Events", 48)
        st.write("Leadership during an era of crisis... Hard but rewarding?")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("War: 24 +  war.: 4 = 28  \n" +
                     "Climate: 6 + environment: 1 + nature: 1 = 8  \n" +
                     "Revolution: 5 + revolutions: 1 = 6  \n" +
                     "Total: 48")
    # ---
    with positions:
        barChart(source.positionOfPower, "#EBAA4E", "Positions Of Power", 172, tickanglevalue=45)
        st.write("Just pointing out that they usually are in a position of power inside the government.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("President: 44  \n" +
                     "Secretary: 14  \n" +
                     'Minister: 9 +  minister): 1 + ministers: 3 = 13  \n' +
                     'General: 11  \n' +
                     'Chairman: 9  \n' +
                     'Chancellor: 9 + vice-chancellor: 1 = 10  \n' +
                     'Marshall: 9  \n' +
                     'Pope: 7  \n' +
                     'Governor: 6  \n' +
                     'Senator: 6  \n' +
                     'Head: 6  \n' +
                     'King: 6  \n' +
                     'Mayor: 5 + mayor".: 1 = 6  \n' +
                     'Queen: 5  \n' +
                     'Commander: 5  \n' +
                     'Emperor: 3 + king-emperor: 1 = 4  \n' +
                     'Chief: 4  \n' +
                     'Dictator: 2  \n'
                     "Total: 172"
                     )
    # ---
    coljobs, colcountries = st.columns(2)
    with coljobs:
        barChart(source.jobs, "#E01E5A", "Occupations", 47)

        st.write("Other jobs that give influence apart from directly politics. ")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("Lawyer: 6 + Attorney: 6 + lawyers: 1 =13  \n"
                     'Businessman: 6 + entrepreneur: 2 + founder: 4 = 12  \n'
                     'Executive: 5 + ceo: 3 = 8  \n'
                     'Author: 3 +  writer: 2 + columnist.: 1 = 6  \n'
                     'Activist: 4  \n'
                     'Diplomat: 4  \n'
                     "Total: 47"
                     )

    # ---
    with colcountries:
        barChart(source.countries, "#ECB22E", "Countries", 186, tickanglevalue=45)
        st.write("Well.. The list was made from an american perspective. I guess it helps if your nation is powerful.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("American: 35 + u.s.: 22 + america: 2 + america\'s: 1 + america.: 1 = 61  \n" +
                     "Germany: 11, +  german: 8, german: 4, + germany.: 1 + germany's: 1 = 25  \n" +
                     "China: 11 + chinese: 8 + china.: 2 +  china'.: 1 + china's: 1 +  (chinese: 1 = 24  \n" +
                     'Soviet: 18  \n' +
                     'French: 6 france: 6 + france: 2 +  (french: 2  = 16  \n' +
                     "Poland: 5, +  poland's: 1 + polish: 7 = 13  \n" +
                     'Iran: 4, + iranian: 8 = 12  \n' +
                     'British: 7  \n' +
                     'Columbia: 5  \n' +
                     'Africa: 4 + african: 1  = 5  \n' +
                     "Total: 186"

                     )

    # ---

    colmil, colreligion = st.columns(2)

    with colmil:
        barChart(source.military, "#5D6728", "Military", 50)
        st.write("Not surprised by this.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write('Army: 11 + army.: 1 = 12  \n' +
                     'General: 11  \n' +
                     'Military: 9  \n' +
                     'Marshall: 9  \n' +
                     'Commander: 5  \n' +
                     'Chief: 4  \n' +
                     "Total: 50"
                     )
    # ---
    with colreligion:
        barChart(source.religion, "#EAEAEA", "Religion", 19)
        st.write("The head of the Catholic Church has a huge following and an audience that listens to "
                 "him.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write('Pope: 7  \n'
                     'Church: 3  \n'
                     'Vatican: 3  \n'
                     'Catholic: 3  \n'
                     'Religious: 3  \n'
                     "Total: 19")
    # ---

    leftouter, inner, rightouter = st.columns([0.5, 1, 0.5])

    with inner:
        barChart(source.other, "#2D3C4E", "Other - Non Categorized, But Worth Mention", 95, tickanglevalue=45)
        st.write("Miscellaneous.")
        with st.expander("See the data and word bundles for this table :point_up:"):
            st.write("World: 15 + world.: 4 + world's: 3 = 22  \n"
                     "Member: 17  \n"
                     "Power: 11  \n"
                     "Known: 11  \n"
                     "Social: 8  \n"
                     'Company: 7  \n'
                     "Against: 7  \n"
                     'Following: 6  \n'
                     "Nobel: 6  \n"
                     "Total:  95 \n")

with trends:
    leftmargin, core, rightmargin = st.columns([0.5, 1, 0.5])
    with core:
        st.header("Word Trends")

        st.write("This section demonstrates the fluctuations in the popularity of words used in the articles of the "
                 "honorees between the timeframes.")

        st.write("To do this, I scraped the honorees selected during the specified timeframe and picked the top 10 nouns "
                 "and/or adjectives that occurred in the first paragraph of their wikipedia articles. "
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

