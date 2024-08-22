import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
import pygame


# window
window = Tk()
window.title("In Between ")
window.geometry("1000x600")
window.configure(bg='#ffffff')
canvas = Canvas(window, width=1000, height=600)
canvas.pack()

# Initialize Pygame
pygame.mixer.init()
# Bg Music
background_music = pygame.mixer.Sound("mp3_background_music.mp3")
background_music.play()

# images
button1 = PhotoImage(file="reveal_button.png")
button2 = PhotoImage(file="new_game_button.png")
button3 = PhotoImage(file="bet_button.png")
button4 = PhotoImage(file="deal_button.png")
button5 = PhotoImage(file="no_deal_button.png")
button6 = PhotoImage(file="high_button.png")
button7 = PhotoImage(file="low_button.png")
start_button = PhotoImage(file="start_button.png")
quit_button = PhotoImage(file="quit_button.png")
back_button = PhotoImage(file="back_button.png")
main_menu_button = PhotoImage(file="main_menu_button.png")
money_box = PhotoImage(file="money_box.png")
rounds_box = PhotoImage(file="rounds_box.png")
bet_box = PhotoImage(file="bet_box.png")
three_rounds_button = PhotoImage(file="three_rounds.png")
five_rounds_button = PhotoImage(file="five_rounds.png")
ten_rounds_button = PhotoImage(file="ten_rounds.png")
background_image = PhotoImage(file="main bg.png")
background_image2 = PhotoImage(file="bg3.png")
background_image3 = PhotoImage(file="bg5.png")
background_image4 = PhotoImage(file="bg10.png")
won_image = PhotoImage(file="you_won.png")
lose_image = PhotoImage(file="you_lose.png")
jackpot_image = PhotoImage(file="jackpot.png")
in_between_logo = PhotoImage(file="in_between.png")
all_in_button = PhotoImage(file="all_in_button.png")
back_card = PhotoImage(file="back_card.png")
status_box = PhotoImage(file="status_box.png")
canvas.create_image(500, 300, image=background_image)
canvas.create_image(500, 300, image=in_between_logo)

# variables
global money
global card_image1
global card_image2
global card_image3
global first_card
global second_card
global third_card
global user_bet
global user_input
global rounds
global btn_back
global btn_reveal
global btn_new_game
global btn_bet
global btn_low
global btn_high
global num_rounds
global lbl_rounds
global lbl_money
global lbl_game_status
global ans
global bg_rounds
global money_scale
global btn_no_deal
global btn_deal

# random
ace = PhotoImage(file='A.png')
two = PhotoImage(file='2.png')
three = PhotoImage(file='3.png')
four = PhotoImage(file='4.png')
five = PhotoImage(file='5.png')
six = PhotoImage(file='6.png')
seven = PhotoImage(file='7.png')
eight = PhotoImage(file='8.png')
nine = PhotoImage(file='9.png')
ten = PhotoImage(file='10.png')
jack = PhotoImage(file='j.png')
queen = PhotoImage(file='q.png')
king = PhotoImage(file='k.png')
first_card = random.randint(0, 12)
second_card = random.randint(0, 12)
third_card = random.randint(0, 12)
first_card = 2
second_card = 2
third_card = 2
card_list1 = [ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king]
card_image1 = Label(window, image=card_list1[first_card])
card_image2 = Label(window, image=card_list1[second_card])
card_image3 = Label(window, image=card_list1[third_card])

# disabling to minimize windows
window.resizable(False, False)


def start():
    global btn_back
    global btn_three_rounds
    global btn_five_rounds
    global btn_ten_rounds
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    btn_back = Button(window, image=back_button, command=back, bg="#603b32", borderwidth=0)
    btn_three_rounds = Button(window, image=three_rounds_button, command=three_rounds, bg="#603b32", borderwidth=0)
    btn_five_rounds = Button(window, image=five_rounds_button, command=five_rounds, bg="#603b32", borderwidth=0)
    btn_ten_rounds = Button(window, image=ten_rounds_button, command=ten_rounds, bg="#603b32", borderwidth=0)
    btn_back.place(x=380, y=210)
    btn_three_rounds.place(x=120, y=300)
    btn_five_rounds.place(x=380, y=300)
    btn_ten_rounds.place(x=640, y=300)
    btn_start.destroy()
    btn_quit.destroy()
    canvas.delete()
    canvas.create_image(500, 300, image=background_image)


def quit_command():
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    answer = messagebox.askyesno("Quit?", "Are you sure?")
    if answer == 1:
        window.destroy()


def back():
    global btn_start
    global btn_back
    global btn_three_rounds
    global btn_five_rounds
    global btn_ten_rounds
    global btn_quit
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    btn_back.destroy()
    btn_start = Button(window, image=start_button, command=start, bg="#603b32", borderwidth=0)
    btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
    btn_start.place(x=180, y=465)
    btn_quit.place(x=580, y=465)
    btn_three_rounds.destroy()
    btn_five_rounds.destroy()
    btn_ten_rounds.destroy()
    canvas.delete()
    canvas.create_image(500, 300, image=background_image)
    canvas.create_image(500, 300, image=in_between_logo)
    btn_back = Button(window, image=back_button, command=back, bg="#603b32", borderwidth=0)
    btn_three_rounds = Button(window, image=three_rounds_button, command=three_rounds, bg="#603b32", borderwidth=0)
    btn_five_rounds = Button(window, image=five_rounds_button, command=five_rounds, bg="#603b32", borderwidth=0)
    btn_ten_rounds = Button(window, image=ten_rounds_button, command=ten_rounds, bg="#603b32", borderwidth=0)


def main_menu():
    global btn_start
    global btn_quit
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    btn_main_menu.destroy()
    btn_quit.destroy()
    btn_start = Button(window, image=start_button, command=start, bg="#603b32", borderwidth=0)
    btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
    btn_start.place(x=180, y=465)
    btn_quit.place(x=580, y=465)
    lbl_rounds.destroy()
    lbl_money.destroy()
    lbl_bet.destroy()
    canvas.delete()
    canvas.create_image(500, 300, image=background_image)
    canvas.create_image(500, 300, image=in_between_logo)


def three_rounds():
    btn_back.destroy()
    btn_three_rounds.destroy()
    btn_five_rounds.destroy()
    btn_ten_rounds.destroy()
    global money
    global num_rounds
    global btn_reveal
    global btn_new_game
    global btn_bet
    global lbl_rounds
    global lbl_money
    global lbl_bet
    global bg_rounds
    global money_scale
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    num_rounds = 3
    money = 300
    bg_rounds = 3
    money_scale = Scale(window, from_=0, to=money, orient=HORIZONTAL, command=slider,
                        state='disabled', bg='#603b32',
                        fg='white', length=350, width=25)
    btn_reveal = Button(window, image=button1, command=reveal, bg="#603b32", borderwidth=0)
    btn_new_game = Button(window, image=button2, command=new_game, bg="#603b32", borderwidth=0, state='disabled')
    btn_bet = Button(window, image=button3, command=bet, bg="#603b32", borderwidth=0, state='disabled')
    lbl_money = Label(window, font=('card characters', 13), text=money, bg='#c58d6b')
    lbl_rounds = Label(window, font=('card characters', 30), text=num_rounds, bg='#c58d6b')
    lbl_bet = Label(window, font=('card characters', 13), text="PHP 0000", bg='#c58d6b')
    lbl_rounds.config(text='0' + str(num_rounds))
    lbl_money.config(text='PHP 0' + str(money))
    btn_bet.place(x=380, y=487)
    btn_reveal.place(x=45, y=487)
    btn_new_game.place(x=710, y=487)
    lbl_money.place(x=53, y=100)
    lbl_rounds.place(x=870, y=90)
    lbl_bet.place(x=53, y=300)
    canvas.delete()
    canvas.create_image(500, 300, image=background_image2)
    canvas.create_image(100, 100, image=money_box)
    canvas.create_image(900, 100, image=rounds_box)
    canvas.create_image(100, 300, image=bet_box)
    canvas.create_image(280, 160, image=back_card)
    canvas.create_image(500, 160, image=back_card)
    canvas.create_image(720, 160, image=back_card)


def five_rounds():
    btn_back.destroy()
    btn_three_rounds.destroy()
    btn_five_rounds.destroy()
    btn_ten_rounds.destroy()
    global money
    global num_rounds
    global btn_reveal
    global btn_new_game
    global btn_bet
    global lbl_rounds
    global lbl_money
    global lbl_bet
    global bg_rounds
    global money_scale
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    num_rounds = 5
    money = 500
    bg_rounds = 5
    money_scale = Scale(window, from_=0, to=money, orient=HORIZONTAL, command=slider,
                        state='disabled', bg='#603b32',
                        fg='white', length=350, width=25)
    btn_reveal = Button(window, image=button1, command=reveal, bg="#603b32", borderwidth=0)
    btn_new_game = Button(window, image=button2, command=new_game, bg="#603b32", borderwidth=0, state='disabled')
    btn_bet = Button(window, image=button3, command=bet, bg="#603b32", borderwidth=0, state='disabled')
    lbl_money = Label(window, font=('card characters', 13), text=money, bg='#c58d6b')
    lbl_rounds = Label(window, font=('card characters', 30), text=num_rounds, bg='#c58d6b')
    lbl_bet = Label(window, font=('card characters', 13), text="PHP 0000", bg='#c58d6b')
    lbl_rounds.config(text='0' + str(num_rounds))
    lbl_money.config(text='PHP 0' + str(money))
    btn_bet.place(x=380, y=487)
    btn_reveal.place(x=45, y=487)
    btn_new_game.place(x=710, y=487)
    lbl_money.place(x=53, y=100)
    lbl_rounds.place(x=870, y=90)
    lbl_bet.place(x=53, y=300)
    canvas.delete()
    canvas.create_image(500, 300, image=background_image3)
    canvas.create_image(100, 100, image=money_box)
    canvas.create_image(900, 100, image=rounds_box)
    canvas.create_image(100, 300, image=bet_box)
    canvas.create_image(280, 160, image=back_card)
    canvas.create_image(500, 160, image=back_card)
    canvas.create_image(720, 160, image=back_card)


def ten_rounds():
    btn_back.destroy()
    btn_three_rounds.destroy()
    btn_five_rounds.destroy()
    btn_ten_rounds.destroy()
    global money
    global num_rounds
    global btn_reveal
    global btn_new_game
    global btn_bet
    global lbl_rounds
    global lbl_money
    global lbl_bet
    global bg_rounds
    global money_scale
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    num_rounds = 10
    money = 1000
    bg_rounds = 10
    money_scale = Scale(window, from_=0, to=money, orient=HORIZONTAL, command=slider,
                        state='disabled', bg='#603b32',
                        fg='white', length=350, width=25)
    btn_reveal = Button(window, image=button1, command=reveal, bg="#603b32", borderwidth=0)
    btn_new_game = Button(window, image=button2, command=new_game, bg="#603b32", borderwidth=0, state='disabled')
    btn_bet = Button(window, image=button3, command=bet, bg="#603b32", borderwidth=0, state='disabled')
    lbl_money = Label(window, font=('card characters', 13), text=money, bg='#c58d6b')
    lbl_rounds = Label(window, font=('card characters', 30), text=num_rounds, bg='#c58d6b')
    lbl_bet = Label(window, font=('card characters', 13), text="PHP 0000", bg='#c58d6b')
    lbl_rounds.config(text=num_rounds)
    lbl_money.config(text='PHP ' + str(money))
    btn_bet.place(x=380, y=487)
    btn_reveal.place(x=45, y=487)
    btn_new_game.place(x=710, y=487)
    lbl_money.place(x=53, y=100)
    lbl_rounds.place(x=870, y=90)
    lbl_bet.place(x=53, y=300)
    canvas.delete()
    canvas.create_image(500, 300, image=background_image4)
    canvas.create_image(100, 100, image=money_box)
    canvas.create_image(900, 100, image=rounds_box)
    canvas.create_image(100, 300, image=bet_box)
    canvas.create_image(280, 160, image=back_card)
    canvas.create_image(500, 160, image=back_card)
    canvas.create_image(720, 160, image=back_card)


def reveal():
    global card_image1
    global card_image2
    global btn_no_deal
    global btn_deal
    global btn_low
    global btn_high
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    btn_high = Button(window, image=button6, command=high, bg="#603b32", borderwidth=0)
    btn_low = Button(window, image=button7, command=low, bg="#603b32", borderwidth=0)
    btn_new_game['state'] = 'disable'
    btn_reveal['state'] = 'disable'
    canvas.create_image(280, 160, image=card_list1[first_card])
    canvas.create_image(720, 160, image=card_list1[second_card])
    if first_card != second_card:
        btn_deal = Button(window, image=button4, command=deal, bg="#603b32", borderwidth=0)
        btn_no_deal = Button(window, image=button5, command=no_deal, bg="#603b32", borderwidth=0)
        btn_deal.place(x=45, y=400)
        btn_no_deal.place(x=710, y=400)
    else:
        btn_high = Button(window, image=button6, command=high, bg="#603b32", borderwidth=0)
        btn_low = Button(window, image=button7, command=low, bg="#603b32", borderwidth=0)
        btn_high.place(x=45, y=400)
        btn_low.place(x=710, y=400)


def slider(var):
    global user_bet
    user_bet = int(money_scale.get())
    if user_bet < 1000:
        lbl_bet.config(text='PHP 0' + str(user_bet))
    elif user_bet < 100:
        lbl_bet.config(text='PHP 00' + str(user_bet))
    elif user_bet < 10:
        lbl_bet.config(text='PHP 000' + str(user_bet))
    else:
        lbl_bet.config(text='PHP ' + str(user_bet))
    if user_bet >= 100:
        btn_bet['state'] = 'normal'
    else:
        btn_bet['state'] = 'disable'


def deal():
    global card_image3
    global third_card
    global money
    global money_scale
    global btn_all_in
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    if money < 100:
        btn_all_in = Button(window, image=all_in_button, command=all_in, bg="#603b32", borderwidth=0)
        btn_all_in.place(x=380, y=400)
    else:
        money_scale = Scale(window, from_=0, to=money, orient=HORIZONTAL, command=slider,
                            state='disabled', bg='#603b32',
                            fg='white', length=350, width=25)
        money_scale.place(x=325, y=400)
        money_scale['state'] = 'normal'
    btn_deal['state'] = 'disable'
    btn_no_deal['state'] = 'disable'
    btn_reveal['state'] = 'disable'


def all_in():
    global user_bet
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    user_bet = money
    lbl_bet.config(text='PHP 00' + str(user_bet))
    btn_bet['state'] = 'normal'


def no_deal():
    global first_card
    global second_card
    global money
    global num_rounds
    global btn_main_menu
    global btn_quit
    global lbl_money
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    num_rounds -= 1
    if num_rounds == 10:
        lbl_rounds.config(text=num_rounds)
    else:
        lbl_rounds.config(text='0' + str(num_rounds))
    btn_deal['state'] = 'disable'
    btn_new_game['state'] = 'normal'
    btn_no_deal['state'] = 'disable'
    btn_reveal['state'] = 'disable'
    card_image1.destroy()
    card_image2.destroy()
    first_card = random.randint(0, 12)
    second_card = random.randint(0, 12)
    if bg_rounds == 10:
        if money < 100:
            money = money - money
        else:
            money = money - 100
    elif bg_rounds == 5:
        if money < 75:
            money = money - money
        else:
            money = money - 75
    else:
        if money < 50:
            money = money - money
        else:
            money = money - 50
    if money < 1000:
        lbl_money.config(text='PHP 0' + str(int(money)))
    elif money < 100:
        lbl_money.config(text='PHP 00' + str(int(money)))
    elif money < 10:
        lbl_money.config(text='PHP 000' + str(int(money)))
    else:
        lbl_money.config(text='PHP ' + str(int(money)))
    print(money)
    if num_rounds == 0:
        canvas.create_image(500, 300, image=status_box)
        btn_bet.destroy()
        btn_new_game.destroy()
        btn_reveal.destroy()
        lbl_money.destroy()
        lbl_bet.destroy()
        btn_main_menu = Button(window, image=main_menu_button, command=main_menu, bg="#603b32", borderwidth=0)
        btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
        lbl_money = Label(window, font=('card characters', 20), text=money, bg='#603b32', fg='white')
        lbl_money.place(x=580, y=446)
        btn_quit.place(x=580, y=486)
        btn_main_menu.place(x=180, y=486)
        if money < 1000:
            lbl_money.config(text='PHP 0' + str(int(money)))
        elif money < 100:
            lbl_money.config(text='PHP 00' + str(int(money)))
        elif money < 10:
            lbl_money.config(text='PHP 000' + str(int(money)))
        else:
            lbl_money.config(text='PHP ' + str(int(money)))
        if first_card != second_card:
            btn_deal.destroy()
            btn_no_deal.destroy()
        else:
            btn_high.destroy()
            btn_low.destroy()
    if money == 0:
        canvas.create_image(500, 300, image=status_box)
        btn_bet.destroy()
        btn_new_game.destroy()
        btn_reveal.destroy()
        lbl_money.destroy()
        lbl_bet.destroy()
        btn_main_menu = Button(window, image=main_menu_button, command=main_menu, bg="#603b32", borderwidth=0)
        btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
        lbl_money = Label(window, font=('card characters', 20), text=money, bg='#603b32', fg='white')
        lbl_money.place(x=580, y=446)
        btn_quit.place(x=580, y=486)
        btn_main_menu.place(x=180, y=486)
        if money < 1000:
            lbl_money.config(text='PHP 0' + str(money))
        if money < 100:
            lbl_money.config(text='PHP 00' + str(money))
        if money < 10:
            lbl_money.config(text='PHP 000' + str(money))
        if first_card != second_card:
            btn_deal.destroy()
            btn_no_deal.destroy()
        else:
            btn_high.destroy()
            btn_low.destroy()


def high():
    global card_image3
    global third_card
    global money
    global money_scale
    global user_input
    global btn_all_in
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    user_input = "high"
    btn_high['state'] = 'disable'
    btn_low['state'] = 'disable'
    if money < 100:
        btn_all_in = Button(window, image=all_in_button, command=all_in, bg="#603b32", borderwidth=0)
        btn_all_in.place(x=380, y=400)
    else:
        money_scale = Scale(window, from_=0, to=money, orient=HORIZONTAL, command=slider,
                            state='disabled', bg='#603b32',
                            fg='white', length=350, width=25)
        money_scale.place(x=325, y=400)
        money_scale['state'] = 'normal'


def low():
    global card_image3
    global third_card
    global money
    global money_scale
    global user_input
    global btn_all_in
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    user_input = "low"
    btn_high['state'] = 'disable'
    btn_low['state'] = 'disable'
    if money < 100:
        btn_all_in = Button(window, image=all_in_button, command=all_in, bg="#603b32", borderwidth=0)
        btn_all_in.place(x=380, y=400)
    else:
        money_scale = Scale(window, from_=0, to=money, orient=HORIZONTAL, command=slider,
                            state='disabled', bg='#603b32',
                            fg='white', length=350, width=25)
        money_scale.place(x=325, y=400)
        money_scale['state'] = 'normal'


def new_game():
    global card_image1
    global card_image2
    global first_card
    global second_card
    global third_card
    global btn_high
    global btn_low
    global btn_back
    global bg_rounds
    global num_rounds
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    if num_rounds == 10:
        lbl_rounds.config(text=num_rounds)
    else:
        lbl_rounds.config(text='0' + str(num_rounds))
    lbl_bet.config(text="PHP 0000")
    if first_card != second_card:
        btn_deal.destroy()
        btn_no_deal.destroy()
    else:
        btn_low.destroy()
        btn_high.destroy()
    btn_new_game['state'] = 'disable'
    btn_reveal['state'] = 'normal'
    canvas.delete()
    if bg_rounds == 3:
        canvas.create_image(500, 300, image=background_image2)
    elif bg_rounds == 5:
        canvas.create_image(500, 300, image=background_image3)
    else:
        canvas.create_image(500, 300, image=background_image4)
    canvas.create_image(100, 100, image=money_box)
    canvas.create_image(900, 100, image=rounds_box)
    canvas.create_image(100, 300, image=bet_box)
    canvas.create_image(280, 160, image=back_card)
    canvas.create_image(500, 160, image=back_card)
    canvas.create_image(720, 160, image=back_card)
    first_card = random.randint(0, 12)
    second_card = random.randint(0, 12)
    third_card = random.randint(0, 12)
    first_card = 2
    second_card = 2
    third_card = 2
    btn_high = Button(window, image=button6, command=high, bg="#603b32", borderwidth=0)
    btn_low = Button(window, image=button7, command=low, bg="#603b32", borderwidth=0)


def bet():
    global money
    global third_card
    global card_image3
    global user_bet
    global rounds
    global lbl_rounds
    global lbl_money
    global lbl_game_status
    global btn_main_menu
    global btn_quit
    global num_rounds
    pygame.mixer.music.load("button_sfx.mp3")
    pygame.mixer.music.play(loops=0)
    num_rounds -= 1
    btn_new_game['state'] = 'normal'
    third_card = random.randint(0, 12)
    third_card = 2
    canvas.create_image(500, 160, image=card_list1[third_card])
    print(str(first_card))
    print(str(second_card))
    print(str(third_card))
    btn_bet['state'] = 'disable'
    btn_all_in.destroy()
    if first_card != second_card:
        if ((second_card > third_card > first_card) or
                (second_card < third_card < first_card)):
            money = money + user_bet
            print("won")
            print(money)
            pygame.mixer.music.load("win_sfx.mp3")
            pygame.mixer.music.play(loops=0)
            canvas.create_image(500, 340, image=won_image)
            if money < 1000:
                lbl_money.config(text='PHP 0' + str(money))
            elif money < 100:
                lbl_money.config(text='PHP 00' + str(money))
            elif money < 10:
                lbl_money.config(text='PHP 000' + str(money))
            else:
                lbl_money.config(text='PHP ' + str(money))
        else:
            money = money - user_bet
            print("lose")
            print(money)
            canvas.create_image(500, 340, image=lose_image)
            pygame.mixer.music.load("lose_sfx.mp3")
            pygame.mixer.music.play(loops=0)
            if money < 1000:
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
    else:
        if user_input == "high":
            if first_card < third_card:
                money = money + user_bet
                print("won")
                print(money)
                pygame.mixer.music.load("win_sfx.mp3")
                pygame.mixer.music.play(loops=0)
                canvas.create_image(500, 340, image=won_image)
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
            elif first_card == third_card:
                money = money + (user_bet * 3)
                print("won")
                print(money)
                pygame.mixer.music.load("win_sfx.mp3")
                pygame.mixer.music.play(loops=0)
                canvas.create_image(500, 340, image=jackpot_image)
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
            else:
                money = money - user_bet
                print("lose")
                print(money)
                canvas.create_image(500, 340, image=lose_image)
                pygame.mixer.music.load("lose_sfx.mp3")
                pygame.mixer.music.play(loops=0)
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
        else:
            if first_card > third_card:
                money = money + user_bet
                print("won")
                print(money)
                pygame.mixer.music.load("win_sfx.mp3")
                pygame.mixer.music.play(loops=0)
                canvas.create_image(500, 340, image=won_image)
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
            elif first_card == third_card:
                money = money + (user_bet * 3)
                print("won")
                print(money)
                pygame.mixer.music.load("win_sfx.mp3")
                pygame.mixer.music.play(loops=0)
                canvas.create_image(500, 340, image=jackpot_image)
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
            else:
                money = money - user_bet
                print("lose")
                print(money)
                canvas.create_image(500, 340, image=lose_image)
                pygame.mixer.music.load("lose_sfx.mp3")
                pygame.mixer.music.play(loops=0)
                if money < 1000:
                    lbl_money.config(text='PHP 0' + str(money))
                elif money < 100:
                    lbl_money.config(text='PHP 00' + str(money))
                elif money < 10:
                    lbl_money.config(text='PHP 000' + str(money))
                else:
                    lbl_money.config(text='PHP ' + str(money))
    money_scale.destroy()
    if num_rounds != 0:
        if money == 0:
            canvas.create_image(500, 300, image=status_box)
            btn_bet.destroy()
            btn_new_game.destroy()
            btn_reveal.destroy()
            lbl_money.destroy()
            lbl_bet.destroy()
            btn_main_menu = Button(window, image=main_menu_button, command=main_menu, bg="#603b32", borderwidth=0)
            btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
            lbl_money = Label(window, font=('card characters', 20), text=money, bg='#603b32', fg='white')
            lbl_money.place(x=580, y=446)
            btn_quit.place(x=580, y=486)
            btn_main_menu.place(x=180, y=486)
            if money < 1000:
                lbl_money.config(text='PHP 0' + str(money))
            if money < 100:
                lbl_money.config(text='PHP 00' + str(money))
            if money < 10:
                lbl_money.config(text='PHP 000' + str(money))
            if first_card != second_card:
                btn_deal.destroy()
                btn_no_deal.destroy()
            else:
                btn_high.destroy()
                btn_low.destroy()
    else:
        if money == 0:
            canvas.create_image(500, 300, image=status_box)
            btn_bet.destroy()
            btn_new_game.destroy()
            btn_reveal.destroy()
            lbl_money.destroy()
            lbl_bet.destroy()
            btn_main_menu = Button(window, image=main_menu_button, command=main_menu, bg="#603b32", borderwidth=0)
            btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
            lbl_money = Label(window, font=('card characters', 20), text=money, bg='#603b32', fg='white')
            lbl_money.place(x=580, y=446)
            btn_quit.place(x=580, y=486)
            btn_main_menu.place(x=180, y=486)
            if first_card != second_card:
                btn_deal.destroy()
                btn_no_deal.destroy()
            else:
                btn_high.destroy()
                btn_low.destroy()
        else:
            canvas.create_image(500, 300, image=status_box)
            btn_bet.destroy()
            btn_new_game.destroy()
            btn_reveal.destroy()
            lbl_money.destroy()
            lbl_bet.destroy()
            btn_main_menu = Button(window, image=main_menu_button, command=main_menu, bg="#603b32", borderwidth=0)
            btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
            lbl_money = Label(window, font=('card characters', 20), text=money, bg='#603b32', fg='white')
            lbl_money.place(x=580, y=446)
            btn_quit.place(x=580, y=486)
            btn_main_menu.place(x=180, y=486)
            if first_card != second_card:
                btn_deal.destroy()
                btn_no_deal.destroy()
            else:
                btn_high.destroy()
                btn_low.destroy()


print(first_card)
print(second_card)
# labels
lbl_bet = Label(window, font=('card characters', 30), text="000", bg='#c58d6b')

# buttons
background = Label(window, image=background_image)
btn_start = Button(window, image=start_button, command=start, bg="#603b32", borderwidth=0)
btn_main_menu = Button(window, image=main_menu_button, command=main_menu, bg="#603b32", borderwidth=0)
btn_quit = Button(window, image=quit_button, command=quit_command, bg="#603b32", borderwidth=0)
btn_three_rounds = Button(window, image=three_rounds_button, command=three_rounds, bg="#603b32", borderwidth=0)
btn_five_rounds = Button(window, image=five_rounds_button, command=five_rounds, bg="#603b32", borderwidth=0)
btn_ten_rounds = Button(window, image=ten_rounds_button, command=ten_rounds, bg="#603b32", borderwidth=0)
btn_all_in = Button(window, image=all_in_button, command=all_in, bg="#603b32", borderwidth=0)

# background.pack()
btn_start.place(x=180, y=465)
btn_quit.place(x=580, y=465)

window.mainloop()
