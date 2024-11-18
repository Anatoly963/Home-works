
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if sender.find('@') == -1 or recipient.find('@') == -1:
        print()
        print("Невозможно отправить письмо с адреса", (sender), "на адрес", (recipient))
        print('У адреса отправителя или получателя нет знака @')
        return
    if sender.find('.com') == -1 and sender.find('.ru') == -1 and sender.find('.net') == -1 or\
            recipient.find('.com') == -1 and recipient.find('.ru') == -1 and recipient.find('.net') == -1:
        print()
        print("Невозможно отправить письмо с адреса", (sender), "на адрес", (recipient))
        print('У адреса отправителя или получателя неверное расширение')
        return
    if sender == recipient:
        print()
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":
        print()
        print("Письмо успешно отправлено с адреса", (sender), "на адрес", (recipient))
        return
    elif sender != "university.help@gmail.com":
        print()
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", (sender), "на адрес", (recipient))


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.nt')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


