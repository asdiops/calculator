from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical')
        hl1 = BoxLayout(orientation='horizontal')
        hl2 = BoxLayout(orientation='horizontal')
        hl3 = BoxLayout(orientation='horizontal')
        hl4 = BoxLayout(orientation='horizontal')

        btn1 = Button(text='1')
        btn2= Button(text='2')
        btn3= Button(text='3')
        btn4 = Button(background_color=(0,0,1), text='+')

        btn5 = Button(text='4')
        btn6 = Button(text='5')
        btn7 = Button(text='6')
        btn8 = Button(background_color=(0,0,1), text='-')

        btn9 = Button(text='7')
        btn10 = Button(text='8')
        btn11 = Button(text='9')
        btn12 = Button(background_color=(0,0,1), text='*')

        btn13 = Button(background_color=(1,0,0), text='Clear')
        btn14 = Button(text='0')
        btn15 = Button(background_color=(0,1,0), text='=')
        btn16 = Button(background_color=(0,0,1), text='/')

        self.lbl = Label(text='')

        vl.add_widget(self.lbl)
        vl.add_widget(hl1)
        hl1.add_widget(btn1)
        hl1.add_widget(btn2)
        hl1.add_widget(btn3)
        hl1.add_widget(btn4)
        vl.add_widget(hl2)
        hl2.add_widget(btn5)
        hl2.add_widget(btn6)
        hl2.add_widget(btn7)
        hl2.add_widget(btn8)
        vl.add_widget(hl3)
        hl3.add_widget(btn9)
        hl3.add_widget(btn10)
        hl3.add_widget(btn11)
        hl3.add_widget(btn12)
        vl.add_widget(hl4)
        hl4.add_widget(btn13)
        hl4.add_widget(btn14)
        hl4.add_widget(btn15)
        hl4.add_widget(btn16)

        btn1.on_press = self.wr1
        btn2.on_press = self.wr2
        btn3.on_press = self.wr3
        btn4.on_press = self.wrpls
        btn5.on_press = self.wr4
        btn6.on_press = self.wr5
        btn7.on_press = self.wr6
        btn8.on_press = self.wrmin
        btn9.on_press = self.wr7
        btn10.on_press = self.wr8
        btn11.on_press = self.wr9
        btn12.on_press = self.wrmult
        btn13.on_press = self.clear
        btn14.on_press = self.wr0
        btn15.on_press = self.total
        btn16.on_press = self.wrdiv
        self.add_widget(vl)

    def wr1(self):
        self.lbl.text += '1'
    def wr2(self):
        self.lbl.text += '2'
    def wr3(self):
        self.lbl.text += '3'
    def wrpls(self):
        self.lbl.text += '+'
    def wr4(self):
        self.lbl.text += '4'
    def wr5(self):
        self.lbl.text += '5'
    def wr6(self):
        self.lbl.text += '6'
    def wrmin(self):
        self.lbl.text += '-'
    def wr7(self):
        self.lbl.text += '7'
    def wr8(self):
        self.lbl.text += '8'
    def wr9(self):
        self.lbl.text += '9'
    def wrmult(self):
        self.lbl.text += '*'
    def clear(self):
        self.lbl.text = ''
    def wr0(self):
        self.lbl.text += '0'
    def total(self):
        self.chek()
    def wrdiv(self):
        self.lbl.text += '/'
        
    def chek(self):
        stroka = self.lbl.text
        try:
            result = eval(stroka)
            self.lbl.text = str(result)
        except:
            self.lbl.text = 'Неверный пример'
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen())
        return sm

app = MyApp()
app.run()
