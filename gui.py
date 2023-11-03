import tkinter
from tkinter import ttk
import crypt_engine


def out_of_prog():
    exit()


decrypted_text = None

created_widgets = []


def encrypt(button1, button2, button3, button4, button5):
    button_destroy(button1, button2, button3, button4, button5)
    encrypt_text = tkinter.Text(font='arial 12', height=15, width=30)
    encrypt_text.pack(anchor='nw')

    all_crypts = ["Шифр Цезаря", "Шифр Вернама", "Шифр Виженера", "Динамический Цезарь"]
    possible_crypts = ttk.Combobox(values=all_crypts)
    possible_crypts.pack(anchor='e', padx=45)

    key = tkinter.Entry()
    key.pack(anchor='e', padx=51)

    button4 = tkinter.Button(text="Зашифровать", width=20,
                             command=lambda: get_text_encrypt(encrypt_text, possible_crypts, key))
    button4.pack(anchor="e", padx=40)

    def back():
        encrypt_text.destroy()
        possible_crypts.destroy()
        key.destroy()
        button4.destroy()
        button5.destroy()
        create_buttons()
        for i in created_widgets:
            i.destroy()

    button5 = tkinter.Button(text="Назад", command=back, width=20)
    button5.pack(anchor='e', padx=40)


def get_text_encrypt(encrypt_text, crypt, key):
    crypt = crypt.get()
    key = key.get()
    function = {"Шифр Цезаря": crypt_engine.cesar_encrypting, "Шифр Вернама": crypt_engine.verman_encrypting,
                "Шифр Виженера": crypt_engine.visener_encrypting,
                "Динамический Цезарь": crypt_engine.dynamic_cesar_encrypting}
    global decrypted_text
    try:
        decrypted_text.destroy()
    except AttributeError:
        pass
    try:
        key = int(key)
    except ValueError:
        pass
    if crypt == '':
        string = "Выберите метод шифрования"
    elif key == '':
        string = 'Впишите ключ'
    else:
        string = encrypt_text.get("1.0", 'end-1c')
        string = function[crypt](string, key)
    decrypted_text = tkinter.Label(font='arial 12', anchor='nw', bg="white", text=string, height=15, width=30,
                                   wraplength=280, justify='left')
    decrypted_text.pack(anchor='sw')
    created_widgets.append(decrypted_text)


def decrypt(button1, button2, button3, button4, button5):
    button_destroy(button1, button2, button3, button4, button5)
    decrypt_text = tkinter.Text(font='arial 12', height=15, width=30)
    decrypt_text.pack(anchor='nw')

    all_crypts = ["Шифр Цезаря", "Шифр Вернама", "Шифр Виженера", "Динамический Цезарь", "Взлом Цезаря"]
    possible_crypts = ttk.Combobox(values=all_crypts)
    possible_crypts.pack(anchor='e', padx=45)

    key = tkinter.Entry()
    key.pack(anchor='e', padx=51)

    button4 = tkinter.Button(text="Расшифровать", width=20,
                             command=lambda: get_text_decrypt(decrypt_text, possible_crypts, key))
    button4.pack(anchor="e", padx=40)

    def back():
        decrypt_text.destroy()
        possible_crypts.destroy()
        key.destroy()
        button4.destroy()
        button5.destroy()
        create_buttons()
        for i in created_widgets:
            i.destroy()

    button5 = tkinter.Button(text="Назад", command=back, width=20)
    button5.pack(anchor='e', padx=40)


def get_text_decrypt(decrypt_text, crypt, key):
    crypt = crypt.get()
    key = key.get()
    function = {"Шифр Цезаря": crypt_engine.cesar_decrypt, "Шифр Вернама": crypt_engine.verman_decrypt,
                "Шифр Виженера": crypt_engine.visener_decrypt,
                "Динамический Цезарь": crypt_engine.dynamic_cesar_decrypt, "Взлом Цезаря": crypt_engine.auto_hack_cesar}
    global decrypted_text
    try:
        decrypted_text.destroy()
    except AttributeError:
        pass
    if function != crypt_engine.auto_hack_cesar:
        try:
            key = int(key)
        except ValueError:
            pass
    else:
        key = None
    if crypt == '':
        string = "Выберите метод шифрования"
    elif key == '' and function[crypt] != crypt_engine.auto_hack_cesar:
        string = 'Впишите ключ'
    else:
        string = decrypt_text.get("1.0", 'end-1c')
        string = function[crypt](string, key)
    decrypted_text = tkinter.Label(font='arial 12', anchor='nw', bg="white", text=string, height=15, width=30,
                                   wraplength=280, justify='left')
    decrypted_text.pack(anchor='sw')
    created_widgets.append(decrypted_text)


def encrypt_file(button1, button2, button3, button4, button5):
    button_destroy(button1, button2, button3, button4, button5)

    in_file = tkinter.Text(font='arial 12', height=7, width=30)
    in_file.pack(anchor='nw')

    all_crypts = ["Шифр Цезаря", "Шифр Вернама", "Шифр Виженера", "Динамический Цезарь"]
    possible_crypts = ttk.Combobox(values=all_crypts)
    possible_crypts.pack(anchor='e', padx=45)

    key = tkinter.Entry()
    key.pack(anchor='e', padx=51)

    button4 = tkinter.Button(text="Зашифровать", width=20,
                             command=lambda: file_text_encrypt(in_file, out_file, possible_crypts, key))
    button4.pack(anchor="e", padx=40)

    def back():
        in_file.destroy()
        possible_crypts.destroy()
        key.destroy()
        button4.destroy()
        button5.destroy()
        create_buttons()
        out_file.destroy()
        for i in created_widgets:
            i.destroy()

    button5 = tkinter.Button(text="Назад", command=back, width=20)
    button5.pack(anchor='e', padx=40)

    out_file = tkinter.Text(font='arial 12', height=7, width=30)
    out_file.pack(anchor='w')


def file_text_encrypt(in_file, out_file, crypt, key):
    function = {"Шифр Цезаря": crypt_engine.cesar_encrypting, "Шифр Вернама": crypt_engine.verman_encrypting,
                "Шифр Виженера": crypt_engine.visener_encrypting,
                "Динамический Цезарь": crypt_engine.dynamic_cesar_encrypting}
    crypt = crypt.get()
    key = key.get()
    global decrypted_text
    try:
        decrypted_text.destroy()
    except AttributeError:
        pass
    try:
        key = int(key)
    except ValueError:
        pass
    if crypt == '':
        string = "Выберите метод шифрования"
    elif key == '':
        string = 'Впишите ключ'
    else:
        fin = open(in_file.get("1.0", 'end-1c'), encoding='utf8')
        file_string = fin.read()
        fin.close()
        if len(out_file.get("1.0", 'end-1c')) == 0:
            fout = open(in_file.get("1.0", 'end-1c'), "w", encoding='utf8')
        else:
            fout = open(out_file.get("1.0", 'end-1c'), "w", encoding='utf8')

        file_ecrypted = function[crypt](file_string, key)
        fout.write(file_ecrypted)
        fout.close()
        string = "Успешно"
    decrypted_text = tkinter.Label(font='arial 12', anchor='nw', bg="white", text=string, height=7, width=30,
                                   wraplength=280, justify='left')
    decrypted_text.pack(anchor='sw', pady=90)
    created_widgets.append(decrypted_text)


def decrypt_file(button1, button2, button3, button4, button5):
    button_destroy(button1, button2, button3, button4, button5)

    in_file = tkinter.Text(font='arial 12', height=7, width=30)
    in_file.pack(anchor='nw')

    all_crypts = ["Шифр Цезаря", "Шифр Вернама", "Шифр Виженера", "Динамический Цезарь", "Взлом Цезаря"]
    possible_crypts = ttk.Combobox(values=all_crypts)
    possible_crypts.pack(anchor='e', padx=45)

    key = tkinter.Entry()
    key.pack(anchor='e', padx=51)

    button4 = tkinter.Button(text="Расшифровать", width=20,
                             command=lambda: file_text_decrypt(in_file, out_file, possible_crypts, key))
    button4.pack(anchor="e", padx=40)

    def back():
        in_file.destroy()
        possible_crypts.destroy()
        key.destroy()
        button4.destroy()
        button5.destroy()
        create_buttons()
        out_file.destroy()
        for i in created_widgets:
            i.destroy()

    button5 = tkinter.Button(text="Назад", command=back, width=20)
    button5.pack(anchor='e', padx=40)

    out_file = tkinter.Text(font='arial 12', height=7, width=30)
    out_file.pack(anchor='w')


def file_text_decrypt(in_file, out_file, crypt, key):
    function = {"Шифр Цезаря": crypt_engine.cesar_encrypting, "Шифр Вернама": crypt_engine.verman_encrypting,
                "Шифр Виженера": crypt_engine.visener_encrypting,
                "Динамический Цезарь": crypt_engine.dynamic_cesar_encrypting,
                "Взлом Цезаря": crypt_engine.auto_hack_cesar}
    crypt = crypt.get()
    key = key.get()
    global decrypted_text
    try:
        decrypted_text.destroy()
    except AttributeError:
        pass
    try:
        key = int(key)
    except ValueError:
        pass
    if crypt == '':
        string = "Выберите метод шифрования"
    elif key == '' and function[crypt] != crypt_engine.auto_hack_cesar:
        string = 'Впишите ключ'
    else:
        fin = open(in_file.get("1.0", 'end-1c'), encoding='utf8')
        file_string = fin.read()
        fin.close()
        if len(out_file.get("1.0", 'end-1c')) == 0:
            fout = open(in_file.get("1.0", 'end-1c'), "w", encoding='utf8')
        else:
            fout = open(out_file.get("1.0", 'end-1c'), "w", encoding='utf8')

        file_ecrypted = function[crypt](file_string, key)
        fout.write(file_ecrypted)
        fout.close()
        string = "Успешно"
    decrypted_text = tkinter.Label(font='arial 12', anchor='nw', bg="white", text=string, height=7, width=30,
                                   wraplength=280, justify='left')
    decrypted_text.pack(anchor='sw', pady=90)
    created_widgets.append(decrypted_text)


def button_destroy(button1, button2, button3, button4, button5):
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()


def create_buttons():
    button1 = tkinter.Button(text="Зашифровать", width=20,
                             command=lambda: encrypt(button1, button2, button3, button4, button5))
    button1.pack(anchor='center', pady=30)
    button2 = tkinter.Button(text="Расшифровать", width=20,
                             command=lambda: decrypt(button1, button2, button3, button4, button5))
    button2.pack(anchor="center", pady=30)
    button4 = tkinter.Button(text="Зашифровать файл", width=20,
                             command=lambda: encrypt_file(button1, button2, button3, button4, button5))
    button4.pack(anchor="center", pady=30)
    button5 = tkinter.Button(text="Расшифровать файл", width=20,
                             command=lambda: decrypt_file(button1, button2, button3, button4, button5))
    button5.pack(anchor="center", pady=30)
    button3 = tkinter.Button(text="Выход", width=20, command=out_of_prog)
    button3.pack(anchor="center", pady=30)


def start_program():
    main = tkinter.Tk()
    wide = '600'
    high = '700'
    create_buttons()
    main.title("Cryptographer")
    main.geometry(f'{wide}x{high}+100+100')

    main.mainloop()
