from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalculatorLayout(BoxLayout):
    def clear(self):
        self.ids.input_box.text = ""

    def delete(self):
        self.ids.input_box.text = self.ids.input_box.text[:-1]

    def add_text(self, value):
        self.ids.input_box.text += value

    def calculate(self):
        try:
            expression = self.ids.input_box.text
            result = str(eval(expression))
            self.ids.input_box.text = result
        except:
            self.ids.input_box.text = "Error"

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()