from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class ClickCounterApp(App):
    def build(self):
        self.counter = 0

        # Tworzenie układu
        layout = BoxLayout(orientation='vertical')

        # Tworzenie etykiety
        self.label = Label(text='Kliknięcia: 0', font_size=24)
        layout.add_widget(self.label)

        # Tworzenie przycisku
        button = Button(text='Kliknij mnie!', font_size=24)
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        self.counter += 1
        self.label.text = f'Kliknięcia: {self.counter}'

if __name__ == '__main__':
    ClickCounterApp().run()
