### Import variables from all cookieData files ####
#Import the name, skill, type, position and rarity from the original files (cookieData_2021/22/23/24/25) to here by assigning it to variables within this file.
#Do this so the our project isn't as cluttered by combing the data and our findings (this file) into one file.
#Use this site: http://www.mynikko.com/tools/tool_incrementstr.html
#Google Search "Online number increment by set"

import re

#2021 Cookies

#Import 2021 Cookie Data
import cookieData_2021 # type: ignore

c21_1_main = cookieData_2021.c21_1
c21_2_main = cookieData_2021.c21_2
c21_3_main = cookieData_2021.c21_3
c21_4_main = cookieData_2021.c21_4
c21_5_main = cookieData_2021.c21_5
c21_6_main = cookieData_2021.c21_6
c21_7_main = cookieData_2021.c21_7
c21_8_main = cookieData_2021.c21_8
c21_9_main = cookieData_2021.c21_9
c21_10_main = cookieData_2021.c21_10
c21_11_main = cookieData_2021.c21_11
c21_12_main = cookieData_2021.c21_12
c21_13_main = cookieData_2021.c21_13
c21_14_main = cookieData_2021.c21_14
c21_15_main = cookieData_2021.c21_15
c21_16_main = cookieData_2021.c21_16
c21_17_main = cookieData_2021.c21_17
c21_18_main = cookieData_2021.c21_18
c21_19_main = cookieData_2021.c21_19
c21_20_main = cookieData_2021.c21_20
c21_21_main = cookieData_2021.c21_21
c21_22_main = cookieData_2021.c21_22
c21_23_main = cookieData_2021.c21_23
c21_24_main = cookieData_2021.c21_24
c21_25_main = cookieData_2021.c21_25
c21_26_main = cookieData_2021.c21_26
c21_27_main = cookieData_2021.c21_27
c21_28_main = cookieData_2021.c21_28
c21_29_main = cookieData_2021.c21_29
c21_30_main = cookieData_2021.c21_30
c21_31_main = cookieData_2021.c21_31
c21_32_main = cookieData_2021.c21_32
c21_33_main = cookieData_2021.c21_33
c21_34_main = cookieData_2021.c21_34
c21_35_main = cookieData_2021.c21_35
c21_36_main = cookieData_2021.c21_36
c21_37_main = cookieData_2021.c21_37
c21_38_main = cookieData_2021.c21_38
c21_39_main = cookieData_2021.c21_39
c21_40_main = cookieData_2021.c21_40
c21_41_main = cookieData_2021.c21_41
c21_42_main = cookieData_2021.c21_42

#Store all 2021 Cookies' variables into an array to store them as a single variable, in order to loop through them all at once, to find
#the word count of all Cookies

array2021 = [
    c21_1_main, c21_2_main, c21_3_main, c21_4_main, c21_5_main, c21_6_main, c21_7_main, c21_8_main, c21_9_main, c21_10_main, \
    c21_11_main, c21_12_main, c21_13_main, c21_14_main, c21_15_main, c21_16_main, c21_17_main, c21_18_main, c21_19_main, \
    c21_20_main, c21_21_main, c21_22_main, c21_23_main, c21_24_main, c21_25_main, c21_26_main, c21_27_main, c21_28_main, \
    c21_29_main, c21_30_main, c21_31_main, c21_32_main, c21_33_main, c21_34_main, c21_35_main, c21_36_main, c21_37_main, \
    c21_38_main, c21_39_main, c21_40_main, c21_41_main, c21_42_main
]

#2022 Cookies
import cookieData_2022 # type: ignore

c22_1_main = cookieData_2022.c22_1
c22_2_main = cookieData_2022.c22_2
c22_3_main = cookieData_2022.c22_3
c22_4_main = cookieData_2022.c22_4
c22_5_main = cookieData_2022.c22_5
c22_6_main = cookieData_2022.c22_6
c22_7_main = cookieData_2022.c22_7
c22_8_main = cookieData_2022.c22_8
c22_9_main = cookieData_2022.c22_9
c22_10_main = cookieData_2022.c22_10
c22_11_main = cookieData_2022.c22_11
c22_12_main = cookieData_2022.c22_12
c22_13_main = cookieData_2022.c22_13
c22_14_main = cookieData_2022.c22_14
c22_15_main = cookieData_2022.c22_15
c22_16_main = cookieData_2022.c22_16
c22_17_main = cookieData_2022.c22_17
c22_18_main = cookieData_2022.c22_18
c22_19_main = cookieData_2022.c22_19
c22_20_main = cookieData_2022.c22_20

#Store all 2022 Cookies' variables into an array to store them as a single variable

array2022 = [
    c22_1_main, c22_2_main, c22_3_main, c22_4_main, c22_5_main, c22_6_main, c22_7_main, c22_8_main, c22_9_main, c22_10_main, \
    c22_11_main, c22_12_main, c22_13_main, c22_14_main, c22_15_main, c22_16_main, c22_17_main, c22_18_main, c22_19_main, c22_20_main
]

#2023 Cookies
import cookieData_2023 # type: ignore

c23_1_main = cookieData_2023.c23_1
c23_2_main = cookieData_2023.c23_2
c23_3_main = cookieData_2023.c23_3
c23_4_main = cookieData_2023.c23_4
c23_5_main = cookieData_2023.c23_5
c23_6_main = cookieData_2023.c23_6
c23_7_main = cookieData_2023.c23_7
c23_8_main = cookieData_2023.c23_8
c23_9_main = cookieData_2023.c23_9
c23_10_main = cookieData_2023.c23_10
c23_11_main = cookieData_2023.c23_11
c23_12_main = cookieData_2023.c23_12
c23_13_main = cookieData_2023.c23_13
c23_14_main = cookieData_2023.c23_14
c23_15_main = cookieData_2023.c23_15
c23_16_main = cookieData_2023.c23_16
c23_17_main = cookieData_2023.c23_17
c23_18_main = cookieData_2023.c23_18
c23_19_main = cookieData_2023.c23_19
c23_20_main = cookieData_2023.c23_20
c23_21_main = cookieData_2023.c23_21
c23_22_main = cookieData_2023.c23_22
c23_23_main = cookieData_2023.c23_23
c23_24_main = cookieData_2023.c23_24
c23_25_main = cookieData_2023.c23_25
c23_26_main = cookieData_2023.c23_26
c23_27_main = cookieData_2023.c23_27

#Store all 2023 Cookies' variables into an array to store them as a single variable
array2023 = [
    c23_1_main, c23_2_main, c23_3_main, c23_4_main, c23_5_main, c23_6_main, c23_7_main, c23_8_main, c23_9_main, \
    c23_10_main, c23_11_main, c23_12_main, c23_13_main, c23_14_main, c23_15_main, c23_16_main, c23_17_main, c23_18_main, \
    c23_19_main, c23_20_main, c23_21_main, c23_22_main, c23_23_main, c23_24_main, c23_25_main, c23_26_main, c23_27_main
]

#2024 Cookies
import cookieData_2024 # type: ignore

c24_1_main = cookieData_2024.c24_1
c24_2_main = cookieData_2024.c24_2
c24_3_main = cookieData_2024.c24_3
c24_4_main = cookieData_2024.c24_4
c24_5_main = cookieData_2024.c24_5
c24_6_main = cookieData_2024.c24_6
c24_7_main = cookieData_2024.c24_7
c24_8_main = cookieData_2024.c24_8
c24_9_main = cookieData_2024.c24_9
c24_10_main = cookieData_2024.c24_10
c24_11_main = cookieData_2024.c24_11
c24_12_main = cookieData_2024.c24_12
c24_13_main = cookieData_2024.c24_13
c24_14_main = cookieData_2024.c24_14
c24_15_main = cookieData_2024.c24_15
c24_16_main = cookieData_2024.c24_16
c24_17_main = cookieData_2024.c24_17
c24_18_main = cookieData_2024.c24_18
c24_19_main = cookieData_2024.c24_19
c24_20_main = cookieData_2024.c24_20
c24_21_main = cookieData_2024.c24_21
c24_22_main = cookieData_2024.c24_22
c24_23_main = cookieData_2024.c24_23
c24_24_main = cookieData_2024.c24_24
c24_25_main = cookieData_2024.c24_25
c24_26_main = cookieData_2024.c24_26
c24_27_main = cookieData_2024.c24_27

#Store all 2024 Cookies' variables into an array to store them as a single variable
array2024 = [
    c24_1_main, c24_2_main, c24_3_main, c24_4_main, c24_5_main, c24_6_main, c24_7_main, c24_8_main, c24_9_main, \
    c24_10_main, c24_11_main, c24_12_main, c24_13_main, c24_14_main, c24_15_main, c24_16_main, c24_17_main, c24_18_main, \
    c24_19_main, c24_20_main, c24_21_main, c24_22_main, c24_23_main, c24_24_main, c24_25_main, c24_26_main, c24_27_main
]

import cookieData_2025 # type: ignore
c25_1_main = cookieData_2025.c25_1
c25_2_main = cookieData_2025.c25_2
c25_3_main = cookieData_2025.c25_3
c25_4_main = cookieData_2025.c25_4
c25_5_main = cookieData_2025.c25_5
c25_6_main = cookieData_2025.c25_6

array2025 = [
    c25_1_main, c25_2_main, c25_3_main, c25_4_main, c25_5_main, c25_6_main
]

#Count how many items in array. Will tell how many Cookies were released then during that year
### 2021 Cookies ###
highestRankingList2021 = [] 
totalNoOfWords2021 = 0 
cookieNumber2021 = 0

### 2022 Cookies ###
highestRankingList2022 = []
totalNoOfWords2022 = 0
cookieNumber2022 = 0

### 2023 Cookies ###
highestRankingList2023 = []
totalNoOfWords2023 = 0
cookieNumber2023 = 0

### 2024 Cookies ###
highestRankingList2024 = [] 
totalNoOfWords2024 = 0 
cookieNumber2024 = 0

### 2025 Cookies ###
highestRankingList2025 = []
totalNoOfWords2025 = 0
cookieNumber2025 = 0

#ONLY USED WHEN FILTERING. Empty arrays to send to the append function below, to slot in the filtered characters.
emptyMan2021 = []
emptyMan2022 = []
emptyMan2023 = []
emptyMan2024 = []
emptyMan2025 = []

typeCheck = ["Ambush", "Bomber", "Charge", "Defense", "Healing", "Magic", "Ranged", "Support"]
positionCheck = ["Front", "Middle", "Rear"]
rarityCheck = ["Epic", "Super Epic", "Legendary", "Ancient", "Beast", "Awakened"]

#Ask user what they want to do

print("Welcome! Select an Option!")
print("1) Count all words, filtering by Rarity/Type/Position")
print("2) Count all words without limitations")

while True:
    myAnswer = input("Input here! ")
    if myAnswer == "1":
        print("Option 1 selected!")
        break
    elif myAnswer == "2":
        print("Option 2 selected!")
        break
    else:
        print("Invalid input.")

if myAnswer == "1":
    while True:
        desiredRarity = input("Rarity, Type or Position? ").title() #Use .title() method to force capitalization of first letter.
                                                                    #as the if-checks use a capitalized version of Rarity/Type/Position
        if desiredRarity == "Rarity":
            while True:
                desiredRarity2 = input("Okay. What rarity will it be? ").title()

                if desiredRarity2 in rarityCheck:
                    def emptyArray(arrayToSend, whichYear):
                        for x in whichYear: #For every item under the selected year array...
                            if x.rarity == desiredRarity2: #Only slot in Cookies under the chosen rarity under the array
                                arrayToSend.append(x) #Append every Cookie under this rarity
                        #qnaComplete == True
                        return arrayToSend
                    break
                else:
                    print("Doesn't exist.")
            break

        elif desiredRarity == "Type":
            while True:
                desiredRarity2 = input("Okay. What type will it be? ").title()

                if desiredRarity2 in typeCheck:
                    def emptyArray(arrayToSend, whichYear):
                        for x in whichYear: #For every item under the selected year array...
                            if x.type == desiredRarity2: #Only slot in Cookies under the chosen rarity under the array
                                arrayToSend.append(x) #Append every Cookie under this rarity
                        #qnaComplete == True
                        return arrayToSend
                    break
                else:
                    print("Doesn't exist.")
            break

        elif desiredRarity == "Position":
            while True:
                desiredRarity2 = input("Okay. What type will it be? ").title()

                if desiredRarity2 in positionCheck:
                    def emptyArray(arrayToSend, whichYear):
                        for x in whichYear: #For every item under the selected year array...
                            if x.position == desiredRarity2: #Only slot in Cookies under the chosen rarity under the array
                                arrayToSend.append(x) #Append every Cookie under this rarity
                        #qnaComplete == True
                        return arrayToSend
                    break
                else:
                    print("Doesn't exist.")
            break
        else:
            print("Try again...") #If not either of the 3 options, ask again (while loop forces answer)

    emptyMan2021 = emptyArray(emptyMan2021, array2021)
    emptyMan2022 = emptyArray(emptyMan2022, array2022)
    emptyMan2023 = emptyArray(emptyMan2023, array2023)
    emptyMan2024 = emptyArray(emptyMan2024, array2024)
    emptyMan2025 = emptyArray(emptyMan2025, array2025)

    rarity2021 = len(emptyMan2021)
    rarity2022 = len(emptyMan2022)
    rarity2023 = len(emptyMan2023)
    rarity2024 = len(emptyMan2024)
    rarity2025 = len(emptyMan2025)

    #Only used when filtering
    print("\n---- Total No. of Cookies released per year, under label ----")
    print(f"From the year 2021, there are {rarity2021} Cookies under the {desiredRarity}: {desiredRarity2} label.")
    print(f"From the year 2022, there are {rarity2022} Cookies under the {desiredRarity}: {desiredRarity2} label.")
    print(f"From the year 2023, there are {rarity2023} Cookies under the {desiredRarity}: {desiredRarity2} label.")
    print(f"From the year 2024, there are {rarity2024} Cookies under the {desiredRarity}: {desiredRarity2} label.")
    print(f"From the year 2025, there are {rarity2025} Cookies under the {desiredRarity}: {desiredRarity2} label.")
    print(f"Total cookies per {desiredRarity}: {desiredRarity2} label - {rarity2021 + rarity2022 + rarity2023 + rarity2024 + rarity2025}\n")

################################

elif myAnswer == "2":
    def cookieNumberCounter(arraySelect, cookieAmount):
        for y in arraySelect:
            cookieAmount += 1
        return cookieAmount

    print("\n---- Total No. of Cookies released per year ----")
    #2021
    cookies2021_Number = cookieNumberCounter(array2021, cookieNumber2021)
    print(f"{cookies2021_Number} Cookies were released in 2021")

    #2022
    cookies2022_Number = cookieNumberCounter(array2022, cookieNumber2022)
    print(f"{cookies2022_Number} Cookies were released in 2022")

    #2023
    cookies2023_Number = cookieNumberCounter(array2023, cookieNumber2023)
    print(f"{cookies2023_Number} Cookies were released in 2023")

    #2024
    cookies2024_Number = cookieNumberCounter(array2024, cookieNumber2024)
    print(f"{cookies2024_Number} Cookies were released in 2024")

    #2025
    cookies2025_Number = cookieNumberCounter(array2025, cookieNumber2025)
    print(f"{cookies2025_Number} Cookies were released in 2025")

    print(f"Total no. of cookies: {cookies2021_Number + cookies2022_Number + cookies2023_Number + cookies2024_Number + cookies2025_Number}\n")

    ####Word Counter per Cookie####
    print("---- Total Words for Each Year ----")

def wordCounterMain(arraySelect, rankingList, totalNoOfWordsYear, yearNumber):
    for x in arraySelect:
        words = re.findall(r'\b\w+\b', x.skill) #Delete all punctuation/symbols for each skill while looping
        word_count = len(words) #Use the len function to count the total no. of words per current Cookie while looping
        #print(f"{x.name}: {word_count} words")
        
        rankingList.append([x.name, word_count]) #Add the current name and their no. of words together at once into the array, hRL
        totalNoOfWordsYear += word_count #Keep adding onto the total word count at the end of each loop
    wordTotalSentence = f"{yearNumber} Cookies have a total of {totalNoOfWordsYear} words, as of now" #Print total word count

    #Reorder by descending word count. Sort by the second element of each Tuple (word count), reverse=True to put in descending order. 
    rankingList.sort(key=lambda x: x[1], reverse=True)
    return rankingList, wordTotalSentence, totalNoOfWordsYear #Return the rankingList list, the sentence to print and the amount of words per each year.

if myAnswer == "1": 
    #2021
    cookies2021_ranked_array, cookies2021_wordTotalSentence, no_2021 = wordCounterMain(emptyMan2021, highestRankingList2021, totalNoOfWords2021, "2021")
    #print(cookies2021_ranked_array)
    print(cookies2021_wordTotalSentence)
    #print(f"{no_2021} DEBUG")

    #2022
    cookies2022_ranked_array, cookies2022_wordTotalSentence, no_2022 = wordCounterMain(emptyMan2022, highestRankingList2022, totalNoOfWords2022, "2022")
    #print(cookies2022_ranked_array)
    print(cookies2022_wordTotalSentence)

    #2023
    cookies2023_ranked_array, cookies2023_wordTotalSentence, no_2023 = wordCounterMain(emptyMan2023, highestRankingList2023, totalNoOfWords2023, "2023")
    #print(cookies2023_ranked_array)
    print(cookies2023_wordTotalSentence)

    #2024
    cookies2024_ranked_array, cookies2024_wordTotalSentence, no_2024 = wordCounterMain(emptyMan2024, highestRankingList2024, totalNoOfWords2024, "2024")
    #print(cookies2024_ranked_array)
    print(cookies2024_wordTotalSentence)

    #2025
    cookies2025_ranked_array, cookies2025_wordTotalSentence, no_2025 = wordCounterMain(emptyMan2025, highestRankingList2025, totalNoOfWords2025, "2025")
    #print(cookies2025_ranked_array)
    print(cookies2025_wordTotalSentence)

    print(f"Total number of words per {desiredRarity} label: {no_2021 + no_2022 + no_2023 + no_2024 + no_2025}")

elif myAnswer == "2":
    #2021
    cookies2021_ranked_array, cookies2021_wordTotalSentence, no_2021 = wordCounterMain(array2021, highestRankingList2021, totalNoOfWords2021, "2021")
    #print(cookies2021_ranked_array)
    print(cookies2021_wordTotalSentence)
    #print(f"{no_2021} DEBUG")

    #2022
    cookies2022_ranked_array, cookies2022_wordTotalSentence, no_2022 = wordCounterMain(array2022, highestRankingList2022, totalNoOfWords2022, "2022")
    #print(cookies2022_ranked_array)
    print(cookies2022_wordTotalSentence)

    #2023
    cookies2023_ranked_array, cookies2023_wordTotalSentence, no_2023 = wordCounterMain(array2023, highestRankingList2023, totalNoOfWords2023, "2023")
    #print(cookies2023_ranked_array)
    print(cookies2023_wordTotalSentence)

    #2024
    cookies2024_ranked_array, cookies2024_wordTotalSentence, no_2024 = wordCounterMain(array2024, highestRankingList2024, totalNoOfWords2024, "2024")
    #print(cookies2024_ranked_array)
    print(cookies2024_wordTotalSentence)

    #2025
    cookies2025_ranked_array, cookies2025_wordTotalSentence, no_2025 = wordCounterMain(array2025, highestRankingList2025, totalNoOfWords2025, "2025")
    #print(cookies2025_ranked_array) #The descending array of based on highest word count. No need to actually print this except for debugging
    print(cookies2025_wordTotalSentence)

    print(f"Total number of words: {no_2021 + no_2022 + no_2023 + no_2024 + no_2025}")

####Placeholder Inserter
def placeholder_insert(target):
     target.insert(0, ["A", "B"]) #Place a fake extra list at the start, to let our loop skip index 0 to properly start at index 1
     #where the content is, to prevent confusion with where x currently is. 
     return target

#Add this fake list to all previous lists
cookies2021_ranked_array = placeholder_insert(cookies2021_ranked_array)
cookies2022_ranked_array = placeholder_insert(cookies2022_ranked_array)
cookies2023_ranked_array = placeholder_insert(cookies2023_ranked_array)
cookies2024_ranked_array = placeholder_insert(cookies2024_ranked_array)
cookies2025_ranked_array = placeholder_insert(cookies2025_ranked_array)

#Create empty arrays for the top 3 to be thrown in here for each year
top3array_2021 = []
top3array_2022 = []
top3array_2023 = []
top3array_2024 = []
top3array_2025 = []

#Update the rarity length due to the fake list ((if you don't, the last cookie will be excluded))
rarity2021 = len(cookies2021_ranked_array)
rarity2022 = len(cookies2022_ranked_array)
rarity2023 = len(cookies2023_ranked_array)
rarity2024 = len(cookies2024_ranked_array)
rarity2025 = len(cookies2025_ranked_array)

#### Actually print the Cookie Names and their Word Count, without the list in the way ####
def cleanFinalRanking(cookieNumber, cookieRankArray, top3array):
    z = 1
    for x in range(cookieNumber): #Loop through the number of Cookies in given year
            if x == 0:
                #Do not do anything for first array, start at 1
                pass

            elif x == 1:
                cookieRankText = f"{cookieRankArray[x][0]}: {cookieRankArray[x][1]} words #{(z)}"
                print(cookieRankText) 

            elif x > 0 and cookieRankArray[x][1] != cookieRankArray[x - 1][1]: 
                z += 1
                cookieRankText = f"{cookieRankArray[x][0]}: {cookieRankArray[x][1]} words #{(z)}"
                print(cookieRankText)

            elif x > 0 and cookieRankArray[x][1] == cookieRankArray[x - 1][1]: #Say we're currently at [2][1], [2 - 1][1]
                cookieRankText = f"{cookieRankArray[x][0]}: {cookieRankArray[x][1]} words #{z}"
                print(cookieRankText)
                #y += 1
                #print(y)
            if z < 4 and x > 0: 
                #If you don't set x > 0, this will start even before the first character has been printed at x = 1
                #Only store all values that are ranked from #1 - #3, based on z
                #print(cookieRankText)
                top3array.append(cookieRankText) #Append the top 3 for the given empty array

#2021
print("\n---- 2021 Cookies ----")
cleanFinalRanking(rarity2021, cookies2021_ranked_array, top3array_2021)

#2022
print("\n---- 2022 Cookies ----")
cleanFinalRanking(rarity2022, cookies2022_ranked_array, top3array_2022)

#2023
print("\n---- 2023 Cookies ----")
cleanFinalRanking(rarity2023, cookies2023_ranked_array, top3array_2023)

#2024
print("\n---- 2024 Cookies ----")
cleanFinalRanking(rarity2024, cookies2024_ranked_array, top3array_2024)

#2025
print("\n---- 2025 Cookies ----")
cleanFinalRanking(rarity2025, cookies2025_ranked_array, top3array_2025)
print("") #Create a new line, 2021 Cookies: Top 3 may not print

#print(" ")
#Print only the top 3 items
def rankingPrinter(finalarray):
    for x in range(len(finalarray)): #Loop through the whole array by index. 
        #make sure range(len()) functions are created, otherwise it can't pull each item by index and work on them individually
        s = finalarray[x] 
        sub = ":" #Split by :
        sub2 = " " #Split by space
        res = s.split(sub)[0]  #Split before the first :, get the name
        res2 = s.split(sub2)[-3] #Split before the third space from the right, get the word count 
        res3 = s[-2:] #Print the last two letters, #1/#2/#3
        #print(res)
        #print(res2)
        #print(res3)
        print(f"{res} has a total of {res2} words and is ranked {res3}")

print("---- 2021 Cookies: Top 3 ----")
rankingPrinter(top3array_2021)

print("\n---- 2022 Cookies: Top 3 ----")
rankingPrinter(top3array_2022)

print("\n---- 2023 Cookies: Top 3 ----")
rankingPrinter(top3array_2023)

print("\n---- 2024 Cookies: Top 3 ----")
rankingPrinter(top3array_2024)

print("\n---- 2025 Cookies: Top 3 ----")
rankingPrinter(top3array_2025)