from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(BoxLayout):
    def check_credentials(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text

        # Instead of only checking, also show what user entered
        self.ids.status_label.text = f"Username: {username}\nPassword: {password}"
        self.ids.status_label.color = (0, 1, 1, 1)  # Cyan color for info


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == "__main__":
    LoginApp().run()
# Simple validation (hardcoded username/password for demonstration)
if username == "admin" and password == "password":
self.status_label.text = "Login Successful"
self.status_label.color = (0, 1, 0, 1) # Green color for success
else:
self.status_label.text = "Invalid Credentials"
self.status_label.color = (1, 0, 0, 1) # Red color for error