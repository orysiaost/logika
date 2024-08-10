#відкриваємо файл для читання
with open("quotes.txt","r",encoding="UTF-8") as file:
    for line in file:
        print(line)

answer = input("Хто написав ці рядки? ")

#відкриваємо для дозапису
with open("quotes.txt","a",encoding="UTF-8") as file:
    for line in file:
        file.write("\n",answer) 


while True:
    answer=input("Хочете додати ще одну цитату? (так\ні)")
    answer= answer.lower()
    if answer == "так":
            quote = input("Введіть цитату: ")
            author = input("Введіть автора: ")
            with open("quotes.txt","a",encoding="UTF-8") as file:
                for line in file:
                    file.write("\n",quote) 
                    file.write("\n",author)
                    file.close()
    else:
        break


with open("quotes.txt","r",encoding="UTF-8") as file:
    for line in file:
        print(line)
