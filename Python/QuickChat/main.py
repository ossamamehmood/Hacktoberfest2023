from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import Window
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
Window.size = (300,500)

class MainApp(MDApp):
    def on_start(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Teal"
        self.theme_cls.accent_hue = "400"
        self.title = "QuickChat"

    #     self.new_message('Sumit', "Reached Home", "sumit.jpeg")
    #     self.new_message('Eshant',"Bawala ho gaya hai k","eshant.jpeg")
    #     self.new_message('Hardeep',"Bhai eshant se ladai ho gai","hardeep.jpeg")
    #     self.new_message( 'Saksham',"Thanks bro","saksham.jpeg")
    #     self.new_message('Natendar',"Hello","natendar.jpeg")
    #     self.new_message('Owner',"Rent de do bhai","budha.jpg")
    def new_message(self, name, message, image_name):
        new_mesage = TwoLineAvatarIconListItem(text=name, secondary_text=message)
        new_mesage.add_widget(ImageLeftWidget(source=image_name))
        self.root.ids.list.add_widget(new_mesage)
    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        pass

class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

MainApp().run()