from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
#--------------------------вікно програми
notes = {
    "Ласкаво просимо!": {
        "text" : "Це найкращий додаток для заміток, у світі!",
        "tag" : ["добро", "інструкція"]
    }
}

def writeToFile():
    with open("notes_data.json", "w") as file:
        json.dump(notes, file, sort_keys=True)


#---------------------------------------------------------


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
#----------------------------------------------
'''Функціонал програми'''



def show_notes():
    global key
    key = list_widget1.selectedItems()[0].text()
    list_widget2.clear()
    text_editor.setText(notes[key]["text"])
    list_widget2.addItem(notes[key]["tag"])

def add_notes():
    note_name,ok = QInputDialog.getText(window, "Додати зміну", "Назва замітки")
    if note_name and ok:
        list_widget1.addItem(note_name)
        notes[note_name] = {"text":"","tag": []}
    writeToFile()

def delete_notes():
    if list_widget1.currentItem():
        if key in notes:
            notes.pop(key)

            text_editor.clear()
            list_widget2.clear()
            list_widget1.clear()
            list_widget1.addItem(notes)
            writeToFile()

def save_notes():
    if list_widget1.currentItem():
        key = list_widget1.currentItem().text()
        notes[key]['text']=text_editor.toPlainText()
        writeToFile()

'''Запуск програми'''
#підключення обробки подій
list_widget1.itemClicked.connect(show_notes)

#Зчитання файл
with open("notes_data.json", "r") as file:
    notes = json.load(file)
    list_widget1.addItem(notes)

window.show()
app.exec_()