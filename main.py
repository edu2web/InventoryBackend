import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('your-private-key.json', scope)
client = gspread.authorize(creds)
iQue_sheet = client.open("InventoryBackend").get_worksheet(1)

#root layout
class InventoryWindow(Screen):
    pass

#Layout in question
class AddPartWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.np = []


    #Is there anything else I need to do with these before saving into a list or dictionary?
    
    part_name = ObjectProperty(None)
    serial_number = ObjectProperty(None)
    on_hand_cnt = ObjectProperty(None)
    min_needed = ObjectProperty(None)

    #This function should save the user input into a list, np, and then append to the google sheet iQue_sheet
    #Wasn't sure if it should be a list or a dictionary.
    #I'm assuming .text is type-casting each object to a string.  Can this be used for numerical inputs?
    
    def new_part(self):
        self.part_name = self.ids.part_name.text
        self.serial_number = self.ids.serial_number.text
        self.on_hand_cnt = self.ids.on_hand_cnt.text
        self.min_needed = self.ids.min_needed.text

        self.np = [self.part_name, self.serial_number, self.on_hand_cnt, self.min_needed]
        iQue_sheet.append_row(self.np)

class OnOrderWindow(Screen):
    pass

class OrderFormWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class InventoryApp(App):
    def build(self):
        #These are used to enable going back and forth between screens using buttons
        sm = ScreenManager()
        sm.add_widget(InventoryWindow(name='inv_window'))
        sm.add_widget(OnOrderWindow(name='on_order_window'))
        sm.add_widget(AddPartWindow(name='add_part_window'))
        sm.add_widget(OrderFormWindow(name='order_form_window'))
        return sm

if __name__ == "__main__":
    InventoryApp().run()
