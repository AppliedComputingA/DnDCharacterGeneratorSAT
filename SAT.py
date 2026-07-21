import customtkinter as ctk
from PIL import Image

colour1 = "#2E3A35"
colour2 = "#1A2420"
colour3 = "#2B463B"
colour4 = "#000000"
colour5 = "#873F30"
colour6 = "#3B6E5E"
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
        bg = backgroundImage(self, "forestBackground.png")
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        self.buildSidebar()

    def buildSidebar(self):
        self.sidebar = ctk.CTkScrollableFrame(
            self, width=260, fg_color=colour6, corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")




if __name__ == "__main__":
    app = App()
    app.mainloop()