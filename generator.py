import csv
from pyclbr import Class
import random

#sortedList = sorted(List)
#Remember for later

class CharacterGenerator():
    """
    This class is used to generate a random character for the DnD Character Generator.

    Arguments:
        None

    Methods:
        _init_(self): 
            Initializes the class and sets the file locations for the CSV files.

        generateTrait(self, fileLocation, traitSet, filterSet):
            Generates a random trait from a specified CSV file.
        
        generateFeatureList(self, fileLocation, traitSet):
            Builds a descriptive appearance sentence for a given race.

        generateAppearanceValue(self, filterSet):
            Generates a descriptive appearance sentence for a given race.
 
# ------------------------------------------------------------------------------------------------------------------------------------
# Functions to generate each trait type.
# ------------------------------------------------------------------------------------------------------------------------------------
 
        generateRace(self, filterSet):
            Generates a single random race trait.
 
        generateClass(self, filterSet):
            Generates a single random class trait.
 
        generateBackground(self, filterSet):
            Generates a single random background trait.
 
        generateHomebrew(self):
            Generates a single random Homebrew trait entry.
 
        generateName(self):
            Generates a single random name trait.
 
        generatePersonality(self, filterSet):
            Generates a single random personality trait.
 
        generateAppearance(self, filterSet):
            Generates a single random appearance trait row.
 
        generateApperanceStr(self, traitValue):
            Builds a descriptive appearance sentence for a given race.
 
        generateSkills(self, characterClass, background, filterSet):
            Picks a set of skill proficiencies for a character's class.
 
        loadClassSkills(self):
            Loads skill proficiency options for every class from the class traits CSV.
 
# ------------------------------------------------------------------------------------------------------------------------------------
# Functions to list every available option for each trait type.
# ------------------------------------------------------------------------------------------------------------------------------------
 
        generateRaceList(self):
            Lists every available race name.
 
        generateClassList(self):
            Lists every available class name.
 
        generateBackgroundList(self):
            Lists every available background name.
 
        generateHomebrewList(self):
            Lists every available Homebrew entry name.
 
        generateNameList(self):
            Lists every available name.
 
        generatePersonalityList(self):
            Lists every available personality trait name.
 
        generateAppearanceList(self):
            Lists every race name that has appearance data.
 
        generateAllignmentList(self):
            Lists every possible alignment combination.
 
        generateSkillList(self):
            Lists every possible skill name.
 
# ------------------------------------------------------------------------------------------------------------------------------------
# Random attribute generation.
# ------------------------------------------------------------------------------------------------------------------------------------
 
        statGeneration(self):
            Generates stats scores for a character.
 
        alignmentGeneration(self):
            Generates a random alignment for the character.
 
        NameGeneration(self):
            Generates a random name for the character.
 
# ------------------------------------------------------------------------------------------------------------------------------------
# Homebrew management.
# ------------------------------------------------------------------------------------------------------------------------------------
 
        addHomebrew(self, type, name, description):
            Adds a homebrew trait to the HomebrewValues.csv file.
 
        editHomebrew(self, oldType, oldName, newType, newName, newdescription):
            Edits a homebrew trait in the HomebrewValues.csv file.
 
        deleteHomebrew(self, type, name, description):
            Deletes a homebrew trait from the HomebrewValues.csv file.
 
        applyFilters(self, traitSet, filters):
            Placeholder for future filter-application logic.
 
        loadHomebrew(self, filePath="Traits/HomebrewValues.csv"):
            Loads and alphabetically sorts every Homebrew entry.
 
        homebrewValues(self, traitType):
            Returns the name of all Homebrew values matching a given type.

    """
    def __init__(self):
        self.raceLocation = "Traits/RaceTraits.csv"
        self.classLocation = "Traits/ClassTraits.csv"
        self.backgroundLocation = "Traits/BackgroundTraits.csv"
        self.HomebrewLocation = "Traits/HomebrewTraits.csv"
        self.NameLocation = "Traits/NameTraits.csv"
        self.PersonalityLocation = "Traits/PersonalityTraits.csv"
        self.AppearanceLocation = "Traits/AppearanceTraits.csv"

    def generateTrait(self, fileLocation, traitSet, filterSet):
        """
        Generates a random trait from a specified csv file.

        Args:
            self: The instance of the CharacterGenerator class.
            fileLocation: Path to the CSV file.
            traitSet: The trait category name.
            filterSet: A list of allowed values to restrict entries to.
 
        Returns:
            dict: The randomly selected trait row.
 
        Raises:
            ValueError: If fileLocation is None.
        """
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
                        # Normalize so it matches the official CSV's key shape
                        normalizedRow = {
                            traitSet: row["Name"],
                            "Description": row.get("Description", "")
                        }
                        lstEntries.append(normalizedRow)
        except FileNotFoundError:
            pass

        if filterSet:
            lstEntries = [row for row in lstEntries if row[traitSet] in filterSet]  

        #print(lstEntries)
        roll = random.randint(1, len(lstEntries)) - 1
        traitValue = lstEntries[roll]
        #print(roll)
        #print(len(lstRaceEntries))
        #print(traitValue)
        return traitValue

    def generateFeatureList(self, fileLocation, traitSet):
        """
        This function will create the dictonary from generateTrait but return the entire thing allowing the filters to pull from all possible options.
        """
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
                        # Normalize so it matches the official CSV's key shape
                        normalizedRow = {
                            traitSet: row["Name"],
                            "Description": row.get("Description", "")
                        }
                        lstEntries.append(normalizedRow)
        except FileNotFoundError:
            pass
        return lstEntries
        
    def generateAppearanceValue(self, filterSet):
        """
        Generates a appearance sentence for a given race.

        Args:
            self: The instance of the CharacterGenerator class.
            filterSet: the dictonary of filters to apply to the appearance generation.

        Returns:
            str: A descriptive appearance sentence for the given race.

        Raises:
            ValueError: If the Appearance CSV file is not found or if no entries match the filter
        """
        lstEntries = []
        try:
            try:
                with open(self.AppearanceLocation, newline='', encoding='utf-8-sig') as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if row['Race'] == filterSet:
                            lstEntries.append(row)

            except FileNotFoundError:
                pass

            dctRow = lstEntries[0]

            dctChosen = {}
            for strKey in ("HairColour", "SkinTone", "EyeColour", "Height", "Build", "DistinguishingFeature"):
                lstOptions = dctRow[strKey].split("|")
                dctChosen[strKey] = random.choice(lstOptions)

            return dctRow["SentenceTemplate"].format(**dctChosen)
        except:
            return "An excited adventurer, ready to begin their journey."
        #return lstEntries

    def createFilteredAppearance(self, appearanceFilters, Race):
        """
        Generates a descriptive appearance sentence for a given race, applying any specified filters.

        Args:
            self: The instance of the CharacterGenerator class.
            appearanceFilters: A dictionary containing filters for appearance traits.
            Race: The race of the character.

        Returns:
            str: A descriptive appearance sentence for the given race, with filters applied.
            
        Raises:
            ValueError: If the Appearance CSV file is not found or if no entries match the filter
        """
        appearanceOptions = self.generateAppearanceDict()
        try:
            dctChosen = {}
            for strKey, lstOptions in appearanceFilters.items():
                #if lstOptions:
                #    dctChosen[strKey] = random.choice(lstOptions)
                lstAvailable = lstOptions if lstOptions else appearanceOptions[strKey]
                dctChosen[strKey] = random.choice(lstAvailable)

            return (f"A {dctChosen['Height']}, {dctChosen['Build']} {Race} with "
                    f"{dctChosen['Skin Tone']} skin, {dctChosen['Hair Colour']} hair, "
                    f"and {dctChosen['Eye Colour']} eyes. Bearing "
                    f"{dctChosen['Distinguishing Feature']}.")
        except:
            #print("error")
            print(appearanceFilters)
            return "An Error Occured"


    # ------------------------------------------------------------------
    # Functions to generate each trait type.
    # ------------------------------------------------------------------

    def generateRace(self, filterSet):
        """
        Generates a single random race trait.

        Args:
            self: The instance of the CharacterGenerator class.
            filterSet: A list of allowed race values to restrict entries to.

        Returns:
            dict: The randomly selected race trait row.

        Raises:
            ValueError: If the Race CSV file is not found or if no entries match the filter
        """
        return self.generateTrait(self.raceLocation, "Race", filterSet)

    def generateClass(self, filterSet):
        """
        Generates a single random class trait.

        Args:
            self: The instance of the CharacterGenerator class.
            filterSet: A list of allowed class values to restrict entries to.

        Returns:
            dict: The randomly selected class trait row.

        Raises:
            ValueError: If the Class CSV file is not found or if no entries match the filter
        """
        return self.generateTrait(self.classLocation, "Class", filterSet)

    def generateBackground(self, filterSet):
        """
        Generates a single random background trait.

        Args:
            self: The instance of the CharacterGenerator class.
            filterSet: A list of allowed background values to restrict entries to.

        Returns:
            dict: The randomly selected background trait row.

        Raises:
            ValueError: If the Background CSV file is not found or if no entries match the filter
        """
        return self.generateTrait(self.backgroundLocation, "Background", filterSet)

    def generateHomebrew(self):
        """
        Generates a single random homebrew trait.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            dict: The randomly selected homebrew trait row.
        """
        return self.generateTrait(self.HomebrewLocation, "Homebrew", [])

    def generateName(self):
        """
        Generates a single random name trait.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            dict: The randomly selected name trait row.
        """
        return self.generateTrait(self.NameLocation, "Name", [])

    def generatePersonality(self, filterSet):
        """
        Generates a single random personality trait.

        Args:
            self: The instance of the CharacterGenerator class.
            filterSet: A list of allowed personality values to restrict entries to.

        Returns:
            dict: The randomly selected personality trait row.

        Raises:
            ValueError: If the Personality CSV file is not found or if no entries match the filter
        """
        return self.generateTrait(self.PersonalityLocation, "Personality", filterSet)

    def generateAppearance(self, filterSet):
        """
        Generates a single random appearance trait.

        Args:
            self: The instance of the CharacterGenerator class.
            filterSet: A list of allowed appearance values to restrict entries to.

        Returns:
            dict: The randomly selected appearance trait row.

        Raises:
            ValueError: If the Appearance CSV file is not found or if no entries match the filter
        """
        return self.generateTrait(self.AppearanceLocation, "Race", filterSet)

    def generateApperanceStr(self, traitValue):
        """
        Generates a descriptive appearance sentence for a given race.

        Args:
            self: The instance of the CharacterGenerator class.
            traitValue: The race value for which to generate the appearance description.    

        Returns:
            str: A descriptive appearance sentence for the given race.
        """
        return self.generateAppearanceValue(traitValue)
    
    def generateSkills(self, characterClass, background, filterSet):
        """
        Picks a set of skill proficiencies for a character's class. 
    
        Args:
            self: The instance of the CharacterGenerator class.
            characterClass: The class of the character for which to generate skills.
            background: The background of the character for which to generate skills.
            filterSet: A list of allowed skill values to restrict entries to.

        Returns:
            list: A list of the selected skill proficiencies.
        """
        """
        lstEntries = []
        skillList = self.generateSkillList()
        skillNumbers = random.sample(range(0, len(skillList)), 4)
        #return self.unique_numbers
        for each in skillNumbers:
            skillValue = skillList[each]
            lstEntries.append(skillValue)
        return lstEntries"""
        try:
            classData = self.loadClassSkills()
            classInfo = classData.get(characterClass)

            skillPool = classInfo["skillOptions"]
            numToPick = classInfo["numChoices"]

            #lstEntries = random.sample(skillPool, numToPick)

            if filterSet:
                filteredSkills = [skill for skill in skillPool if skill in filterSet]
                if filteredSkills:
                    skillPool = filteredSkills

            numToPick = min(numToPick, len(skillPool))
            chosenSkills = random.sample(skillPool, numToPick)

        except:
            chosenSkills = []
            skillList = self.generateSkillList()

            if filterSet:
                filteredList = [skill for skill in skillList if skill in filterSet]
                if filteredList:
                    skillList = filteredList

            numToPick = min(4, len(skillList))
            skillNumbers = random.sample(range(0, len(skillList)), numToPick)
            for each in skillNumbers:
                skillValue = skillList[each]
                chosenSkills.append(skillValue)

        try:
            backgroundData = self.loadBackgroundSkills()
            backgroundSkills = backgroundData.get(background, [])
        except:
            backgroundSkills = []

        lstEntries = list(dict.fromkeys(chosenSkills + backgroundSkills))

        return lstEntries

        #return lstEntries


        #return self.generateTrait(self.AppearanceLocation, "Appearance", filterSet)

    def loadClassSkills(self):
        """
        Loads the skill proficiency options for every class from the Class traits CSV.
        
        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            dict: A dictionary where each key is a class name and the value is another dictionary containing the description, skill options, and number of choices for that class.

        Raises:
            ValueError: If the Class CSV file is not found.
        """
        classData = {}
        with open("Traits/ClassTraits.csv", newline='', encoding='utf-8') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                classData[row["Class"]] = {
                    "description": row["Description"],
                    "skillOptions": row["Proficiency"].split(";"),
                    "numChoices": int(row["NumChoices"])
                }
        return classData

    def loadBackgroundSkills(self):
        """
        Loads the fixed skill proficiencies granted by each background
        from the Background traits CSV (semicolon-separated skill names).

        Args:
            backgroundSkills: The instance of the CharacterGenerator class.

        Returns:
            dict: A dictionary where each key is a background name and the value is a list of skill proficiencies granted by that background.

        Raises:
            ValueError: If the Background CSV file is not found.
        """
        backgroundSkills = {}
        with open(self.backgroundLocation, newline='', encoding='utf-8') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                backgroundSkills[row["Background"]] = [
                    skill.strip() for skill in row["SkillProficiencies"].split(";") if skill.strip()
                ]
        return backgroundSkills



    
    # ------------------------------------------------------------------
    # Functions to generate each trait type.
    # ------------------------------------------------------------------
    def generateAppearanceDict(self):
        """
        Generates a dictionary of appearance traits and their possible values.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            dict: A dictionary where each key is an appearance trait and the value is a list of
            possible values for that trait.

        Raises:
            ValueError: If the Appearance CSV file is not found.
        """
        appearanceDictionary = {
                        "Hair Colour": ["Black", "Blonde", "Brown", "Curly red", "Dark red", "Deep purple", "Grey", "None (scaled head)", "Pale grey", "Red", "Sandy blonde", "Silver", "White"],
                        "Skin Tone": ["Ashen grey", "Black scales", "Bronze scales", "Charcoal", "Dark blue", "Dark brown", "Dark grey", "Deep purple", "Fair", "Gold scales", "Golden brown", "Green scales", "Jet black", "Olive", "Pale", "Red", "Red scales", "Ruddy", "Tanned"],
                        "Eye Colour": ["Amber", "Blue", "Brown", "Dark green", "Gold", "Green", "Grey", "Hazel", "Pale yellow", "Red", "Silver", "Solid black", "Violet"],
                        "Height": ["Average", "Short", "Tall", "Towering"],
                        "Build": ["Athletic", "Muscular", "Slender", "Stocky"],
                        "Distinguishing Feature": ["A deep gravelly voice", "A draconic snout", "A faint magical glow in the eyes", "A long scar across the face", "A long tail", "A pointed tail", "A soot-stained face", "A thick braided beard", "Angular features", "Bare feet with tough soles", "Covered in tattoos", "Curly hair", "Curved horns", "Faintly glowing eyes", "Fine angular features", "Missing a finger", "Perpetually cheerful expression", "Pointed ears", "Sharp elongated teeth", "Small horns"]
                    }
        return appearanceDictionary

    def generateRaceList(self):
        """
        Generates a list of available races.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of race names.

        Raises:
            ValueError: If the Race CSV file is not found.
        """
        rows = self.generateFeatureList(self.raceLocation, "Race")
        return [row["Race"] for row in rows]
    
    def generateClassList(self):
        """
        Generates a list of available classes.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of class names.

        Raises:
            ValueError: If the Class CSV file is not found.
        """
        rows = self.generateFeatureList(self.classLocation, "Class")
        return [row["Class"] for row in rows]

    def generateBackgroundList(self):
        """
        Generates a list of available backgrounds.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of background names.

        Raises:
            ValueError: If the Background CSV file is not found.
        """
        rows = self.generateFeatureList(self.backgroundLocation, "Background")
        return [row["Background"] for row in rows]

    def generateHomebrewList(self):
        """
        Generates a list of available homebrew options.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of homebrew names.

        Raises:
            ValueError: If the Homebrew CSV file is not found.
        """
        rows = self.generateFeatureList(self.HomebrewLocation, "Homebrew")
        return [row["Homebrew"] for row in rows]
    
    def generateNameList(self):
        """
        Generates a list of available names.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of name options.

        Raises:
            ValueError: If the Name CSV file is not found.
        """
        rows = self.generateFeatureList(self.NameLocation, "Name")
        return [row["Name"] for row in rows]

    def generatePersonalityList(self):
        """
        Generates a list of available personalities.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of personality options.

        Raises:
            ValueError: If the Personality CSV file is not found.
        """
        rows = self.generateFeatureList(self.PersonalityLocation, "Personality")
        return [row["Personality"] for row in rows]
    
    def generateAppearanceList(self):
        """
        Generates a list of available appearance traits.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of appearance trait options.

        Raises:
            ValueError: If the Appearance CSV file is not found.
        """
        rows = self.generateFeatureList(self.AppearanceLocation, "Appearance")
        return [row["Appearance"] for row in rows]

    def generateAllignmentList(self):
        """
        Generates a list of all possible alignment combinations.
        
        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of alignment combinations.

        Raises:
            ValueError: If the alignment generation fails.
        """
        axis1 = ["Lawful", "Neutral", "Chaotic"]
        axis2 = ["Good", "Neutral", "Evil"]

        lstEntries = []

        for i in axis1:
            for e in axis2:
                lstEntries.append(f"{i} {e}")

        return lstEntries

    def generateSkillList(self):
        """
        Generates a list of all possible skill names.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            list: A list of skill names.

        Raises:
            ValueError: If the skill list generation fails.
        """
        self.lstSkills = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
        return self.lstSkills
    
    def statGeneration(self):
        """
        This function generates a random stat value between 1 and 18 for each of the six ability scores.
        This will be done by rolling 4d6 and dropping the lowest die. This will be done for each of the six ability scores.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            dict: A dictionary containing the six ability scores and their corresponding values.

        Raises:
            ValueError: If the stat generation fails.
        """
        abilityScores = {}
        for ability in ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]:
            rolls = [random.randint(1, 6) for _ in range(4)]
            rolls.remove(min(rolls))
            abilityScores[ability] = sum(rolls)
        return abilityScores

    def alignmentGeneration(self, filterSet=None):
        """
        This function generates a random alignment for the character.
        This will be done by rolling a d9 and assigning an alignment based on the roll.

        Args:
            self: The instance of the CharacterGenerator class.
        
        Returns:
            str: A string representing the randomly generated alignment.

        Raises:
            ValueError: If the alignment generation fails.
        """
        intRoll1 = random.randint(1, 3)
        intRoll2 = random.randint(1, 3)
        axis1 = ["Lawful", "Neutral", "Chaotic"]
        axis2 = ["Good", "Neutral", "Evil"]
        if filterSet:
            roll = random.randint(1, len(filterSet)) - 1
            traitValue = filterSet[roll]
            return traitValue
        else:
            characterAlignment = axis1[intRoll1 - 1] + " " + axis2[intRoll2 - 1]
            return characterAlignment

    def NameGeneration(self):
        """
        This function generates a random name for the character.
        This will be done by rolling a d6 and assigning a name based on the roll.

        Args:
            self: The instance of the CharacterGenerator class.

        Returns:
            str: A string representing the randomly generated name.

        Raises:
            ValueError: If the name generation fails.
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

    def addHomebrew(self, type, name, description):
        """
        This function adds a homebrew trait to the HomebrewValues.csv file.
        This will be done by appending a new row to the CSV file with the type and name of the homebrew trait.

        Args:
            self: The instance of the CharacterGenerator class. 

        Returns:
            None

        Raises:
            ValueError: If the homebrew addition fails.
        """
        with open("Traits/HomebrewValues.csv", "a", newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Type", "Name", "Description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({"Type": type, "Name": name, "Description": description})

    def editHomebrew(self, oldType, oldName, newType, newName, newdescription):
        """
        This function edits a homebrew trait in the HomebrewValues.csv file.
        This will be done by reading the CSV file and writing a new CSV file with the updated values.

        Args:
            self: The instance of the CharacterGenerator class.
            oldType: The type of the homebrew trait to be edited.
            oldName: The name of the homebrew trait to be edited.
            newType: The new type of the homebrew trait.
            newName: The new name of the homebrew trait.
            newdescription: The new description of the homebrew trait.

        Returns:
            None

        Raises:
            ValueError: If the homebrew editing fails.
        """
        fieldnames = ["Type", "Name", "Description"]
        lstEntries = []
        try:
            with open("Traits/HomebrewValues.csv", newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Type"] == oldType and row["Name"] == oldName:
                        row["Type"] = newType
                        row["Name"] = newName
                        row["Description"] = newdescription
                    lstEntries.append(row)
        except FileNotFoundError:
            pass

        with open("Traits/HomebrewValues.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lstEntries)

    def deleteHomebrew(self, type, name, description):
        """
        This function deletes a homebrew trait from the HomebrewValues.csv file.
        This will be done by reading the CSV file and writing a new CSV file without the deleted values.

        Args:
            self: The instance of the CharacterGenerator class.
            type: The type of the homebrew trait to be deleted.
            name: The name of the homebrew trait to be deleted.
            description: The description of the homebrew trait to be deleted.

        Returns:
            None

        Raises:
            ValueError: If the homebrew deletion fails.
        """
        fieldnames = ["Type", "Name", "Description"]
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

        with open("Traits/HomebrewValues.csv", "w", newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lstEntries)

    def applyFilters(self, traitSet, filters):
        """
        This function applies filters to a given trait set.

        Got deleted and literally does nothing, left to not break anything.
        
        Args:
            self: The instance of the CharacterGenerator class.
            traitSet: The trait set to which the filters will be applied.
            filters: A list of filters to apply to the trait set.

        Returns:
            None

        Raises:
            ValueError: If the filter application fails.
        """
        #left here as placeholder
        pass

    def loadHomebrew(self, filePath="Traits/HomebrewValues.csv"):
        """
        This function loads and alphabetically sorts every Homebrew entry.

        Args:
            self: The instance of the CharacterGenerator class.
            filePath: Path to the Homebrew CSV file.

        Returns:
            list: A list of dictionaries representing the sorted Homebrew entries.

        Raises:
            ValueError: If the Homebrew CSV file is not found.
        """
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

    def homebrewValues(self, traitType):
        """
        returns the name of all Homebrew values matching a given type
        This is used to add icons to homebrew values

        Args:
            self: The instance of the CharacterGenerator class.
            traitType: The type of homebrew values to retrieve.

        Returns:
            set: A set of names of homebrew values matching the given type.

        Raises:
            ValueError: If the homebrew value retrieval fails.
        """
        return {
        entry["Name"] for entry in self.loadHomebrew()
        if entry["Type"] == traitType
        }
    

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
    print(CharacterGenerator().generateAppearanceValue("Drow"))
    