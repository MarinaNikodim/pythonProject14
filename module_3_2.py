def send_email(massage, recipient, *, sender="university.help@gmail.com"):
    index = recipient.find("@") and sender.find("@")
    variants = (".com", ".ru", ".net")
    if sender.endswith(variants) or recipient.endswith(variants):
        if index != -1:
            print("Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com")
        else:
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient, ".")

        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
            if sender == "university.help@gmail.com":
                print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient, ".")
        else:
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient, ".")


send_email('Это сообщение для проверки связи,', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
