from queue import Queue

class ServiceCenter: #клас що імітує роботу сервісного центру
    def __init__(self):
        self.aplications = Queue()

    def generate_request(self,numb): #функція для генерування та додавання заявки в чергу
        numb_apl=numb
        for i in range(numb_apl):
            self.aplications.put(f"Заявка #{i+1}")

    def process_request(self): #функція яка обробляє та видаляє заявки. Якщо черга порожня виводить відповідне повідмлення.
        if not self.aplications.empty():
            while not self.aplications.empty():
                current_aplication = self.aplications.get()
                print(f"Обробляється {current_aplication}")
        else:
            print("Черга порожня")    

# Створюємо сервісний центр
center=ServiceCenter()

#Головний цикл програми:
while True:
    print("Привіт це чат бот сервісного центру!")
    command=int(input("Введідть команду: \n1- запуск сервісного центру, \n2-завершити роботу."))
    if command==1:
        center.generate_request(int(input("Введи кількість заявок, яку бажаєте обробити сервісним центром, число має бути цілим та додатнім:")))
        center.process_request()
        print("Сервісний центр обробив всі заявки")
        print("*"*30)
    if command==2:
        break
