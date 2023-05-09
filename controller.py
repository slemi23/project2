import csv
from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QWidget, Ui_Form):

    """
    Class representing details of registration form
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor to create inital state of registration form

        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.register_button.clicked.connect(lambda: self.register())

    def register(self) -> None:
        """"
        function that verifies all fields are input correctly
        """
        # Grabs all inputs
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        email_address = self.email.text()
        password1 = self.password1.text()
        password2 = self.password2.text()

        # Checking if inputs are valid
        if len(first_name) == 0 or len(last_name) == 0 or len(email_address) == 0 or len(password1) == 0 or len(password2) == 0:
            self.register_box.setText('Please fill in all inputs!')
        elif password1 != password2:
            self.register_box.setText('Passwords do not match!')
            self.password1.setText('')
            self.password2.setText('')
        else:
            # Checks if email already exists in CSV file
            with open('registration.csv', 'r') as data:
                rows = csv.reader(data)

                for i in rows:
                    if email_address in i:
                        self.register_box.setText('An account with this email\nis already registered.\nPlease try again')
                        self.email.setText('')
                        break
                else:
                    # If no duplicate email entered:
                    self.register_box.setText(f'Congrats {first_name} {last_name}!\n'
                                      f'You have successfully registered!\n'
                                      f'A verification link has been sent to\n'
                                      f'{email_address}')


                    with open('registration.csv', 'a') as file:
                        file.write(f'{first_name},{last_name},{email_address}\n')

                    self.first_name.setText('')
                    self.last_name.setText('')
                    self.email.setText('')
                    self.password1.setText('')
                    self.password2.setText('')





