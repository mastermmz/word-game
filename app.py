from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from random import randint
from kivymd.uix.snackbar import Snackbar
from kivy.animation import Animation

# Adjust the page size
Window.size = (700, 400)

Wordgame_helper = """
Screen:

    ScreenManager:
        MenuScreen:
        gameScreen:

<MenuScreen>:
    name:'start' 
    Image:
        id : Image_uotpot
        source : "start.jpg"
    MDRaisedButton:
        text: "start"
        font_size: "25sp"
        pos_hint: {"center_x":0.485, "center_y":0.35}
        on_release :    
            root.manager.transition.direction : 'down'                 
            root.manager.current = 'game'
            app.Light_mood_Scren()
            root.Select_the_word()


<gameScreen>:
    name:"game"
    Image:
        id : Image
        source : ""
        width: 300
    MDToolbar:
        id : toolbar
        pos_hint: {"x":0, "center_y":0.9}
        MDIconButton:
            id : heart_1
            pos_hint: {"x":1, "center_y":0.5}
            icon: "cards-heart"
            user_font_size: "30sp"
        MDIconButton:
            id : heart_2
            pos_hint: {"x":1, "center_y":0.5}
            icon: "cards-heart"
            user_font_size: "30sp"
        MDIconButton:
            id : heart_3
            pos_hint: {"x":1, "center_y":0.5}
            icon: "cards-heart"
            user_font_size: "30sp"
        MDIconButton:
            id : heart_4
            pos_hint: {"x":1, "center_y":0.5}
            icon: "cards-heart"
            user_font_size: "30sp"
        MDIconButton:
            id : heart_5
            pos_hint: {"x":1, "center_y":0.5}
            icon: "cards-heart"
            user_font_size: "30sp" 
            
                       
    MDRaisedButton:
        text: "check"
        pos_hint: {"center_x":0.5, "center_y":0.15}
        on_release : 
            root.check(self , input_Letters , Letters1 , Letters2 , Letters3 , Letters4, Letters5 , toolbar)
              
    MDTextField:
        hint_text: "Fill mode"
        id : input_Letters
        pos_hint: {"center_x":0.5, "center_y":0.3}   
        max_text_length: 1



    MDLabel:
        text: "_" 
        id : Letters1
        pos_hint: {"center_x":0.8, "center_y":0.5}  
        font_size: "50sp" 

    MDLabel:
        id : Letters2
        text: "_"  
        pos_hint: {"center_x":0.9, "center_y":0.5}   
        font_size: "50sp" 
    MDLabel:
        id : Letters3
        text: "_" 
        pos_hint: {"center_x":1.0, "center_y":0.5} 
        font_size: "50sp"       
    MDLabel:
        id : Letters4
        text: "_" 
        pos_hint: {"center_x":1.1, "center_y":0.5} 
        font_size: "50sp" 
        
    MDLabel:
        id : Letters5
        text: "_" 
        pos_hint: {"center_x":1.2, "center_y":0.5} 
        font_size: "50sp"                               
"""


class Variable():
    number_False = 0  # Number of wrong attempts
    number_True = 0
    word = ""


# start Screen
class MenuScreen(Screen):

    def Select_the_word(self):
        with open("words.txt", "r") as file:
            data_file = file.read()
        list_words = data_file.split("\\")
        number_list_words_item = len(list_words)
        number = randint(0, number_list_words_item - 1)
        Variable.word = list_words[number]


# game Screen
class gameScreen(Screen):

    def check(self, widget, input_Letters, Letters1, Letters2, Letters3, Letters4, Letters5, toolbar):
        jumper = 1
        msg = self.ids.input_Letters.text
        word = Variable.word

        if len(msg) == 1:

            check = check_Answer(msg)
            if check:
                if msg in word:

                    list = search_word(word, msg)
                    for i in list:
                        Letters = word[i]
                        if i == 0:
                            self.ids.Letters1.text = Letters
                            Variable.number_True = Variable.number_True + 1
                        if i == 1:
                            self.ids.Letters2.text = Letters
                            Variable.number_True = Variable.number_True + 1
                        if i == 2:
                            self.ids.Letters3.text = Letters
                            Variable.number_True = Variable.number_True + 1
                        if i == 3:
                            self.ids.Letters4.text = Letters
                            Variable.number_True = Variable.number_True + 1
                        if i == 4:
                            self.ids.Letters5.text = Letters
                            Variable.number_True = Variable.number_True + 1
                else:
                    if Variable.number_False == 0 and jumper == 1:
                        self.ids.heart_1.icon = "heart-broken-outline"
                        Variable.number_False = Variable.number_False + 1
                        jumper = 0

                    if Variable.number_False == 1 and jumper == 1:
                        self.ids.heart_2.icon = "heart-broken-outline"
                        Variable.number_False = Variable.number_False + 1
                        jumper = 0

                    if Variable.number_False == 2 and jumper == 1:
                        self.ids.heart_3.icon = "heart-broken-outline"
                        Variable.number_False = Variable.number_False + 1
                        jumper = 0

                    if Variable.number_False == 3 and jumper == 1:
                        self.ids.heart_4.icon = "heart-broken-outline"
                        Variable.number_False = Variable.number_False + 1
                        jumper = 0

                    if Variable.number_False == 4 and jumper == 1:
                        self.ids.heart_5.icon = "heart-broken-outline"
                        Variable.number_False = Variable.number_False + 1
                        jumper = 0

                    if Variable.number_False > 4 and jumper == 1:
                        jumper = 0
            if check == False:
                snak = Snackbar(text="Only letters").open()
        elif len(msg) == 0:
            snak = Snackbar(text="type somting in fild").open()
        else:
            snak = Snackbar(text="Just write one letter").open()

        if Variable.number_True == 5:
            snak = Snackbar(text="you Wine").open()
            self.ids.Image.source = "win.jpg"
            animation_hiden = Animation(
                opacity=0
            )
            animation_hiden.start(widget)
            animation_hiden.start(input_Letters)
            animation_hiden.start(toolbar)
            animation_hiden.start(Letters1)
            animation_hiden.start(Letters2)
            animation_hiden.start(Letters3)
            animation_hiden.start(Letters4)
            animation_hiden.start(Letters5)

        if Variable.number_False == 5:
            snak = Snackbar(text="GAME OVER").open()
            self.ids.Image.source = "gameover.jpg"
            animation_hiden = Animation(
                opacity=0
            )
            animation_hiden.start(widget)
            animation_hiden.start(input_Letters)
            animation_hiden.start(toolbar)
            animation_hiden.start(Letters1)
            animation_hiden.start(Letters2)
            animation_hiden.start(Letters3)
            animation_hiden.start(Letters4)
            animation_hiden.start(Letters5)


def check_Answer(Letters):
    number = "0123456789"
    if Letters in number:
        return False
    else:
        return True


def search_word(word, Letters):
    list_of_number = []
    if Letters in word:
        for i in range(len(word)):
            if Letters == word[i]:
                list_of_number.append(i)

    return list_of_number


sm = ScreenManager()
sm.add_widget(MenuScreen(name='start'))
sm.add_widget(gameScreen(name='game'))


class WordgameApp(MDApp):
    def Light_mood_Scren(self):
        self.theme_cls.theme_style = "Light"  # ['Light', 'Dark']

    def Dark_mood_Screen(self):
        self.theme_cls.theme_style = "Dark"  # ['Light', 'Dark']

    def build(self):
        self.theme_cls.theme_style = "Dark"  # ['Light', 'Dark']
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.primary_hue = "900"
        screen = Builder.load_string(Wordgame_helper)
        return screen


# run App
WordgameApp().run()
