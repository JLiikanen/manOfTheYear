import pandas as pd

topwords = {"Words": ['President', "Politician", "American", "War", "First", "Leader"],
            "Count": [78, 74, 57, 51, 50, 45]}

adjectives = {"Words": ["First", "Leader", "New", "Most", "Known", "Revolutionary", "Prominent",
                        "Largest", "Female"],
              "Count": [51, 45, 29, 21, 14, 8, 6, 6, 6]
              }
politics = {"Words": ["Politician", "Party", "Government", "Democratic", "National", "Federal", "Republican",
                      "Presidential", "Politics"],
            "Count": [74, 48, 23, 20, 16, 16, 14, 11, 6]
            }
events = {"Words": ["War", "Death", "Revolution", "Election", "Crisis"],
          "Count": [51, 21, 11, 11, 5]
          }
copyandpaste = {"Words": [],
                "Count": []
                }

positionOfPower = {"Words": ["President", "Secretary", "Chairman", "Marshall", "Minister", "General", "Senator",
                             "Commander", "King", "Chancellor", "Pope",
                             "Governor", "Head", "Chief", "Mayor", "Queen", "Emperor",
                             "Dictator"
                             ],
                   "Count": [78, 22, 18, 18, 17, 16, 15, 11, 11, 10, 10, 9, 8, 8, 6, 5, 4, 4]
                   }
jobs = {"Words": ["Lawyer", "Businessman", "Executive", "Writer", "Activist", "Diplomat", ],
        "Count": [19, 19, 14, 6, 6, 5]
        }

countries = {"Words": ["America", "China", "Soviet", "Germany", "France", "Hungary", "Poland", "Iran",
                       "Africa", "Saudi", "Britain", "Russia"
                       ],
             "Count": [100, 38, 31, 25, 16, 15, 13, 12, 11, 9, 7, 6]
             }
military = {"Words": ["Military", "Army", "Marshall", "General", "Forces",
                      "Commander", "Officer", "Chief"],
            "Count": [24, 23, 18, 16, 13, 11, 10, 8]
            }
religion = {"Words": ["Pope", "Church", "Vatican", "Catholic", "Religious"],
            "Count": [10, 4, 4, 4, 4]
            }
other = {"Words": ["World", "During", "Member", "Environmentalism",
                   "Civil", "Social", "Against", "Power", "Economic", "Communist",
                   "Company", "University", "Following", "Peace"],
         "Count": [39, 35, 31, 21, 17, 16, 15, 14, 14, 14, 13, 13, 12, 9]
         }

# putting data into frames
# ALL READY AND SET 11.12.2022

topwords = pd.DataFrame(topwords)

adjectives = pd.DataFrame(adjectives)

politics = pd.DataFrame(politics)

events = pd.DataFrame(events)

positionOfPower = pd.DataFrame(positionOfPower)

jobs = pd.DataFrame(jobs)

countries = pd.DataFrame(countries)

military = pd.DataFrame(military)

religion = pd.DataFrame(religion)

other = pd.DataFrame(other)

# trends


firstPeriod1927 = {"Words": ["American", "War", "World", "First", "Leader", "Party", "Marshall",
                             "New", "Soviet", "President"],
                   "Count": [14, 13, 13, 13, 11, 9, 9, 9, 9, 7]
                   }

secondPeriod1946 = {"Words": ["President", "American", "War", "U.S", "Hungarian",
                              "Marshall", "Government", "Secretary", "Civil",
                              "Military"],
                    "Count": [15, 14, 14, 12, 11, 9, 8, 8, 8, 8]
                    }

thirdPeriod1965 = {"Words": ["President", "War", "First", "Leader", "China",
                             "U.S", "Saudi", "Politician", "Boomers", "Politcal"],
                   "Count": [22, 10, 10, 9, 9, 8, 8, 8, 8, 7]
                   }

fourthPeriod1984 = {"Words": ["President", "New", "Soviet", "Party", "American", 1989, "Politician",
                              "Chairman", "Republican", "U.S"],
                    "Count": [18, 16, 12, 11, 10, 9, 9, 8, 7, 6]
                    }

fifthPeriod2003 = {"Words": ["President", "First", "American", "Member", "Politician", "World", "University",
                             "Military", "Leader", "Climate", ],
                   "Count": [16, 15, 13, 9, 9, 7, 7, 6, 6, 6]
                   }

firstPeriod1927 = pd.DataFrame(firstPeriod1927)

secondPeriod1946 = pd.DataFrame(secondPeriod1946)

thirdPeriod1965 = pd.DataFrame(thirdPeriod1965)

fourthPeriod1984 = pd.DataFrame(fourthPeriod1984)

fifthPeriod2003 = pd.DataFrame(fifthPeriod2003)


