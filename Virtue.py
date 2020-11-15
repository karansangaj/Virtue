from tkinter import *
import os
import io
import uuid
import ctypes
import math
from PIL import Image, ImageTk
import mysql.connector
import datapass_virtue
from Crypto import Random
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
# noinspection PyPep8Naming
from Cryptodome.Cipher import AES as domeAES
# noinspection PyPep8Naming
from Crypto.Cipher import AES as cryptoAES
import base64
import hashlib
from datetime import datetime, time
import re
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import threading
import urllib.request
import pyttsx3
from pynput.keyboard import Key, Controller
import time as times
import screen_brightness_control as sbc
import smtplib
import textwrap
import random

global root_main
global root_sub
global main_screen
global drag
global screen_controls
global min_button1
global max_button1
global close_button1
global login_screen
global login_screen_back
global username_login_entry
global password_login_entry
global login_button
global login_screen_error
global forgot_button
global signup_button
global show_password
global hide_password
global signup_screen
global signup_screen_back
global back_button
global register_name_entry
global register_email_entry
global register_pass_entry
global DOB_label
global month_entry
global day_entry
global year_entry
global register_button
global Signup_Screen_error
global Length
global LowerCase
global UpperCase
global Number
global SpecialChar
global Confirm
global month_list_drop
global forgot_password_screen
global forgot_password_screen_back
global verify_email_entry
global verify_email_button
global forgot_password_screen_error
global forgot_password_screen_back_button
global verification_screen
global verification_screen_back
global verify_otp_entry
global verify_code_button
global verification_screen_error
global verification_Screen_back_button
global reset_password_screen
global reset_password_screen_back
global new_password_enter
global confirm_password_enter
global reset_button
global reset_password_screen_error
global reset_password_screen_back_button
global length_rp
global lower_case_rp
global upper_case_rp
global number_rp
global special_char_rp
global confirm_rp
global virtue_screen
global greet
global error
global animation
global animation_mask
global mic
global results
global results_weather
global Settings_icon
global suggestion
global acc_canvas
global results_main
global account_screen
global results_bright
global hover_math


# noinspection SpellCheckingInspection
class Settings:
    """global Settings"""
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    screen_res_x = int(user32.GetSystemMetrics(0) * (1080 / 3840))  # 1080
    screen_res_y = int(user32.GetSystemMetrics(1) * (1920 / 2160))  # 1920
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)
    c1 = int((screen_width - screen_res_x) / 2)
    c2 = int((screen_height - screen_res_y) / 2)
    country = ""
    conn = "conn"  # change to null
    state = ""
    state_count = 0
    app_ver = "11.14.20"
    last_click_x = int(0)
    last_click_y = int(0)
    minimized_thread = ""
    progress_bar_thread = ""
    reset_email = ""
    acc_holder_name = ""

    "Font Family"

    font_light_7 = "helvetica", 7
    font_bold_7 = "helvetica", 7, "bold"
    font_light_8 = "helvetica", 8
    font_bold_8 = "helvetica", 8, "bold"
    font_light_10 = "helvetica", 10
    font_bold_10 = "helvetica", 10, "bold"
    font_light_12 = "helvetica", 12
    font_bold_12 = "helvetica", 12, "bold"
    font_light_14 = "helvetica", 14
    font_bold_14 = "helvetica", 14, "bold"
    font_light_16 = "helvetica", 16
    font_bold_16 = "helvetica", 16, "bold"
    font_light_24 = "helvetica", 24
    font_bold_24 = "helvetica", 24, "bold"
    font_bold_36 = "helvetica", 36, "bold"

    font_light_6_segoe = "Segoe UI", 6
    font_bold_6_segoe = "Segoe UI", 6, "bold"
    font_light_8_segoe = "Segoe UI", 8
    font_bold_8_segoe = "Segoe UI", 8, "bold"
    font_light_10_segoe = "Segoe UI", 10
    font_bold_10_segoe = "Segoe UI", 10, "bold"
    font_light_12_segoe = "Segoe UI", 12
    font_bold_12_segoe = "Segoe UI", 12, "bold"
    font_light_14_segoe = "Segoe UI", 14
    font_bold_14_segoe = "Segoe UI", 14, "bold"
    font_light_16_segoe = "Segoe UI", 16
    font_bold_16_segoe = "Segoe UI", 16, "bold"
    font_light_36_segoe = "Segoe UI", 36
    font_bold_36_segoe = "Segoe UI", 36, "bold"

    "Color"

    black = "black"
    white = "white"
    gray = "#1F1F1F"


class Extras:

    @staticmethod
    def resource_path(relative_path):
        # noinspection SpellCheckingInspection
        get_base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(get_base_path, relative_path)

    # noinspection PyMethodMayBeStatic,PyMethodParameters,PyUnresolvedReferences
    def resize_image(event, im):
        new_width = event.width
        new_height = event.height
        image = im.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        event.widget.config(image=photo)
        event.widget.image = photo

    @staticmethod
    def search_db(procedure, *args):

        try:

            db = mysql.connector.connect(
                host=datapass_virtue.host,
                user=datapass_virtue.user,
                password=datapass_virtue.password,
                port=datapass_virtue.port,
                db=datapass_virtue.db
            )

            if not args:
                cursor = db.cursor()
                cursor.callproc(procedure)
                for result in cursor.stored_results():
                    result = result.fetchall()
                    cursor.close()
                    db.close()
                    return result

            else:
                cursor = db.cursor()
                cursor.callproc(procedure, args)
                for result in cursor.stored_results():
                    result = result.fetchall()
                    if str(result) == "[]":
                        cursor.close()
                        db.close()
                        result = [('',)]
                        return result
                    else:
                        cursor.close()
                        db.close()

                    return result

        except (ValueError, Exception):
            pass

    @staticmethod
    def modify_db(procedure, para):

        try:

            my_db = mysql.connector.connect(
                host=datapass_virtue.host,
                user=datapass_virtue.user,
                password=datapass_virtue.password,
                port=datapass_virtue.port,
                db=datapass_virtue.db
            )

            my_cursor = my_db.cursor()
            n_para = para.split(",")
            my_cursor.callproc(procedure, n_para)
            my_db.commit()
            my_cursor.close()
            my_db.close()

        except (ValueError, Exception):
            pass

    @staticmethod
    def encrypt(passkey):
        block_size_1 = AES.block_size
        key = passkey.encode()
        keys = hashlib.sha256(key).digest()
        bs = cryptoAES.block_size
        pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        raw = base64.b64encode(pad(passkey).encode('utf8'))
        iv = get_random_bytes(cryptoAES.block_size)
        cipher = cryptoAES.new(key=keys, mode=cryptoAES.MODE_CFB, iv=iv)
        a = base64.b64encode(iv + cipher.encrypt(raw))
        iv = Random.new().read(block_size_1)
        aes = domeAES.new(keys, domeAES.MODE_CFB, iv)
        b = base64.b64encode(iv + aes.encrypt(a))
        c = str(b.decode("utf-8"))
        return c

    @staticmethod
    def decrypt(enc, passkey):
        block_size_1 = AES.block_size
        key = passkey.encode()
        keys = hashlib.sha256(key).digest()
        passphrase = keys
        encrypted = base64.b64decode(enc)
        iv = encrypted[:block_size_1]
        aes = domeAES.new(passphrase, domeAES.MODE_CFB, iv)
        enc = aes.decrypt(encrypted[block_size_1:])
        un_pad = lambda s: s[:-ord(s[-1:])]
        enc = base64.b64decode(enc)
        iv = enc[:cryptoAES.block_size]
        cipher = cryptoAES.new(keys, cryptoAES.MODE_CFB, iv)
        b = un_pad(base64.b64decode(cipher.decrypt(enc[cryptoAES.block_size:])).decode('utf8'))
        return b

    @staticmethod
    def scale_x(dim):

        new_dim = math.ceil((Settings.screen_width / 3840) * dim)
        return int(new_dim)

    @staticmethod
    def scale_y(dim):

        new_dim = math.ceil((Settings.screen_height / 2160) * dim)
        return int(new_dim)

    @staticmethod
    def text_to_speech(audio):
        engine = pyttsx3.init()  # object creation
        engine.setProperty('rate', 140)  # setting up new voice rate
        engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')  # getting details of current voice
        engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
        engine.say(audio)
        engine.runAndWait()
        engine.stop()


# noinspection PyMethodParameters,PyUnresolvedReferences
class Main:

    @staticmethod
    def main_account_screen():

        res = f"{str(Settings.screen_res_x)}x{str(Settings.screen_res_y)}+{str(Settings.c1)}+{str(Settings.c2)}"

        global root_main
        root_main = Tk()
        root_main.lower()
        root_main.iconify()
        root_main.title('Virtue')
        root_main.geometry(res)
        root_main.configure(bg="black", highlightbackground="black")
        root_main.attributes('-alpha', 0.0)
        root_main.iconphoto(False, PhotoImage(file=Extras.resource_path("DataBase\\UIX\\icon_2.png")))
        root_main.bind("<FocusIn>", lambda e: root_main.focus_set())

        global root_sub
        root_sub = Toplevel()
        root_sub.overrideredirect(1)
        root_sub.attributes('-topmost', 1)
        root_sub.geometry(res)
        root_sub.wm_minsize(Settings.screen_res_x, Settings.screen_res_y)
        root_sub.wm_maxsize(Settings.screen_res_x, Settings.screen_res_y)
        root_sub.configure(bg="#111111", highlightbackground="black")
        root_sub.title('Virtue')
        root_sub.iconphoto(False, PhotoImage(file=Extras.resource_path("DataBase\\UIX\\icon_2.png")))

        global main_screen
        main_screen = Frame(root_sub, bg="black")
        main_screen.place(relx=0, rely=0, relwidth=1080 / 1080, relheight=1920 / 1920)

        global drag
        drag = Label(main_screen, bg="black", borderwidth=0, highlightthickness=0)
        drag.place(relx=0, rely=0, relwidth=1080 / 1080, relheight=65 / 1920)
        drag.bind('<Button-1>', lambda event: Main.last_click(event))
        drag.bind('<B1-Motion>', lambda event: root_sub.geometry(
            "+{}+{}".format(str(event.x - Settings.last_click_x + root_sub.winfo_x()),
                            str(event.y - Settings.last_click_y + root_sub.winfo_y()))))

        Main.screen_bar()

        if Extras.search_db('login_bypass', str(uuid.UUID(int=uuid.getnode())))[0][0] == "Yes":
            Virtue.virtue_screen()
        else:
            Login.login_screen()

        root_sub.mainloop()

    @staticmethod
    def screen_bar():

        bl = "black"
        wh = "white"

        global screen_controls
        screen_controls = Frame(main_screen, bg="black")
        screen_controls.place(relx=729 / 1080, rely=0, relwidth=351 / 1080, relheight=65 / 1920)

        global min_button1
        min_button1 = Button(screen_controls, fg=bl, bd=0, activebackground=bl, activeforeground=bl, highlightthickness=0)
        min_button1.place(relx=0, rely=0, relheight=1, relwidth=1 / 3)
        min_button1.bind("<Button-1>", Main.minimize)
        min_button1.bind("<Enter>", Main.min_enter)
        min_button1.bind("<Leave>", Main.min_leave)

        im_min = Image.open(Extras.resource_path("DataBase\\UIX\\mini.png"))
        resize = im_min.resize((int((Settings.screen_width / 3840) * im_min.size[0]), int((Settings.screen_height / 2160) * im_min.size[1])))
        mini = ImageTk.PhotoImage(resize)
        min_button1.configure(image=mini)
        min_button1.image = mini

        global max_button1
        max_button1 = Button(screen_controls, bg="#181818", fg=bl, bd=0, activebackground=bl, activeforeground=bl, highlightthickness=0)
        max_button1.place(relx=1 / 3, rely=0, relheight=1, relwidth=1 / 3)
        im_max = Image.open(Extras.resource_path("DataBase\\UIX\\max75.png"))
        resize = im_max.resize((int((Settings.screen_width / 3840) * im_max.size[0]), int((Settings.screen_height / 2160) * im_max.size[1])))
        close = ImageTk.PhotoImage(resize)
        max_button1.configure(image=close)
        max_button1.image = close

        global close_button1

        close_button1 = Button(screen_controls, fg=wh, bd=0, activebackground=bl, activeforeground=wh, highlightthickness=0)
        close_button1.place(relx=2 / 3, rely=0, relheight=1, relwidth=1 / 3)
        close_button1.bind("<Button-1>", lambda e: root_main.destroy())
        close_button1.bind("<Enter>", Main.close_enter)
        close_button1.bind("<Leave>", Main.close_leave)

        im_close = Image.open(Extras.resource_path("DataBase\\UIX\\close.png"))
        resize = im_close.resize((int((Settings.screen_width / 3840) * im_close.size[0]), int((Settings.screen_height / 2160) * im_close.size[1])))
        close = ImageTk.PhotoImage(resize)
        close_button1.configure(image=close)
        close_button1.image = close

    """Button Animations"""

    # noinspection PyMethodMayBeStatic
    def min_enter(self):

        im_min = Image.open(Extras.resource_path("DataBase\\UIX\\mini1.png"))
        resize = im_min.resize((int((Settings.screen_width / 3840) * im_min.size[0]), int((Settings.screen_height / 2160) * im_min.size[1])))
        mini = ImageTk.PhotoImage(resize)
        min_button1.configure(image=mini)
        min_button1.image = mini

    # noinspection PyMethodMayBeStatic
    def min_leave(self):

        min_button1.update()
        im_min = Image.open(Extras.resource_path("DataBase\\UIX\\mini.png"))
        resize = im_min.resize((int((Settings.screen_width / 3840) * im_min.size[0]), int((Settings.screen_height / 2160) * im_min.size[1])))
        mini = ImageTk.PhotoImage(resize)
        min_button1.configure(image=mini)
        min_button1.image = mini

    # noinspection PyMethodMayBeStatic
    def close_leave(self):

        im_close_le = Image.open(Extras.resource_path("DataBase\\UIX\\close.png"))
        resize = im_close_le.resize((int((Settings.screen_width / 3840) * im_close_le.size[0]), int((Settings.screen_height / 2160) * im_close_le.size[1])))
        close = ImageTk.PhotoImage(resize)
        close_button1.config(image=close)
        close_button1.image = close

    # noinspection PyMethodMayBeStatic
    def close_enter(self):

        im_close_en = Image.open(Extras.resource_path("DataBase\\UIX\\close1.png"))
        resize = im_close_en.resize((int((Settings.screen_width / 3840) * im_close_en.size[0]), int((Settings.screen_height / 2160) * im_close_en.size[1])))
        close = ImageTk.PhotoImage(resize)
        close_button1.config(image=close)
        close_button1.image = close

    """Screen Resize"""

    # noinspection PyMethodMayBeStatic
    def minimize(self):

        root_sub.overrideredirect(0)
        root_main.overrideredirect(1)
        root_sub.wm_state('iconic')
        Settings.minimized_thread = "True"
        Main.check_maximize()

    @staticmethod
    def check_maximize():

        if Settings.minimized_thread == "True":
            if root_sub.winfo_ismapped():
                root_sub.overrideredirect(True)
                root_main.overrideredirect(0)
                Settings.minimized_thread = "False"
            root_sub.after(100, Main.check_maximize)

    def last_click(event):
        Settings.last_click_x = event.x
        Settings.last_click_y = event.y


class Login:

    @staticmethod
    def login_screen():
        bl = "black"
        wh = "white"
        gr = "#1F1F1F"

        global login_screen
        login_screen = Frame(main_screen, bg="black")
        login_screen.place(relx=0, rely=65 / 1920, relheight=1855 / 1920, relwidth=1)

        global login_screen_back
        raw_im_login_screen_back = Image.open(Extras.resource_path("DataBase\\UIX\\login_page.png"))
        login_back = ImageTk.PhotoImage(raw_im_login_screen_back)
        login_screen_back = Label(login_screen, image=login_back, borderwidth=0, highlightthickness=0)
        login_screen_back.image = login_back
        login_screen_back.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_login_screen_back))
        login_screen_back.pack(fill=BOTH, expand=YES)
        login_screen_back.wait_visibility()

        global username_login_entry
        email = StringVar(login_screen, ' Email')
        username_login_entry = Entry(login_screen, textvariable=email, bg=gr, border=0, fg=wh, font=Settings.font_bold_10,
                                     disabledbackground=gr, insertbackground='white', disabledforeground="white")
        username_login_entry.place(relx=210 / 1080, rely=605 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        username_login_entry.bind("<KeyRelease>", lambda e: login_screen_error.configure(text=""))
        username_login_entry.bind("<Button-1>", Login.email_entry)
        username_login_entry.bind("<Leave>", Login.email_leave)
        username_login_entry.configure(state="disabled")

        global password_login_entry
        password = StringVar(login_screen, ' Password')
        password_login_entry = Entry(login_screen, textvariable=password, bg=gr, border=0, fg=wh, font=Settings.font_bold_10,
                                     disabledbackground=gr, insertbackground='white', disabledforeground="white")
        password_login_entry.place(relx=210 / 1080, rely=755 / 1855, relheight=90 / 1855, relwidth=660 / 1080)
        password_login_entry.bind("<KeyRelease>", lambda e: login_screen_error.configure(text=""))
        password_login_entry.bind("<Button-1>", Login.password_entry)
        password_login_entry.bind("<Leave>", Login.password_leave)
        password_login_entry.configure(state="disabled")

        global login_button
        login_button = Button(login_screen, text="Sign In", command=Login.login_engine, bg=gr, fg=wh, bd=0, font=Settings.font_bold_10, activebackground=gr, activeforeground=wh,
                              relief=SUNKEN)
        login_button.place(relx=210 / 1080, rely=905 / 1855, relheight=90 / 1855, relwidth=660 / 1080)

        global login_screen_error
        login_screen_error = Label(login_screen, textvariable="", bg=bl, fg="red", font=Settings.font_bold_10, anchor=CENTER)
        login_screen_error.place(relx=210 / 1080, rely=1020 / 1855, relheight=60 / 1855, relwidth=660 / 1080)

        global forgot_button
        forgot_button = Button(login_screen, text="Forgot Password?", bg=bl, fg=wh, bd=0, font=Settings.font_light_10, activebackground=bl, activeforeground=wh,
                               anchor=CENTER, relief=SUNKEN, command=ForgotPassword.forgot_password_frame)
        forgot_button.place(relx=210 / 1080, rely=1100 / 1855, relheight=60 / 1855, relwidth=660 / 1080)

        global signup_button
        signup_button = Button(login_screen, text="Create an Account", bg=bl, fg="#00A5EC", bd=0, font=Settings.font_bold_10, activebackground=bl,
                               activeforeground="#00A5EC", anchor=CENTER, relief=SUNKEN, command=SignUp.signup_page)
        signup_button.place(relx=210 / 1080, rely=1180 / 1855, relheight=60 / 1855, relwidth=660 / 1080)

        """Password Visibility"""

        global show_password
        raw_im_show_password = Image.open(Extras.resource_path("DataBase\\UIX\\Show_pass.png"))
        photo = ImageTk.PhotoImage(raw_im_show_password)
        show_password = Button(password_login_entry, image=photo, bg=gr, bd=0, activebackground=gr, command=Login.show_password)
        show_password.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_show_password))
        show_password.image = photo
        show_password.place_forget()

        global hide_password
        raw_im_hide_password = Image.open(Extras.resource_path("DataBase\\UIX\\Hide_pass.png"))
        photo1 = ImageTk.PhotoImage(raw_im_hide_password)
        hide_password = Button(password_login_entry, image=photo1, bg=gr, bd=0, activebackground=gr, command=Login.hide_password)
        hide_password.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_hide_password))
        hide_password.image = photo1
        hide_password.place_forget()

    @staticmethod
    def login_engine():

        login_button.configure(cursor="wait")
        username1 = username_login_entry.get()
        password1 = password_login_entry.get()

        if username1 == " Email":
            login_screen_error.configure(text="Please Enter Email Address")
            login_button.configure(cursor="")

        elif password1 == " Password":
            login_screen_error.configure(text="Please Enter Password")
            login_button.configure(cursor="")

        else:
            acc_check = Extras.search_db('signup_check_account', username1)[0][0]

            if acc_check == "No Internet Connectivity":
                login_screen_error.configure(text="No Internet Connectivity")
                login_button.configure(cursor="")

            elif not acc_check:
                login_screen_error.configure(text="Incorrect Email or Password")
                login_button.configure(cursor="")

            else:
                try:
                    Extras.modify_db('sign_out', str(uuid.UUID(int=uuid.getnode())))
                    Extras.decrypt((Extras.search_db('login_get_pass', username1))[0][0], password1)
                except (ValueError, Exception):
                    login_screen_error.configure(text="Incorrect Email or Password")
                    login_button.configure(cursor="")
                else:
                    current_machine_id = str(uuid.UUID(int=uuid.getnode()))
                    Extras.modify_db('login_logged', "{},{}".format(current_machine_id, username1))
                    login_button.configure(cursor="")
                    Virtue.virtue_screen()
                    login_screen_error.configure(text="Logged IN")

    "Email"

    # noinspection PyMethodMayBeStatic
    def email_entry(self):
        if Settings.conn == "conn":
            username_login_entry.configure(state="normal")
            if username_login_entry.get() == " Email":
                username_login_entry.delete(0, 'end')
                login_screen_error.configure(text="")

    # noinspection PyMethodMayBeStatic
    def email_leave(self):

        if username_login_entry.cget("state") == "normal":
            if len(username_login_entry.get()) == 0:
                entry = StringVar(login_screen, " Email")
                username_login_entry.configure(textvariable=entry)
                login_screen_error.configure(text="")

        username_login_entry.configure(state="disabled")
        username_login_entry.configure(disabledforeground="white")

    "Password"

    @staticmethod
    def show_password():
        password_login_entry.configure(show="")
        show_password.place_forget()
        hide_password.place(relx=0.9, rely=18 / 90, relheight=54 / 90, relwidth=54 / 660)

    @staticmethod
    def hide_password():
        password_login_entry.configure(show="\u26B9")
        hide_password.place_forget()
        show_password.place(relx=0.9, rely=18 / 90, relheight=54 / 90, relwidth=54 / 660)

    # noinspection PyMethodMayBeStatic
    def password_entry(self):

        if Settings.conn == "conn":
            password_login_entry.configure(state="normal")
            if password_login_entry.get() == " Password":
                password_login_entry.delete(0, 'end')
                password_login_entry.configure(show='\u26B9')
                show_password.place(relx=0.9, rely=18 / 90, relheight=54 / 90, relwidth=54 / 660)
                hide_password.place_forget()
                login_screen_error.configure(text="")

    # noinspection PyMethodMayBeStatic
    def password_leave(self):

        if password_login_entry.cget("state") == "normal":
            if len(password_login_entry.get()) == 0:
                entry = StringVar(login_screen, " Password")
                password_login_entry.configure(textvariable=entry)
                password_login_entry.configure(show='')
                show_password.place_forget()
                hide_password.place_forget()
                login_screen_error.configure(text="")

        password_login_entry.configure(state="disabled")
        password_login_entry.configure(disabledforeground="white")


class SignUp:

    @staticmethod
    def signup_page():

        # login_screen.destroy()

        bl = "black"
        wh = "white"
        gr = "#1F1F1F"

        global signup_screen
        signup_screen = Frame(main_screen, bg=bl)
        signup_screen.place(relx=0, rely=65 / 1920, relheight=1855 / 1920, relwidth=1)

        global signup_screen_back
        raw_im_signup_screen_back = Image.open(Extras.resource_path("DataBase\\UIX\\signup_page.png"))
        signup_back = ImageTk.PhotoImage(raw_im_signup_screen_back)
        signup_screen_back = Label(signup_screen, image=signup_back, borderwidth=0, highlightthickness=0)
        signup_screen_back.image = signup_back
        signup_screen_back.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_signup_screen_back))
        signup_screen_back.pack(fill=BOTH, expand=YES)
        signup_screen_back.wait_visibility()

        global back_button
        back_button = Button(main_screen, fg=bl, bg="black", bd=0, activebackground=bl, activeforeground=bl, highlightthickness=0, command=SignUp.back)

        back_button.update()
        im_raw_back_button = Image.open(Extras.resource_path("DataBase\\UIX\\back.png"))
        im_raw_back_button_resized = im_raw_back_button.resize((min_button1.winfo_width(), min_button1.winfo_height()))
        back_button_img = ImageTk.PhotoImage(im_raw_back_button_resized)

        back_button.configure(image=back_button_img)
        back_button.image = back_button_img

        back_button.place(relx=0, rely=0, relwidth=117 / 1080, relheight=65 / 1920)

        global register_name_entry
        register_name = StringVar(signup_screen, ' Name')
        register_name_entry = Entry(signup_screen, textvariable=register_name, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        register_name_entry.place(relx=210 / 1080, rely=605 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        register_name_entry.bind("<Key>", lambda e: Signup_Screen_error.configure(text=""))
        register_name_entry.bind("<Button-1>", SignUp.register_name_enter)
        register_name_entry.bind("<Leave>", SignUp.register_name_leave)

        global register_email_entry
        register_email = StringVar(signup_screen, ' Email')
        register_email_entry = Entry(signup_screen, textvariable=register_email, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        register_email_entry.place(relx=210 / 1080, rely=755 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        register_email_entry.bind("<Key>", lambda e: Signup_Screen_error.configure(text=""))
        register_email_entry.bind("<Button-1>", SignUp.register_email_enter)
        register_email_entry.bind("<Leave>", SignUp.register_email_leave)

        global register_pass_entry
        register_pass = StringVar(signup_screen, ' Password')
        register_pass_entry = Entry(signup_screen, textvariable=register_pass, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        register_pass_entry.place(relx=210 / 1080, rely=905 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        register_pass_entry.bind("<KeyRelease>", SignUp.requirements)
        register_pass_entry.bind("<Key>", lambda e: Signup_Screen_error.configure(text=""))
        register_pass_entry.bind("<Button-1>", SignUp.register_pass_enter)
        register_pass_entry.bind("<Leave>", SignUp.register_pass_leave)

        global DOB_label
        DOB_label = Label(signup_screen, text="When is your birthday ?", bg=bl, fg="white", font=Settings.font_light_8, anchor=NW)
        DOB_label.place(relx=190 / 1080, rely=1035 / 1855, relwidth=700 / 1080, relheight=50 / 1855)

        global month_entry
        month = StringVar(signup_screen, ' Month')
        month_entry = Label(signup_screen, textvariable=month, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, anchor=W)
        month_entry.place(relx=210 / 1080, rely=1105 / 1855, relwidth=280 / 1080, relheight=90 / 1855)
        month_entry.bind("<Key>", lambda e: Signup_Screen_error.configure(text=""))
        month_entry.bind("<Button-1>", SignUp.month_enter)

        global day_entry
        day = StringVar(signup_screen, ' Day')
        day_entry = Entry(signup_screen, textvariable=day, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        day_entry.place(relx=545 / 1080, rely=1105 / 1855, relwidth=110 / 1080, relheight=90 / 1855)
        day_entry.bind("<Key>", lambda e: Signup_Screen_error.configure(text=""))
        day_entry.bind("<Button-1>", SignUp.day_enter)
        day_entry.bind("<Leave>", SignUp.day_leave)

        global year_entry
        year = StringVar(signup_screen, ' Year')
        year_entry = Entry(signup_screen, textvariable=year, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        year_entry.place(relx=700 / 1080, rely=1105 / 1855, relwidth=180 / 1080, relheight=90 / 1855)
        year_entry.bind("<Key>", lambda e: Signup_Screen_error.configure(text=""))
        year_entry.bind("<Button-1>", SignUp.year_enter)
        year_entry.bind("<Leave>", SignUp.year_leave)

        global register_button
        register_button = Button(signup_screen, text="Sign up", command=SignUp.create_account, bg="#007FB5", fg=wh, font=Settings.font_bold_10, bd=0, activebackground="#007FB5",
                                 activeforeground=wh)
        register_button.place(relx=210 / 1080, rely=1255 / 1855, relwidth=660 / 1080, relheight=90 / 1855)

        global Signup_Screen_error
        Signup_Screen_error = Label(signup_screen, text="", bg=bl, fg="red", font=Settings.font_bold_10)
        Signup_Screen_error.place(relx=210 / 1080, rely=1370 / 1855, relwidth=660 / 1080, relheight=50 / 1855)

        """PasswordStrengthFrame"""

        password_req = Frame(signup_screen, bg=bl)
        password_req.place(relx=365 / 1080, rely=1450 / 1855, relwidth=350 / 1080, relheight=350 / 1855)

        global Length
        Length = Label(password_req, bg=bl, font=Settings.font_light_10)
        Length.pack(anchor=CENTER)

        global LowerCase
        LowerCase = Label(password_req, bg=bl, font=Settings.font_light_10)
        LowerCase.pack(anchor=CENTER)

        global UpperCase
        UpperCase = Label(password_req, bg=bl, font=Settings.font_light_10)
        UpperCase.pack(anchor=CENTER)

        global Number
        Number = Label(password_req, bg=bl, font=Settings.font_light_10)
        Number.pack(anchor=CENTER)

        global SpecialChar
        SpecialChar = Label(password_req, bg=bl, font=Settings.font_light_10)
        SpecialChar.pack(anchor=CENTER)

        global Confirm
        Confirm = Label(password_req, bg=bl, font=Settings.font_light_10)
        Confirm.pack(anchor=CENTER)

    @staticmethod
    def create_account():

        register_button.configure(cursor="wait")
        r_name = register_name_entry.get()
        r_email = register_email_entry.get()
        r_pass = register_pass_entry.get()
        r_month = month_entry.cget("text")
        r_day = day_entry.get()
        r_year = year_entry.get()

        if r_name == " Name":
            Signup_Screen_error.configure(text="Enter Name")
            register_button.configure(cursor="")

        elif r_email == " Email":
            Signup_Screen_error.configure(text="Enter Email")
            register_button.configure(cursor="")

        elif r_pass == " Password":
            Signup_Screen_error.configure(text="Enter Password")
            register_button.configure(cursor="")

        elif r_month == " Month":
            Signup_Screen_error.configure(text="Enter Month")
            register_button.configure(cursor="")

        elif r_day == " Day":
            Signup_Screen_error.configure(text="Enter Day")
            register_button.configure(cursor="")

        elif r_year == " Year":
            Signup_Screen_error.configure(text="Enter Year")
            register_button.configure(cursor="")

        elif re.search('[@]', r_email) is None:
            Signup_Screen_error.configure(text="Enter Valid Email")
            register_button.configure(cursor="")

        elif not SignUp.requirements(r_pass):
            Signup_Screen_error.configure(text="Password does not meet Requirements")
            register_button.configure(cursor="")

        elif Extras.search_db('signup_check_account', "{}".format(r_email))[0][0]:
            Signup_Screen_error.configure(text="Email already registered")
            register_button.configure(cursor="")

        else:
            Extras.modify_db('signup_create_account', "{},{},{},{}".format(r_email, Extras.encrypt(r_pass), r_name, f"{r_month} {r_day} {r_year}"))
            Signup_Screen_error.configure(text="New Account Registered")
            register_button.configure(cursor="")
            signup_screen.after(1000, SignUp.back())

    # noinspection PyMethodMayBeStatic
    def requirements(self):

        global register_pass_entry
        register_pass = register_pass_entry.get()

        a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0

        if len(register_pass) == 0:
            Length.configure(text="")
        elif len(register_pass) < 8:
            Length.configure(text="\u2715 8 Characters", fg='#962626')
            a1 = 0
        else:
            Length.configure(text="\u2713 8 Characters", fg='#3b8c15')
            a1 = 1

        if len(register_pass) == 0:
            Number.configure(text="")
        elif re.search('[0-9]', register_pass) is None:
            Number.configure(text="\u2715 Number", fg='#962626')
            a2 = 0
        else:
            Number.configure(text="\u2713 Number", fg='#3b8c15')
            a2 = 1

        if len(register_pass) == 0:
            UpperCase.configure(text="")
        elif re.search('[A-Z]', register_pass) is None:
            UpperCase.configure(text="\u2715 Upper Case", fg='#962626')
            a3 = 0
        else:
            UpperCase.configure(text="\u2713 Upper Case", fg='#3b8c15')
            a3 = 1

        if len(register_pass) == 0:
            LowerCase.configure(text="")
        elif re.search('[a-z]', register_pass) is None:
            LowerCase.configure(text="\u2715 Lower Case", fg='#962626')
            a4 = 0
        else:
            LowerCase.configure(text="\u2713 Lower Case", fg='#3b8c15')
            a4 = 1

        if len(register_pass) == 0:
            SpecialChar.configure(text="")
        elif re.search('[!@#$%^&*]', register_pass) is None:
            SpecialChar.configure(text="\u2715 Special Character", fg='#962626')
            a5 = 0
        else:
            SpecialChar.configure(text="\u2713 Special Character", fg='#3b8c15')
            a5 = 1

        if a1 * a2 * a3 * a4 * a5 == 0:
            return False
        else:
            return True

    # noinspection PyMethodMayBeStatic
    def register_name_enter(self):
        if register_name_entry.get() == " Name":
            register_name_entry.delete(0, 'end')
            register_name_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def register_name_leave(self):
        if len(register_name_entry.get()) == 0:
            register_name = StringVar(signup_screen, ' Name')
            register_name_entry.configure(textvariable=register_name)
            register_name_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def register_email_enter(self):
        if register_email_entry.get() == " Email":
            register_email_entry.delete(0, 'end')
            register_email_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def register_email_leave(self):
        if len(register_email_entry.get()) == 0:
            register_email = StringVar(signup_screen, ' Email')
            register_email_entry.configure(textvariable=register_email)
            register_email_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def register_pass_enter(self):
        if register_pass_entry.get() == " Password":
            register_pass_entry.delete(0, 'end')
            register_pass_entry.configure(show='\u26B9')

    # noinspection PyMethodMayBeStatic
    def register_pass_leave(self):
        if len(register_pass_entry.get()) == 0:
            register_pass = StringVar(signup_screen, ' Password')
            register_pass_entry.configure(textvariable=register_pass)
            register_pass_entry.configure(show='')

    # noinspection PyMethodMayBeStatic
    def day_enter(self):
        if day_entry.get() == " Day":
            day_entry.delete(0, 'end')
            day_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def day_leave(self):
        if len(day_entry.get()) == 0:
            day = StringVar(signup_screen, ' Day')
            day_entry.configure(textvariable=day)
            day_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def year_enter(self):
        if year_entry.get() == " Year":
            year_entry.delete(0, 'end')
            year_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def year_leave(self):
        if len(year_entry.get()) == 0:
            year = StringVar(signup_screen, ' Year')
            year_entry.configure(textvariable=year)
            year_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def month_enter(self):

        global month_list_drop
        try:
            month_list_drop.destroy()
        except (ValueError, Exception):
            pass
        month_list_drop = Label(signup_screen, bg="grey")
        month_list_drop.place(relx=190 / 1080, rely=1200 / 1855, relheight=600 / 1855, relwidth=320 / 1080)

        month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                      'November', 'December']

        for x in month_list:
            zz = Label(month_list_drop, text=x, anchor=W, bg="grey", fg="white", font=Settings.font_light_10)
            y = (int(month_list.index(x))) / 12
            zz.place(relx=0, rely=y, relheight=1 / 12, relwidth=1)
            zz.bind('<Button-1>', lambda event: SignUp.select_month(event))

    # noinspection PyMethodMayBeStatic,PyUnresolvedReferences,PyMethodParameters
    def select_month(event):
        month = StringVar(signup_screen, str(event.widget.cget("text")))
        month_entry.configure(textvariable=month)
        month_list_drop.destroy()

    @staticmethod
    def back():

        signup_screen.destroy()
        back_button.destroy()


class ForgotPassword:

    @staticmethod
    def forgot_password_frame():

        login_screen.destroy()

        bl = "black"
        wh = "white"
        gr = "#1F1F1F"

        global forgot_password_screen
        forgot_password_screen = Frame(main_screen, bg=bl)
        forgot_password_screen.place(relx=0, rely=65 / 1920, relheight=1855 / 1920, relwidth=1)

        global forgot_password_screen_back
        raw_im_forgot_password_screen_back = Image.open(Extras.resource_path("DataBase\\UIX\\forget_page.png"))
        forgot_back = ImageTk.PhotoImage(raw_im_forgot_password_screen_back)
        forgot_password_screen_back = Label(forgot_password_screen, image=forgot_back, borderwidth=0, highlightthickness=0)
        forgot_password_screen_back.image = forgot_back
        forgot_password_screen_back.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_forgot_password_screen_back))
        forgot_password_screen_back.pack(fill=BOTH, expand=YES)
        forgot_password_screen_back.wait_visibility()

        global verify_email_entry
        email = StringVar(forgot_password_screen, ' Email')
        verify_email_entry = Entry(forgot_password_screen, textvariable=email, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr, insertbackground='white',
                                   disabledforeground="white")
        verify_email_entry.place(relx=210 / 1080, rely=605 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        verify_email_entry.bind("<KeyRelease>", lambda e: forgot_password_screen_error.configure(text=""))
        verify_email_entry.bind("<Button-1>", ForgotPassword.email_entry)
        verify_email_entry.bind("<Leave>", ForgotPassword.email_leave)

        global verify_email_button
        verify_email_button = Button(forgot_password_screen, text="Get Verification Code", command=ForgotPassword.send_verification_code_engine, bg=gr, fg=wh,
                                     font=Settings.font_bold_10, bd=0, activebackground=gr, activeforeground=wh)
        verify_email_button.place(relx=210 / 1080, rely=755 / 1855, relheight=90 / 1855, relwidth=660 / 1080)

        global forgot_password_screen_error
        forgot_password_screen_error = Label(forgot_password_screen, text="", bg=bl, fg="red", font=Settings.font_bold_10)
        forgot_password_screen_error.place(relx=210 / 1080, rely=905 / 1855, relheight=60 / 1855, relwidth=660 / 1080)

        global forgot_password_screen_back_button
        forgot_password_screen_back_button = Button(main_screen, fg=bl, bg="black", bd=0, activebackground=bl, activeforeground=bl, highlightthickness=0,
                                                    command=ForgotPassword.back)
        forgot_password_screen_back_button.update()
        im_raw_back_button = Image.open(Extras.resource_path("DataBase\\UIX\\back.png"))
        im_raw_back_button_resized = im_raw_back_button.resize((min_button1.winfo_width(), min_button1.winfo_height()))
        back_button_img = ImageTk.PhotoImage(im_raw_back_button_resized)
        forgot_password_screen_back_button.configure(image=back_button_img)
        forgot_password_screen_back_button.image = back_button_img
        forgot_password_screen_back_button.place(relx=0, rely=0, relwidth=117 / 1080, relheight=65 / 1920)

    @staticmethod
    def send_verification_code_engine():

        verify_email_button.configure(cursor="wait")
        verify_email = verify_email_entry.get()

        if verify_email == " Email":
            forgot_password_screen_error.configure(text="Please Enter Email Address")
            verify_email_button.configure(cursor="")

        else:
            email = (Extras.search_db('verify_email', verify_email))[0][0]

            if not email:
                forgot_password_screen_error.configure(text="Please Enter Registered Email Address")
                verify_email_button.configure(cursor="")
            else:
                rnd_otp = str(random.choice(range(100000, 999999)))
                current_machine_id = str(uuid.UUID(int=uuid.getnode()))
                Extras.modify_db('verify_email_2', f"{verify_email},{Extras.encrypt(rnd_otp)},{current_machine_id}")

                sent_from = datapass_virtue.Email
                to = [verify_email_entry.get()]
                subject = 'Password Reset'
                body = 'Verification Code is %s' % rnd_otp
                message = textwrap.dedent("""\
                                                From: %s
                                                To: %s
                                                Subject: %s
                                                %s
                                                """ % (sent_from, ", ".join(to), subject, body))

                try:
                    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    server.ehlo()
                    server.login(datapass_virtue.Email, datapass_virtue.Epass)
                    server.sendmail(sent_from, to, message)
                    server.close()
                except (ValueError, Exception):
                    forgot_password_screen_error.configure(text="Check Network Connectivity")
                    verify_email_button.configure(cursor="")
                else:
                    verify_email_button.configure(cursor="")
                    Verification.verification_frame()
                    Settings.reset_email = verify_email

    # noinspection PyMethodMayBeStatic
    def email_entry(self):
        if verify_email_entry.get() == " Email":
            verify_email_entry.delete(0, 'end')
            verify_email_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def email_leave(self):
        if len(verify_email_entry.get()) == 0:
            entry = StringVar(forgot_password_screen, " Email")
            verify_email_entry.configure(textvariable=entry)
            verify_email_entry.configure(text="")

    @staticmethod
    def back():

        Extras.modify_db('delete_enc', str(uuid.UUID(int=uuid.getnode())))
        forgot_password_screen.destroy()
        forgot_password_screen_back_button.destroy()
        Settings.reset_email = ""
        Login.login_screen()


class Verification:

    @staticmethod
    def verification_frame():

        forgot_password_screen_back_button.destroy()
        forgot_password_screen.destroy()

        bl = "black"
        wh = "white"
        gr = "#1F1F1F"

        global verification_screen
        verification_screen = Frame(main_screen, bg=bl)
        verification_screen.place(relx=0, rely=65 / 1920, relheight=1855 / 1920, relwidth=1)

        global verification_screen_back
        raw_im_verification_screen_back = Image.open(Extras.resource_path("DataBase\\UIX\\forget_page.png"))
        verification_back = ImageTk.PhotoImage(raw_im_verification_screen_back)
        verification_screen_back = Label(verification_screen, image=verification_back, borderwidth=0, highlightthickness=0)
        verification_screen_back.image = verification_back
        verification_screen_back.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_verification_screen_back))
        verification_screen_back.pack(fill=BOTH, expand=YES)
        verification_screen_back.wait_visibility()

        global verify_otp_entry
        email = StringVar(verification_screen, ' Verification Code')
        verify_otp_entry = Entry(verification_screen, textvariable=email, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr, insertbackground='white',
                                 disabledforeground="white")
        verify_otp_entry.place(relx=210 / 1080, rely=605 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        verify_otp_entry.bind("<KeyRelease>", lambda e: verify_otp_entry.configure(text=""))
        verify_otp_entry.bind("<Button-1>", Verification.email_entry)
        verify_otp_entry.bind("<Leave>", Verification.email_leave)

        global verify_code_button
        verify_code_button = Button(verification_screen, text="Verify Code", bg=gr, fg=wh, font=Settings.font_bold_10, bd=0, activebackground=gr, activeforeground=wh,
                                    command=Verification.verify)
        verify_code_button.place(relx=210 / 1080, rely=755 / 1855, relheight=90 / 1855, relwidth=660 / 1080)

        global verification_screen_error
        verification_screen_error = Label(verification_screen, text="", bg=bl, fg="red", font=Settings.font_bold_10)
        verification_screen_error.place(relx=210 / 1080, rely=905 / 1855, relheight=60 / 1855, relwidth=660 / 1080)

        global verification_Screen_back_button
        verification_Screen_back_button = Button(main_screen, fg=bl, bg="black", bd=0, activebackground=bl, activeforeground=bl, highlightthickness=0, command=Verification.back)
        verification_Screen_back_button.update()
        im_raw_back_button = Image.open(Extras.resource_path("DataBase\\UIX\\back.png"))
        im_raw_back_button_resized = im_raw_back_button.resize((min_button1.winfo_width(), min_button1.winfo_height()))
        back_button_img = ImageTk.PhotoImage(im_raw_back_button_resized)
        verification_Screen_back_button.configure(image=back_button_img)
        verification_Screen_back_button.image = back_button_img
        verification_Screen_back_button.place(relx=0, rely=0, relwidth=117 / 1080, relheight=65 / 1920)

    @staticmethod
    def verify():

        verify_code_button.configure(cursor="wait")
        otp = verify_otp_entry.get()

        if verify_otp_entry.get() == " Verification Code":
            verification_screen_error.configure(text="Please Enter OTP")
            verify_code_button.configure(cursor="")

        else:

            try:
                Extras.decrypt((Extras.search_db('Verification_get_enc', str(uuid.UUID(int=uuid.getnode()))))[0][0], otp)
            except (ValueError, Exception):
                verification_screen_error.configure(text="Invalid OTP")
                verify_code_button.configure(cursor="")
            else:
                verify_code_button.configure(cursor="")
                ResetPassword.reset_password_frame()

    # noinspection PyMethodMayBeStatic
    def email_entry(self):
        if verify_otp_entry.get() == " Verification Code":
            verify_otp_entry.delete(0, 'end')
            verify_otp_entry.configure(text="")

    # noinspection PyMethodMayBeStatic
    def email_leave(self):
        if len(verify_otp_entry.get()) == 0:
            entry = StringVar(verification_screen, " Verification Code")
            verify_otp_entry.configure(textvariable=entry)
            verify_otp_entry.configure(text="")

    @staticmethod
    def back():

        Extras.modify_db('delete_enc', str(uuid.UUID(int=uuid.getnode())))
        verification_Screen_back_button.destroy()
        verification_screen.destroy()
        Settings.reset_email = ""
        Login.login_screen()


class ResetPassword:

    @staticmethod
    def reset_password_frame():

        verification_Screen_back_button.destroy()
        verification_screen.place_forget()

        bl = "black"
        wh = "white"
        gr = "#1F1F1F"

        global reset_password_screen
        reset_password_screen = Frame(main_screen, bg=bl)
        reset_password_screen.place(relx=0, rely=65 / 1920, relheight=1855 / 1920, relwidth=1)

        global reset_password_screen_back
        raw_im_reset_password_screen_back = Image.open(Extras.resource_path("DataBase\\UIX\\login_page.png"))
        reset_back = ImageTk.PhotoImage(raw_im_reset_password_screen_back)
        reset_password_screen_back = Label(reset_password_screen, image=reset_back, borderwidth=0, highlightthickness=0)
        reset_password_screen_back.image = reset_back
        reset_password_screen_back.bind('<Configure>', lambda event: Extras.resize_image(event, raw_im_reset_password_screen_back))
        reset_password_screen_back.pack(fill=BOTH, expand=YES)
        reset_password_screen_back.wait_visibility()

        global new_password_enter
        new_pass = StringVar(reset_password_screen, ' New Password')
        new_password_enter = Entry(reset_password_screen, textvariable=new_pass, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        new_password_enter.place(relx=210 / 1080, rely=605 / 1855, relwidth=660 / 1080, relheight=90 / 1855)
        new_password_enter.bind("<KeyRelease>", ResetPassword.requirements)
        new_password_enter.bind("<Key>", lambda e: reset_password_screen_error.configure(text=""))
        new_password_enter.bind("<Button-1>", ResetPassword.new_password_entry)
        new_password_enter.bind("<Leave>", ResetPassword.new_password_leave)

        global confirm_password_enter
        con_pass = StringVar(reset_password_screen, ' Confirm Password')
        confirm_password_enter = Entry(reset_password_screen, textvariable=con_pass, bg=gr, border=0, fg=wh, font=Settings.font_bold_10, disabledbackground=gr)
        confirm_password_enter.place(relx=210 / 1080, rely=755 / 1855, relheight=90 / 1855, relwidth=660 / 1080)
        confirm_password_enter.bind("<KeyRelease>", ResetPassword.requirements)
        confirm_password_enter.bind("<Key>", lambda e: reset_password_screen_error.configure(text=""))
        confirm_password_enter.bind("<Button-1>", ResetPassword.con_password_entry)
        confirm_password_enter.bind("<Leave>", ResetPassword.con_password_leave)
        confirm_password_enter.configure(state="disabled")

        global reset_button
        reset_button = Button(reset_password_screen, text="Reset Password", command=ResetPassword.reset_password, bg=gr, fg=wh, font=Settings.font_bold_10, bd=0,
                              activebackground=gr, activeforeground=wh)
        reset_button.place(relx=210 / 1080, rely=905 / 1855, relheight=90 / 1855, relwidth=660 / 1080)

        global reset_password_screen_error
        reset_password_screen_error = Label(reset_password_screen, text="", bg=bl, fg="red", font=Settings.font_bold_10)
        reset_password_screen_error.place(relx=210 / 1080, rely=1020 / 1855, relheight=60 / 1855, relwidth=660 / 1080)

        global reset_password_screen_back_button
        reset_password_screen_back_button = Button(main_screen, fg=bl, bg="black", bd=0, activebackground=bl, activeforeground=bl, highlightthickness=0, command=ResetPassword.back)
        reset_password_screen_back_button.update()
        im_raw_back_button = Image.open(Extras.resource_path("DataBase\\UIX\\back.png"))
        im_raw_back_button_resized = im_raw_back_button.resize((min_button1.winfo_width(), min_button1.winfo_height()))
        back_button_img = ImageTk.PhotoImage(im_raw_back_button_resized)
        reset_password_screen_back_button.configure(image=back_button_img)
        reset_password_screen_back_button.image = back_button_img
        reset_password_screen_back_button.place(relx=0, rely=0, relwidth=117 / 1080, relheight=65 / 1920)

        """PasswordStrengthFrame"""

        password_req = Frame(reset_password_screen, bg=bl)
        password_req.place(relx=365 / 1080, rely=1200 / 1855, relwidth=350 / 1080, relheight=350 / 1855)

        global length_rp
        length_rp = Label(password_req, bg=bl, font=Settings.font_light_10)
        length_rp.pack(anchor=CENTER)

        global lower_case_rp
        lower_case_rp = Label(password_req, bg=bl, font=Settings.font_light_10)
        lower_case_rp.pack(anchor=CENTER)

        global upper_case_rp
        upper_case_rp = Label(password_req, bg=bl, font=Settings.font_light_10)
        upper_case_rp.pack(anchor=CENTER)

        global number_rp
        number_rp = Label(password_req, bg=bl, font=Settings.font_light_10)
        number_rp.pack(anchor=CENTER)

        global special_char_rp
        special_char_rp = Label(password_req, bg=bl, font=Settings.font_light_10)
        special_char_rp.pack(anchor=CENTER)

        global confirm_rp
        confirm_rp = Label(password_req, bg=bl, font=Settings.font_light_10)
        confirm_rp.pack(anchor=CENTER)

    @staticmethod
    def reset_password():

        reset_button.configure(cursor="wait")
        new_pass = new_password_enter.get()
        con_pass = confirm_password_enter.get()

        if new_pass == " New Password":
            reset_password_screen_error.configure(text="Enter New Password")
            reset_button.configure(cursor="")

        elif con_pass == " Confirm Password":
            reset_password_screen_error.configure(text="Enter Confirm Password")
            reset_button.configure(cursor="")

        elif new_pass != con_pass:
            reset_password_screen_error.configure(text="Confirm Password Does Not Matches")
            reset_button.configure(cursor="")

        elif not ResetPassword.requirements(new_pass):
            reset_password_screen_error.configure(text="Password does not meet Requirements")
            reset_button.configure(cursor="")

        else:
            Extras.modify_db('Reset_Password', "{},{}".format(Extras.encrypt(new_pass), Settings.reset_email))
            Extras.modify_db('delete_enc', str(uuid.UUID(int=uuid.getnode())))
            reset_password_screen_error.configure(text="New Password Successfully set")
            reset_button.configure(cursor="")
            reset_password_screen.after(1000, ResetPassword.back())

    # noinspection PyMethodMayBeStatic
    def requirements(self):

        new_pass = new_password_enter.get()
        con_pass = confirm_password_enter.get()

        a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0

        if len(new_pass) == 0:
            length_rp.configure(text="")
        elif 1 <= len(new_pass) < 8:
            length_rp.configure(text="\u2715 8 Characters", fg='#962626', padx=20)
            a1 = 0
        else:
            length_rp.configure(text="\u2713 8 Characters", fg='#3b8c15', padx=20)
            a1 = 1

        if len(new_pass) == 0:
            number_rp.configure(text="")
        elif re.search('[0-9]', new_pass) is None:
            number_rp.configure(text="\u2715 Number", fg='#962626', padx=20)
            a2 = 0
        else:
            number_rp.configure(text="\u2713 Number", fg='#3b8c15', padx=20)
            a2 = 1

        if len(new_pass) == 0:
            upper_case_rp.configure(text="")
        elif re.search('[A-Z]', new_pass) is None:
            upper_case_rp.configure(text="\u2715 Upper Case", fg='#962626', padx=20)
            a3 = 0
        else:
            upper_case_rp.configure(text="\u2713 Upper Case", fg='#3b8c15', padx=20)
            a3 = 1

        if len(new_pass) == 0:
            lower_case_rp.configure(text="")
        elif re.search('[a-z]', new_pass) is None:
            lower_case_rp.configure(text="\u2715 Lower Case", fg='#962626', padx=20)
            a4 = 0
        else:
            lower_case_rp.configure(text="\u2713 Lower Case", fg='#3b8c15', padx=20)
            a4 = 1

        if len(new_pass) == 0:
            special_char_rp.configure(text="")
        elif re.search('[!@#$%^&*]', new_pass) is None:
            special_char_rp.configure(text="\u2715 Special Character", fg='#962626', padx=20)
            a5 = 0
        else:
            special_char_rp.configure(text="\u2713 Special Character", fg='#3b8c15', padx=20)
            a5 = 1

        if a1 * a2 * a3 * a4 * a5 == 1:
            confirm_password_enter.configure(state="normal")
        else:
            confirm_password_enter.configure(state="disabled")

        if len(con_pass) == 0:
            confirm_rp.configure(text="")
        elif len(new_pass) == 0:
            confirm_rp.configure(text="")
        elif new_pass == " New Password":
            confirm_rp.configure(text="")
        elif con_pass == " Confirm Password":
            confirm_rp.configure(text="")
        elif con_pass != new_pass:
            confirm_rp.configure(text="\u2715 Confirm Password", fg='#962626', padx=20)
        else:
            confirm_rp.configure(text="\u2713 Confirm Password", fg='#3b8c15', padx=20)

        if a1 * a2 * a3 * a4 * a5 == 0:
            return False
        else:
            return True

    # noinspection PyMethodMayBeStatic
    def new_password_entry(self):
        if new_password_enter.get() == " New Password":
            new_password_enter.delete(0, 'end')
            new_password_enter.configure(show='\u26B9')

    # noinspection PyMethodMayBeStatic
    def new_password_leave(self):
        if len(new_password_enter.get()) == 0:
            entry = StringVar(reset_password_screen, " New Password")
            new_password_enter.configure(textvariable=entry)
            new_password_enter.configure(show='')

    # noinspection PyMethodMayBeStatic
    def con_password_entry(self):
        if confirm_password_enter.cget("state") == "normal":
            if confirm_password_enter.get() == " Confirm Password":
                confirm_password_enter.delete(0, 'end')
                confirm_password_enter.configure(show='\u26B9')

    # noinspection PyMethodMayBeStatic
    def con_password_leave(self):
        if len(confirm_password_enter.get()) == 0:
            entry = StringVar(reset_password_screen, " Confirm Password")
            confirm_password_enter.configure(textvariable=entry)
            confirm_password_enter.configure(show='')

    @staticmethod
    def back():

        Extras.modify_db('delete_enc', str(uuid.UUID(int=uuid.getnode())))
        reset_password_screen_back_button.destroy()
        reset_password_screen.destroy()
        Settings.reset_email = ""
        Login.login_screen()


class Virtue:

    @staticmethod
    def virtue_screen():
        bl = "black"
        wh = "white"
        gr = "#1F1F1F"

        global virtue_screen
        virtue_screen = Frame(main_screen, bg="black")
        virtue_screen.place(relx=0, rely=65 / 1920, relheight=1855 / 1920, relwidth=1)

        if time(4, 0, 0) <= datetime.now().time() <= time(11, 59, 0):
            greet_im = "gm"
        elif time(12, 0, 0) <= datetime.now().time() <= time(17, 59, 0):
            greet_im = "ga"
        else:
            greet_im = "ge"

        global greet
        raw_im_greet = Image.open(Extras.resource_path(f"DataBase\\UIX\\{greet_im}.png"))
        resize = raw_im_greet.resize((int((Settings.screen_width / 3840) * raw_im_greet.size[0]), int((Settings.screen_height / 2160) * raw_im_greet.size[1])))
        login_back = ImageTk.PhotoImage(resize)
        greet = Label(virtue_screen, image=login_back, bg=bl, borderwidth=0, highlightthickness=0)
        greet.image = login_back
        greet.place(relx=50 / 1080, rely=50 / 1855)
        greet.wait_visibility()

        global suggestion
        raw_im_suggestion = Image.open(Extras.resource_path(f"DataBase\\UIX\\suggestion.png"))
        resize = raw_im_suggestion.resize((int((Settings.screen_width / 3840) * raw_im_suggestion.size[0]), int((Settings.screen_height / 2160) * raw_im_suggestion.size[1])))
        im_suggestion = ImageTk.PhotoImage(resize)
        suggestion = Label(virtue_screen, image=im_suggestion, bg=bl, borderwidth=0, highlightthickness=0)
        suggestion.image = im_suggestion
        suggestion.place(relx=90 / 1080, rely=475 / 1855)
        suggestion.wait_visibility()

        global error
        error = Label(virtue_screen, text="Sorry, didn't catch you", bg="red", fg="white", font=Settings.font_bold_16_segoe)
        error.place_forget()

        global animation
        animation = Label(virtue_screen, bg="black")
        animation.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
        Virtue.load_animation(0)

        global animation_mask
        animation_mask = Label(virtue_screen, bg="black")
        animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)

        global mic
        raw_im_mic = Image.open(Extras.resource_path("DataBase\\UIX\\mic.png"))
        resize = raw_im_mic.resize((int((Settings.screen_width / 3840) * raw_im_mic.size[0]), int((Settings.screen_height / 2160) * raw_im_mic.size[1])))
        im_mic = ImageTk.PhotoImage(resize)
        mic = Button(virtue_screen, text="Sign In", image=im_mic, bg=gr, fg=wh, bd=0, font=Settings.font_bold_10, activebackground=bl, activeforeground=bl,
                     command=Virtue.search_init)
        mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
        mic.image = im_mic

        global Settings_icon
        raw_im_greet = Image.open(Extras.resource_path("DataBase\\UIX\\Settings.png"))
        resize = raw_im_greet.resize((int((Settings.screen_width / 3840) * 48), int((Settings.screen_height / 2160) * 48)))
        login_back = ImageTk.PhotoImage(resize)
        Settings_icon = Button(virtue_screen, image=login_back, bg=bl, borderwidth=0, highlightthickness=0, activebackground=bl, activeforeground=bl, relief=SUNKEN,
                               command=Virtue.account)
        Settings_icon.image = login_back
        Settings_icon.place(relx=1030 / 1080, rely=50 / 1855, anchor=NE)

        global results_main
        results_main = Label(virtue_screen, bg="black")
        results_main.place_forget()

    @staticmethod
    def search_init():

        try:
            results_main.place_forget()
        except(ValueError, Exception):
            pass

        th = threading.Timer(0.001, Virtue.search)
        th.daemon = True
        th.start()

        root_sub.after(1000, animation_mask.place_forget())
        mic.place_forget()

    @staticmethod
    def search():

        r = sr.Recognizer()
        r.pause_threshold = 0.8

        with sr.Microphone() as source:

            try:
                audio = r.recognize_google(r.listen(source), language="en-US", key="AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw")
                print(audio)
                if "weather" in audio:
                    AudioProcessor.weather(audio)
                elif any(word in audio for word in
                         ["into", "multiply", "multiplied", "divided", "divide", "upon", "plus", "add", "addition", "to", "and", "subtract", "from", "minus", "square",
                          "root", "+", "*", "/", "-"]):
                    AudioProcessor.maths(audio)
                elif "volume" in audio:
                    AudioProcessor.system_changes(audio)
                elif "brightness" in audio:
                    AudioProcessor.system_changes(audio)
                elif "open" in audio:
                    AudioProcessor.open(audio)
                elif "start" in audio:
                    AudioProcessor.open(audio)
                else:
                    animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                    mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                    Extras.text_to_speech("Sorry, didn't catch you")

            except(ValueError, Exception):
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech("Sorry, didn't catch you")

    # noinspection SpellCheckingInspection
    @staticmethod
    def load_animation(ind):

        list123 = [(Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-001.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-002.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-003.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-004.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-005.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-006.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-007.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-008.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-009.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-010.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-011.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-012.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-013.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-014.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-015.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-016.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-017.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-018.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-019.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-020.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-021.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-022.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-023.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-024.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-025.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-026.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-027.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-028.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-029.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-030.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-031.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-032.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-033.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-034.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-035.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-036.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-037.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-038.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-039.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-040.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-041.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-042.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-043.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-044.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-045.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-046.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-047.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-048.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-049.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-050.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-051.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-052.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-053.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-054.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-055.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-056.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-057.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-058.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-059.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-060.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-061.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-062.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-063.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-064.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-065.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-066.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-067.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-068.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-069.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-070.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-071.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-072.jpg")),
                   (Extras.resource_path("DataBase\\UIX\\animation\\ezgif-frame-073.jpg"))]

        if ind > len(list123) - 1:
            Virtue.load_animation(0)
        else:
            im1 = Image.open(list123[ind])
            resize = im1.resize((int(Settings.screen_res_x * 0.82), int(Settings.screen_res_x * 0.25)))
            login_back = ImageTk.PhotoImage(resize)
            ind += 1
            animation.configure(image=login_back, anchor=CENTER)
            animation.image = login_back
            animation.after(40, Virtue.load_animation, ind)

    @staticmethod
    def account():

        global account_screen
        account_screen = Frame(virtue_screen, bg="black")
        account_screen.place(relx=50 / 1080, rely=350 / 1855, relheight=1400 / 1855, relwidth=980 / 1080)

        global acc_canvas
        acc_canvas = Canvas(account_screen, bg="black", borderwidth=0, highlightthickness=0)
        acc_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        raw_im_account_screen_back = Image.open(Extras.resource_path(f"DataBase\\UIX\\account2.png"))
        resize = raw_im_account_screen_back.resize(
            (int((Settings.screen_width / 3840) * raw_im_account_screen_back.size[0]), int((Settings.screen_height / 2160) * raw_im_account_screen_back.size[1])))
        im_account_screen_back = ImageTk.PhotoImage(resize)

        acc_canvas.create_image(0, 0, image=im_account_screen_back, anchor=NW)
        acc_canvas.image = im_account_screen_back

        close = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(40), anchor=NE)
        acc_canvas.itemconfig(close, text="\u2715", font=Settings.font_light_12, fill="white")
        acc_canvas.tag_bind(close, "<Button-1>", lambda e: account_screen.destroy())

        current_id = str(uuid.UUID(int=uuid.getnode()))
        acc_check = Extras.search_db('about', current_id)

        head_1 = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(75), anchor=NW)
        acc_canvas.itemconfig(head_1, text="Account Details", font=Settings.font_bold_14_segoe, fill="#C0A94A")

        head_1_name = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(200), anchor=NW)
        acc_canvas.itemconfig(head_1_name, text="Username", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_1_name_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(200), anchor=NE)
        acc_canvas.itemconfig(head_1_name_1, text=acc_check[0][0], font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_1_email = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(300), anchor=NW)
        acc_canvas.itemconfig(head_1_email, text="Email", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_1_email_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(300), anchor=NE)
        acc_canvas.itemconfig(head_1_email_1, text=acc_check[0][1], font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_1_bd = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(400), anchor=NW)
        acc_canvas.itemconfig(head_1_bd, text="Birth Date", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_1_bd_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(400), anchor=NE)
        acc_canvas.itemconfig(head_1_bd_1, text=acc_check[0][2], font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_2 = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(550), anchor=NW)
        acc_canvas.itemconfig(head_2, text="Device Info", font=Settings.font_bold_14_segoe, fill="#C0A94A")

        head_2_bd = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(675), anchor=NW)
        acc_canvas.itemconfig(head_2_bd, text="Device ID", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_2_bd_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(675), anchor=NE)
        acc_canvas.itemconfig(head_2_bd_1, text=str(current_id)[-22:-1], font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_3 = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(825), anchor=NW)
        acc_canvas.itemconfig(head_3, text="About", font=Settings.font_bold_14_segoe, fill="#C0A94A")

        head_3_app_name = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(950), anchor=NW)
        acc_canvas.itemconfig(head_3_app_name, text="App Name", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_3_app_name_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(950), anchor=NE)
        acc_canvas.itemconfig(head_3_app_name_1, text="Virtue", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_3_app_version = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(1050), anchor=NW)
        acc_canvas.itemconfig(head_3_app_version, text="Version", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_3_app_version_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(1050), anchor=NE)
        acc_canvas.itemconfig(head_3_app_version_1, text="11.14.20", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_3_app_developer = acc_canvas.create_text(Extras.scale_x(50), Extras.scale_y(1150), anchor=NW)
        acc_canvas.itemconfig(head_3_app_developer, text="Developer", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        head_3_app_developer_1 = acc_canvas.create_text(Extras.scale_x(930), Extras.scale_y(1150), anchor=NE)
        acc_canvas.itemconfig(head_3_app_developer_1, text="Karan Sangaj", font=Settings.font_light_12_segoe, fill="#B9C3C6")

        sign_out = acc_canvas.create_text(Extras.scale_x(490), Extras.scale_y(1300), anchor=CENTER)
        acc_canvas.itemconfig(sign_out, text="Sign out", font=Settings.font_bold_14_segoe, fill="#C0A94A")
        acc_canvas.tag_bind(sign_out, "<Button-1>", Virtue.sign_out)

    @staticmethod
    def sign_out(event):

        Extras.modify_db('sign_out', str(uuid.UUID(int=uuid.getnode())))
        Login.login_screen()
        virtue_screen.destroy()


class AudioProcessor:

    @staticmethod
    def maths(audio_filter):

        num_str = []

        for i in range(-1000, 10000, 1):
            num_str.append(str(i))

        str_filter = ["into", "multiply", "multiplied", "by", "divided", "divide", "upon", "plus", "add", "addition", "to", "and", "subtract", "from", "minus", "square", "of",
                      "root", "+", "*", "/", "-"]
        y = str(audio_filter).split()
        not_required = (set(y) - set(num_str)) - set(str_filter)

        for i in set(y):
            if i in not_required:
                y.remove(i)
            else:
                pass

        cleaned_string = " ".join(y)
        new_string = ""

        for i in range(0, 1, 1):

            "Multiplication"
            if "multiply" in cleaned_string and "by" in cleaned_string:
                new_string = cleaned_string.replace("multiply", "")
                new_string = new_string.replace("by", "*")
                cleaned_string = ""
            if "multiplied" in cleaned_string and "by" in cleaned_string:
                new_string = cleaned_string.replace("multiplied", "")
                new_string = new_string.replace("by", "*")
                cleaned_string = ""
            if "into" in cleaned_string:
                new_string = cleaned_string.replace("into", "*")
                cleaned_string = ""

            "Divide"
            if "divide" in cleaned_string and "by" in cleaned_string:
                new_string = cleaned_string.replace("divide", "")
                new_string = new_string.replace("by", "/")
                cleaned_string = ""
            if "divided" in cleaned_string and "by" in cleaned_string:
                new_string = cleaned_string.replace("divided", "")
                new_string = new_string.replace("by", "/")
                cleaned_string = ""
            if "upon" in cleaned_string:
                new_string = cleaned_string.replace("upon", "/")
                cleaned_string = ""

            "Subtract"
            if "subtract" in cleaned_string and "from" in cleaned_string:
                new_string = cleaned_string.replace("subtract", "-")
                new_string = new_string.replace("from", "+")
                cleaned_string = ""
            if "minus" in cleaned_string:
                new_string = cleaned_string.replace("minus", "-")
                cleaned_string = ""

            "Addition"
            if "add" in cleaned_string and "and" in cleaned_string:
                new_string = cleaned_string.replace("add", "")
                new_string = new_string.replace("and", "+")
                cleaned_string = ""
            if "add" in cleaned_string and "to" in cleaned_string:
                new_string = cleaned_string.replace("add", "")
                new_string = new_string.replace("to", "+")
                cleaned_string = ""
            if "plus" in cleaned_string:
                new_string = cleaned_string.replace("plus", "+")
                cleaned_string = ""
            if "addition" in cleaned_string and "of" in cleaned_string and "and" in cleaned_string:
                new_string = cleaned_string.replace("addition", "")
                new_string = new_string.replace("of", "")
                new_string = new_string.replace("and", "+")
                cleaned_string = ""

            "Expo"
            if "square root of" in cleaned_string:
                new_string = cleaned_string + str("**0.5")
                new_string = new_string.replace("square root of", "")
                cleaned_string = ""
            if "square of" in cleaned_string:
                new_string = cleaned_string + str("**2")
                new_string = new_string.replace("square of", "")
                cleaned_string = ""
            if "square" in cleaned_string:
                new_string = cleaned_string + str("**2")
                new_string = new_string.replace("square", "")
                cleaned_string = ""
            if "root of" in cleaned_string:
                new_string = cleaned_string + str("**0.5")
                new_string = new_string.replace("root of", "")
                cleaned_string = ""
            if "root" in cleaned_string:
                new_string = cleaned_string + str("**0.5")
                new_string = new_string.replace("root", "")
                cleaned_string = ""

            "symbols"
            if "+" in cleaned_string:
                new_string = cleaned_string
                cleaned_string = ""
            if "-" in cleaned_string:
                new_string = cleaned_string
                cleaned_string = ""

        try:

            if eval(new_string):

                results_main.place(relx=0, rely=0, relwidth=1080 / 1080, relheight=1450 / 1855)

                raw_im_results = Image.open(Extras.resource_path("DataBase\\UIX\\result2.png"))
                resize = raw_im_results.resize((int((Settings.screen_width / 3840) * raw_im_results.size[0]), int((Settings.screen_height / 2160) * raw_im_results.size[1])))
                login_back = ImageTk.PhotoImage(resize)
                results_math = Label(results_main, image=login_back, bg="black", borderwidth=0, highlightthickness=0)
                results_math.image = login_back
                results_math.place(relx=50 / 1080, rely=50 / 1450, relheight=980 / 1450, relwidth=980 / 1080)

                global hover_math
                hover_math = Canvas(results_math, bg="#181818", borderwidth=0, highlightthickness=0)
                hover_math.place(relx=0, rely=50 / 980, relwidth=1, relheight=880 / 980)

                close = hover_math.create_text(Extras.scale_x(930), Extras.scale_y(30), anchor=NE)
                hover_math.itemconfig(close, text="\u2715", font=Settings.font_light_12, fill="#545454")
                hover_math.tag_bind(close, "<Button-1>", lambda e: results_main.place_forget())

                question = hover_math.create_text(Extras.scale_x(50), Extras.scale_y(50), anchor="w")
                hover_math.itemconfig(question, text=str(audio_filter), font=Settings.font_light_16, fill="#2187C3")

                hover_math.create_line(Extras.scale_x(50), Extras.scale_y(100), Extras.scale_x(930), Extras.scale_y(100), width=Extras.scale_y(5), fill="#272727")

                answer = hover_math.create_text(Extras.scale_x(50), Extras.scale_y(200), anchor="w")

                if divmod(eval(new_string), 2)[1] == 0:
                    ans = eval(new_string)
                else:
                    ans = round(eval(new_string), 2)
                hover_math.itemconfig(answer, text=ans, font=Settings.font_bold_24, fill="white")

                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech(f'Answer is {ans}')

        except(ValueError, Exception):
            animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
            mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
            Extras.text_to_speech("Sorry, didn't catch you")

    # noinspection SpellCheckingInspection
    @staticmethod
    def weather(audio_filter):

        user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        language = "en-US,en;q=0.5"

        session = requests.Session()
        session.headers['User-Agent'] = user_agent
        session.headers['Accept-Language'] = language
        session.headers['Content-Language'] = language
        url = f'https://www.google.com/search?q={audio_filter.replace(" ", "+")}'
        html = session.get(url)
        soup = BeautifulSoup(html.text, "html.parser")

        result = {'region': soup.find("div", attrs={"id": "wob_loc"}).text, 'temp_now': soup.find("span", attrs={"id": "wob_tm"}).text,
                  'dayhour': soup.find("div", attrs={"id": "wob_dts"}).text, 'weather_now': soup.find("span", attrs={"id": "wob_dc"}).text,
                  'precipitation': soup.find("span", attrs={"id": "wob_pp"}).text, 'humidity': soup.find("span", attrs={"id": "wob_hm"}).text,
                  'wind': soup.find("span", attrs={"id": "wob_ws"}).text, 'image': re.search('src="//(.*)"/>', str(soup.find("img", attrs={"id": "wob_tci"}))).group(1)}

        results_main.place(relx=0, rely=0, relwidth=1080 / 1080, relheight=1450 / 1855)

        global results_weather
        raw_im_results = Image.open(Extras.resource_path("DataBase\\UIX\\result2.png"))
        resize = raw_im_results.resize((int((Settings.screen_width / 3840) * raw_im_results.size[0]), int((Settings.screen_height / 2160) * raw_im_results.size[1])))
        login_back = ImageTk.PhotoImage(resize)
        results_weather = Label(results_main, image=login_back, bg="black", borderwidth=0, highlightthickness=0)
        results_weather.image = login_back
        results_weather.place(relx=50 / 1080, rely=50 / 1450, relheight=980 / 1450, relwidth=980 / 1080)

        hover_up = Canvas(results_weather, bg="#181818", borderwidth=0, highlightthickness=0)
        hover_up.place(relx=0, rely=50 / 980, relwidth=1, relheight=880 / 980)

        close = hover_up.create_text(Extras.scale_x(930), Extras.scale_y(0), anchor=NE)
        hover_up.itemconfig(close, text="\u2715", font=Settings.font_light_12, fill="#545454")
        hover_up.tag_bind(close, "<Button-1>", lambda e: results_main.place_forget())

        region = hover_up.create_text(Extras.scale_x(50), Extras.scale_y(100), anchor="w")
        hover_up.itemconfig(region, text=result['region'].split(",")[0] + ', ' + (result['region'].split(",")[1]).split()[0], font=Settings.font_light_16_segoe, fill="white")

        day = hover_up.create_text(Extras.scale_x(50), Extras.scale_y(185), anchor="w")
        hover_up.itemconfig(day, text=result['dayhour'], font=Settings.font_light_14_segoe, fill="white")
        img_file = io.BytesIO(urllib.request.urlopen("https://" + result['image']).read())
        im = ImageTk.PhotoImage(Image.open(img_file).convert('RGBA').resize((Extras.scale_x(275), Extras.scale_y(275))))
        hover_up.create_image(Extras.scale_x(25), Extras.scale_y(280), image=im, anchor=NW)
        hover_up.image = im

        temp = hover_up.create_text(Extras.scale_x(350), Extras.scale_y(365), anchor="w")
        hover_up.itemconfig(temp, text=result['temp_now'], font=Settings.font_bold_36_segoe, fill="white")

        degree = hover_up.create_text(hover_up.bbox(temp)[2] + Extras.scale_x(10), Extras.scale_y(360), anchor="w")
        hover_up.itemconfig(degree, text="\u00B0", font=Settings.font_light_24, fill="white")

        cel = hover_up.create_text(hover_up.bbox(temp)[2] + Extras.scale_x(50), Extras.scale_y(360), anchor="w")
        hover_up.itemconfig(cel, text="C", font=Settings.font_light_24, fill="white")

        weather_now = hover_up.create_text(Extras.scale_x(350), Extras.scale_y(480), anchor="w")
        hover_up.itemconfig(weather_now, text=result['weather_now'], font=Settings.font_light_14_segoe, fill="white")

        precipitation = hover_up.create_text(Extras.scale_x(50), Extras.scale_y(650), anchor="w")
        hover_up.itemconfig(precipitation, text="Precipitation : " + result['precipitation'], font=Settings.font_light_14_segoe, fill="white")

        humidity = hover_up.create_text(Extras.scale_x(500), Extras.scale_y(650), anchor="w")
        hover_up.itemconfig(humidity, text="Humidity : " + result['humidity'], font=Settings.font_light_14_segoe, fill="white")

        wind = hover_up.create_text(Extras.scale_x(50), Extras.scale_y(720), anchor="w")
        hover_up.itemconfig(wind, text="Wind : " + result['wind'], font=Settings.font_light_14_segoe, fill="white")

        sponsor = hover_up.create_text(Extras.scale_x(650), Extras.scale_y(855), anchor="w")
        hover_up.itemconfig(sponsor, text="powered by Google", font=Settings.font_light_10_segoe, fill="#727272")

        animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
        mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)

        out_res = result['temp_now']
        out_reg = result['region'].split(",")[0]
        Extras.text_to_speech(f'Temperature in {out_reg} is {out_res} degree Celsius')

    bright_text = ""
    bright_audio = ""

    @staticmethod
    def system_changes(audio_filter):

        if "volume" in audio_filter:
            keyboard = Controller()
            if "increase" in audio_filter:
                for i in range(5):
                    keyboard.press(Key.media_volume_up)
                    keyboard.release(Key.media_volume_up)
                    times.sleep(0.1)
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech(f'Volume Increased by 10')
            elif "lower" in audio_filter:
                for i in range(5):
                    keyboard.press(Key.media_volume_down)
                    keyboard.release(Key.media_volume_down)
                    times.sleep(0.1)
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech(f'Volume Decreased by 10')
            elif "decrease" in audio_filter:
                for i in range(5):
                    keyboard.press(Key.media_volume_down)
                    keyboard.release(Key.media_volume_down)
                    times.sleep(0.1)
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech(f'Volume Decreased by 10')
            elif "mute" in audio_filter:
                keyboard.press(Key.media_volume_mute)
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech(f'Volume muted')
            else:
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech("Sorry, didn't catch you")

        if "brightness" in audio_filter:

            print("brightness detected")

            digit_list = re.findall(r'\d+', str(audio_filter))

            if "what" in audio_filter:
                current_brightness = int(sbc.get_brightness())
                bright_text = f"{current_brightness} %"
                bright_audio = f"Brightness is {current_brightness}%"

            elif "increase" in audio_filter:
                if digit_list:
                    level = 10 * round(int(digit_list[0]) / 10)
                    sbc.fade_brightness(f'+{level}', increment=10)
                    bright_text = f"+{level} %"
                    bright_audio = f"Brightness Increased by {level}%"
                else:
                    sbc.fade_brightness('+10', increment=10)
                    bright_text = f"+10 %"
                    bright_audio = f"Brightness Increased by 10 %"

            elif "decrease" in audio_filter:
                if len(digit_list) > 0:
                    level = 10 * round(digit_list[0] / 10)
                    sbc.fade_brightness(f'-{level}', increment=10)
                    bright_text = f"-{level} %"
                    bright_audio = f"Brightness decreased by {level}%"
                else:
                    sbc.fade_brightness('-10', increment=10)
                    bright_text = f"-10 %"
                    bright_audio = f"Brightness decreased by 10 %"

            else:
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)
                Extras.text_to_speech("Sorry, didn't catch you")
                bright_text = ""
                bright_audio = ""

            if len(bright_text) > 0:

                results_main.place(relx=0, rely=0, relwidth=1080 / 1080, relheight=1450 / 1855)

                global results_bright
                raw_im_results = Image.open(Extras.resource_path("DataBase\\UIX\\result2.png"))
                resize = raw_im_results.resize((int((Settings.screen_width / 3840) * raw_im_results.size[0]), int((Settings.screen_height / 2160) * raw_im_results.size[1])))
                login_back = ImageTk.PhotoImage(resize)
                results_bright = Label(results_main, image=login_back, bg="black", borderwidth=0, highlightthickness=0)
                results_bright.image = login_back
                results_bright.place(relx=50 / 1080, rely=50 / 1450, relheight=980 / 1450, relwidth=980 / 1080)

                hover_up = Canvas(results_bright, bg="#181818", borderwidth=0, highlightthickness=0)
                hover_up.place(relx=0, rely=50 / 980, relwidth=1, relheight=880 / 980)

                close = hover_up.create_text(Extras.scale_x(930), Extras.scale_y(30), anchor=NE)
                hover_up.itemconfig(close, text="\u2715", font=Settings.font_light_12, fill="#545454")
                hover_up.tag_bind(close, "<Button-1>", lambda e: results_main.place_forget())

                question = hover_up.create_text(Extras.scale_x(50), Extras.scale_y(50), anchor="w")
                hover_up.itemconfig(question, text=str(audio_filter), font=Settings.font_light_16, fill="#2187C3")

                hover_up.create_line(Extras.scale_x(50), Extras.scale_y(100), Extras.scale_x(930), Extras.scale_y(100), width=Extras.scale_y(5), fill="#272727")

                answer = hover_up.create_text(Extras.scale_x(50), Extras.scale_y(200), anchor="w")
                hover_up.itemconfig(answer, text=bright_text, font=Settings.font_bold_24, fill="white")

                Extras.text_to_speech(bright_audio)
                animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
                mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)

    @staticmethod
    def open(audio_filter):

        app = str(audio_filter).split()[-1]
        os.system(f'start {app}:')
        animation_mask.place(relx=140 / 1080, rely=1500 / 1855, relwidth=800 / 1080, relheight=300 / 1855)
        mic.place(relx=450 / 1080, rely=1560 / 1855, relheight=180 / 1855, relwidth=180 / 1080)


if __name__ == '__main__':
    Main.main_account_screen()
