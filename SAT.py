import customtkinter as ctk
from PIL import Image
import csv
from PIL import Image, ImageDraw, ImageGrab
import pywinstyles
import generator


colour1 = "#2E3A35"
colour2 = "#1A2420"
colour3 = "#2B463B"
colour4 = "#000000"
colour5 = "#873F30"
colour6 = "#3B6E5E"
colourButtonHover = "#30594c"
colourButtonHover2 = "#07412B"
colourButtonHover3 = "#BB5E4B"
colour7 = "#0E7D54"
textColour1 = "#FFFFFF"
panelColour1 = "#242424"
buttonColour1 = "#62BD97"
buttonColour2 = "#E2725B"

ctk.set_appearance_mode("dark")

class backgroundImage(ctk.CTkLabel):
    def __init__(self, master, image_path):
        super().__init__(master, text="")
        self.imagePath = image_path
        self.pillowImage = Image.open(self.imagePath)
        self.bind("<Configure>", self.resizeImage)

    def resizeImage(self, event):
        newSize = (event.width, event.height)
        if newSize[0] <= 0 or newSize[1] <= 0:
            return
        resized = self.pillowImage.resize(newSize)
        self.ctk_image = ctk.CTkImage(
            light_image=resized, dark_image=resized, size=newSize
        )
        self.configure(image=self.ctk_image)

'''class TintOverlay(ctk.CTkToplevel):
    def __init__(self, master, opacity=0.4, tint_colour=colour4):
        super().__init__(master)
        self.master = master

        self.overrideredirect(True)     # no title bar/borders
        self.attributes("-alpha", opacity)   # true transparency
        self.configure(fg_color=tint_colour)

        self.attributes("-topmost", True)
        self.matchGeometry()
        self.master.bind("<Configure>", self.matchGeometry, add="+")

    def matchGeometry(self, event=None):
        # keep overlay locked to the main window's size/position
        x = self.master.winfo_x()
        y = self.master.winfo_y()
        w = self.master.winfo_width()
        h = self.master.winfo_height()
        self.geometry(f"{w}x{h}+{x}+{y}")

    def close(self):
        self.master.unbind("<Configure>")
        self.destroy()'''

class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

class App(ctk.CTk):
    """
    This is the main GUI class for module

    saveCSV is a def statement that takes the
    
    
    
    """
    def __init__(self):
        super().__init__()

        self.title("D&D Character Generator")
        self.geometry("1440x1000")
        """self.appearanceMode = ctk.get_appearance_mode()
        if self.appearanceMode == "Dark":
            self.bg = backgroundImage(self, "forestBackground.png")
            self.bg.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.appearanceMode == "Light":
            self.bg = backgroundImage(self, "BFG.jpeg")
            self.bg.place(x=0, y=0, relwidth=1, relheight=1)"""
        self.configure(fg_color="#000000")

        #bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.buildSidebar()
        self.nameFrame()
        self.statFrames()
        self.generationFrames()
    
        

# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------

    def buildSidebar(self):
        self.sidebar = ctk.CTkScrollableFrame(
            self, width=260, fg_color=panelColour1, corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

        self.filterLabel = ctk.CTkLabel(
            self.sidebar, text="Filters", anchor="w",
            fg_color="transparent", font=("Inter", 20, "bold")
        )
        self.filterLabel.pack()

        characterList = generator.CharacterGenerator().generateClassList()
        raceList = generator.CharacterGenerator().generateRaceList()
        backgroundList = generator.CharacterGenerator().generateBackgroundList()
        appearanceList = generator.CharacterGenerator().generateAppearanceList()
        allignmentList = generator.CharacterGenerator().generateAllignmentList()
        skillsList = generator.CharacterGenerator().generateSkillList()

        self.buildDropdown(self.sidebar, "Race", raceList)
        self.buildDropdown(self.sidebar, "Class", characterList)
        self.buildDropdown(self.sidebar, "Personality", backgroundList)
        self.buildDropdown(self.sidebar, "Appearance", appearanceList)
        self.buildDropdown(self.sidebar, "Alignment", allignmentList)
        self.buildDropdown(self.sidebar, "Skills", skillsList)
        
    # ------------------------------------------------------------------
    # Homebrew Buttons
    # ------------------------------------------------------------------

        self.lblHomebrew = ctk.CTkLabel(
            self.sidebar, 
            text="Homebrew", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
            )

        btnAdd = ctk.CTkButton(
                    self.sidebar, text="Add New", 
                    font=("Inter", 18, "bold"), 
                    fg_color=buttonColour1, 
                    hover_color=colourButtonHover2,
                    border_color=colour7,
                    border_width=3,
                    corner_radius=8, 
                    height=40, 
                    width=120,
                    anchor="w",
                    border_spacing=10,
                    command=self.showOverlay
                    )
        
        intFilterYPad = 2
        intFilterXPad = 10
        self.filterLabel.pack()

        """
        btnRace.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnClass.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnBackground.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnPersonality.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnAppearance.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnAlignment.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnSkills.pack(pady=intFilterYPad, padx=intFilterXPad)
        """

        self.lblHomebrew.pack(pady=20, padx=intFilterXPad)
        self.HomebrewSidebar()
        btnAdd.pack(pady=2, padx=intFilterXPad, anchor="w")

    def buildDropdown(self, parent, title, options):    
        frmDropdown = ctk.CTkFrame(parent, fg_color="transparent")
        frmDropdown.pack(fill="x", padx=10, pady=2)

        contentFrame = ctk.CTkFrame(frmDropdown, fg_color=colour3)

        toggleBtn = ctk.CTkButton(
            frmDropdown, text=f"{title}  ▾",
            font=("Inter", 16, "bold"),
            fg_color=colour6, hover_color=colourButtonHover,
            corner_radius=8, height=40, width=240,
            anchor="w", border_spacing=10,
            command=lambda: self.toggleDropdown(toggleBtn, contentFrame, title)
        )
        toggleBtn.pack()

        if not hasattr(self, "filterCheckboxes"):
            self.filterCheckboxes = {}
        self.filterCheckboxes[title] = {}

        for option in options:
            chk = ctk.CTkCheckBox(
                contentFrame, text=option,
                font=("Inter", 14)
            )
            chk.pack(anchor="w", padx=20, pady=2)
            self.filterCheckboxes[title][option] = chk   

    def toggleDropdown(self, button, contentFrame, title):
        if contentFrame.winfo_ismapped():
            contentFrame.pack_forget()
            button.configure(text=f"{title}  ▾")
        else:
            contentFrame.pack(fill="x")
            button.configure(text=f"{title}  ▴")

    def changeAppearanceMode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)   

    def HomebrewSidebar(self):
        self.homebrewEntries = generator.CharacterGenerator().loadHomebrew()

        for entry in self.homebrewEntries:
            self.buildHomebrewDropdown(self.sidebar, entry) 

    def buildHomebrewDropdown(self, parent, entry):
        frmDropdown = ctk.CTkFrame(parent, fg_color="transparent")
        frmDropdown.pack(fill="x", padx=10, pady=2)

        contentFrame = ctk.CTkFrame(frmDropdown, fg_color=colour3)

        title = f"{entry['Name']} ({entry['Type']})"
        toggleBtn = ctk.CTkButton(
            frmDropdown, text=f"{title}  ▾",
            font=("Inter", 16, "bold"),
            fg_color=colour6, hover_color=colourButtonHover,
            corner_radius=8, height=40, width=240,
            anchor="w", border_spacing=10,
            command=lambda: self.toggleDropdown(toggleBtn, contentFrame, title)
        )
        toggleBtn.pack()

        lblDesc = ctk.CTkLabel(
            contentFrame, 
            text=entry.get("Description", ""),
            font=("Inter", 14),
            wraplength=220, 
            justify="left", 
            anchor="w"
        )
        lblDesc.pack(anchor="w", padx=20, pady=(5, 5))

        btnEdit = ctk.CTkButton(
            contentFrame, text="Edit", 
            font=("Inter", 18, "bold"), 
            fg_color=colour2, 
            hover_color=colourButtonHover2,
            border_color=buttonColour1,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=120,
            anchor="w",
            border_spacing=10,
            command=self.showOverlay
            )
        btnEdit.pack(side="right", anchor="w", padx=5, pady=(5, 5))

    def showOverlay(self):
        self.overlayFrame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.overlayFrame.place(x=0, y=0, relwidth=1, relheight=1)
        self.overlayFrame.lift()
        #For some reason shows an error, cannot find i way to prevent this, however works completely as intended
        pywinstyles.set_opacity(self.overlayFrame, value=0.9, color="#000001")

        """popupFrame = ctk.CTkFrame(self, fg_color=colour2, width=300, height=200)
        popupFrame.place(relx=0.5, rely=0.5, anchor="center")
        popupFrame.pack_propagate(False)
        popupFrame.lift()

        btnCancel = ctk.CTkButton(
            popupFrame, text="Alignment", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10,
            command=lambda: self.HideOverlay(overlayFrame)
            )

        btnCancel.pack(pady=2, padx=10)"""

    def HideOverlay(self, overlayFrame):
        overlayFrame.destroy()

    def nameFrame(self):
        self.topBar = ctk.CTkFrame(
            self, 
            height=92, 
            fg_color=panelColour1, 
            corner_radius=0
        )
        self.topBar.pack(side="top", fill="x")
        self.topBar.pack_propagate(False)
#-------------------------------------------------------------------------------------------------------------------
        """strName = generator.CharacterGenerator().NameGeneration()
        dctClass = generator.CharacterGenerator().generateTrait("Traits/ClassTraits.csv", [])
        dctRace = generator.CharacterGenerator().generateTrait("Traits/RaceTraits.csv", [])
    


        strClassName = dctClass["Class"]
        strRaceName = dctRace["Race"]"""
#-------------------------------------------------------------------------------------------------------------------
        rowFrame = ctk.CTkFrame(self.topBar, fg_color="transparent")
        rowFrame.pack(side="left", padx=20, pady=5, anchor="w")

        nameRow = ctk.CTkFrame(rowFrame, fg_color="transparent")
        nameRow.pack(side="top", anchor="w")
        

        self.lblName = ctk.CTkLabel(
            nameRow,    
            text="Name",
            font=("Inter", 50, "bold")
        )
        self.lblName.pack(side="left")

        traitRow = ctk.CTkFrame(rowFrame, fg_color="transparent")
        traitRow.pack(side="left", anchor="w")

        self.lblRace = ctk.CTkLabel(
            traitRow,
            text="Race",
            font=("Inter", 20, "bold")
        )
        self.lblRace.pack(pady=0, side="left", padx=5)

        self.lblClass = ctk.CTkLabel(
            traitRow,
            text="Class",
            font=("Inter", 20, "bold")
        )
        self.lblClass.pack(pady=0, side="left", padx=5)

    def statFrames(self):

        self.frmGenerationFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.frmGenerationFrame.pack(side="top", padx=0, pady=0, anchor="w")

        row1 = ctk.CTkFrame(self.frmGenerationFrame, fg_color="transparent")
        row1.pack(side="top", fill="x", anchor="w")

        dctStats = generator.CharacterGenerator().statGeneration()
        self.lblStatValues = {}

        for i, (key, value) in enumerate(dctStats.items()):
            row1.columnconfigure(i, weight=1, uniform="statcol")

            self.statBox = ctk.CTkFrame(
                row1, width=100, 
                height=125, 
                fg_color=panelColour1, 
                corner_radius=8,
                border_width=3,
                border_color=colour7
                )
            self.statBox.grid(row=0, column=i, padx=30, pady=15, sticky="nsew")
            self.statBox.pack_propagate(False)

            lblStatName = ctk.CTkLabel(
                self.statBox, 
                text=key, 
                anchor="w",
                fg_color="transparent", 
                font=("Inter", 15, "bold")
                )
            lblStatName.pack(pady=5, anchor="center")

            lblStatValue = ctk.CTkLabel(
                self.statBox, 
                text="", 
                anchor="w",
                fg_color="transparent", 
                font=("Inter", 60, "bold")  
                )
            lblStatValue.pack(pady=5, anchor="center")
            self.lblStatValues[key] = lblStatValue

    def generationFrames(self):

        row2 = ctk.CTkFrame(self.frmGenerationFrame, fg_color="transparent")
        row2.pack(side="top", anchor="w")

        self.frmClassDetails = ctk.CTkScrollableFrame(
            row2, width=500, 
            height=300, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmClassDetails.pack(side="left", padx=30)
        self.frmClassDetails.pack_propagate(False)

        self.frmBackground = ctk.CTkScrollableFrame(
            row2, width=500, 
            height=300, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmBackground.pack(side="left", padx=30)
        self.frmBackground.pack_propagate(False)

        row3 = ctk.CTkFrame(self.frmGenerationFrame, fg_color="transparent")
        row3.pack(side="top", anchor="w")

        self.frmAppearance = ctk.CTkScrollableFrame(
            row3, width=500, 
            height=300, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmAppearance.pack(side="left", padx=30, pady=20)
        self.frmAppearance.pack_propagate(False)

        self.frmSkills = ctk.CTkScrollableFrame(
            row3, width=200, 
            height=300, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmSkills.pack(side="left", padx=30, pady=20)
        self.frmSkills.pack_propagate(False)

        """self.frmMiniGenerationFrame = ctk.CTkFrame(row3, fg_color="transparent")
        self.frmMiniGenerationFrame.pack(side="top", padx=0, pady=0, anchor="w")"""

        self.frmMiniGenerationFrame = ctk.CTkFrame(row3, fg_color="transparent")
        self.frmMiniGenerationFrame.pack(side="left", anchor="n", padx=30, pady=20)

        miniRow1 = ctk.CTkFrame(self.frmMiniGenerationFrame, fg_color="transparent")
        miniRow1.pack(side="top", anchor="w", pady=(0, 10))

        self.frmAllignment = ctk.CTkFrame(
            miniRow1, width=250, 
            height=160, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmAllignment.pack(side="left")
        #no idea why but this and Notes need gid propagation, they break elsewise
        self.frmAllignment.grid_propagate(False)

        miniRow2 = ctk.CTkFrame(self.frmMiniGenerationFrame, fg_color="transparent")
        miniRow2.pack(side="top", anchor="w")
        

        self.frmNotes = ctk.CTkFrame(
            miniRow2, width=250, 
            height=160, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmNotes.grid_propagate(False)
        self.frmNotes.pack(side="left")

        self.GenerationButtons()
        self.generationLabels()
        self.generationInformation()

    def GenerationButtons(self):

        row4 = ctk.CTkFrame(self.frmGenerationFrame, fg_color="transparent")
        row4.pack(side="top", anchor="w", fill = "x")

        self.btnImport =  ctk.CTkButton(
            row4, 
            text="Import", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour1, 
            hover_color=colourButtonHover2,
            border_color=colour7,
            border_width=3,
            corner_radius=8, 
            height=50, 
            width=200,
            anchor="w",
            border_spacing=10,
            #command=self.showOverlay
            )
        self.btnImport.pack(side="left", padx = 20)

        self.btnExport =  ctk.CTkButton(
            row4, 
            text="Export", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour1, 
            hover_color=colourButtonHover2,
            border_color=colour7,
            border_width=3,
            corner_radius=8, 
            height=50, 
            width=200,
            anchor="w",
            border_spacing=10,
            #command=self.showOverlay
            )
        self.btnExport.pack(side="left", padx = 20)

        self.btnGenerate =  ctk.CTkButton(
            row4, 
            text="Generate", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour2, 
            hover_color=colourButtonHover3,
            border_color=colour5,
            border_width=3,
            corner_radius=8, 
            height=50, 
            width=200,
            anchor="w",
            border_spacing=10,
            command=self.generateInformation
            )
        self.btnGenerate.pack(side = "right", padx = 20)

    def generationLabels(self):
        self.lblClassDetails = ctk.CTkLabel(
            self.frmClassDetails, 
            text="Class Details", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 30, "bold")
        )
        self.lblClassDetails.grid(row=0, column=0, sticky="nw", padx=5, pady=0)

        self.lblBackground = ctk.CTkLabel(
            self.frmBackground, 
            text="Background &\nPersonality", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
        )
        self.lblBackground.grid(row=0, column=0, sticky="nw", padx=5, pady=0)

        self.lblAppearance = ctk.CTkLabel(
            self.frmAppearance, 
            text="Appearance", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
        )
        self.lblAppearance.grid(row=0, column=0, sticky="nw", padx=5, pady=0)

        self.lblSkills = ctk.CTkLabel(
            self.frmSkills, 
            text="Skills", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
        )
        self.lblSkills.grid(row=0, column=0, sticky="nw", padx=5, pady=0)

        self.lblNotes = ctk.CTkLabel(
            self.frmNotes, 
            text="Notes", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
        )
        self.lblNotes.grid(row=0, column=0, sticky="nw", padx=10, pady=5)

        self.lblAllignment = ctk.CTkLabel(
            self.frmAllignment, 
            text="Allignment", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
        )
        self.lblAllignment.grid(row=0, column=0, sticky="nw", padx=10, pady=5)

    def generationInformation(self):
        self.lblClassInfo = ctk.CTkLabel(
            self.frmClassDetails, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=460
        )
        self.lblClassInfo.grid(row=1, column=0, sticky="nw", padx=10, pady=0)

        self.lblBackgroundInfo = ctk.CTkLabel(
            self.frmBackground, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=460
        )
        self.lblBackgroundInfo.grid(row=1, column=0, sticky="nw", padx=5, pady=0)

        self.lblAppearanceInfo = ctk.CTkLabel(
            self.frmAppearance, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=460
        )
        self.lblAppearanceInfo.grid(row=1, column=0, sticky="nw", padx=5, pady=0)

        self.lblSkillsInfo = ctk.CTkLabel(
            self.frmSkills, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=230
        )
        self.lblSkillsInfo.grid(row=1, column=0, sticky="nw", padx=5, pady=0)

        self.lblNotesInfo = ctk.CTkLabel(
            self.frmNotes, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=230
        )
        self.lblNotesInfo.grid(row=1, column=0, sticky="nw", padx=10, pady=5)

        self.lblAllignmentInfo = ctk.CTkLabel(
            self.frmAllignment, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=230
        )
        self.lblAllignmentInfo.grid(row=1, column=0, sticky="nw", padx=10, pady=5)

    def generateInformation(self):
        dictFilterSet = self.gatherFiltered()

        strName = generator.CharacterGenerator().NameGeneration()
        dctClass = generator.CharacterGenerator().generateClass(dictFilterSet["Class"])
        dctRace = generator.CharacterGenerator().generateRace(dictFilterSet["Race"])
        dctStats = generator.CharacterGenerator().statGeneration()
        dctBackground = generator.CharacterGenerator().generateBackground(dictFilterSet["Personality"])
        dctPersonality = generator.CharacterGenerator().generatePersonality(dictFilterSet["Personality"])
        dctAppearance = generator.CharacterGenerator().generateAppearance(dictFilterSet["Appearance"])
        strAlignment = generator.CharacterGenerator().alignmentGeneration()

        """strClassName = dctClass["Class"]
        strRaceName = dctRace["Race"]
        strClassDescription=dctClass["Description"]
        strRaceDescription=dctRace["Description"]"""
        

        self.lblName.configure(text=strName)
        self.lblRace.configure(text=dctRace["Race"])
        self.lblClass.configure(text=dctClass["Class"])

        for key, value in dctStats.items():
            self.lblStatValues[key].configure(text=value)

        self.lblClassInfo.configure(text=dctClass["Description"])
        self.lblBackgroundInfo.configure(
            text=f"{dctBackground['Background']}\n\n{dctPersonality['Personality']}")
        self.lblAppearanceInfo.configure(text=dctAppearance["Appearance"])
        #print(dctAppearance)
        self.lblAllignmentInfo.configure(text=strAlignment)

    def gatherFiltered(self):
        dictEntries = {}

        for category, checkboxDict in self.filterCheckboxes.items():
            dictEntries[category] = [
                option for option, chk in checkboxDict.items() if chk.get() == 1
            ]
        return dictEntries


        
        

        


        
        

        






        


if __name__ == "__main__":
    app = App()
    app.mainloop()