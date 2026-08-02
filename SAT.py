import customtkinter as ctk
from PIL import Image
import csv
from PIL import Image, ImageGrab
import pywinstyles


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

class TintOverlay(ctk.CTkToplevel):
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
        self.destroy()



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

    def showOverlay(self):
        overlayFrame = ctk.CTkFrame(self, fg_color=colour4, corner_radius=0)
        overlayFrame.place(x=0, y=0, relwidth=1, relheight=1)
        overlayFrame.lift()
        pywinstyles.set_opacity(overlayFrame, value=0.5, color="#000000")

        popupFrame = ctk.CTkFrame(self, fg_color=colour2, width=300, height=200)
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

        btnCancel.pack(pady=2, padx=10)

    def HideOverlay(self, overlayFrame):
        overlayFrame.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

