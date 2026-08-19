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
colour7 = "#0E7D54"
textColour1 = "#FFFFFF"
panelColour1 = "#242424"
buttonColour1 = "#6FBF9E"
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
        self.geometry("1440x960")
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
        self.generationFrames()
        

# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------

    def buildSidebar(self):
        self.sidebar = ctk.CTkScrollableFrame(
            self, width=260, fg_color=panelColour1, corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

    # ------------------------------------------------------------------
    # Filter Buttons
    # ------------------------------------------------------------------

        self.filterLabel = ctk.CTkLabel(
            self.sidebar, 
            text="Filters", 
            anchor="w",
            fg_color="transparent", 
            font=("Inter", 20, "bold")
            )

        btnRace = ctk.CTkButton(
            self.sidebar, text="Race", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )
        
        btnClass = ctk.CTkButton(
            self.sidebar, text="Class", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10,

            #, command=button_event
            )
        
        btnBackground = ctk.CTkButton(
            self.sidebar, text="Background", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )
        
        btnPersonality = ctk.CTkButton(
            self.sidebar, text="Personality", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )

        btnAppearance = ctk.CTkButton(
            self.sidebar, text="Appearance", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )
        
        btnAlignment = ctk.CTkButton(
            self.sidebar, text="Alignment", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )
        
        btnSkills = ctk.CTkButton(
            self.sidebar, text="Skills", 
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )
        
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
                    self.sidebar, text="Add", 
                    font=("Inter", 16, "bold"), 
                    fg_color=colour2, 
                    hover_color=colourButtonHover2,
                    border_color=colour7,
                    border_width=2,
                    corner_radius=8, 
                    height=40, 
                    width=120,
                    #anchor="w",
                    border_spacing=10,
                    command=self.showOverlay
                    )
        
        intFilterYPad = 2
        intFilterXPad = 10
        self.filterLabel.pack()
        btnRace.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnClass.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnBackground.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnPersonality.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnAppearance.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnAlignment.pack(pady=intFilterYPad, padx=intFilterXPad)
        btnSkills.pack(pady=intFilterYPad, padx=intFilterXPad)
        self.lblHomebrew.pack(pady=20, padx=intFilterXPad)
        self.HomebrewSidebar()
        btnAdd.pack(pady=2, padx=intFilterXPad, anchor="e")

    def changeAppearanceMode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)   

    def HomebrewSidebar(self):
        self.homebrewEntries = generator.CharacterGenerator().loadHomebrew()
        #print(self.homebrewEntries)
        
        for entry in self.homebrewEntries:
            homebrewBtn = ctk.CTkButton(
                self.sidebar, 
                text=f"{entry['Name']} ({entry['Type']})",
            font=("Inter", 16, "bold"), 
            fg_color=colour6, 
            hover_color=colourButtonHover,
            corner_radius=8, 
            height=40, 
            width=240,
            anchor="w",
            border_spacing=10  
            #, command=button_event
            )
            homebrewBtn.pack(pady=2, padx=10) 

    def showOverlay(self):
        self.overlayFrame = ctk.CTkFrame(self, fg_color="#000000", corner_radius=0)
        self.overlayFrame.place(x=0, y=0, relwidth=1, relheight=1)
        self.overlayFrame.lift()
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
        strName = generator.CharacterGenerator().NameGeneration()
        dctClass = generator.CharacterGenerator().generateTrait("Traits/ClassTraits.csv", [])
        dctRace = generator.CharacterGenerator().generateTrait("Traits/RaceTraits.csv", [])
    


        strClassName = dctClass["Class"]
        strRaceName = dctRace["Race"]
#-------------------------------------------------------------------------------------------------------------------
        rowFrame = ctk.CTkFrame(self.topBar, fg_color="transparent")
        rowFrame.pack(side="left", padx=20, pady=5, anchor="w")

        nameRow = ctk.CTkFrame(rowFrame, fg_color="transparent")
        nameRow.pack(side="top", anchor="w")
        

        lblName = ctk.CTkLabel(
            nameRow,    
            text=strName,
            font=("Inter", 50, "bold")
        )
        lblName.pack(side="left")

        traitRow = ctk.CTkFrame(rowFrame, fg_color="transparent")
        traitRow.pack(side="left", anchor="w")

        lblRace = ctk.CTkLabel(
            traitRow,
            text=strRaceName,
            font=("Inter", 20, "bold")
        )
        lblRace.pack(pady=0, side="left", padx=5)

        lblClass = ctk.CTkLabel(
            traitRow,
            text=strClassName,
            font=("Inter", 20, "bold")
        )
        lblClass.pack(pady=0, side="left", padx=5)

    def generationFrames(self):

        self.frmGenerationFrame = ctk.CTkFrame(self, fg_color="transparent")
        self.frmGenerationFrame.pack(side="top", padx=0, pady=0, anchor="w")

        row1 = ctk.CTkFrame(self.frmGenerationFrame, fg_color="transparent")
        row1.pack(side="top", fill="x", anchor="w")

        dctStats = generator.CharacterGenerator().statGeneration()

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
                text=value, 
                anchor="w",
                fg_color="transparent", 
                font=("Inter", 60, "bold")
                )
            lblStatValue.pack(pady=5, anchor="center")

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

        self.frmMiniGenerationFrame = ctk.CTkFrame(row3, fg_color="transparent")
        self.frmMiniGenerationFrame.pack(side="top", padx=0, pady=0, anchor="w")

        miniRow1 = ctk.CTkFrame(self.frmMiniGenerationFrame, fg_color="transparent")
        miniRow1.pack(side="top", anchor="w")

        self.frmAllignment = ctk.CTkFrame(
            miniRow1, width=250, 
            height=140, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmAllignment.pack(side="left", padx=30, pady=15)
        self.frmAllignment.pack_propagate(False)

        self.frmAllignment.configure(height=150)

        miniRow2 = ctk.CTkFrame(self.frmMiniGenerationFrame, fg_color="transparent")
        miniRow2.pack(side="top", anchor="w")
        

        self.frmNotes = ctk.CTkScrollableFrame(
            miniRow2, width=250, 
            height=140, 
            fg_color=panelColour1, 
            corner_radius=8,
            border_width=3,
            border_color=colour7
            )
        self.frmNotes.pack_propagate(False)
        self.frmNotes.pack(side="left", padx=30, pady=0)
        
        

        






        


if __name__ == "__main__":
    app = App()
    app.mainloop()

