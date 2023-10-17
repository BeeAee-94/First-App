# Pacific Racing tips calculator
# Date: 17-10-2023
# @author-Bee

# Import modules and libraries
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivymd.theming import ThemeManager

# Load Kivy file
Builder.load_file('text.kv')

# Set the size of the window
Window.size = (300, 400)

# Define PR class
class MyPR(MDWidget):
    pass

# Define the main class
class PacificRacing(MDApp):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = "Indigo"  # Set the primary color palette
        self.theme_cls.accent_palette = "Amber"   # Set the accent color palette
        self.theme_cls.theme_style = "Light"
        self.title = 'PR Calculator'
        return MyPR()

# Entry point
if __name__ == '__main__':
    PacificRacing().run()
