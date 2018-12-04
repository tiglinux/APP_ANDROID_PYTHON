import kivy


from kivy.uix.label import Label
from kivy.app import App

class MeuAplicativo(App):
    def build(self):
        return Label(text='TIAGOOO!')

if __name__ =='__main__':
    MeuAplicativo().run()
