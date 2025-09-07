from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class TextInputApp(App):
    
    def build(self):
        # The main layout is a vertical BoxLayout
        main_layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Create a Label to display the typed text.
        # It's initialized with a prompt.
        self.output_label = Label(
            text="Type something and press the button!", 
            font_size=24,
            size_hint=(1, 0.4)
        )
        
        # Create a TextInput widget for user input.
        # 'multiline=False' keeps it as a single line of text.
        self.input_text = TextInput(
            multiline=False,
            font_size=32,
            size_hint=(1, 0.2)
        )
        
        # Create a Button to trigger the action.
        display_button = Button(
            text="Display Text", 
            font_size=28,
            size_hint=(1, 0.2)
        )
        
        # Bind the button's 'on_press' event to the update_label method.
        display_button.bind(on_press=self.update_label)
        
        # Add the widgets to the main layout.
        main_layout.add_widget(self.output_label)
        main_layout.add_widget(self.input_text)
        main_layout.add_widget(display_button)
        
        return main_layout

    def update_label(self, instance):
      
        # Get the text from the TextInput widget.
        user_text = self.input_text.text
        
        # Update the text of the output label.
        self.output_label.text = user_text

if __name__ == '__main__':
    TextInputApp().run()