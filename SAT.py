import customtkinter as ctk
from PIL import Image
import csv
from PIL import Image, ImageDraw, ImageGrab
import pywinstyles
import generator
from tkinter import filedialog
import json

# -------------------------------------------------------
# All Colours used repeatedly
# -------------------------------------------------------

colour1 = "#2E3A35"
colour2 = "#1A2420"
colour3 = "#2B463B"
colour4 = "#000000"
colour5 = "#873F30"
colour6 = "#3B6E5E"
colour7 = "#0E7D54"
colour8 = "#2E4A3E"
colourButtonHover = "#30594c"
colourButtonHover2 = "#07412B"
colourButtonHover3 = "#BB5E4B"
colourButtonHover4 = "#569A7E"
textColour1 = "#FFFFFF"
panelColour1 = "#242424"
panelColour2 = "#202A26"
buttonColour1 = "#62BD97"
buttonColour2 = "#E2725B"
buttonColour3 = "#6FBF9E"
textColour1 = "#BCBBBB"
textColour2 = "#E2725B"
textColour3 = "#1A2420"

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
    
        

# ------------------------------------------------------------------------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------------------------------------------------------------------------

    def buildSidebar(self):
        """
        This Function builds the sidebar, creating the label and buttons
        """
        self.sidebar = ctk.CTkScrollableFrame(
            self, width=260, fg_color=panelColour1, corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

        self.filterLabel = ctk.CTkLabel(
            self.sidebar, text="Filters", anchor="w",
            fg_color="transparent", font=("Inter", 20, "bold")
        )
        self.filterLabel.pack()

        self.filterListFrame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.filterListFrame.pack(fill="x")
        self.buildFilterDropdowns()

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

        self.homebrewListFrame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.homebrewListFrame.pack(fill="x")

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
        for widget in self.homebrewListFrame.winfo_children():
            widget.destroy()

        self.homebrewEntries = generator.CharacterGenerator().loadHomebrew()

        for entry in self.homebrewEntries:
             self.buildHomebrewDropdown(self.homebrewListFrame, entry) 

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
            command=lambda:self.showEditOverlay(entry)
            )
        btnEdit.pack(side="right", anchor="w", padx=5, pady=(5, 5))

    def buildFilterDropdowns(self):
        """
        This function is being used to rebuild the dropdown menus used for filtering after a homebrew value is altered
        """

        for widget in self.filterListFrame.winfo_children():
            widget.destroy()

        self.filterCheckboxes = {}

        characterList = generator.CharacterGenerator().generateClassList()
        raceList = generator.CharacterGenerator().generateRaceList()
        backgroundList = generator.CharacterGenerator().generateBackgroundList()
        appearanceList = generator.CharacterGenerator().generateAppearanceList()
        allignmentList = generator.CharacterGenerator().generateAllignmentList()
        skillsList = generator.CharacterGenerator().generateSkillList()

        self.buildDropdown(self.filterListFrame, "Race", raceList)
        self.buildDropdown(self.filterListFrame, "Class", characterList)
        self.buildDropdown(self.filterListFrame, "Personality", backgroundList)
        self.buildDropdown(self.filterListFrame, "Appearance", appearanceList)
        self.buildDropdown(self.filterListFrame, "Alignment", allignmentList)
        self.buildDropdown(self.filterListFrame, "Skills", skillsList)

# ------------------------------------------------------------------------------------------------------------------------------------
# Add Homebrew Popup
# ------------------------------------------------------------------------------------------------------------------------------------

    def tintOverlay(self):
        self.overlayFrame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.overlayFrame.place(x=0, y=0, relwidth=1, relheight=1)
        self.overlayFrame.lift()
        #For some reason shows an error, cannot find a way to prevent this, however works completely as intended with no errors
        pywinstyles.set_opacity(self.overlayFrame, value=0.999, color="#000001")
    
    def showOverlay(self):
        self.tintOverlay()

        self.popupFrame = ctk.CTkFrame(
            self, 
            fg_color=panelColour2, 
            width=1000, 
            height=650,
            corner_radius=12,
            border_width=3,
            border_color=colour8
        )
        self.popupFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.popupFrame.pack_propagate(False)
        self.popupFrame.lift()

        lblTitle = ctk.CTkLabel(
        self.popupFrame, 
        text="Add New Homebrew",
        font=("Inter", 30, "bold")
        )
        lblTitle.pack(side = "top", anchor = "w", padx = 20, pady=(15, 10))

        categoryRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        categoryRow.pack(side="top", anchor="w", padx=20, pady=(0, 2))

        lblCatergoryMain = ctk.CTkLabel(
            categoryRow, 
            text="CATERGORY",
            font=("Inter", 12, "bold"),
            text_color=textColour1
            )
        lblCatergoryMain.pack(side = "left")

        lblCatergorySide = ctk.CTkLabel(
            categoryRow, 
            text="*",
            font=("Inter", 12, "bold"),
            text_color=textColour2
            )
        

        self.categoryOptions = ["Race", "Class", "Background", "Personality", "Appearance", "Alignment", "Skills"]
        self.selectedCategory = ctk.StringVar(value=self.categoryOptions[0])

        categorySelectRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        categorySelectRow.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.categoryDropdown = ctk.CTkOptionMenu(
            categorySelectRow,
            values=self.categoryOptions,
            variable=self.selectedCategory,
            font=("Inter", 16, "bold"),
            fg_color=colour6,
            button_color=colourButtonHover,
            button_hover_color=colourButtonHover2,
            dropdown_fg_color=panelColour1,
            dropdown_hover_color=colourButtonHover,
            corner_radius=8,
            width=963,
            height=39
        )
        self.categoryDropdown.pack()

        nameRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        nameRow.pack(side="top", anchor="w", padx=20, pady=(0, 0))

        lblNameMain = ctk.CTkLabel(
            nameRow, 
            text="NAME",
            font=("Inter", 12, "bold"),
            text_color=textColour1
            )
        lblNameMain.pack(side = "left")

        self.lblNameSide = ctk.CTkLabel(
            nameRow, 
            text="*",
            font=("Inter", 12, "bold"),
            text_color=textColour1
            )   
        self.lblNameSide.pack(side = "left")

        nameEntryRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        nameEntryRow.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.nameEntry = ctk.CTkEntry(
            nameEntryRow, 
            placeholder_text="e.g. Kobold",
            placeholder_text_color=textColour1,
            #placehold_text_font=("Inter", 12, "bold"),
            fg_color="transparent",
            border_color=colour8,
            corner_radius=8,
            width=963,
            height=39
            )
        self.nameEntry.pack()

        descriptionRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        descriptionRow.pack(side="top", anchor="w", padx=20, pady=(0, 0))

        lblDescriptionMain = ctk.CTkLabel(
            descriptionRow, 
            text="NAME",
            font=("Inter", 12, "bold"),
            text_color=textColour1
            )
        lblDescriptionMain.pack(side = "left")

        self.lblDescriptionSide = ctk.CTkLabel(
            descriptionRow, 
            text="*",
            font=("Inter", 12, "bold"),
            text_color=textColour1
            )   
        self.lblDescriptionSide.pack(side = "left")

        descriptionEntryRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        descriptionEntryRow.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.descriptionEntry = ctk.CTkTextbox(
            descriptionEntryRow,
            fg_color="transparent",
            border_color=colour8,
            border_width=2,
            corner_radius=8,
            width=963,
            height=292,
            font=("Inter", 14)
            )
        self.descriptionEntry.pack()

        warningRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        warningRow.pack(side="top", anchor="w", padx=20, pady=(0, 0))

        self.lblWarning = ctk.CTkLabel(
            warningRow, 
            text="THIS FIELD IS REQUIRED*",
            font=("Inter", 12, "bold"),
            text_color=textColour1
            )
        self.lblWarning.pack(side = "left")

        buttonsRow = ctk.CTkFrame(self.popupFrame, fg_color="transparent")
        buttonsRow.pack(side="top", anchor="w", padx=20, pady=(5, 5), fill = "x")

        self.btnAddHomebrew = ctk.CTkButton(
            buttonsRow, 
            text="Add Homebrew", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour3, 
            hover_color=colourButtonHover4,
            border_color=buttonColour3,
            text_color=textColour3,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=176,
            anchor="center",
            border_spacing=10,
            command=self.addHomebrewEntry
        )
        self.btnAddHomebrew.pack(side="right", padx=20) 

        self.btnCancelHomebrew =  ctk.CTkButton(
            buttonsRow, 
            text="Cancel", 
            font=("Inter", 20, "bold"), 
            fg_color=colour8, 
            hover_color=colourButtonHover2,
            border_color=buttonColour3,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=101,
            anchor="center",
            border_spacing=10,
            command=self.hideOverlay
            )
        self.btnCancelHomebrew.pack(side="right", padx = 20)       

        """btnCancel = ctk.CTkButton(
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

    def addHomebrewWarning(self):
        self.lblWarning.configure(text_color = textColour2) #damn merican spelling
        self.lblDescriptionSide.configure(text_color = textColour2) 
        self.lblNameSide.configure(text_color = textColour2) 
        #self.lblWarning.configure(text_color = textColour2) 

    def addHomebrewEntry(self):
        category = self.selectedCategory.get()
        name = self.nameEntry.get()
        description = self.descriptionEntry.get("1.0", "end-1c")

        if name.strip() == "" or description.strip() == "":
            self.addHomebrewWarning()
        else:
            generator.CharacterGenerator().addHomebrew(category, name, description)
            self.hideOverlay()
            self.HomebrewSidebar()
            self.buildFilterDropdowns()

    def hideOverlay(self):
        self.popupFrame.destroy()
        self.overlayFrame.destroy()

# ------------------------------------------------------------------------------------------------------------------------------------
# Edit Homebrew Popup
# ------------------------------------------------------------------------------------------------------------------------------------

    def showEditOverlay(self, editEntry):
        self.tintOverlay()

        self.editPopupFrame = ctk.CTkFrame(
            self, 
            fg_color=panelColour2, 
            width=1000, 
            height=650,
            corner_radius=12,
            border_width=3,
            border_color=colour8
        )
        self.editPopupFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.editPopupFrame.pack_propagate(False)
        self.editPopupFrame.lift()

        lblEditTitle = ctk.CTkLabel(
            self.editPopupFrame, 
            text="Edit Homebrew",
            font=("Inter", 30, "bold")
        )
        lblEditTitle.pack(side="top", anchor="w", padx=20, pady=(15, 10))

        editCategoryRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editCategoryRow.pack(side="top", anchor="w", padx=20, pady=(0, 2))

        lblEditCategoryMain = ctk.CTkLabel(
            editCategoryRow, 
            text="CATERGORY",
            font=("Inter", 12, "bold"),
            text_color=textColour1
        )
        lblEditCategoryMain.pack(side="left")

        lblEditCategorySide = ctk.CTkLabel(
            editCategoryRow, 
            text="*",
            font=("Inter", 12, "bold"),
            text_color=textColour2
        )

        self.editCategoryOptions = ["Race", "Class", "Background", "Personality", "Appearance", "Alignment", "Skills"]
        self.selectedEditCategory = ctk.StringVar(value=editEntry.get("Type", self.editCategoryOptions[0]))

        editCategorySelectRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editCategorySelectRow.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.editCategoryDropdown = ctk.CTkOptionMenu(
            editCategorySelectRow,
            values=self.editCategoryOptions,
            variable=self.selectedEditCategory,
            font=("Inter", 16, "bold"),
            fg_color=colour6,
            button_color=colourButtonHover,
            button_hover_color=colourButtonHover2,
            dropdown_fg_color=panelColour1,
            dropdown_hover_color=colourButtonHover,
            corner_radius=8,
            width=963,
            height=39
        )
        self.editCategoryDropdown.pack()

        editNameRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editNameRow.pack(side="top", anchor="w", padx=20, pady=(0, 0))

        lblEditNameMain = ctk.CTkLabel(
            editNameRow, 
            text="NAME",
            font=("Inter", 12, "bold"),
            text_color=textColour1
        )
        lblEditNameMain.pack(side="left")

        self.lblEditNameSide = ctk.CTkLabel(
            editNameRow, 
            text="*",
            font=("Inter", 12, "bold"),
            text_color=textColour1
        )   
        self.lblEditNameSide.pack(side="left")

        editNameEntryRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editNameEntryRow.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.editNameEntry = ctk.CTkEntry(
            editNameEntryRow, 
            placeholder_text="e.g. Kobold",
            placeholder_text_color=textColour1,
            fg_color="transparent",
            border_color=colour8,
            corner_radius=8,
            width=963,
            height=39
        )
        self.editNameEntry.pack()
        self.editNameEntry.insert(0, editEntry.get("Name", ""))

        editDescriptionRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editDescriptionRow.pack(side="top", anchor="w", padx=20, pady=(0, 0))

        lblEditDescriptionMain = ctk.CTkLabel(
            editDescriptionRow, 
            text="DESCRIPTION",
            font=("Inter", 12, "bold"),
            text_color=textColour1
        )
        lblEditDescriptionMain.pack(side="left")

        self.lblEditDescriptionSide = ctk.CTkLabel(
            editDescriptionRow, 
            text="*",
            font=("Inter", 12, "bold"),
            text_color=textColour1
        )   
        self.lblEditDescriptionSide.pack(side="left")

        editDescriptionEntryRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editDescriptionEntryRow.pack(side="top", anchor="w", padx=20, pady=(0, 5))

        self.editDescriptionEntry = ctk.CTkTextbox(
            editDescriptionEntryRow,
            fg_color="transparent",
            border_color=colour8,
            border_width=2,
            corner_radius=8,
            width=963,
            height=292,
            font=("Inter", 14)
        )
        self.editDescriptionEntry.pack()
        self.editDescriptionEntry.insert("1.0", editEntry.get("Description", ""))

        editWarningRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editWarningRow.pack(side="top", anchor="w", padx=20, pady=(0, 0))

        self.lblEditWarning = ctk.CTkLabel(
            editWarningRow, 
            text="THIS FIELD IS REQUIRED*",
            font=("Inter", 12, "bold"),
            text_color=textColour1
        )
        self.lblEditWarning.pack(side="left")

        editButtonsRow = ctk.CTkFrame(self.editPopupFrame, fg_color="transparent")
        editButtonsRow.pack(side="top", anchor="w", padx=20, pady=(5, 5), fill="x")

        self.btnSaveHomebrew = ctk.CTkButton(
            editButtonsRow, 
            text="Save Changes", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour3, 
            hover_color=colourButtonHover4,
            border_color=buttonColour3,
            text_color=textColour3,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=176,
            anchor="center",
            border_spacing=10,
            command=lambda: self.editHomebrewEntry(editEntry)
        )
        self.btnSaveHomebrew.pack(side="right", padx=20) 

        self.btnCancelEditHomebrew = ctk.CTkButton(
            editButtonsRow, 
            text="Cancel", 
            font=("Inter", 20, "bold"), 
            fg_color=colour8, 
            hover_color=colourButtonHover2,
            border_color=buttonColour3,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=101,
            anchor="center",
            border_spacing=10,
            command=self.hideEditOverlay
        )
        self.btnCancelEditHomebrew.pack(side="right", padx=20)

        self.btnDeleteHomebrew = ctk.CTkButton(
            editButtonsRow, 
            text="Delete", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour2, 
            hover_color=colourButtonHover3,
            border_color=colour5,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=137,
            anchor="center",
            border_spacing=10,
            command=lambda: self.deleteOverlay(editEntry)
        )
        self.btnDeleteHomebrew.pack(side="left", padx=(5, 0))

        """(
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
            )"""

    def addEditHomebrewWarning(self):
        self.lblEditWarning.configure(text_color=textColour2)
        self.lblEditDescriptionSide.configure(text_color=textColour2)
        self.lblEditNameSide.configure(text_color=textColour2)

    def editHomebrewEntry(self, editEntry):
        category = self.selectedEditCategory.get()
        name = self.editNameEntry.get()
        description = self.editDescriptionEntry.get("1.0", "end-1c")

        if name.strip() == "" or description.strip() == "":
            self.addEditHomebrewWarning()
        else:
            generator.CharacterGenerator().editHomebrew(
                editEntry["Type"], editEntry["Name"], category, name, description
            )
            self.hideEditOverlay()
            self.HomebrewSidebar()
            self.buildFilterDropdowns()

    def hideEditOverlay(self):
        self.editPopupFrame.destroy()
        self.overlayFrame.destroy()

# ------------------------------------------------------------------------------------------------------------------------------------
# Are You Sure about Deleting the Value Homebrew Popup
# ------------------------------------------------------------------------------------------------------------------------------------

    def deleteOverlay(self,editEntry):
        self.editPopupFrame.destroy()

        self.deleteFrame = ctk.CTkFrame(
            self, 
            fg_color=panelColour2, 
            width=600, 
            height=170,
            corner_radius=12,
            border_width=3,
            border_color=colour8
        )
        self.deleteFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.deleteFrame.pack_propagate(False)
        self.deleteFrame.lift()

        lblEditTitle = ctk.CTkLabel(
            self.deleteFrame, 
            text="Are You Sure?",
            font=("Inter", 30, "bold")
        )
        lblEditTitle.pack(side="top", anchor="w", padx=20, pady=(15, 10))

        buttonRow = ctk.CTkFrame(self.deleteFrame, fg_color="transparent")
        buttonRow.pack(side="bottom", anchor="w", padx=10, pady=(0, 10), fill = "x")

        self.btnConfirmDelete = ctk.CTkButton(
            buttonRow, 
            text="Pretty Sure", 
            font=("Inter", 20, "bold"), 
            fg_color=buttonColour2, 
            hover_color=colourButtonHover3,
            border_color=colour5,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=166,
            anchor="center",
            border_spacing=10,
            command=lambda: self.deleteHomebrewEntry(editEntry)
        )
        self.btnConfirmDelete.pack(side="right", padx=(0, 0))

        self.btnCancelEditHomebrew = ctk.CTkButton(
            buttonRow, 
            text="Cancel", 
            font=("Inter", 20, "bold"), 
            fg_color=colour8, 
            hover_color=colourButtonHover2,
            border_color=buttonColour3,
            border_width=3,
            corner_radius=8, 
            height=40, 
            width=101,
            anchor="center",
            border_spacing=10,
            command=self.hideDeleteOverlay
        )
        self.btnCancelEditHomebrew.pack(side="left", padx=0)

    def hideDeleteOverlay(self):
        self.deleteFrame.destroy()
        self.overlayFrame.destroy()

    def deleteHomebrewEntry(self, editEntry):
        generator.CharacterGenerator().deleteHomebrew(editEntry["Type"], editEntry["Name"], editEntry["Description"])
        self.hideDeleteOverlay()
        self.HomebrewSidebar()
        self.buildFilterDropdowns()
    
# ------------------------------------------------------------------------------------------------------------------------------------
# Functions to create the boxes when Generation will occur
# ------------------------------------------------------------------------------------------------------------------------------------

    def nameFrame(self):
        """
        This function builds a frame at the top of the screen and everything inside of it
        """
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

        self.entryName = ctk.CTkEntry(nameRow, font=("Inter", 40, "bold"), width=400)
        self.entryRace = ctk.CTkEntry(traitRow, font=("Inter", 20, "bold"), width=150)
        self.entryClass = ctk.CTkEntry(traitRow, font=("Inter", 20, "bold"), width=150)

        self.isEditingName = False

        self.editIcon = ctk.CTkImage(
            light_image=Image.open("icons/editIcon.png"),
            dark_image=Image.open("icons/editIcon.png"),
            size=(64, 64)
            )

        self.saveIcon = ctk.CTkImage(
            light_image=Image.open("icons/saveIcon.png"),
            dark_image=Image.open("icons/saveIcon.png"), 
            size=(64, 64))
        
        self.btnEditName = ctk.CTkButton(
            self.topBar,
            image=self.editIcon,
            text="",
            fg_color="transparent",
            hover_color=colourButtonHover2,
            width=40,
            height=40,
            command=self.toggleNameEdit
        )
        self.btnEditName.pack(side="right", padx=20)
        
    def statFrames(self):

        self.frmGenerationFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.frmGenerationFrame.pack(side="top", padx=0, pady=0, anchor="w")

        row1 = ctk.CTkFrame(self.frmGenerationFrame, fg_color="transparent")
        row1.pack(side="top", fill="x", anchor="w")

        dctStats = generator.CharacterGenerator().statGeneration()
        self.lblStatValues = {}
        self.entryStatValues = {}

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

            entryStatValue = ctk.CTkEntry(
                self.statBox, font=("Inter", 30, "bold"),
                justify="center", width=80
            )
            self.entryStatValues[key] = entryStatValue

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
            command=self.importCharacter
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
            command=self.exportCharacter
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

        self.txtClassInfo = ctk.CTkTextbox(
            self.frmClassDetails, 
            font=("Inter", 16, "bold"),
            width=460, 
            height=200, 
            fg_color="transparent"  
            )

        self.lblBackgroundInfo = ctk.CTkLabel(
            self.frmBackground, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=460
        )
        self.lblBackgroundInfo.grid(row=1, column=0, sticky="nw", padx=5, pady=0)

        self.txtBackgroundInfo = ctk.CTkTextbox(
            self.frmBackground, 
            font=("Inter", 16, "bold"),
            width=460, 
            height=200, 
            fg_color="transparent"  
            )

        self.lblAppearanceInfo = ctk.CTkLabel(
            self.frmAppearance, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=460
        )
        self.lblAppearanceInfo.grid(row=1, column=0, sticky="nw", padx=5, pady=0)

        self.txtAppearanceInfo = ctk.CTkTextbox(
            self.frmAppearance, 
            font=("Inter", 16, "bold"),
            width=460, 
            height=200, 
            fg_color="transparent"  
            )

        self.lblSkillsInfo = ctk.CTkLabel(
            self.frmSkills, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=230
        )
        self.lblSkillsInfo.grid(row=1, column=0, sticky="nw", padx=5, pady=0)

        self.txtSkillsInfo = ctk.CTkTextbox(
            self.frmSkills, 
            font=("Inter", 16, "bold"),
            width=460, 
            height=200, 
            fg_color="transparent"  
            )

        self.lblNotesInfo = ctk.CTkLabel(
            self.frmNotes, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=200
        )
        self.lblNotesInfo.grid(row=1, column=0, sticky="nw", padx=10, pady=5)

        self.txtNotesInfo = ctk.CTkTextbox(
            self.frmNotes, 
            font=("Inter", 16, "bold"),
            width=200, 
            height=100, 
            fg_color="transparent"  
            )

        self.lblAllignmentInfo = ctk.CTkLabel(
            self.frmAllignment, 
            text="", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 16, "bold"),
            wraplength=230
        )
        self.lblAllignmentInfo.grid(row=1, column=0, sticky="nw", padx=10, pady=5)

        self.txtAllignmentInfo = ctk.CTkTextbox(
            self.frmAllignment, 
            font=("Inter", 16, "bold"),
            width=200, 
            height=100, 
            fg_color="transparent"  
            )

# ------------------------------------------------------------------------------------------------------------------------------------
# Actually Generating the Character
# ------------------------------------------------------------------------------------------------------------------------------------

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

# ------------------------------------------------------------------------------------------------------------------------------------
# Importing and Exporting
# ------------------------------------------------------------------------------------------------------------------------------------
    def exportCharacter(self):
        character = {
        "Name": self.lblName.cget("text"),
        "Race": self.lblRace.cget("text"),
        "Class": self.lblClass.cget("text"),
        "Stats": {key: lbl.cget("text") for key, lbl in self.lblStatValues.items()},
        "ClassInfo": self.lblClassInfo.cget("text"),
        "BackgroundInfo": self.lblBackgroundInfo.cget("text"),
        "AppearanceInfo": self.lblAppearanceInfo.cget("text"),
        "AllignmentInfo": self.lblAllignmentInfo.cget("text"),
        }

        filePath = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json")],
            initialfile=f"{character['Name']}.json"
        )
        if filePath:
            with open(filePath, "w", encoding="utf-8") as f:
                json.dump(character, f, indent=2)

    def importCharacter(self):
        filePath = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")]
        )
        if not filePath:
            return

        with open(filePath, "r", encoding="utf-8") as f:
            character = json.load(f)

        self.lblName.configure(text=character.get("Name", ""))
        self.lblRace.configure(text=character.get("Race", ""))
        self.lblClass.configure(text=character.get("Class", ""))

        for key, value in character.get("Stats", {}).items():
            if key in self.lblStatValues:
                self.lblStatValues[key].configure(text=value)

        self.lblClassInfo.configure(text=character.get("ClassInfo", ""))
        self.lblBackgroundInfo.configure(text=character.get("BackgroundInfo", ""))
        self.lblAppearanceInfo.configure(text=character.get("AppearanceInfo", ""))
        self.lblAllignmentInfo.configure(text=character.get("AllignmentInfo", ""))
# ------------------------------------------------------------------------------------------------------------------------------------
# Editing
# ------------------------------------------------------------------------------------------------------------------------------------

    def toggleNameEdit(self):
        if self.isEditingName == False:

            for key in self.lblStatValues:
                self.entryStatValues[key].insert(0, self.lblStatValues[key].cget("text"))
                self.lblStatValues[key].pack_forget()
                self.entryStatValues[key].pack(pady=5, anchor="center")

            for lbl, txt in [
                (self.lblClassInfo, self.txtClassInfo),
                (self.lblBackgroundInfo, self.txtBackgroundInfo),
                (self.lblAppearanceInfo, self.txtAppearanceInfo),
                (self.lblSkillsInfo, self.txtSkillsInfo),
                (self.lblNotesInfo, self.txtNotesInfo),
                (self.lblAllignmentInfo, self.txtAllignmentInfo),
            ]:
                txt.insert("1.0", lbl.cget("text"))
                lbl.grid_remove()
                txt.grid(row=1, column=0, sticky="nw", padx=10, pady=0)
    
            self.entryName.insert(0, self.lblName.cget("text"))
            self.entryRace.insert(0, self.lblRace.cget("text"))
            self.entryClass.insert(0, self.lblClass.cget("text"))

            self.lblName.pack_forget()
            self.entryName.pack(side="left")

            self.lblRace.pack_forget()
            self.entryRace.pack(side="left", padx=5)

            self.lblClass.pack_forget()
            self.entryClass.pack(side="left", padx=5)

            self.isEditingName = True
            self.btnEditName.configure(image=self.saveIcon)
        else:
            for key in self.lblStatValues:
                self.lblStatValues[key].configure(text=self.entryStatValues[key].get())
                self.entryStatValues[key].delete(0, "end")
                self.entryStatValues[key].pack_forget()
                self.lblStatValues[key].pack(pady=5, anchor="center")

            for lbl, txt in [
                (self.lblClassInfo, self.txtClassInfo),
                (self.lblBackgroundInfo, self.txtBackgroundInfo),
                (self.lblAppearanceInfo, self.txtAppearanceInfo),
                (self.lblSkillsInfo, self.txtSkillsInfo),
                (self.lblNotesInfo, self.txtNotesInfo),
                (self.lblAllignmentInfo, self.txtAllignmentInfo),
            ]:
                lbl.configure(text=txt.get("1.0", "end-1c"))
                txt.delete("1.0", "end")
                txt.grid_remove()
                lbl.grid()

            self.lblName.configure(text=self.entryName.get())

            self.lblName.configure(text=self.entryName.get())
            self.lblRace.configure(text=self.entryRace.get())
            self.lblClass.configure(text=self.entryClass.get())

            self.entryName.delete(0, "end")
            self.entryRace.delete(0, "end")
            self.entryClass.delete(0, "end")

            self.entryName.pack_forget()
            self.lblName.pack(side="left")

            self.entryRace.pack_forget()
            self.lblRace.pack(pady=0, side="left", padx=5)

            self.entryClass.pack_forget()
            self.lblClass.pack(pady=0, side="left", padx=5)

            self.isEditingName = False
            self.btnEditName.configure(image=self.editIcon)
        

if __name__ == "__main__":
    app = App()
    app.mainloop()