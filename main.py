from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp

# Setting the app size
Window.size = (450, 650)

# Designation of the kv design file
Builder.load_file("main.kv")


class MyLayout(Widget):
    # Creation of a Button Press Function
    def button_press(self, button):
        # Determination of whether or not self.ids.calc_input.text == 0
        if self.ids.calc_input.text == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text += f'{button}'

    # Creation of a Clear(C) Function
    def clear(self):
        self.ids.calc_input.text = '0'

    # Creation of Major Operands (+, -, /, *) Functions
    def operands(self, sign):
        self.ids.calc_input.text += f'{sign}'

    # Creation of an Evaluation(=) Function
    def equal(self):
        try:
            self.ids.calc_input.text = f'{round(eval(self.ids.calc_input.text),6)}'
        except Exception:
            self.ids.calc_input.text = '0'

    # Creation of a Backspace(<<) Function
    def remove(self):
        if self.ids.calc_input.text == '':
            self.ids.calc_input.text = '0'
        else:
            self.ids.calc_input.text = self.ids.calc_input.text[:-1]

    # Creation of a Decimal(.) Function
    def dot(self):
        # Error!!!
        # Such a problematic piece of code **sigh**
        if self.ids.calc_input.text[-1] in ['.', '+', '-', '/', '*']:
            pass
        elif '.' in self.ids.calc_input.text and self.ids.calc_input.text[-1] in ['+', '-', '/', '*']:
            pass
        else:
            self.ids.calc_input.text += "."

    # Creation of a Toggle(+/-) Function
    def toggle(self):
        if self.ids.calc_input.text == '0':
            pass
        elif self.ids.calc_input.text[0] == '-':
            self.ids.calc_input.text = self.ids.calc_input.text[1:]
        else:
            self.ids.calc_input.text = '-' + self.ids.calc_input.text

    # Creation of a Percentage(%) Function
    def percent(self):
        try:
            self.ids.calc_input.text = str(round(eval(self.ids.calc_input.text) * 0.01, 4))
        except Exception:
            pass


class Calculator(MDApp):
    def build(self):
        self.title = 'Calculator'
        self.icon = 'calculator.png'
        Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


if __name__ == '__main__':
    Calculator().run()
