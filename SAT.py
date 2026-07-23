import customtkinter as ctk
from PIL import Image
import csv

colour1 = "#2E3A35"
colour2 = "#1A2420"
colour3 = "#2B463B"
colour4 = "#000000"
colour5 = "#873F30"
colour6 = "#3B6E5E"
colourButtonHover = "#30594c"
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



class App(ctk.CTk):
    """
    This is the main GUI class for module

    saveCSV is a def statement that takes the
    
    
    
    """
    def __init__(self):
        super().__init__()
 
        self.title("D&D Character Generator")
        self.geometry("1440x960")
        self.appearanceMode = ctk.get_appearance_mode()
        if self.appearanceMode == "Dark":
            bg = backgroundImage(self, "forestBackground.png")
            bg.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.appearanceMode == "Light":
            bg = backgroundImage(self, "BFG.jpeg")
            bg.place(x=0, y=0, relwidth=1, relheight=1)

        #bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.buildSidebar()

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

    def changeAppearanceMode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def loadHomebrewFromCSV(self, filePath="HomebrewValues.csv"):
        lstHomebrewEntries = []
        try:
            with open(filePath, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    lstHomebrewEntries.append(row)
        except FileNotFoundError:
            pass
        print(lstHomebrewEntries)
        return lstHomebrewEntries

    def HomebrewSidebar(self):
        self.homebrewEntries = self.loadHomebrewFromCSV()
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

if __name__ == "__main__":
    app = App()
    app.mainloop()

