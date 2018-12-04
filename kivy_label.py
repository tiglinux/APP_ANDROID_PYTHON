import kivy


from kivy.uix.label import Label
from kivy.app import App

class Aplicativo(App):
    def build(self):
        return Label(text='TIAGOOO!')

if __name__ =='__main__':
    Aplicativo().run()
