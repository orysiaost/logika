from PyQt5.QtWidgets import QApplication # Імпорт класів для створення об’єктів вікна та додатку.
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow             # Імпорт класу інтерфейсу з ui.py

import random # імпортуємо рандом

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.example)  # підключаємо виклик фукнції на кнопку

    # метод для генерації пародів (або з букв або з цифр)
    def example(self):
       signs = ''                                # Ініціалізація змінної для зберігання символів, з яких буде формуватися випадковий рядок.

       # Перевіряється, чи встановлений прапорець 'cb_alphabet'. Якщо так, додаються символи латинського алфавіту.
       if self.ui.cb_alphabet.isChecked():      
           signs = 'qwertyuiopsdfghjklzxcvbnm'

       # Перевіряється, чи встановлений прапорець 'cb_numbers'. Якщо так, додаються цифри до існуючих символів.
       if self.ui.cb_numbers.isChecked():
           signs += '0123456789'
      
       result = ''                           # Ініціалізація змінної для зберігання результату  
       number = random.randint(5, 10)        # рандомиться довжина паролю    
       for i in range(number):
           result += random.choice(signs)    
      
       self.ui.result.setText(result)        # пароль передається на надпис

# --------------------------------------


app = QApplication([])   # Створення об’єктів вікна та додатку. Показ вікна.
ex = Widget()

ex.show()
app.exec_()