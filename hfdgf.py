from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
#--------------------------вікно програми
app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600
window.setWindowTitle("Smart Notes")
window.resize(main_width, main_height)
window.setStyleSheet('background-color:rgb(235, 231, 255), font-size:15px')

#--------------------------------------------------
#              Елементи інтерфейсу
#--------------------------------------------------

text_editor = QTextEdit()                                 #список тексту
text_editor.setPlaceholderText("Введіть текст...")
text_editor.setStyleSheet('background-color:#CCFFFF;')

list_widget1 = QListWidget()
list_widget1.setStyleSheet('background-color:#CCFFFF;')   #список заміток

list_widget2 = QListWidget()
list_widget2.setStyleSheet('background-color:#CCFFFF;')    #список тегів

text_searcher = QLineEdit()                                #пошук по тексту
text_searcher.setPlaceholderText("Введіть текст...")

tag_searcher = QLineEdit()                                 #пошук по тегу
tag_searcher.setPlaceholderText("Введіть тег...")

#--------------------------------------------------
#                     КНОПКИ
#--------------------------------------------------

make_note = QPushButton()
make_note.setText("Створити замітку")

delete_note = QPushButton()
delete_note.setText("Видалити замітку")

save_note = QPushButton()
save_note.setText("Зберегти замітку")

add_to_note = QPushButton()
add_to_note.setText("Додати до замітки")

unpin_to_note = QPushButton()
unpin_to_note.setText("Відкріпити від замітки")

search_for_text = QPushButton()
search_for_text.setText("Шукати замітку за текстом")

search_for_tag = QPushButton()
search_for_tag.setText("Шукати замітку за тегом")

action_theme_btn = QPushButton()
action_theme_btn.setText("Заміна тему")

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget1)
col2.addLayout(row1)
col2.addWidget(save_note)

col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget2)

col2.addWidget(QLabel("Ввід данних:"))
col2.addWidget(tag_searcher)

col2.addWidget(text_searcher)

col2.addLayout(row2)

col2.addWidget(search_for_tag)

col2.addWidget(search_for_text)

col2.addWidget(action_theme_btn)

layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

window.setLayout(layout_note)

window.show()
app.exec_()
