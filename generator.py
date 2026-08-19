import csv
from pyclbr import Class
import random

#sortedList = sorted(List)
#Remember for later

class CharacterGenerator():
    def __init__(self):
        self.raceLocation = "Traits/RaceTraits.csv"
        self.classLocation = "Traits/ClassTraits.csv"
        self.backgroundLocation = "Traits/Background Traits.csv"
        self.HomebrewLocation = "Traits/HomebrewTraits.csv"
        self.NameLocation = "Traits/NameTraits.csv"
        self.PersonalityLocation = "Traits/PersonalityTraits.csv"
        self.AppearanceLocation = "Traits/AppearanceTraits.csv"

    def generateTrait(self, fileLocation, traitSet):
        location = fileLocation
        if location is None:
            raise ValueError(f"File location not found")

        lstEntries = []
        try:
            with open(location, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    lstEntries.append(row)
        except FileNotFoundError:
            pass

        try:
            with open("Traits/HomebrewValues.csv", newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Type"] == traitSet:
                        lstEntries.append(row)
        except FileNotFoundError:
            pass

        #print(lstEntries)
        roll = random.randint(1, len(lstEntries)) - 1
        traitValue = lstEntries[roll]
        #print(roll)
        #print(len(lstRaceEntries))
        #print(raceValue)
        return traitValue

    # ------------------------------------------------------------------
    # Functions to generate each trait type.
    # ------------------------------------------------------------------

    def generateRace(self):
        return self.generateTrait(self.raceLocation, "Race")

    def generateClass(self):
        return self.generateTrait(self.classLocation, "Class")

    def generateBackground(self):
        return self.generateTrait(self.backgroundLocation, "Background")

    def generateHomebrew(self):
        return self.generateTrait(self.HomebrewLocation, "Homebrew")

    def generateName(self):
        return self.generateTrait(self.NameLocation, "Name")

    def generatePersonality(self):
        return self.generateTrait(self.PersonalityLocation, "Personality")

    def generateAppearance(self):
        return self.generateTrait(self.AppearanceLocation, "Appearance")

    

    def statGeneration(self):
        """
        This function generates a random stat value between 1 and 18 for each of the six ability scores.
        This will be done by rolling 4d6 and dropping the lowest die. This will be done for each of the six ability scores.
        """
        abilityScores = {}
        for ability in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            abilityScores[ability] = sum(rolls)
        return abilityScores

    def alignmentGeneration(self):
        """
        This function generates a random alignment for the character.
        This will be done by rolling a d9 and assigning an alignment based on the roll.
        """
        intRoll1 = random.randint(1, 3)
        intRoll2 = random.randint(1, 3)
        axis1 = ["Lawful", "Neutral", "Chaotic"]
        axis2 = ["Good", "Neutral", "Evil"]
        characterAlignment = axis1[intRoll1 - 1] + " " + axis2[intRoll2 - 1]
        return characterAlignment

    def NameGeneration(self):
        """
        This function generates a random name for the character.
        This will be done by rolling a d6 and assigning a name based on the roll.
        """
        location = "Traits/NameTraits.csv"
        lstEntries = []
        try:
            with open(location, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    lstEntries.append(row)
        except FileNotFoundError:
            pass
        roll = random.randint(1, len(lstEntries)) - 1
        nameValue = lstEntries[roll]
        nameString = nameValue["Name"]
        #print(roll)
        #print(len(lstEntries))
        #print(nameValue)
        return nameString

    def addHomebrew(self, type, name):
        """
        This function adds a homebrew trait to the HomebrewValues.csv file.
        This will be done by appending a new row to the CSV file with the type and name of the homebrew trait.
        """
        with open("Traits/HomebrewValues.csv", "a", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Type", "Name"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"Type": type, "Name": name})

    def editHomebrew(self, oldType, oldName, newType, newName):
        """
        This function edits a homebrew trait in the HomebrewValues.csv file.
        This will be done by reading the CSV file and writing a new CSV file with the updated values.
        """
        fieldnames = ["Type", "Name"]
        lstEntries = []
        try:
            with open("Traits/HomebrewValues.csv", newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Type"] == oldType and row["Name"] == oldName:
                        row["Type"] = newType
                        row["Name"] = newName
                    lstEntries.append(row)
        except FileNotFoundError:
            pass

    def deleteHomebrew(self, type, name):
        """
        This function deletes a homebrew trait from the HomebrewValues.csv file.
        This will be done by reading the CSV file and writing a new CSV file without the deleted values.
        """
        fieldnames = ["Type", "Name"]
        lstEntries = []
        try:
            with open("Traits/HomebrewValues.csv", newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Type"] == type and row["Name"] == name:
                        continue
                    lstEntries.append(row)
        except FileNotFoundError:
            pass

    def applyFilters(self, traitSet, filters):
        #left here as placeholder
        pass

    def loadHomebrew(self, filePath="Traits/HomebrewValues.csv"):
        lstHomebrewEntries = []
        try:
            with open(filePath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    lstHomebrewEntries.append(row)
        except FileNotFoundError:
            pass
        #print(lstHomebrewEntries)
        lstSortedHomebrewList = sorted(lstHomebrewEntries, key=lambda x: x['Name'])
        return lstSortedHomebrewList


    

if __name__ == "__main__":
    """
    2/08/26 This is a test to see if the CharacterGenerator class is working correctly.

    Expected Value is roll between 1 and 6
    Test 1-4: Recieved Value is between 1 and 6 with a cap of 6, the number of races in the RaceTraits.csv file

    Working as expected.

    CharacterGenerator().generateRace()
    """

    """
    2/08/26 This is a test to see if the alignmentGeneration function is working correctly.
    Expected Value is a string of the form "Lawful Good", "Neutral Evil", etc.

    Test 1: Lawful Evil
    Test 2: Lawful Neutral
    Test 3: Neutral Evil
    Test 4: Chaotic Evil
    Test 5: Neutral Good

    Working as expected.
    
    print(CharacterGenerator().alignmentGeneration())
    """

    """
    2/08/26 This is a test to see if the statGeneration function is working correctly.
    Expected Value is a dictionary with the keys "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", and "Charisma" and values between 3 and 18.
    Test 1: {'Strength': 8, 'Dexterity': 9, 'Constitution': 16, 'Intelligence': 9, 'Wisdom': 15, 'Charisma': 16}
    Test 2: {'Strength': 15, 'Dexterity': 16, 'Constitution': 12, 'Intelligence': 12, 'Wisdom': 12, 'Charisma': 14}

    Working as expected.

    print(CharacterGenerator().statGeneration())
    """

    """
    2/08/26 This is a test to see if the generateTrait function is working correctly.
    Expected Value is a dictionary with the keys being the column names of the CSV file and the values being the values of the randomly selected row. Values in CSV files and placeholders and subject to change.
    Test 1: {'Race': 'Halfling', 'AbilitySoreBonus': '+2 Dexterity', 'Speed': '25', 'Size': 'Small', 'Traits': 'Lucky; Brave; Halfling Nimbleness'}
    Test 2: {'Race': 'Human', 'AbilitySoreBonus': '+1 to all stats', 'Speed': '30', 'Size': 'Medium', 'Traits': 'Extra skill proficiency and feat at level 1'}

    print(CharacterGenerator().generateRace())

    Test 3: {'Background': 'Acolyte', 'SkillProficiencies': 'Insight Religion', 'Languages': '2 of choice', 'Equipment': 'Holy symbol prayer book vestments', 'Feature': 'Shelter of the Faithful'}
    Test 4: {'Background': 'Sage', 'SkillProficiencies': 'Arcana History', 'Languages': '2 of choice', 'Equipment': 'Ink quill small knife letter from a colleague', 'Feature': 'Researcher'}

    print(CharacterGenerator().generateBackground())

    Test 5: 'Abasolo': 'Mauldwin'
        Forgot a line in the Name CSV, so the name of the column is the first name in the CSV.
    Test 6: {'Name': 'Purkey'}

    Seems to be working as expected.
    """

    """
        13/08/26 This is test to see if the addHomebrew function is working correctly.
        Expected Result is a new row in the HomebrewValues.csv file with the type and name of the homebrew trait.

        CharacterGenerator().addHomebrew("Race", "Dragonborn")
        Test 1: Resulted added to HomebrewValues.csv file with the type "Race" and name "Dragonborn"

        Works and expected.
        """