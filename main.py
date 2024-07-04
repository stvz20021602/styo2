# Import the App class from kivy.app
from kivy.app import App
# Import the Label class from kivy.uix.label to display text
from kivy.uix.label import Label

# Define the main application class, inheriting from Kivy's App class
class HelloWorldApp(App):
    # The build method returns the root widget of the application
    def build(self):
        # Create and return a Label widget with the text "Hello World"
        return Label(text='Hello World')

# If this script is run (rather than imported as a module), create an instance of the HelloWorldApp and run it
if __name__ == '__main__':
    HelloWorldApp().run()
