import time

class Pupil:
    def __init__(self, surname, name, mark):
        self.Surname = surname
        self.Name = name
        self.Mark = mark

pupils = []

def print_class(pupils):
    for pupil in pupils:
        print(pupil.Surname, pupil.Name," - ",pupil.Mark)
        print("\n")

def print_five(puplis):
    print("Відмінники: ")
    for pupil in pupils:
        if pupil.Mark == 5:
            print(pupil.Surname)
    print("\n")

def find_average(pupils):
    average = 0
    for pupil in pupils:
        average += pupil.Mark
    average /= len(pupils)
    print("Середня оцінка класу: ", average)

with open("pupils.txt", "r", encoding= "utf-8") as file:
    for line in file:
        data = line.split(" ")
        pupil = Pupil(data[0], data[1], int(data[2]))
        pupils.append(pupil)

print_class(pupils)

