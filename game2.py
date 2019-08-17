import os
import time
from random import randrange
def cls():
	os.system("clear")
	
import datetime
from datetime import timedelta

import random

def inv():
	global gt
	while gt=="inv":
		print("Инвентарь. \n(1)Оружие. \n(2)Броня. \n(3)Зелья. \n(4)Книги. \n(5)Выход.")
		gt=input()
		if gt not in (["1", "2", "3", "4", "5"]):
			gt="inv"
		
		if gt=="5":
			gt=gb

def inp():
	global gt
	global gb
	gt=input()
	bo()
	if gt=="menu":
		cls()
		print("Меню.\n(1)Инвентарь. \n(2)Задания. \n(3)Карта. \n(4)Выйти.")
		gt=input()
		if gt not in(["1", "2", "3", "4"]):
			gt="menu"
		if gt=="1":
			gt="inv"
			inv()
		if gt=="2":
			mission()
		if gt=="3":
			map()
		if gt=="4":
			time.sleep(2)
		gt=gb
	if gt in c:
		perehod()
	else:
		gt=gb

def gosip():
	global gt
	print("Вы подходите к хозяину гостиницы и просите его рассказать вам последние сплетни.")
	gosip=random.randint(1,10)
	print("\n")
	if gosip==1:
		print("А слышал ты о том, что...")
					
	if gosip==2:
		print("Рассказывал, ли я тебе о том, что...")
					
	if gosip==3:
		print("Доводилось ли тебе слышать о...")
	time.sleep(2)
	input()

# Program simulate Blackjack game.
#   with multiple game
#   Using method: Top-Down design, spiral development

n=0
c=0
def bo():
	global n
	global c
	b=list(range(n+1))
	del b[0]
	c=[str(i) for i in b]
	c.append("menu")
	return c


def blackjack():
    print_intro()
    player_win, dealer_win, game = play_multiple_game()
    final_result(player_win, dealer_win, game)

def print_intro():
    print("БлэкДжек (очко) карточная игра в казино.")
    print("Цель игры набрать число карт близкое к значению 21.")
    print("Нельзя допускать перебора. У кого будет больше 21, тот проиграл.")
    print("Сначала, ваш ход:")
    return None

def play_multiple_game():
	global money
	player_win = 0
	dealer_win = 0
	game = 0
	play_again = "да"
    # Ask user whether continue another game or stop
    # Condition True, if user want to play.
	while (play_again[0] == "д" or play_again[0] == "Д"):
		print("У вас: " + str(money) + " монет.")
		for i in range(4):
			perehod()
		print("Сколько вы хотите поставить?")
		bet=input()
		while int(bet) > money:
			print("У вас недостаточно денег. У вас только: " + str(money) + ". Попробуйте еще раз.")
			play_multiple_game()
		money-=int(bet)
		player_hand = player_turn()
		dealer_hand = dealer_turn()
		player_score, dealer_score = compare_between(player_hand, dealer_hand)
		result_of_this_game(player_hand, dealer_hand)
		if (player_score > dealer_score):
			print("\nВы победили!")
			money+=int(bet)*2
			player_win += 1
		elif (dealer_score > player_score):
			print("\nПобедил дилер!")
			dealer_win += 1
		else:
			print("\nНичья!")
			money+=int(bet)
			player_win == dealer_win
		game += 1
		play_again = input("\nХотите сыграть еще (Да или Нет)? ")      
	return player_win, dealer_win, game

def player_turn():
    hand = []
    ans = "еще"
    hand.append(take_card())
    # Ask user whether Hit or Stand?
    # Condition True, if user want to Hit.
    while (ans[0] == "е" or ans[0] == "Е"):
        hand.append(take_card())
        hand = eval_ace(hand)
        print("\nВы взяли: {0} всего = {1}".format(hand, sum(hand)))
        if (is_bust(hand) or
            is_blackjack(hand)):
            break
        ans = input("Хотите взять ЕЩЕ или ХВАТИТ (ЕЩЕ или ХВАТИТ)?")
    return hand

def take_card():
    # get arbitrary card from 2 to 11.
    shuffle_card = randrange(2, 11 + 1)
    return shuffle_card

def eval_ace(hand):
    # Determine Ace = 1 or 11, relying on total hand. 
    total = sum(hand)
    for ace in hand:
        if (ace == 11 and total > 21):
            # at position, where Ace == 11, replace by Ace == 1.
            position_ace = hand.index(11)
            hand[position_ace] = 1
    return hand

def is_bust(hand):
    # Condition True: if the hand of player (or dealer) > 21.
    total = sum(hand)
    if total > 21:
        return True
    return None

def is_blackjack(hand):
    # Condition True: if the hand of player (or dealer) == 21.
    total = sum(hand)
    if total == 21:
        return True
    return None

def dealer_turn():
    hand = []
    while sum(hand) < 18:
        hand.append(take_card())
        hand = eval_ace(hand)
    return hand

def compare_between(player, dealer):
    total_player = sum(player)
    total_dealer = sum(dealer)
    player_bust = is_bust(player)
    dealer_bust = is_bust(dealer)
    player_blackjack = is_blackjack(player)
    dearler_blackjack = is_blackjack(dealer)
    player_score = 0
    dealer_score = 0
    # when player (dealer) is_bust.
    if player_bust:
        if (not dearler_blackjack and
                total_dealer < 21):
            dealer_score += 1
    if dealer_bust:
        if (not player_blackjack and
                total_player < 21):
            player_score += 1
    if (player_bust and
            dealer_bust):
        if (total_player > total_dealer):
            player_score += 1
        elif (total_dealer > total_player):
            dealer_score += 1
        else:
            player_score == dealer_score
    # when player (dealer) get blackjack.
    if player_blackjack:
        player_score += 1
    if dearler_blackjack:
        dealer_score += 1
    if (player_blackjack and
            dearler_blackjack):
        player_score == dealer_score
    # when total hand of player (dealer) < 21.
    if (total_player < 21 and
            total_dealer < 21):
        if (total_player > total_dealer):
            player_score += 1
        elif (total_dealer > total_player):
            dealer_score += 1
        else:
            player_score == dealer_score
    return player_score, dealer_score

def result_of_this_game(player_hand, dealer_hand):
    print("\nПо итогу у нас: ")
    print("У вас: {0} всего = {1}".format(
        player_hand, sum(player_hand)))    
    print("У дилера: {0} всего = {1}".format(
        dealer_hand, sum(dealer_hand)))
    return None

def final_result(player_win, dealer_win, game):
    print("\nИтог после {} игр:".format(game))
    print("Игрок: {} | Дилер: {}".format(
        player_win, dealer_win))
    return None
  
	

#blackjack


d = datetime.datetime(1304, 6, 15, 18, 5)
month=["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]

def perehod():
	global d
	global p_health
	d=d + timedelta (minutes =5)
	global ustal
	ustal+=1
	global golod
	golod+=2
	if golod>=100:
		p_health-=1
	global drunk
	drunk-=1
	global rana
	if rana==1:
		p_health-=2
		
def eda():
	global d
	global ustal
	global golod
	global p_health
	d=d + timedelta (minutes =30)
	ustal+=6
	golod-=100
	p_health+=50
	if p_health>=total_p_health:
		p_health=total_p_health
	

#миссии mission

father_potion=0
m_posoh=0
father_sword=0
mother_picture=0
sister_book=0
perin_dom=0
mother_herbs=0
sister_work=0
father_pole=0
hunter_les=0
final_fire=0

#статы для миссий
non=0
adda_angry=0
adda_amur=0
self_amur=0
self_potion=0
self_tea=0
self_amur=0
potion_name=0


#отношения

mother_p=0
mother_lp=0
father_p=0
sister_p=0
sister_lp=0
philip_p=0
miss_tetcher_p=0
miss_tetcher_lp=0
lily_p=0
lily_lp=0
phily_p=0
phily_lp=0
gily_p=0
gily_lp=0
mitch_p=0
mis_kennet_p=0
mis_kennet_lp=0
lucy_p=0
lucy_lp=0

# ниже перечислены переменные для статы. stats

a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
a7=0
a8=0
a9=0
elve=0
h_potion=1
m_potion=0
h_herbs=0
m_herbs=0
e_health=10
distance=6
p_atack=2
p_defence=1
e_atack=2
e_defence=1
total_p_health=100
cena=1
char_ch=0
intel_ch=0
agil_ch=0
endur_ch=0
stren_ch=0
p_health=100
ustal = 0
fish=0
fishing=1
udochka=0
golod=0
drunk=0
dance=1
rana=0
pole_work=0
sword_p=10
sword=sword_p//10
endurance_p=10
endurance=endurance_p//10
strenght_p=10
strenght=strenght_p//10
intel_p=100
intel=intel_p//10
agil_p=10
agil=agil_p//10
charisma_p=100
charisma=charisma_p//10
smithing_p=10
smithing=smithing_p//10
hunting_p=10
hunting=hunting_p//10
alchemy=0
game = 0
eda_dom=0
money=10
food=0
potion=0
self_smithing=0
gt="ж"
gz="ж"
gb=0
place="хиден"
player_name="Алан"
zagatovka_blade=0
smith_blade=0
blade=0
hamer=0
light_armor=0
heavy_armor=0
pot_nam=0
bow=0
kovan_blade=0
chest=0
father_help=0
batle=0


def chest():
	global p_weapon
	global p_armor
	global p_atack
	global p_defence
	global gt
	global gb
	global n
	global a1
	global a2
	global a3
	global a4
	global a5
	global a6
	global a7
	global a8
	global a9
	gt="chest"
	while gt =="chest":
		date(d)
		chest=1
		print("Вы открываете свой сундук.\n")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Оружие.")
		n+=1
		a2=str(n)
		print("("+str(n)+")Броня.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Закрыть.")
		inp()
		if gt==a1:
			print("Оружие.")
			time.sleep(2)
			gt="оружие"
			while gt=="оружие":
				date(d)
				print("Что вы хотите взять?")
				print("Сейчас у вас в руках: "+p_weapon.name)
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Кулаки.")
				if blade==1:
					n+=1
					a2=str(n)
					print("("+str(n)+")Меч.")
				if noj==1:
					n+=1
					a3=str(n)
					print("("+str(n)+")Нож.")
				if bow==1:
					n+=1
					a4=str(n)
					print("("+str(n)+")Лук.")
				if kovan_blade==1:
					n+=1
					a5=str(n)
					print("("+str(n)+")Кованный меч.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Закрыть.")
				inp()
				if gt==a1:
					print("Вы решаете что будете безоружны.")
					p_weapon=hands
					p_atack+=p_weapon.damage
					time.sleep(2)
					gt="ж"
					gt="chest"
					
				if gt==a2 and blade==1:
					print("Вы решаете что возьмете меч.")
					p_weapon=blade
					p_atack+=p_weapon.damage
					time.sleep(2)
					gt="chest"
				
				if gt==a3 and noj==1:
					print("Вы решаете что возьмете нож.")
					p_weapon=noj
					p_atack+=p_weapon.damage
					time.sleep(2)
					gt="chest"
					
				if gt==a4 and bow==1:
					print("Вы решаете что возьмете лук.")
					p_weapon=bow
					p_atack+=p_weapon.damage
					time.sleep(2)
					gt="chest"
					
				if gt==a5 and kovan_blade==1:
					print("Вы решаете что возьмете кованный меч.")
					p_weapon=kovan_blade
					p_atack+=p_weapon.damage
					time.sleep(2)
					gt="chest"
				
				if gt==a9:
					print("Из оружия вам пока ничего не нужно.")
					time.sleep(2)
					gt="chest"
					
		if gt==a2:
			gt="броня"
			print("Броня.")
			time.sleep(2)
			while gt=="броня":
				date(d)
				print("Что из брони вы хотите надеть?")
				print("Сейчас на вас: "+p_armor.name)
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Льняная рубаха.")
				if light_armor==1:
					n+=1
					a2=str(n)
					print("("+str(n)+")Легкий доспех.")
				if heavy_armor==1:
					n+=1
					a3=str(n)
					print("("+str(n)+")Тяжелый доспех.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Закрыть.")
				inp()
				if gt==a1:
					print("Вы решаете надеть льняную рубаху, она не защитит вас от ударов, но все же лучше чем ничего.")
					p_armor=leen_shirt
					p_defence+=p_armor.defence
					time.sleep(2)
					gt="chest"
					
				if gt==a2 and light_armor==1:
					print("Вы решаете надеть легкие доспехи.")
					p_armor=light_armor
					p_defence+=p_armor.defence
					time.sleep(2)
					gt="chest"
				
				if gt==a3 and heavy_armor==1:
					print("Вы решаете надеть тяжелые доспехи.")
					p_armor=heavy_armor
					p_defence+=p_armor.defence
					time.sleep(2)
					gt="chest"
					
				if gt==a9:
					print("Из брони вам пока ничего не нужно.")
					time.sleep(2)
					gt="chest"
				
		if gt==a9:
			print("Вы закрываете сундук.")
			perehod()
			time.sleep(2)
			gt=gb
	


def reb():
	global n
	global a1
	global a2
	global a3
	global a4
	global a5
	global a6
	global a7
	global a8
	global a9
	n=0
	a1=0
	a2=0
	a3=0
	a4=0
	a5=0
	a6=0
	a7=0
	a8=0
	a9=0

def smth():
	global n
	global gt
	global gb
	global smithing_p
	global strenght_p
	global smith_blade
	global zagatovka_blade
	global kovan_blade
	global smithing
	print("Что вы хотите изготовить?")
	n=0
	if zagatovka_blade>=1 and smith_blade==0:
		n+=1
		a1=str(n)
		print("("+str(n)+")Выковать меч.")
	if smith_blade>=1:
		n+=1
		a2=str(n)
		print("("+str(n)+")Продолжить ковать меч.")
	n+=1
	a9=str(n)
	print("("+str(n)+")Ничего.")
	
	inp()
	if gt==a1 and zagatovka_blade>=1 and smith_blade==0:
		print("Вы приступаете к ковке меча.")
		smith_blade+=1
		zagatovka_blade-=1
		smithing_p+=1
		strenght_p+=1
		time.sleep(2)
		for i in range(12):
			perehod()
		print("Вы проработали целый час. Пот льется с вас ручьями, но работа над мечем немного продвинулась.")
		time.sleep(2)
		gt=gb
	if gt==a2:
		print("Вы продолжаете ковать меч.")
		time.sleep(2)
		print("Меч готов на "+str(smith_blade)+"%")
		smith_blade+=1
		smithing_p+=1
		strenght_p+=1
		time.sleep(2)
		for i in range(12):
			perehod()
		print("Вы проработали целый час. Пот льется с вас ручьями, но работа над мечем немного продвинулась.")
		time.sleep(2)
		if smith_blade>=100:
			print("Вы закончили свой меч!")
			kovan_blade=1
			kovan_blade.damage*=smithing
		gt=gb
	if gt==a9:
		print("В другой раз.")
		perehod()
		time.sleep(2)
		gt=gb

def alch():
	global n
	global a1
	global a2
	global a3
	global a4
	global a5
	global a6
	global a7
	global a8
	global a9
	global gb
	global gt
	global h_herbs
	global h_potion
	global m_herbs
	global m_potion
	date(d)
	print("Вы выложили перед собой все имеющиеся у вас ингредиенты. Что же можно из этого сделать?")
	n=0
	if h_herbs>=1:
		n+=1
		a1=str(n)
		print("("+str(n)+")Сделать зелье здоровья.")
	if m_herbs>=1:
		n+=1
		a2=str(n)
		print("("+str(n)+")Сделать зелье маны.")
	n+=1
	a9=str(n)
	print("("+str(n)+")Выйти.")
	inp()
	if gt==a1:
		pole_rand=random.randint(1,4)
		if pole_rand!=3:
			h_potion+=1
			for i in range(6):
				perehod()
			print("Вы приготовили зелье здоровья.")
		else:
			print("Что-то пошло не так. Зелье не получилось, а травы потрачены зря.")
	if gt==a2:
		pole_rand=random.randint(1,4)
		if pole_rand!=3:
			m_potion+=1
			for i in range(6):
				perehod()
			print("Вы приготовили зелье маны.")
		else:
			print("Что-то пошло не так. Зелье не получилось, а травы потрачены зря.")
	if gt==a9:
		print("Вы решаете оставить все на потом.")
		perehod()
		time.sleep(2)
		gt=gb

class Armor:
	def __init__(self, name, defence):
		self.name=name
		self.defence=defence
leen_shirt=Armor("льняная рубаха", 2)
light_armor=Armor("легкие доспехи", 5)
heavy_armor=Armor("тяжелые доспехи", 10)
p_armor=leen_shirt

class Weapon:
	def __init__(self, name, type, distance, damage, weapon_atack):
		self.name=name
		self.type = type
		self.distance = distance
		self.damage = damage
		self.weapon_atack=weapon_atack
	def __str__(self):
		return '[You got: %s, it is %s weapon, it is distance:%s, it is damage:%s]' % (self.name,self.type, self.distance, self.damage)
hands=Weapon("ничего нет", "melee", (1,2), 1, "Вы бьете кулаком.")
noj = Weapon("нож", "melee", (1,2,3,4), 2, "Вы наносите удар ножом.")
luk = Weapon("лук", "far", (3,4,5,6), 3, "Вы стреляете из лука.")
kovan_blade=Weapon("кованый меч", "melee", (1,2,3,4), 3, "Вы наносите удар мечем.")
claws=Weapon("когти", "melee", (1,2,3), 2, 0)
p_weapon=hands

class Enemy:
	def __init__(self, name, damage, defence, weapon):
		self.name=name
		self.damage = damage
		self.defence=defence
		self.weapon = weapon
#враги
shpana=Enemy("Шпана", 1, 1, 0)
bandit=Enemy("Бандит", 2, 2, 0)
wolf=Enemy("Волк", 2, 1, 0)
bear=Enemy("Медведь", 4, 2, 0)
#перед битвой надо определить оружие врага и назначить такового
#e_weapon=random.choice([noj, luk])
#enemy=bandit
#enemy.weapon=e_weapon
#enemy.damage+=e_weapon.damage


##batle
p_weapon=hands


def status():
	global distance
	global p_health
	global e_health
	print("Растояние между вами: "+str(distance)+"\n Ваше здоровье: "+str(p_health)+"\n Здоровье врага: "+str(e_health)+".")

def fight():
	p_turn()
	e_turn()
	end_batle()
		
def p_turn():
	status()
	global a1
	global a2
	global a3
	global a4
	global n
	global distance
	global p_health
	global e_health
	global h_potion
	n=0
	if distance in p_weapon.distance:
		n+=1
		a1=n
		print("("+str(n)+")Атаковать.")
	if distance<=6 and distance >1:
		n+=1
		a2=n
		print("("+str(n)+")Приблизиться.")
	if distance>=1 and distance<6:
		n+=1
		a3=n
		print("("+str(n)+")Отойти.")
	if h_potion>=1 and p_health<total_p_health:
		n+=1
		a4=n
		print("("+str(n)+")Выпить зелье здоровья.")
		
	gt=int(input())
	if gt==a1:
		print(p_weapon.weapon_atack)
		time.sleep(2)
		if sword<=2:
			#Вариант боя зависящий от прокаченности навыка
			#hit=random.randint(1,3)
#			hit_ch=list(range(sword+1))
#			del hit_ch[0]
		#	if hit in (hit_ch):
			hit=random.randint(1,4)
			if hit!=3:
				print("Вы попали по врагу.")
				e_def=random.randint(1,4)
				if e_def==3:
					e_health-=p_weapon.damage-enemy.defence
					print("Враг защитился.")
				else:
					e_health-=p_weapon.damage
				if e_health<=0:
					end_batle()
				else:
					time.sleep(2)
					e_turn()
			else:
				print("Вы промахнулись.")
				time.sleep(2)
				e_turn()
	if gt==a2:
		print("Вы приблизились.")
		distance-=1
		time.sleep(2)
		e_turn()
	if gt==a3:
		print("Вы отошли назад.")
		distance+=1
		time.sleep(2)
		e_turn()
	if gt==a4:
		print("Вы выпили зелье здоровья.")
		h_potion-=1
		p_health+=100
		if p_health>=100:
			p_health=100
		time.sleep(2)
		e_turn()
				
def e_turn():
	status()
	global n
	global distance
	global p_health
	global e_health
	print("Ход врага.")
	time.sleep(2)
	if distance in e_weapon.distance:
		print(enemy.name+" атакует.")
		time.sleep(2)
		e_hit=random.randint(1,3)
		if e_hit==2:
			print(enemy.name+" промахивается.")
			time.sleep(2)
			p_turn()
		else:
			if agil<=2:
				e_hit=random.randint(1,3)
				if e_hit==1:
					print("Вы уклонились.")
					time.sleep(2)
					p_turn()
				else:
					print(enemy.name+" попадает.")
					p_health-=enemy.damage+e_weapon.damage
					if p_health<=0:
						time.sleep(2)
						end_batle()
					else:
						time.sleep(2)
						p_turn()
	else:
		if distance in (1,2):
			if distance not in e_weapon.distance:
				print(enemy.name+" делает шаг назад.")
				distance+=1
				time.sleep(2)
				p_turn()
		if distance in (5,6):
			if distance not in e_weapon.distance:
				print(enemy.name+ " делает шаг вперед.")
				distance-=1
				time.sleep(2)
				p_turn()
						
def end_batle():
	global p_health
	global e_health
	if p_health<=0:
		batle="lose"
		print("Вы проиграли.")
		if money>=150:
			dengi_minus=random.randint(1,5)
			b=150
		if money> 0 and money <150:
			dengi_minus=random.randint(1,5)
			b=money
		if dengi_minus==4:
			print("К тому же ваш кошелек опустел на " + str(random.randrange(5,b,5)) + " монет." )
		gt=gb
		if lucy_fight==1:
			print("Спасибо что заступился за меня. Они убежали, как вырубили тебя. Пойдем, я хотя бы залатаю твои раны.")
			time.sleep(2)
			print("Вы оказываетесь в комнате Люси, она приносит тазик с теплой водой и тряпку. Она быстро обрабатывает ваши раны.")
			p_health+=200
			time.sleep(2)
			gt="дом кеннет"
	if e_health<=0:
		print("Вы победили!")
		batle="win"
		time.sleep(2)
		gt=gb
		if lucy_fight==1:
			print("Ты мой герой, пойдем ко мне я тебя заштопаю.")
			time.sleep(2)
			print("Вы оказываетесь в комнате Люси, она приносит тазик с теплой водой и тряпку. Она быстро обрабатывает ваши раны.")
			p_health+=200
			lucy_p+=5
			lucy_lp+=5
			time.sleep(2)
			gt="дом кеннет"
		
def hunt():
	global bow
	global food
	global hunting
	global endurance_p
	global agil_p
	print("Отлично, охота. Пора начинать.")
	time.sleep(2)
	if bow!=1:
		print("Охотиться без лука? Хм, ну ладно. Давай побегаем за зайцами.")
		time.sleep(2)
		catch=random.randint(1,6)
		if catch==4:
			print("\nВот это повезло! Вы поймали зайца! Голыми руками!!!\n")
			endurance_p+=1
			agil_p+=1
			food+=1
			hunting+=1
		else:
			print("\nНеудача. Может все-таки стоит взять лук?\n")
	else:
		print("Взяв в руки свой верный лук, вы отправляетесь на охоту.")
		time.sleep(2)
		if hunting>=1 and hunting<=10:
			for i in range(12):
				perehod()
			print("Вы громко шумите, когда передвигаетесь в лесу. Так можно и всю живность распугать. Бегая по лесу вы чуть не угодили в капкан. ")
			catch=random.randint(1,4)
			if catch in ([1, 3, 4]):
				print("Вы ничего не поймали.")
			else:
				print("О чудо, вам удалось поймать зайца")
				endurance_p+=1
				agil_p+=1
				food+=1
				hunting+=1
				
		if hunting>=11 and hunting<=30:
			for i in range(10):
				perehod()
			print("Вы держите лук более уверенно и стараетесь издавать меньше шума. Иногда вам это даже удается.")
			catch=random.randint(1,4)
			if catch in ([1, 2]):
				print("Вы ничего не поймали.")
			else:
				print("О чудо, вам удалось поймать зайца!!!")
				endurance_p+=1
				agil_p+=1
				food+=1
				hunting+=1
				
		if fishing>=31:
			for i in range(8):
				perehod()
			print("Лес, это ваша стихия. Вы бегаете как лань, передвигаетесь тихо как тень. Лесные жители, берегитесь!")
			catch=random.randint(1,3)
			if catch in ([1]):
				print("Вы ничего не поймали.")
			else:
				print("Вы легко ловите зайца")
				endurance_p+=1
				agil_p+=1
				food+=1
				hunting+=1
	pole_rand=random.randint(1,4)
	if pole_rand!=4:
		print("Вы вернулись обратно без происшествий.")
	else:
		print("Вы натыкаетесь на дикого зверя.")
		pole_rand=random.randint(1,4)
		if pole_rand!=4:
			print("Вы натыкаетесь на волка.")
			enemy=wolf
			e_weapon=claws
			enemy.weapon=e_weapon
			enemy.damage+=e_weapon.damage
		else:
			print("Вы натыкаетесь на медведя!!!")
			enemy=bear
			e_weapon=claws
			enemy.weapon=e_weapon
			enemy.damage+=e_weapon.damage
	time.sleep(2)
	gt=gb
		
		
	time.sleep(2)

def fishin():
	global fish
	global fishing
	if udochka==0:
		print("\nЛовить рыбу голыми руками? Это нечто. Ладно, можно попробовать...\n")
		time.sleep(2)
		catch=random.randint(1,6)
		if catch==4:
			print("\nВот это повезло! Рыба! Голыми руками!!!\n")
			fish+=1
			fishing+=1
		else:
			print("\nНеудача. Может все-таки стоит взять удочку?\n")
			
	if udochka==1:
		print("\nВы решили порыбачить.\n")
		time.sleep(2)
		if fishing>=1 and fishing<=10:
			for i in range(12):
				perehod()
			print("Вы неуклюже держите удочку. Кое-как пытаетесь закинуть наживку в воду. Пару раз вы поймали собственные штаны. ")
			catch=random.randint(1,4)
			if catch in ([1, 3, 4]):
				print("Вы ничего не поймали.")
			else:
				print("О чудо, вам удалось поймать рыбу!!!")
				fish+=1
				fishing+=1
				
		if fishing>=11 and fishing<=30:
			for i in range(10):
				perehod()
			print("Ваши руки больше не трясутся, когда вы держите удочку. Всплески воды больше не пугают вас. Может еще немного и у вас начнет даже получаться.")
			catch=random.randint(1,4)
			if catch in ([1, 2]):
				print("Вы ничего не поймали.")
			else:
				print("О чудо, вам удалось поймать рыбу!!!")
				fish+=1
				fishing+=1
				
		if fishing>=31 and fishing<=60:
			for i in range(8):
				perehod()
			print("А вам нравится рыбачить! Свежий воздух, птички поют. Теплое приятное солнце. Рыба плещется в воде. Красота!")
			catch=random.randint(1,3)
			if catch in ([1]):
				print("Вы ничего не поймали.")
			else:
				print("Вы легко ловите рыбу!!!")
				fish+=1
				fishing+=1
	time.sleep(2)
	input()

def date(d):
	cls()
	global ustal
	global golod
	global p_health
	global gt
	month=["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
	days=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
	dayNumber=d.weekday()
	print(str(d.year) + " год " + str(d.day) + " " + month[d.month-1] + "." +"          В кошельке у вас " + str(money) + " монет.")
	if d.minute==5 or d.minute==0:
		print(str(d.hour) + ":" + "0" +(str(d.minute)))
	else:
		print(str(d.hour) + ":" +(str(d.minute)))
	print(days[dayNumber])
	gt="ж"
	global drunk
	global place
	
	if drunk <=0:
		drunk=0
	if drunk >=100:
		drunk=100
	if drunk >=30 and drunk <=50:
		print("Вы слегка пьяны.")
	if drunk >=51 and drunk <=90:
		print("Вы сильно пьяны.")
	if drunk >=91:
		print("Вы в драбодан.")
	if drunk == 100:
		print("Вы перебрали...")
		
		if place=="хиден":
			gt=random.choice(["дом", "поле", 0])
			
		if place=="река":
			gt=random.choice(["#", "0"])
			
		if place=="двор":
			gt=random.choice(["таверна", 0])
		
		if place=="город":
			gt=random.choice(["магазин", "0"])
		
		print("Голова жутко гудит. Вы не помните как тут очутились.")
		drunk-=90
		d=d+timedelta(hours=3)
		ustal-=60
		golod+=30
		if money>=150:
			dengi_minus=random.randint(1,5)
			b=150
		if money> 0 and money <150:
			dengi_minus=random.randint(1,5)
			b=money
		if dengi_minus==4:
			print("К тому же ваш кошелек опустел на " + str(random.randrange(5,b,5)) + " монет." )
		else:
			print("Ну хотя бы мои пожитки при мне.")
		
	
	global rana
	if rana==1:
		print("Вы ранены!")
		p_health-=2
		
	if ustal<0:
		ustal=0
	if ustal >=100 and ustal <=150:
		print("Вы немного устали.")
	if ustal >=151 and ustal <= 190:
		print("Вы сильно устали.")
	if ustal >200:
		ustal=200
	if ustal >=191:
		print("Вы обессилены. Нужно СРОЧНО отдохнуть!!!")
		
	if golod<=0:
		golod=0
	if golod > 100:
		golod=100
	if golod >=30 and golod <=60:
		print("Вы немного голодны.")
	if golod >=61 and golod <= 95:
		print("Вы сильно голодны.")
	if golod >=96:
		p_health-=1
		print("Вы умираете с голоду. Нужно СРОЧНО поесть!!!")
	print("здоровье: " + str(p_health) + "| голод: " + str(golod) + "|   усталость: " + str(ustal))
	print("\n")

# это добавляет время:	d=d + timedelta (days =int(c))


#					
#dance()
#

def danc():
	global dance
	global agil
	global agil_p
	for i in range(6):
		perehod()
	print("\nВы решаетесь выйти и показать свои навыки танца.\n")
	time.sleep(2)
	if dance >=1 and dance <= 10:
		print("Вы двигаетесь как корова на льду. Люди странно на вас поглядывают.")
		dance+=1
		agil_p+=1
	if dance>=11 and dance <= 30:
		print("Вы двигаетесь более уверенно, но вам не хватает мастерства. Люди все еще улыбаются глядя на вас.")
		dance+=1
		agil_p+=1
	if dance>=31 and dance <= 60:
		print("Вы хорошо двигаетесь. Люди больше не шатаются в страхе от ваших движений. Вы слышите музыку и двигаетесь вместе с другими в такт.")
		dance+=1
		agil_p+=1
	if dance>=61 and dance <= 99:
		print("Ваши легкие движения в танце заводят толпу. Все оглядываются на вас, но только лишь для того что бы восхитится вашими движениями.")
		dance+=1
		agil_p+=1
	if dance==100:
		print("Вы король этого танца. Все просто замерли с открытыми ртами от ваших движений. Ваша гибкость и ловкость просто поражает. Мужчины хотят быть похожими на вас, а женщины хотят быть с вами.")
	time.sleep(2)
	input()

#					
#dance()
#



while game == 0:
	
	#река
	
	while place=="река":
		gt="ж"
		date(d)
		print("Вы выходите к полноводной реке. Здесь есть маленькая рыбацкая будка. В реке плещется рыба, вы можете порыбачить. Можно окунуться в прохладную воду и поплавать. Можете вернуться обратно домой.")
		n=4
		print("(1) Пойти в будку рыбака.")
		print("(2) Пойти порыбачить.")
		print("(3) Пойти поплавать.")
		print("(4) Вернуться домой.")
		n+=1
		a1=str(n)
		print("("+str(n)+")Переправа.")
		
		inp()
		
		if gt==a1:
			print("Переправа временно закрыта.")
        
			perehod()
			gt="ж"
		
		if gt=='2':
			gt="порыбачить"
			fishin()
			
		if gt=="3":
			gt="поплавать"
			for i in range(6):
				perehod()
			agil_p+=1
			endurance_p+=1
			strenght_p+=1
			if d.hour >=10 and d.hour<=23:
				print("\nВы заходите в теплую воду и плаваете полчаса.")
				for i in range(6):
					perehod()
			if d.hour>=1 and d.hour<=9:
				print("А водичка-то холодная, ну да ладно.")
				cold=random.randint(1,6)
				if cold ==5:
					print("\nХотя вода была слишком холодной, что сказалось на вашем здоровье.")
					p_health-=5
			time.sleep(2)
		
		if gt=="4":
			gt="домой"
			print("\nВы отправляетесь домой\n")
			time.sleep(2)
			place="хиден"
			gt="ж"
			
		
		if gt=="1":
			gt="будка"
			gb="будка"
			time.sleep(2)
		while gt=="будка":
			date(d)
			if d.hour>=5 and d.hour<=23:
				print("Вы стоите в будке рыбака. Рыбак Фрэнк попыхивает трубкой и смотрит в засаленное окно куда-то в даль.")
				print("Вы можете поговорить с рыбаком. Можно продать ему рыбу или купить вещи для рыбалки. Или можно выйти из этой тесной комнатушки.")
				n=4
				print("(1)Поговорить. \n(2)Продать рыбу.\n(3)Купить вещи для рыбалки.\n(4)Выйти к реке.")
				inp()
					
				if gt=="1":
					date(d)
					gt="поговорить"
					cls()
					print("-Фрэнк, а расскажи мне о море. \n-Парень, да что я могу тебе сказать? Море... Море это жизнь... Если ты не был на море, то тебя не поймут на небесах, когда ты представишься. Ведь там, все разговоры, только что о море...")
					time.sleep(4)
					gt="будка"
					
					
				if gt=="2":
					gt="продать"
					date(d)
					print("-Фрэнк, я хотел бы продать тебе рыбу. \n-Что? На кой ляд мне твоя рыба пацан? Я ж рыбак, крейсер мне в бухту. Ааа, хрен с тобой, давай сюда свою рыбу.")
					money+=fish*2
					fish=-fish
					time.sleep(4)
					gt="будка"
				
				if gt=="3":
					gt="купить"	
					gb="купить"
				while gt =="купить":
					date(d)
					print("-Фрэнк, мне б для рыбалки что-нибудь приобрести. \n-Ну смотри малой. Вот все что есть. У меня здесь есть удочка, можешь ее купить. Ну а не хош, что есть, так можешь выйти вон.")
					n=2
					print("(1)Купить удочку. \n(2)Я передумал.")
					inp()
					
					if gt=="1":
						gt= "удочка"
						if udochka==1:
							print("-Малой, зачем тебе еще одна. С двух рук ловить рыбу будешь?")
							time.sleep(2)
							gt="купить"
						else:
							if not money>=15:
								print("Малой, тебе нужно больше золота...")
								time.sleep(2)
								gt="будка"
								
							else:
								money-=15
								udochka=1
								print("-Ну на, держи. Пользуйся на здоровье.")
								time.sleep(2)
								gt="будка"
								
					if gt=="2":
						gt="выйти"
						print("\nЛадно, ничего не нужно.")
						time.sleep(2)
						gt="будка"
						
					
				if gt=="4":
					gt="выйти"
					print("\nВы выбрались наружу к реке.\n")
					time.sleep(2)
					gt="ж"
				
			else:
				print("\nВ такое время старина Фрэнк не откроет дверь.\n")
				time.sleep(2)
				gt="ж"
		
	#река
	
	
	#двор
	
	while place=="двор":
		date(d)
		print("Вы стоите по середине большого двора. Здесь есть таверна, есть лавка, так же местная знахарка продает здесь свои травы. Недавно открылась кузня. Но вы всегда можете вернуться к себе домой.")
		n=4
		print("(1)Пойти в таверну.\n(2)Пойти в лавку.\n(3)Зайти к знахарке.\n(4)Заглянуть к кузнецу.")
		n+=1
		a1=str(n)
		print("("+str(n)+")На проселочную дорогу.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Вернуться домой.")
	
		inp()
		
		if gt==a1:
			print("Вы выходите на проселочную дорогу.")
			for i in range(3):
				perehod()
			time.sleep(2)
			place="проселочная дорога"
		
		if gt=="3":
			gt="знахарка"
			gb=gt
			print("\nВы отправляетесь к знахарке.")
			time.sleep(2)
		while gt=="знахарка":
			date(d)
			print("Вы стоите в маленькой захламленной комнате. В помещении стоит запах дыма и каких-то трав. За столом сидит женщина на вид лет 40, но вы слышали слухи, что ей намного больше. \nНе успев произнести не слова, она спрашивает вас: \n-Здравствуй "+player_name+". Ты что-то хотел? \n-Как вы узнали что это я? Вы же даже не отрывались от... Чем бы вы там не занимались. \n-Л, мне много что известно. И так, ты что-то хотел?")
			n=1
			print("(1)Предложить помощь.")
			if alchemy==1:
				n+=1
				a2=str(n)
				print("("+str(n)+")Можно мне воспользоваться алхимическим столом?")
			n+=1
			a3=str(n)
			print("("+str(n)+")Купить зелье и травы.")
			n+=1
			a1=str(n)
			print("("+str(n)+")Выйти")
			
			inp()
			if gt==a2:
				print("Да конечно. Стол в углу.")
				time.sleep(2)
				alch()
				time.sleep(2)
				gt="знахарка"
				
			if gt==a1:
				print("-Я пожалуй пойду.")
				time.sleep(2)
				gt="ж"
				
			if gt==a3:
				date(d)
				gb=gt
				print("Вы решаете кое-что купить.")
				time.sleep(2)
				print("-Можно посмотреть что вы продаете? \n-Конечно. Все травы я выращивала и собирала сама. Зелья тоже сделаны моей рукой. Так что не переживай за их качество.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Купить зелье здоровья.")
				n+=1
				a2=str(n)
				print("("+str(n)+")Купить зелье маны.")
				n+=1
				a3=str(n)
				print("("+str(n)+")Купить трав, для зелья жизни.")
				n+=1
				a4=str(n)
				print("("+str(n)+")Купить зелье маны.")
				if father_potion==1:
					n+=1
					a5=str(n)
					print("("+str(n)+")Мазь для отца.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Выйти.")
				
				inp()
				if gt==a1:
					if money>=50:
						print("Вы покупаете зелье здоровья.")
						money-=50
						h_potion+=1
						time.sleep(2)
						perehod()
						gt="знахарка"
					else:
						print("У вас недостаточно монет.")
						time.sleep(2)
						perehod()
						gt="знахарка"
			
				if gt==a2:
					if money>=50:
						print("Вы покупаете зелье маны.")
						money-=50
						m_potion+=1
						time.sleep(2)
						perehod()
						gt="знахарка"
					else:
						print("У вас недостаточно монет.")
						time.sleep(2)
						perehod()
						gt="знахарка"
						
				if gt==a3:
					if money>=25:
						print("Вы покупаете травы для зелья здоровья.")
						money-=25
						h_herbs+=1
						time.sleep(2)
						perehod()
						gt="знахарка"
					else:
						print("У вас недостаточно монет.")
						time.sleep(2)
						perehod()
						gt="знахарка"
						
				if gt==a4:
					if money>=25:
						print("Вы покупаете травы для зелья маны.")
						money-=25
						m_herbs+=1
						time.sleep(2)
						perehod()
						gt="знахарка"
					else:
						print("У вас недостаточно монет.")
						time.sleep(2)
						perehod()
						gt="знахарка"
						
				if gt==a5:
					print("-Адда, отец попросил меня, забрать у вас мазь для его больных ног. \n-Ах да, точно. Сходи на кухню и возьми там баночку на полке. Она стоит среди других зелий. И завари пожалуйста чай.")
					time.sleep(2)
					print("Придя на кухню первым делом вы включили чайник, затем вы обнаружили шкафчик с зельями. Порывшись в них вы нашли подписанную красивым подчерком банку. Для 'Гарольда' гласила надпись на ней. Пока вы искали эту банку вам попадались такие интересные экземпляры как 'Силач', 'Ловкач', 'Умник' 'Очаровашка', 'Амур' \nВы берете мазь для отца. Выключаете чайник. Завариваете чай и собираетесь вернуться к Адде. Но быть может взять с собой еще пузырек?")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Взять зелье 'Силач'.")
					n+=1
					a2=str(n)
					print("("+str(n)+")Взять зелье 'Ловкач'.")
					n+=1
					a3=str(n)
					print("("+str(n)+")Взять зелье 'Умник'.")
					n+=1
					a4=str(n)
					print("("+str(n)+")Взять зелье 'Очаровашка'.")
					n+=1
					a5=str(n)
					print("("+str(n)+")Взять зелье 'Амур'.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Ничего не брать.")
					inp()
					if gt==a1:
						potion_name="Силач"
						pot_nam=1
					if gt==a2:
						potion_name="Ловкач"
						pot_nam=1
					if gt==a3:
						potion_name="Умник"
						pot_nam=1
					if gt==a4:
						potion_name="Очаровашка"
						pot_nam=1
					if gt==a5:
						potion_name="Амур"
						pot_nam=1
					if gt==a9:
						pot_nam=1
						non=1
						gt=non
						
				if pot_nam==1:
					if gt!=non:
						print("Вы берете зелье под названием "+potion_name+" \nВыпить самому или добавить в чашку Адды?")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Добавить себе.")
						n+=1
						a2=str(n)
						print("("+str(n)+")Добавить Адде.")
						
						inp()
						if gt==a1:
							print("Вы выливаете пузырек к себе в чашку.")
							if potion_name=="Силач":
								strenght_p+=50
							if potion_name=="Ловкач":
								agil_p+=50
							if potion_name=="Умник":
								intel_p+=50
							if potion_name=="Очаровашка":
								charisma_p+=50
							if potion_name=="Амур":
								self_amur=1
								self_tea=1
							gt="adda_tea"
						if gt==a2:
							print("Вы выливаете пузырек к Адде в чашку.")
							if potion_name !="Амур":
								adda_angry=1
								gt="adda_tea"
							else:
								adda_amur=1
								gt="adda_tea"
					else:
						print("Вы решаете не брать лишнего.")
						time.sleep(2)
						gt="adda_tea"
					
					if gt=="adda_tea":
						print("Вы возвращаетесь в комнату к Адде с двумя чашками чая. Одну вы протягиваете ей, а с другой садитесь в кресло. Вы одновременно делаете глоток.")
						if non==1:
							print("Вы мило беседуете, затем благодарите ее и уходите.")
							time.sleep(2)
							father_potion=2
							gt="ж"
						if adda_amur==1 or adda_angry==1:
							print("Вы видите как глаза Адды расширяются.")
							if adda_angry==1:
								print("Она бросает на вас злобный взгляд и выливает чашку вам в лицо. \n-Как ты посмел брать мои пузырьки без спросу, да еще и подмешивать мне их в чай. А ну убирайся вон!!!")
								time.sleep(2)
								father_potion=2
								gt="ж"
							if adda_amur==1:
								print("Она мило улыбается вам. Хороший напиток. Не следовало конечно брать его без спросу, но раз ты его уже взял...")
								time.sleep(2)
								father_potion=2
								gt="ж"
							
						if self_tea==1:
							print("Вы чувствуете странное покалывание в области шеи.\n")
							if self_amur==1:
								print("Затем покалывание спадает ниже.")
							time.sleep(2)
							print("Адда хмурится, смотря на вас. \n-Знаешь я была о тебе лучшего мнения. Зачем ты трогал мои склянки без спроса. А если б это было что-то опасное?")
							if self_amur==1:
								print("\nНу и что ты теперь будешь с этим делать?")
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Придумать.")
								n+=1
								a2=str(n)
								print("("+str(n)+")Ничего.")
								inp()
								if gt==a1:
									print("Вот это да. Ладно, заходи позже.")
									time.sleep(2)
									father_potion=2
									gt="ж"
								if gt==a2:
									print("Что ж, я разочарована. Ладно, заходи позже.")
									time.sleep(2)
									father_potion=2
									gt="ж"
							else:
								print("Ладно, заходи позже.")
								time.sleep(2)
								father_potion=2
								gt="ж"
						
						
				if gt==a9:
					print("Вы выходите на улицу.")
					time.sleep(2)
					perehod()
					gt="ж"
					
			if gt=="1":
				print("-Адда, я могу вам чем-нибудь помочь?")
				time.sleep(2)
				
				if alchemy==1:
					print(player_name+" сварика мне пару зелий по этому рецепту.")
					time.sleep(2)
					for i in range(12):
						perehod()
					potion=random.randint(1,4)
					if potion==3:
						print("У вас не получилось. \n-Пожалуйста, будь внимательней!")
						time.sleep(2)
						gt="знахарка"
					else:
						print("У вас получилось!")
						potion_get=random.randint(1,5)
						intel_p+=1
						if potion_get==5:
							print("Вот тебя, за хорошую работу.")
							time.sleep(2)
							h_potion+=1
							gt="знахарка"
				else:
					print("-Сходи ко мне на задний двор и поработай на грядке. Там растут целебные травы. А как закончишь, я расскажу тебе кое-что о них.")
					for i in range(18):
						perehod()
					intel_p+=1
					time.sleep(2)
					print("С сорняками вы справились быстро, а вот с обучением дело шло туго.")
					time.sleep(2)
					if intel>=5 and alchemy==0:
						print("-Знаешь, я думаю ты готов к тому, что бы я показала тебе, как смешивать травы.")
						alchemy=1
						for i in range(24):
							perehod
						time.sleep(2)
					gt="знахарка"
					
					
		if gt=="4":
			gt="кузня"
			gb=gt
			print("\nВы отправляетесь к кузне.")
			time.sleep(2)
		while gt=="кузня":
			date(d)
			print("Вы стоите у деревенской кузни. Вы ощущаете жар идущий от печи. И как Перин его выдерживает? Перин Айбара, местный кузнец. Говорят раньше он был знаменит, но ему захотелось спокойной жизни и он осел в нашей деревушке. \n-Здравствуйте мастер Айбара. \n-А это ты парень. Я же просил называть меня просто Перин. Ты что-то хотел?")
			n=0
			n+=1
			a1=str(n)
			print("("+str(n)+")Помочь в кузне.")
			if self_smithing==1:
				n+=1
				a2=str(n)
				print("("+str(n)+")Поработать самостоятельно.")
			if perin_dom==1:
				n+=1
				a3=str(n)
				print("("+str(n)+")Войти в дом.")
			n+=1
			a4=str(n)
			print("("+str(n)+")Покупки.")
			if father_sword==1:
				n+=1
				a5=str(n)
				print("("+str(n)+")Спросить про меч отца.")
			n+=1
			a9=str(n)
			print("("+str(n)+")Уйти.")
			
			inp()
			if gt==a1:
				print("-Перин, а можно тебе помочь?")
				time.sleep(2)
				print("-Конечно, я всегда рад помощи. Вставай к малой кузне. Вот что мне от тебя надо...")
				time.sleep(2)
				print("Вы работали целый час. Жар от кузни был не выносим, но вы кое-чему научились. И Перин даже дал вам пару монет")
				for i in range(12):
					perehod()
				money+=2
				smithing_p+=1
				strenght_p+=1
				time.sleep(2)
				if smithing>=5 and self_smithing==0:
					print("Теперь я думаю ты можешь работать и без моей помощи.")
					self_smithing=1
					time.sleep(2)
				gt="кузня"
			
			if gt==a2 and self_smithing==1:
				print("Перин, можно я сам поработаю?")
				time.sleep(2)
				print("-Конечно. Если нужны будут материалы, можешь приобрести их у меня.")
				time.sleep(2)
				smth()
				
			if gt==a3 and perin_dom==1:
				print("Можно войти?")
				time.sleep(2)
				print("-Да думаю Фейли, тоже нужна помощь.")
				if d.hour>=23 and d.hour<=6:
					print("Слишком поздно для визитов.")
				else:
					gt="дом перина"
				while gt=="дом перина":
					date(d)
					print("Вы стоите в прихожей дома кузнеца. После жара от кузни вас окружает приятная прохлада. Дом чистый и уютный. Вокруг витает приятный запах кожи и раскаленного железа.")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Пойти в хозяйскую спальню.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Выйти на улицу.")
					inp()
					if gt==a1:
						print("Вы идете в хозяйскую спальню.")
						perehod()
						time.sleep(2)
						gt="спальня айбара"
						while gt=="Спальня айбара":
							date(d)
							print("Вы стоите в хозяйской спальне. Она не очень большая, но очень уютная. Кованная кровать выполнена в искусных узорах, чего и следовало ожидать от такого кузнеца.")
							if father_sword==2:
								print("Вы видите свет идущий из маленького чулана в спальне.")
							n=0
							if feily_help==1:
								n+=1
								a1=str(n)
								print("("+str(n)+")Помочь Фейли.")
							if father_sword==2:
								n+=1
								a2=str(n)
								print("("+str(n)+")Пойти на свет.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Выйти из спальни.")
							inp()
							if gt==a1 and feily_help==1:
								print("Фейли во всю занята работой над средством для полировки. \n-Ох как славно что ты пришел. Не хочешь мне немного помочь? А то я зашиваюсь. Оплата обеспечена. Совмести приятное с полезным.")
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Помочь.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Отказаться.")
								inp()
								if gt==a1:
									print("Вы присоединяетесь и повторяете за движениями Фейли. \n-Вот так, хорошо. Вдвоем мы быстро управимся. Спасибо тебе за помощь. Если что, заходи еще.")
									for i in range(6):
										perehod()
									time.sleep(2)
									money+=3
									gt="дом перина"
									
								if gt==a9:
									print("-Спасибо за предложение, но я может быть в другой раз.")
									perehod()
									time.sleep(2)
									gt="дом перина"
							
							if gt==a2 and father_sword==2:
								print("Вы идете на свет. Заходите в кладовую и видите перед собой Фейли Айбара. Красивая, молодая женщина. Она сидит и занимается пропиткой меча. \n-Ох, здравствуй. Ты же сын Генри? За мечем пришел? Ну я почти закончила, подожди немного. Да ты не стесняйся, если хочешь можешь даже мне помочь.")
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Помочь.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Подождать.")
								inp()
								if gt==a1:
									print("Вы присоединяетесь и повторяете за движениями Фейли. \n-Вот так, хорошо. Это тайный рецепт моей семьи. Сталь смазанная этим настоем получается более крепкой. Кожа для доспехов дольше сохраняет упругость. Спасибо тебе за помощь. Если что, заходи еще. В последнее время работы появилось очень много и сама я очень устаю, а Перину не до этого, своих дел целая кузня. Ну вот и ладушки, вот меч твоего отца. Передавай ему от меня привет.")
									father_sword=3
									for i in range(3):
										perehod()
									time.sleep(2)
									feily_help=1
									gt="дом перина"
									
								if gt==a9:
									print("-Спасибо за предложение, но я лучше тут постою. \n-Ну как знаешь. Тогда хотя бы присядь, а то даже не знаю как скоро управлюсь сама.")
									time.sleep(2)
									print("Ну вот, вроде готово. Ух и навозилась я с этим мечем. Ну, давай забирай меч и передавай привет отцу. Кстати если вдруг захочешь помочь, милости просим. Работы всегда много.")
									father_sword=3
									for i in range(3):
										perehod()
									time.sleep(2)
									feily_help=1
									gt="дом перина"
									
														
							if gt==a9:
								print("Вы выходите из спальни.")
								perehod()
								time.sleep(2)
								gt="дом перина"
						
					
					
			if gt==a4:
				print("-Перин, можно посмотреть, что у тебя есть? \n-Конечно, смотри сколько душе угодно.")
				gt="кузня покупка"
				time.sleep(2)
				while gt=="кузня покупка":
					date(d)
					print("На прилавке вы видите различное оружие и даже доспехи.")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Купить меч.")
					n+=1
					a2=str(n)
					print("("+str(n)+")Купить булаву.")
					n+=1
					a3=str(n)
					print("("+str(n)+")Купить легкий доспех.")
					n+=1
					a4=str(n)
					print("("+str(n)+")Купить тяжелый доспех.")
					n+=1
					a5=str(n)
					print("("+str(n)+")Купить загатовку для меча.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Ничего.")
					
					inp()
					if gt==a1:
						if blade==1:
							print("Нее, второй меч мне не нужен.")
							perehod()
							time.sleep(2)
							gt="кузня"
						else:
							if money>=300:
								print("Вы купили меч.")
								blade=1
								time.sleep(2)
								gt="кузня"
							else:
								print("Нужно больше золота.")
								time.sleep(2)
								gt="кузня покупка"
						
					if gt==a2:
						if hamer==1:
							print("Нее, второй молот мне не нужен.")
							perehod()
							time.sleep(2)
							gt="кузня"
						else:
							if money>=400:
								print("Вы купили молот.")
								hamer=1
								time.sleep(2)
								gt="кузня"
							else:
								print("Нужно больше золота.")
								time.sleep(2)
								gt="кузня покупка"
					
					if gt==a3:
						if light_armor==1:
							print("Нее, вторые доспехи мне не нужны.")
							perehod()
							time.sleep(2)
							gt="кузня"
						else:
							if money>=500:
								print("Вы купили легкие доспехи.")
								light_armor=1
								time.sleep(2)
								gt="кузня"
							else:
								print("Нужно больше золота.")
								time.sleep(2)
								gt="кузня покупка"
					
					if gt==a4:
						if heavy_armor==1:
							print("Нее, вторые доспехи мне не нужны.")
							perehod()
							time.sleep(2)
							gt="кузня покупка"
						else:
							if money>=500:
								print("Вы купили тяжелые доспехи.")
								heavy_armor=1
								time.sleep(2)
								gt="кузня покупка"
							else:
								print("Нужно больше золота.")
								time.sleep(2)
								gt="кузня покупка"
					
					if gt==a5:
						if money>=100:
							print("Вы купили заготовку для меча.")
							zagatovka_blade+=1
							perehod()
							time.sleep(2)
							gt="кузня покупка"
						else:
							print("Нужно больше золота.")
							perehod()
							time.sleep(2)
							gt="кузня покупка"
						
					if gt==a9:
						print("Пожалуй ничего не надо.")
						time.sleep(2)
						perehod()
						gt="кузня"
					
			if gt==a5 and father_sword==1:
				print("-Перин, я по поводу отцовского меча. \n-Ах да, точно. Мы его уже заканчиваем. Как будет время загляни ко мне домой. Фейли уже должна наносить последние штрихи.")
				time.sleep(2)
				father_sword=2
				perin_dom=1
				gt="кузня"
											
			if gt==a9:
				print("Вы отходите от кузни.")
				time.sleep(2)
				perehod()
				gt="ж"
			
		if gt==a9:
			gt="домой"
			print("\nВы отправляетесь домой.\n")
			perehod()
			place="хиден"
			gt="ж"
			time.sleep(2)
		
		if gt=="2":
			gt="лавка"
			gb=gt
			print("\nВы отправляетесь к лавке.")
			time.sleep(2)
		while gt=="лавка":
			date(d)
			print("Вы находитесь в старой деревенской лавке. Множество поколений купцов содержали ее. Вы можете купить что-нибудь. Можно поговорить с продавцом. Можно выйти обратно во двор.")
			n=0
			n+=1
			a1=str(n)
			print("("+str(n)+")Купить что-нибудь.")
			n+=1
			a2=str(n)
			print("("+str(n)+")Поговорить с продавцом.")
			if mother_herbs=="opened" or mother_herbs=="not opened":
				n+=1
				a3=str(n)
				print("("+str(n)+")Спросить о специях для матери.")
			if mother_herbs=="taken":
				n+=1
				a4=str(n)
				print("("+str(n)+")Отвлечь Ларика, что бы пробраться в заднюю комнату.")
			n+=1
			a9=str(n)
			print("("+str(n)+")Выйти из лавки.")
			
			inp()
			if gt==a4 and mother_herbs=="taken":
				print("Вы решаете отвлечь Ларика. Вы выходите на улицу и заходите за угол. Берете камень и бросаете его в окно лавки. Спустя мгновенье из нее выскакивает разъяренный Ларик, выкрикивая явные ругательства на непонятном вам языке. Он подбегает к вам. \n-Кто это сделал, эфенди? \n-Местная шпана, мастер Ларик. Они побежали вон в ту сторону. Еще они что-то кричали про длинный нос и короткий... В общем туда они побежали. \n-Ах шайтан их подери, я покажу им короткий... нос еще в придачу... \nИ он удаляется в даль от магазина.")
				time.sleep(2)
				print("Вы заходите в лавку и направляетесь прямиком к задней двери. К вашему счастью Ларик не успел ее запереть. Вы открываете ее и попадаете в маленькую темную комнатушку. Вам удаётся различить лишь стол , потому что на нем догорает свеча. Тусклый свет освещает какую-то странную книгу и картинку которую передала ваша матушка. Вы бросаете на нее взгляд и краснеете от ушей до пяток. Вы хватаете картинку вместе с книгой и быстро выбегаете из лавки.")
				perehod()
				time.sleep(2)
				mother_herbs="taken+photo"
				gt="ж"
			if gt==a3 and (mother_herbs=="opened" or mother_herbs=="not opened"):
				date(d)
				print("-Мастер Ларик, мой матушка попросила меня, взять у вас какие-то специи для таверны. \n-Какие еще специи, не знаю я ни о каких специях. \n-Так же матушка просила вам передать этот конверт. \nВы протягиваете конверт купцу.")
				time.sleep(2)
				if mother_herbs=="opened":
					print("Ларик смотрит на вас сощурив глаза. \n-Так а почему это конверт открыт? Юный эфенди, неужели вы его вскрывали? \nНеприятная ухмылка исказила лицо продавца. \n-Понимаю, понимаю. Юность. Хотел было вас наградить за доставку, но в сложившихся обстоятельствах...")
					time.sleep(2)
					mother_herbs="delivered"
					
				elif mother_herbs=="not opened":
					print("-О, вижу конверт в целости и сохранности, благодарю вас за столь надежную доставку. Вот вам за труды.")
					money+=20
					time.sleep(2)
					mother_herbs="delivered"
				if mother_herbs=="delivered":
					print("Ларик заглядывает в конверт. Он ссыпает монеты на стол и достает картинку. Он пристально рассматривает ее несколько минут. Выражение его лица резко изменилось. Он начал нервно облизывать губы, глупо хихикать и краснеть. Спустя какое-тл время он отрывает взгляд от картинки и его лицо возвращается к прежнему спокойному состоянию. \n-Замечательно эфенди. Сейчас я вынесу ваши специи. \nОн забирает с собой картинку и скрывается в дальней комнате. Буквально через минуту он возвращается к вам с мешочком душистых трав. \n-Вот. Это то что заказывала ваша матушка. Передавайте ей от меня пламенный привет.")
					perehod()
					time.sleep(2)
					mother_herbs="taken"
					gt="лавка"
					
			
			if gt==a2:
				print("Вы подходите к продавцу.")
				time.sleep(2)
				date(d)
				print("-Здравствуйте мастер Ларик. Как торговля? \n-Здравствуй юный эфенди, торговля пошла на спад, после того как закрыли переправу на другую сторону реки. Деревушка у вас хоть тихая и живописная, да вот только добраться сюда ой как тяжело. Если переправу не откроют в ближайшее время, я даже не знаю что и делать.")
				perehod()
				time.sleep(2)
				gt="лавка"
			
			if gt==a3:
				gt="выйти"
				gb=gt
				print("\nВы выходите во двор.")
				time.sleep(2)
				gt="ж"
				
			if gt==a1:
				gt="купить"
				gb=gt
			while gt=="купить":
				date(d)
				print("Вы подходите к продавцу. \n-Здравствуйте! Меня заинтересовал ваш товар. Что можете мне предложить? \n-Здравствуйте юный эфенди. В моем магазине вы можете приобрести книги, припасы для путешествия. Может даже оружие где-то завалялось. Если вас ничего не заинтересовало, прошу Вас отойти от прилавка.")
				n=4
				print("(1)Купить книги. \n(2)Купить припасы. \n(3)Купить оружие. \n(4)Отойти от прилавка.")
				gt=input()
				n=4
				if gt not in(["1", "2", "3", "4"]):
					gt="купить"
				else:
					perehod()
					
				if gt=="4":
					print("Пожалуй пока, мне ничего не надо.")
					perehod()
					time.sleep(2)
					gt="лавка"
					
				if gt=="2":
					date(d)
					print("-Могу ли я приобрести у вас припасов в дорогу? \n-Конечно. Один комплект сух.пайка стоит 10 монет.")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Купить сух.паек.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Отказаться.")
					inp()
					if gt==a9:
						print("Пожалуй пока я ничего не буду брать.")
						perehod()
						time.sleep(2)
						gt="лавка"
						
					if gt==a1:
						if money>=10:
							print("Да я пожалуй возьму одну порцию.")
							food+=1
							perehod()
							time.sleep(2)
							print("Спасибо за покупку, приходите еще.")
						else:
							print("Нужно больше золота.")
						time.sleep(2)
						gt="лавка"
					
				if gt=="3":
					gt="оружие"
				while gt=="оружие":
					if cena ==700:
						m_posoh=2
					if cena==400:
						m_posoh=3
					if cena==0:
						m_posoh=4
					date(d)
					if m_posoh==3:
						print("-Что там с тем посохом? \nС посохом??? С посохом!!! Да забери ты уже этот посох за жалкие "+str(cena)+" монет и уходи.")
					if m_posoh==2:
						print("Так что там с посохом? \n-Да, да посох. За "+str(cena)+" монет, я согласен отдать тебе его.")
					if m_posoh==0:
						cena=1000
						char_ch=1
						intel_ch=1
						print("-И что же за оружие вы продаете? Мечи? Луки? Арбалеты? \n-Ну не совсем. Это мистическое, древние оружие, которое переходило в моей семье из поколения в поколение. Поэтому и стоит оно так дорого. \nИ что же это такое и сколько оно стоит? \Это посох древних... Ты можешь ощутить его мощь даже отсюда... и стоит он 1000 монет.")
					if m_posoh==1:
						print("-Так что там на счет того посоха? \n-Ах да. посох. Всего 1000 монет и он твой.")
					if m_posoh>=0:
						n=2
						print("\nОго, вот это вещь!")
						print("(1)Я беру этот замечательный посох.")
						print("(2)Может быть в другой раз.")
							
						if intel>=10 and intel_ch==1:
							n+=1
							z=str(n)
							print("("+str(n)+")(ИНТ)Дорого!!!")
						
						if charisma>=10 and char_ch==1:
							n+=1
							y=str(n)
							print("("+str(n)+")(ХАР)Дорого!!!")
							
						inp()
							
						if gt=="1":
							if money>=cena:
								print("Вы приобрели волшебный посох.")
								money-=cena
								posoh=1
								m_posoh=4
								gt="купить"
								time.sleep(2)
							else:
								print("Нужно больше золота.")
								m_posoh=1
								time.sleep(2)
								gt="купить"
									
						if gt == "2":
							print("Вы передумали.")
							m_posoh=1
							time.sleep(2)
							gt="купить"
								
						if gt == y:
							print("-Уважаемый, может быть вы снизите цену. Она непомерно высока. И тем более вы сами знаете, что этот посох столько не стоит.")
							cena-=300
							char_ch=0
								
							if cena==700:
								print("\nНу хорошо умник. Твоя взяла. Давай 700 монет и разбежались.")
								time.sleep(2)
								gt="купить"
								input()
									
							if cena==400:
								print("\n-Ах ты ушлый сорванец!!! Хорошо. "+str(cena)+" монет и забирай этот чертов посох!!!")
								m_posoh=3
								time.sleep(2)
								gt="купить"
								input()

								
						if gt==z:
							print("-Знаешь я действительно его чувствую. И могу сказать тебе на полном серьезе, что ты врешь. Да это магический посох, но он не стоит таких денег. Снизь цену и мы поговорим.")
							cena-=300
							intel_ch=0
							if cena==700:
								print("\nНу хорошо умник. Твоя взяла. Давай 700 монет и разбежались.")
								time.sleep(2)
								gt="купить"
								input()
									
							if cena==400:
								print("\n-Ах ты ушлый сорванец!!! Хорошо. "+str(cena)+" монет и забирай этот чертов посох!!!")
								m_posoh=3
								time.sleep(2)
								gt="купить"
								input()
									
				if gt=="1":
					gt="книги"		
				while gt=="книги":
					gb=gt
					date(d)
					print("\nМеня заинтересовали ваши книги. Что у вас есть? \nО мой юный друг, раньше у меня была огромная библиотека. И я так любил читать. Сейчас у меня есть скудные остатки моей библиотеки. Но я думаю мы сможем подобрать что-нибудь для тебя. \nВот смотри у меня есть Книги Навыков: ИНТ, СИЛ, ВЫН, ЛОВ. \nНу а если тебя ничего не заинтересовало, прошу на ВЫХОД.")
					n=3
					print("(1)Купить книгу интеллекта. \n(2)Купить книгу харизмы. \n(3)Ничего не надо.")
					inp()
					
						
					if gt=="1":
						if money>=100:
							print("\nВы покупаете книгу развивающую интеллект")
							time.sleep(2)
							gt="книги"
						else:
							print("У вас недостаточно денег.")
							time.sleep(2)
							gt="книги"
							
					if gt=="2":
						if money>=100:
							print("\nВы покупаете книгу развивающую харизму")
							time.sleep(2)
							gt="книги"
						else:
							print("У вас недостаточно денег.")
							time.sleep(2)
							gt="книги"
							
					if gt=="3":
						print("\nПока меня ничего не интересует.")
						time.sleep(2)
						gt="купить"
					
				
		if gt=="1":
			gt="таверна"
			print("Вы идете в местную таверну.")
			time.sleep(2)
			gb=gt
		while gt == "таверна":
			date(d)
			print("Эта таверна знакома вам с детства, так как ваша матушка заправляет ей сколько вы себя помните. Не то что бы дела шли очень хорошо, но таверна до сих пор открыта. С куни доносится приятный запах. Иногда вы помогаете матери в обслуживании клиентов. По вечерам народ собирается на танцы. Местные шулера играют в БлекДжек.")
			if d.hour==23 and (sister_work==0 or sister_work=="youtoo"):
				print("Вы видите, как ваша сестра скрывается в подсобном помещении с каким-то типом.")
			if d.hour>=18 and mother_p>=20 and mother_herbs==0:
				print("Ваша матушка подзывает вас к себе.")
			n=0
			n+=1
			a1=str(n)
			print("("+str(n)+")Поработать")
			n+=1
			a2=str(n)
			print("("+str(n)+")Спросить про слухи.")
			n+=1
			a3=str(n)
			print("("+str(n)+")Потанцевать")
			n+=1
			a4=str(n)
			print("("+str(n)+")Сыграть в БлэкДжек.")
			if mother_p>=30:
				n+=1
				a5=str(n)
				print("("+str(n)+")Выпить рюмашку.")
			n+=1
			a6=str(n)
			print("("+str(n)+")Зайти на кухню.")
			if d.hour>=18 and mother_p>=20 and mother_herbs==0:
				n+=1
				a7=str(n)
				print("("+str(n)+")Подойти к матушке.")
			if d.hour==23 and (sister_work==0 or sister_work=="youtoo"):
				n+=1
				a8=str(n)
				print("("+str(n)+")Пойти за сестрой.")
			if d.hour>=18 and mother_p>=20 and (mother_herbs=="taken" or mother_herbs=="taken+photo"):
				n+=1
				a7=str(n)
				print("("+str(n)+")Подойти к матушке.")
				
			n+=1
			a9=str(n)
			print("("+str(n)+")Выйти")
		
			inp()
			if gt==a8 and d.hour==23 and (sister_work==0 or sister_work=="youtoo"):
				print("Вы идете за сестрой в подсобное помещение.")
				time.sleep(2)
				if sister_work==0:
					print("Вы видмте вашу сестру.")
					time.sleep(2)
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Попросить ответной услуги.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Согласиться молчать.")
					inp()
					if gt==a1:
						if sister_lp>=20:
							print("Я хочу тоже самое.")
							print("Хорошо.")
							sister_work="youtoo"
							perehod()
							time.sleep(2)
							gt="таверна"
						else:
							print("Я хочу тоже самое.")
							print("Никогда.")
							perehod()
							time.sleep(2)
							gt="таверна"
					if gt==a9:
						print("Хорошо я буду молчать.")
						perehod()
						sister_p+=5
						time.sleep(2)
						gt="таверна"
						
						
				if sister_work=="youtoo":
					print("Я за услугой.")
					time.sleep(2)
					if sister_lp>=30:
						print("Я думая за так пойдет.")
						perehod()
						time.sleep(2)
						gt="таверна"
					else:
						print("За деньги?")
						n=0
						if money>=50:
							n+=1
							a1=str(n)
							print("("+str(n)+")Хорошо, вот твои деньги.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Ну уж нет.")
						inp()
						if gt==a1 and money>=50:
							print("("+str(n)+")Хорошо, вот твои деньги.")
							money-=50
							perehod()
							time.sleep(2)
							
						if gt==a9:
							print("Ну уж нет.")
							perehod()
							time.sleep(2)
							gt="таверна"
						
			if gt==a7 and d.hour>=18 and mother_p>=20 and (mother_herbs=="taken" or mother_herbs=="taken+photo"):
				print("Вы подходите к своей матушке.")
				time.sleep(2)
				print("-Вот специи от Ларика. \n-Ох, спасибо сынок. Сейчас одну минуту. \nМатушка забирает у вас мешочек со специями и подходит к большому камину в центре таверны. Она берет щепотку специй и бросает их в огонь. Огонь окрашивается причудливыми красками. \nМатушка возвращается к вам. Она странно улыбается. \n-Большое спасибо дорогой. Ты спас этот вечер. Но думаю тебе лучше уйти. Вот тебе за труды. \nМатушка передает вам горсть монет и целует вас в макушку.")
				n=0
				if mother_herbs=="taken+photo":
					n+=1
					a9=str(n)
					print("("+str(n)+")Я тут хотел спросить на счет одной картинки.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Уйти.")
				inp()
				if gt==a1 and mother_herbs=="taken+photo":
					print("-Ма, я тут хотел спросить на счет одной картинки. \n-Что милый? Какой картинки? \nВы протягиваете ей карточку, взятую у Ларика. \n-Ах ты на счет этого... \nМатушка смотрит на вас серьезным взглядом, а потом вдруг начинает смеяться. \n-Ах ты ж мой проказник, дорвался все-таки. Ну что ж, пойдем за мной. \nМатушка ведет вас в подсобку. Смотри.")
					time.sleep(2)
					perehod()
					mother_p+=3
					mother_lp+=3
					gt="ж"
					mother_herbs="complete"
				
				if gt==a9:
					print("Ладно ма, спасибо. Я пойду.")
					time.sleep(2)
					perehod()
					mother_p+=3
					gt="ж"
					mother_herbs="complete"
				
			
			if gt==a7 and d.hour>=18 and mother_p>=20 and mother_herbs==0:
				print("Вы подходите к своей матушке. \n-Ты что-то хотела, ма? \n-Да малыш. Ты не мог бы сходить к Ларику и забрать у него заграничные специи для таверны. Специи эти поднимут настроение нашим клиентам. Вот, передай ему этот конверт, там плата за специи. Только не вздумай открывать конверт, будь добр.")
				time.sleep(2)
				print("Матушка передает вам конверт. Затем она целует вас в макушку и скрывается за стойкой бара.")
				time.sleep(2)
				print("Вы рассматриваете конверт. На ощупь там горстка монет и что-то плоское и прямоугольное, наверное какой-то рисунок.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Вскрыть конверт.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Оставить все как есть.")
				inp()
				if gt==a1:
					print("Вы не можете удержаться и вскрываете конверт, хотя вас просили его не открывать. \nВы ссыпаете горсть монет в ладонь, а сверху падает картинка. \nВы берете картинку и рассматриваете ее. Вдруг ваши уши, щеки, да и вы сам краснеете как рак. На картинке изображена ваша матушка. И это она хотела передать Ларику? Как же быть?")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Забрать монеты себе и спросить про картинку у матушка.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Положить все обратно в конверт и пойти к Ларику.")
					inp()
					if gt==a1:
						print("Вы решаете спросить у матушке, что же это она удумала.")
						time.sleep(2)
						print("Вы подходите к барной стойке, за которой стоит ваша матушка. Вы оглядываетесь вокруг и убедившись, что никого рядом нет, вы кладете картинку на стол. \n-Ма, что ж это такое? \nВаша матушка присматривается к картинке, ее глаза расширяются, она молнией сметает ее со стойки. \n-Я же велела не открывать конверт... \n-Но я... \nНикаких но, молодой человек!!! Вы безответственный юноша и мне за вас очень стыдно. А теперь я попрошу вас удалиться")
						time.sleep(2)
						perehod()
						mother_p=0
						mother_lp=0
						mother_herbs="fail"
					
					if gt==a9:
						print("Вы складываете все обратно в конверт и идете к Ларику.")
						time.sleep(2)
						perehod()
						mother_herbs="opened"
						gt="таверна"
					
				if gt==a9:
					print("Вы держите себя в руках. Ведь вы обещали выполнить поручение матушки и вы его выполните.")
					mother_herbs="not opened"
					perehod()
					time.sleep(2)
					gt="таверна"
				
			
			if gt==a6:
				print("Вы идете на кухню.")
				gt="кухня"
				gb=gt
				time.sleep(2)
				while gt=="кухня":
					date(d)
					print("Вы стоите посреди огромной кухни в таверне. Пахнет восхитительно. Местный повар, старик Митчем готовит просто великолепно. Ему помогают его дочери. По утрам он обучает младшую Лили, а вечером его заменяют Фили и Гили. ")
					if d.hour >6 and d.hour <18:
						print("Сейчас на кухне заправляет Митч. Он показывает своей дочурке Лили, как устроена кухня. Увидев вас Митч улыбается, а Лили краснеет. \n-Чего-то хотел, парень?")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Поесть.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти.")
						
						inp()
						if gt==a1:
							print("Митч, может накормишь меня? \n-Парень ты же знаешь, я против благотворительности. Давай как помоги нам часок и я с удовольствием накормлю тебя.")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Согласиться.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Отказаться.")
							inp()
							if gt==a1:
								print("Вы работали в течении часа, но Митчим накормил вас.")
								endurance_p+=1
								for i in range(2):
									eda()
								time.sleep(2)
								gt="кухня"
							if gt==a2:
								print("Не, старик, давай в другой раз.")
								perehod()
								time.sleep(2)
								gt="кухня"
						if gt==a9:
							print("Да ничего, я уже ухожу.")
							perehod()
							time.sleep(2)
							gt="таверна"
					else:
						print("Сейчас на кухне Фили и Гили. Хоть они и близняшки, характер у них совершенно разный. Единственное что их объединяет это любовь к кухне которую привил им отец. \n-Ты что-то хотел, мелкий?")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Перестаньте называть меня мелким.")
						n+=1
						a2=str(n)
						print("("+str(n)+")Поесть.")
						n+=1
						a3=str(n)
						print("("+str(n)+")Выйти.")
						
						inp()
						if gt==a1:
							print("-Да перестаньте называть меня мелким. Я давно уже вырос!")
						if gt==a2:
							print("Девчонки, может накормите меня?")
							eda()
							time.sleep(2)
							gt="кухня"
						if gt==a3:
							print("Да ничего не нужно.")
							perehod()
							time.sleep(2)
							gt="таверна"
						
						
			if gt==a1:
				if d.hour>=17 or d.hour<=4:
					print("Вы помогаете матери в управлении таверны. Вы разносите заказы, убираете со столов. Моете полы.")
					money+=2
					mother_p+=1
					for i in range(12):
						perehod()
					gt="таверна"
				else:
					print("Спасибо, пока помощь не требуется.")
					perehod()
					time.sleep(2)
					gt="таверна"
					
			
			if gt==a9:
				gt="выйти"
				print("\nВы выходите во двор.")
				perehod()
				gt="ж"
				time.sleep(2)
			
			if gt == "поесть":
				eda=random.choice(["яишницу.", "овощное рагу.", "тушеные бобы.", "томатный суп."])
				print("Вы заказали " + eda)
				money-=5
				golod-=100
				d=d+timedelta(minutes=30)
				time.sleep(2)
				gt="таверна"
				
			if gt==a2:
				gt="сплетни"
				gosip()
				gt="таверна"
				
			if gt==a5:
				gt="выпить"
				if gt=="выпить":
					print("Вы заказали стаканчик горячительного.")
					money-=5
					drunk+=20
					time.sleep(2)
					gt="таверна"
				
			if gt==a4:
				gt="играть"
				cls()
				blackjack()
				gt="таверна"
				
			if gt==a3:
				gt="потанцевать"
				if d.hour>=17 or d.hour<=4:
					danc()
				else:
					print("Для танцев слишком рано.")
					time.sleep(2)
				gt="таверна"
				

	#двор



	while place=="дорога к переправе":
		date(d)
		print("Вы скрываетесь в зарослях и продвигаетесь в глубь леса. Отсюда до переправы можно добраться двумя путями. Напрямик по освещенной дороге. Но на ней могут встретится людей которые устроили боюня в деревне. Можно обогнуть лес и выйти прям к заставе. Но эта дорога длинна и в лесу могут обидать дикие звери.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Напрямик.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Через лес.")
		
		inp()
		if gt==a1:
			gt="short way"
			gb=gt
		while gt=="short way":
			print("Вы решаете пойти коротким путем через лес.")
			long_way=4
			while short_way>=1:
				pole_rand=random.randint(1,3)
				if pole_rand!=3:
					print("Вы продвигаетесь все ближе к заставе.")
					short_way-=1
					perehod()
					time.sleep(2)
				else:
					enemy=bandit
					e_weapon=noj
					enemy.weapon=e_weapon
					enemy.damage+=e_weapon.damage
					short_way-=1
					fight()
				if short_way==0:
					place="переправа"
		
		if gt==a9:
			gt="long way"
			gb=gt
		while gt=="long way":
			print("Вы решаете пойти длинным путем через лес.")
			long_way=4
			while long_way>=1:
				pole_rand=random.randint(1,5)
				if pole_rand!=5:
					print("Вы продвигаетесь все ближе к заставе.")
					long_way-=1
					perehod()
					time.sleep(2)
				else:
					enemy=wolf
					e_weapon=claws
					enemy.weapon=e_weapon
					enemy.damage+=e_weapon.damage
					long_way-=1
					fight()
				if long_way==0:
					place="переправа"
					
	while place=="переправа":
		date(d)
		print("Уставшие и обессиленные вы добераетесь до переправы. Она закрыта на ночь, как и должно быть. Вы подошли ближе и постучали в ворота.")
		tine.sleep(2)
		print("Спустя несколько минут обзорное окошко отворилось со скрипом. \n-Кто такие и почему вы черт вас дери такие чумазые? \n-Мы жители из деревни Хиден. А чумазые мы потому что наша деревня горит. Какие-то бандиты устроили там боюня. Мы единственные кто выжил. \nОхо, парень, ну ты это, проходи, сядь, дп расскажи что случилось. И вы милая барышня проходите тоже.")
		time.sleep(2)
		print("Внутри сторожки на заставе было тепло. После ночных приключений тепла вам очень не доставало. \n-Ну парень рассказывай что случилось. \nВы пересказали слова эльфийки и рассказали о том что видели сами. Ваша сестра плакала, а когда один из охранников попытался ее утешить, положив руку ей на плечо, она вздрогнула и спряталась за вас. \n-И после всей этой кровавой резни, мне бы хотелось узнать как эти люди попали к нам, если застава была закрыта. \n-Парень, я сочувствую твоему горю, но на что это ты намекаешь? Что мы пустиои в вашу деревню головорезов? Ты с ума сошел от горя? Застава давно уже закрыта и в близжайшие дни никто через не не проходил. \nХорошо, допустим, но тогда нам нужно в город. Может там знают что-нибудь. \n-Ээ, парень, повремени. В город я тебя тоже не могу пропустить. Застава закрыта. Без доверительное грамоты никого пропустить не могу. \n-Значит по грамоте пройти можно? \n-Ну дык на то она и грамота.\n-Так значит они могли пройти к нам в деревню по этой проклятой грамоте! Вы же сказали что никого не пропускали.\n-Ну дык так оно собственно и было. Грамоты уже пару дней никто не казывал. Приходил вчера  по-утру какой-то тип в лохмотьях, но мы в зашей его выперли. Негоже таких без грамоты пускать, да и откуд она у него.")
		time.sleep(2)
		print("Вы вспомнили путника в длинной рясе, которого встретили в то злосчастное утро. \nКак он попал к вам в деревню, если не переходил заставу. И был ли он причастен к бойне в деревне или тоже пал жертвой этого ужасного события.\nУ вас не хватало сил на раздумья. Вы жутко устали, хотя и проспали в безпамятнгм сне весь прошлый день.\n-Пожалуйста дяденьки пустите нас в город. Ваша сестра состроила губки бантиком, сделавшись совсем совсем маленькой. \n-Девчуля мыж тебе говорим, шо без грамоты…\n-Да да, без грамоты вы не пропустите. Но неужели никак нельзя обойтись без нее?")
		time.sleep(2)
		gt="dogovor"
		gb=gt
		while gt=="dogovor":
			print("Ну... Мы можем договориься.\nСказав это он перевел свой взгляд на сестру...")
			n=0
			n+=1
			a1=str(n)
			print("("+str(n)+")Заплатить.")
			n+=1
			a2=str(n)
			print("("+str(n)+")Драться.")
			n+=1
			a3=str(n)
			print("("+str(n)+")Поговорить с сестрой.")
			inp()
			if gt==a1:
				print("Запатить охранникам 500 монет.")
				if money>=500:
					print("Вы отдаете нужную сумму охранникам и они пропускают вас в город.")
					money-=500
					perehod()
					time.sleep(2)
					place="город"
					final_fire=5
				else:
					print("У вас недостаточно денег.")
					time.sleep(2)
					gt="dogovor"
			
			if gt==a2:
				enemy=bandit
				e_weapon=noj
				enemy.weapon=e_weapon
				enemy.damage+=e_weapon.damage
				fight()
				if batle=="win":
					print("Вы побеждаете охранников, обыскав их вы находите грамоту и несколько монет. Затем выходите в город.")
					perehod()
					time.sleep(2)
					place="город"
					final_fire=5
				if batle=="lose":
					print("Охранники избили вас и вашу сестру у вас на глазах. Они забрали у вас все деньги, но все же выкинули вас в город, думая что там вы и пропадете.")
					money-=money
					perehod()
					time.sleep(2)
					place="город"
					final_fire=5
					
			if gt==a3:
				print("Вы говорите с сестрой.")
				if sister_p>=30:
					print("Вы уговорили.")
					time.sleep(2)
					print("Ладно парень, можете пройти в город.")
					perehod()
					time.sleep(2)
					place="город"
					final_fire=5
				else:
					print("Ни за что и никогда")
					time.sleep(2)
					gt="dogovor"
	
	#хиден	
	
	while place=="хиден":
		cls()
		date(d)
		print("Это ваша деревушка Хиден. В ней вы родились и выросли. Посмотрев вокруг вы видите свой дом, рядом поле, которое вы помогаете обрабатывать. Рядом с вашим домом бежит горная речка. Так же проселочная дорога ведет к деревенской площади.")
		if final_fire==0:
			print("Перед домом сидит ваша сестра.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Зайти в дом.")
		n+=1
		a2=str(n)
		print("("+str(n)+")Выйти в поле.")
		n+=1
		a3=str(n)
		print("("+str(n)+")Пойти к реке.")
		if final_fire==0:
			n+=1
			a4=str(n)
			print("("+str(n)+")Подойти к сестре.")
		if final_fire==1 and d.hour==5:
			n+=1
			a3=str(n)
			print("("+str(n)+")Дождаться сестры.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Выйти на деревенскую площадь.")
		
		
		inp()
		if gt==a4 and final_fire==1 and d.hour==5:
			print("Вы встаете чуть поодаль дома и дожидаетесь сестру.")
			time.sleep(2)
			print("Через пару минут вы видите как она выходит из-за дома. \n-Сколько можно тебя ждать? Скоро матушка вернется. \n-Ну проспала я маленько, просто была в предвкушении от предстоящего приключения. На вот, я поесть тебе принесла. Ладно, пойдем скорее.")
			golod-=100
			time.sleep(2)
			print("Солнце только встает, а вы стремительным шагом идете к реке. \nЕще слишком рано и вы не встретилт практически ни души. Только какой-то пьяный бродяга закутавшийся в плащ брел куда-то бесцельно.")
			time.sleep(2)
			print("Вы подошли к реке. -Ну что ж, нужно плыть на тот берег. Где-то там эта таинственная лачуга. Вперед. Вы заходите в воду. Утренняя вода невероятно бодрит. Вы сразу же проснулись.")
			time.sleep(2)
			for i in range(6):
				perehod()
			ustal-=200
			print("Перебравшись на другую сторону вы немногл устали. Но после такой воды усталость практически не чувствуется.")
			perehod()
			time.sleep(2)
			print("Ваша сестра выходит из воды.")
			time.sleep(2)
			if sister_lp>=20:
				print("Ничего не говорит.")
			else:
				print("Не смотри.")
			time.sleep(2)
			print("Вы идете через кушири. и через некоторое время выходите на опушку. Перед вами предстает полуразрушенная хибарка. \n-И что же в ней такого особенного? \n-Так пойдем и посмотрим.")
			time.sleep(2)
			print("Вы заходите внутрь. Поломанная мебель, разбитые склянки. Вдруг вы замечаете сундук. Он прикрыт каким-то одеялом. Стянув одеяло вы рассматриваете сундук. \n-Как-то не видно замка. \nВаша сестра вертит сундук и так и эдак. \n-Нет, ничего не вижу. Может тут есть что-то чем можно поддеть крышку. Сейчас посмотрю. \nОставив вас одного, она уходит искать рычаг. Вы долго смотрите на сундук. Вы испытываете какое-то странное ощущение. Вы проводите рукой по сундуку. Слышится щелчек, звук ходищих шарниров и сундуе открывается.")
			time.sleep(2)
			print("На звук пришла впша сестра с какой-то железкой в руке. \n-Как ты его открыл? \n-Без понятия, он просто взял и открылся. \n-Хмм, занятно. Ладно подумаем об этом позже. И так, что же у нас тут есть?")
			time.sleep(2)
			print("Ваша сестра заглядывает внутрь сундука. \n-Так, какие-то записи и какой-то ларчик. Что возьмешь?")
			n=0
			n+=1
			a1=str(n)
			print("("+str(n)+")Ларчик.")
			n+=1
			a9=str(n)
			print("("+str(n)+")Письмена.")
			inp()
			if gt==a1:
				print("Дай мне ларчик.")
				time.sleep(2)
				print("Сестра передает вам ларчик, а сама принимается за изучение писем. \nВы осматриваете ларчик. На нем выведены какие-то странные иероглифы и узоры. Что же там внутри? \n-Ого, тут что-то про маму... \n-В письмах? Что именно? \n-Точно не знаю, тут весь текст какая-то тарабарщина. Встречаются конечно знакомые слова, но остальные... Явно не наш язык. А мама упоминается несколко раз. Точнее ее имя в кавычках. \n-Странно это. \n-Что там у тебя с ларчиком? \n-Я как раз хотел его открыть.")
				final_fire=2
				time.sleep(2)
				
			if gt==a9:
				print("Дай мне письмена.")
				time.sleep(2)
				print("Сестра передает вам письмена, а сама принимается за изучение ларчика. \nВы осматриваете письмена. Это какие-то письма или доклад. Вы поняли это по тому как написанны слова. Сначала вы понимали язык, но потом он начал меняться, при чем менялся он с одного на другой и опять пару фраз вам удовалось прочесть. Среди этой тарабарщины, вам попалось имя вашей матери. \n-Ого, тут что-то про маму... \n-В письмах? Что именно? \n-Точно не знаю, тут весь текст какая-то тарабарщина. Встречаются конечно знакомые слова, но остальные... Явно не наш язык. А мама упоминается несколко раз. Точнее ее имя в кавычках. \n-Странно это. \n-Что там у тебя с ларчиком? \n-Я как раз хотела его открыть.")
				final_fire=2
				time.sleep(2)
			if final_fire==2:
				print("Ларчик открывается со звонким щелчком. Крышка стремительно откидывается назад и из его недр исходит странный туман. \nОт неожиданности вы вздрагиваете и делаете вдох. После чего ваши глаза смыкаются и вы падаете на землю.")
				time.sleep(2)
				d+=timedelta(hours=18)
				print("Вы открываете глаза. Вы видите луну через дыры в крыше. Ночь? Было же утро... \nРядом с вами кряхтит сестра. \nЧто ж это было-то такое черт возьми? и Почему так пахнет паленым? \nВы подымаетесь на ноги и выходите из хибары.")
				time.sleep(2)
				print("Пожар...")
				time.sleep(2)
				print("Вы видите как пожар обуял вашу деревню. Горит все от полей до деревенских ворот. \n-Быстрее, нужно бужать и тушить это все. \nВы срываетесь на бег. Быстро пернплывпете речку и входите в деревню.")
				time.sleep(2)
				print("Никого...")
				time.sleep(2)
				print("У городских ворот нет ни души. Никто не бегает, не кричит, не пытается потушить огонь. Вы к городской площади.")
				time.sleep(2)
				print("И тут вы не застали никого. Никого из живых. Перед вашими глазами предстает страшная картина. Горы трупов лежат вдоль дороги, лужи крови бегут к дубу который растет в центре. Все здания объяиы огнем. Что странно вы замечаете лишь мужские трупы.")
				time.sleep(2)
				print("Вы бежите к себе домой, боясь самого худшего. Что же случилось с вашими родителями?")
				time.sleep(2)
				print("Уже из далеко вы замечаете ято и ваш дом объят огнем.\nПодойдя ближе вы замечаете что кто-то висит на дереве перед домом. Вы подходите ближе...")
				time.sleep(2)
				print("-О нет... \nВаша сестра падает на колени и начинает рыдать. \n-Отец... \nВы подходите к телу своего отца. Он явно мертв. Никто бы не выжил после стольких ран. Что-то начерчено клинклм у него на груди.")
				time.sleep(2)
				print("Закон Вашамет")
				time.sleep(2)
				print("Вот что глачит эта ужасная надпись. Что бы она значила?")
				time.sleep(2)
				print("-Я видела как это произошло... \nВдруг из неоткуда появляется та самая эльфийка с поля. \n-Я все видела, но ничего не могла сделать. Их было слишком много и они не знали жалости.")
				catch=1
				while catch==1:
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Кто это был?")
					n+=1
					a2=str(n)
					print("("+str(n)+")Что произошло?")
					n+=1
					a9=str(n)
					print("("+str(n)+")Нам нужно идти.")
					inp()
					if gt==a1:
						print("-Кто сделал... Это? \n-Я не уверенна, но помоему это были ОНИ... Вашну. \n-Я прочел это слово на груди своего отца. Кто они черт возьми такие? \n-Я точно не знаю. Сама я слышала о них лишь краем уха от старейшин. Точнее я подслушала их разговор. У нас это запретная тема. Я лишь слышала о их повалках, что они появляются из неоткуда и уходят в никуда. Что они владеют магией. И то что они беспощадны к своим врагам и тех кто их предал. Но не смотря на это отбоя от их последователей нет. Об этом я и услышала от старейшин. Что ИХ последователкй все больше.")
						time.aleep(2)
						gt="ж"
					
					if gt==a2:
						print("-Что здесь произошло? \n-Они пришли ровно в полдень. Сначала на них никто не обращал внимания. Они пришли к этому дому и стали стучаться в двери. Когда женщина живущая там открыла дверь, она громко закричала и попыталась тут же ее захлопнула. Ниговоря больше ни слова они подожгли дом. Просто подожгди ни масла ничего. Думаю это магия. Наши старейшины тоже ее используют. На крики женщины прибежал мужчина с которым я видела тебя тогда на поле. Он попытался дать ИМ отпор, но они расправились с ним даже не заметив. Потом они вырезали эти надписи на его груди. Затемком быстро закрутилось. ОНИ ушли оставив за собой своих преспешников, они-то и устроили эту резню. Всех мужчин они убили, а женщин связали у увели за собой. Все случилось так быстро...")
						time.sleep(2)
						gt="ж"
					
					if gt==a9:
						print("Все уже не важно. Нам нужно убираться отсюда.")
						final_fire=3
					if final_fire==3:
						print("Эти люди... Мужчина и женщина, они были тебе дороги? \n-Да, это были наши родители.")
						if elve=="save":
							print("-Мне очень жаль, мой друг. \nОна подходит к вам и прислоняет руку к вашему лбу. \n-Vac'haren. \n-Ваш брат спас мне жизнь. И я благодарна ему. Если будете рядом с брокилоном, спросите Эльзу. И вас проводят ко мне. Ну а сейчас мне нужно уходить. Я и так нарушаю слишком много правил. Vaedro, друзья мои.")
							elve="invite"
							time.sleep(2)
							final_fire=4
						if elve=="not save":
							print("-Они не заслужили такой учести. Даже не смотря на то, как они воспитали своего сына.")
							time.sleep(2)
							final_fire=4
						if final_fire==4:
							print("После этих слов эльфийка скрывается за деревьями. \n-Что же нам делать сестра? \n-Я не знаю. Мне так холодно и я совсем выбита из сил. Нам нужна крыша над головой. Та лачуга, дааай вернеммя к ней и переждем эту ночь, а после уже будем думать что делать дальше.")
							time.sleep(2)
							print("Вы направляетесь к лачуге. \nВам еле удалось переплыть реку. Последние несколько метров вам приходилось тащить на себе сестру. Выйдя на берег вы почувствовали запах гари. \nВыбежав на опушку с лачугой, вы обнаружили лишь тлеющие угольки.")
							time.sleep(2)
							print("Идти больше некуда. Единственный путь, через переправу в город. но переправа была закрыта, как же ОНИ проникли в деревню. Нужно добраться туда и разузнать. Вдруг в далеке вы слышить голоса и грубый смех. \n-Пойдем сестра. Нам нужно добраться до переправы пока нас не заметили. \n-Зачем нам к переправе? \n-За ней город, а там мы сможем что-нибудь узнать. Здесь нам тояно коне. Пойдем со мной если хочешь жить.")
							tine.sleep(2)
							place="дорога к переправе"
							
			
		
		if gt==a4 and final_fire==0:
			cls()
			print("Если вы продолжите в деревню вы вернуться уже не сможите, по крайнй мере близжайшее время. Так что если остались какие-то не заыершенные дела. Лучше их завершить.")
			n=0
			n+=1
			a1=str(n)
			print("("+str(n)+")Продолжить.")
			n+=1
			a9=str(n)
			print("("+str(n)+")Остаться.")
			inp()
			if gt==a1:
				print("Вы решаете продолжить.")
				time.sleep(2)
				date(d)
				print("Привет братишка. Слушай, надо поговорить. Я тут давече услышала разговор родителей. Они говорили о какой-то заброшенной лачуге за рекой. И мне вот стало жутко интересно. Но знаешь, сама я идти боюсь. так что... Не мог бы ты сходить со мной?")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Согласиться.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Отказаться.")
				inp()
				if gt==a1:
					print("Ну хорошо, давай я тебя провожу. Что-то я раньше не замечал что ты такая трусиха. \n-Просто отведи меня к той лачуге. Не будь задницей. \n-Ну хорошо, хорошо. Пойдем прямотсейчас? \n-конечно же нет, дурилка ты картонная. Жди меня после 5 часов у дома. Но выйти до 6 часов. До того как матушка вернетсч из таверны. Нас не должны увидеть. Раз родители перешептывались по поводу той лачуги, значит там что-то жутко секретное. \n-Хорошо, хорошо. Понял. В 5 у дома. Ясно. Ну я пошел.")
					perehod()
					time.sleep(2)
					final_fire=1
					gt="ж"
					
				if gt==a9:
					print("Прости, но я пожалуй еще по деревне погуляю.")
				
				
			if gt==a9:
				print("Вы решаете остаться.")
				gt="ж"
				time.sleep(2)
			
		
		if gt==a2:
			gt="поле"	
			gb=gt
			print("Вы идете к полю.")
			time.sleep(2)
		while gt == "поле":
			date(d)
			print("Перед вами раскинулось огромное поле, которое вы возделываете вместе с отцом.")
			if d.hour >=6 and d.hour <= 21:
				print("Ваш отец, во всю трудится. вы можете помочь ему.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Помочь пахать.")
				n+=1
				a2=str(n)
				print("("+str(n)+")Поговорить с отцом.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Уйти с поля.")
			
				inp()
									
				if gt==a1:
					gt="поработать"
					date(d)
					print("Вы работаете в течении часа. Солнце нещадно палит ваше тело. Вы устаете.")
					father_help+=1
					pole_work+=1
					endurance_p+=1
					for i in range(12):
						perehod()
					time.sleep(2)
					gt="поле"
					
				if gt==a2:
					print("Вы решили поговорить с отцом.")
					time.sleep(2)
					gt="поговорить"
				while gt=="поговорить":
					date(d)
					gt=gb
					print("Вы подходите к отцу. Он прекращает работу и откладывает мотыгу в сторону. \n-Что-то хотел, сынок?")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Па, а расскажи мне о войне.")
					n+=1
					a2=str(n)
					print("("+str(n)+")Я за оплатой.")
					if father_help>=10 and father_sword==0:
						n+=1
						a3=str(n)
						print("Спросить про отцовский меч.")
					if father_sword==3:
						n+1
						a5=str(n)
						print("("+str(n)+")Па, вот твой меч.")
					if father_sword==5:
						n+1
						a4=str(n)
						print("("+str(n)+")Давай потренируемся на мечах.")
					if father_help>=20 and father_potion==0:
						n+1
						a6=str(n)
						print("("+str(n)+")Па, как твоя спина?")
					if father_potion==2:
						n+=1
						a7=str(n)
						print("("+str(n)+")Па, вот твоя мазь.")
					if father_pole==0:
						pole_rand=random.randint(1,10)
					if pole_rand==1:
						n+=1
						a8=str(n)
						print("("+str(n)+")Па, я кажется что-то слышал, там в дали.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Да ничего.")
					
					inp()
					if gt==a8 and pole_rand==1:
						print("Правда? Ну пойдем посмотрим, что же там такое. \nВы отправляетесь на звук идущий с дальнего конца поля. Подойди ближе вы обнаруживаете диких зверей, которые портят ваши посевы. Вдруг вы слышите женский крик чуть поодаль края вашего поля. \nВаш отец срывается и бежит от гонять диких зверей с вашего поля. Что же делать? Помочь отцу или посмотреть кто кричал? ")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Помочь отцу.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Пойти на женский крик.")
						inp()
						if gt==a1:
							print("Вы подбегаете к ротцу и помогаете ему прогнать диких зверей. \nТы слышал, кто-то кричал. Нужно пойти посмотреть.")
							time.sleep(2)
							print("Прийдя на место откуда доносился крик, вы обнаружили лишь следы крови и лоскуты ткани лежащие на полу. \nДа зверье лютует в последнее время.")
							perehod()
							time.sleep(2)
							gt="поле"
							elve="not save"
							father_pole="complete"
						if gt==a9:
							print("Вы решаете что отец справится и сам. Вы бежите в ту сторону откуда доносился крик. Прибежав вы обнаружили эльфийку, которая борется с диким зверем.")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Помочь эльфийке.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Не вмешиваться.")
							inp()
							if gt==a1:
								print("Вы с воинственным кличем подбегаете к зверю готлвые вступить в бой, но от неожидонности ч которой вы бежали, зверь пугается и дает деру. Вы стоите ошаращенный пару минут, пока эльфийка не поцеловала вас в щеку. \nБлагодарю мой герой. Старейшины бфли не правы на ваш счет. Вы добры и милы. Будешь в боклере, заглядывай. \nПосле этих слов, она мило вам улыбается и сурывается из виду.")
								father_pole="after"
								elve="save"
								perehod()
								time.sleep(2)
							if gt==a9:
								print("Вы решаете не вмешиваться и посмотреть чем закончится дело. \nЭльфийка проигрывает монстру. Она видит вас, просит о помощи но вы не вмешиаетесь. Он оставляет ей шрам. Она плачет. \nЯ так и знала что не стоило выходить из леса, про вас людей старейшины говорилт правду. Будьте вы прокляты. \nПосле этих слов она собирает свои вещи и чкрывается из виду.")
								father_pole="after"
								elve="save"
								perehod()
								time.sleep(2)
							if father_pole=="after":
								print("К вам подходит отец и отвешивает вам подзотыльник. Променял отца на юбку. Ну как так можно? Еще и на эту эльфийку. Ладно уж там. Пойдем обратно.")
								father_pole="complete"
								perehod()
								time.sleep(2)
								gt="поле"
							
					if gt==a7 and father_potion==2:
						print("-Па, вот твоя мазь. \n-О, спасибо большое, а то работать уже невозможно. Как все прошло? \n-Эм, все было в порядке. Главное что мазь у тебя. Ну я пошел...")
						perehod()
						time.sleep(2)
						father_potion=4
						gt="поле"
					
					if gt==a6 and father_potion==0:
						print("Па, как твоя спина? \n-Да что-то стреляет, проклятая. Ты не мог бы сходить к знахарке Адде. Она должна была приготовить для меня мазь для спины. \n-Конечно отец.")
						father_potion=1
						perehod()
						time.sleep(2)
						gt="поле"
					
					if gt==a5 and father_sword==3:
						print("Па, вот твой меч, я принес его от Перина. \n-Большое спасибо сынок. Как все прошло? Гладко? \n-Эм, да все было гладко и чисто. \n-Ну еще раз спасибо сынок.")
						time.sleep(2)
						perehod()
						father_sword=5
						gt="поле"
					
					if gt==a1:
						print("-Ты же знаешь, я не люблю говорить о прошлом. Ну ладно, так уж и быть...\nВ течении часа отец рассказывал вам о давно минувшей войне.")
						for i in range(12):
							perehod()
						sword_p+=1
						gt="поле"
						time.sleep(2)
						
					if gt==a2:
						print("-Ну и сколько же ты наработал?")
						if pole_work>=1:
							print("-Я наработал "+str(pole_work)+ " часов. \n-Ну хорошо, вот твои честно заработанные деньги.")
							money+=pole_work
							father_p+=pole_work
							pole_work-=pole_work
							gt="поле"
							perehod()
							time.sleep(2)
						else:
							print("Хотя я еще поработаю.")
							gt="поле"
							perehod()
							time.sleep(2)
					
					if gt==a3 and father_help>=10 and father_sword==0:
						print("-Па, а где твой меч, что-то я давно его не видел? \n-Кстати о нем. Не мог бы ты сходит к Перину и забрать его. А то с этой работой у меня совсем нет на это времени.")
						father_sword=1
						
					if gt==a4 and fathet_sword==5:
						print("-Па а давай с мечем потренируемся.")
						time.sleep(2)
						print("Отец показывал вам как нужно обращаться с мечем в течении часа.")
						for i in range(12):
							perehod()
						time.sleep(2)
						gt="поле"
					if gt==a9:
						print("Прости, па. Пока ничего.")
						perehod()
						gt="поле"
						time.sleep(2)
					
				if gt==a9:
					print("Вы уходите с поля.")
					perehod()
					gt="j"
					time.sleep(2)
			else:
				print("Слишком темно что бы работать. ")
				if d.hour>21 and d.hour<=6:
					print("В такое время на поле делать нечего.")
					pole_rand=random.randint(1,3)
					if pole_rand==3:
						print("Но в ночи вы слишите звуки доносящиеся с поля.")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Пойти узнать.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Уйти с поля.")
						inp()
						if gt==a1:
							print("Вы решаете пойти на звук и узнать, что там происходит.")
							pole_rand=random.randint(1,3)
							if pole_rand==1:
								print("Вы нарываетесь на драку.")
								enemy=shpana
								e_weapon=random.choice([noj, hands])
								enemy.weapon=e_weapon
								enemy.damage+=e_weapon.damage
								time.sleep(2)
								fight()
							elif pole_rand==2:
								print("Вы натыкаетесь на детей леса.")
								perehod()
								time.sleep(2)
								gt="j"
							else:
								print("Видимо вам показалось.")
								perehod()
								time.sleep(2)
								gt="ж"
						
						if gt==a9:
							print("Вы решаете уйти по добру по здорову.")
							perehod()
							time.sleep(2)
							gt="ж"
					else:
						time.sleep(2)
						perehod()
						gt="ж"

		if gt==a3:
			gt=="направо"
			print("\nВы решаете спуститься к реке.")
			time.sleep(2)
			for i in range(2):
				perehod()
			place="река"
			
		if gt==a9:
			gt ="налево"
			for i in range(2):
				perehod()
			print("\nВы отправляетесь к деревенской площади.")
			time.sleep(2)
			place="двор"
			
		if gt==a1:
			gt="дом"
			print("Вы заходите к себе домой.")
			gb=gt
			perehod()
			time.sleep(2)
		while gt=="дом":
			gb=gt
			date(d)
			print("Вы находитесь у себя дома. У вас есть замечательная кухня, Вы можете зайти к себе в комнату, можете зайти в комнату где обычно спят родители, можете зайти в комнату где обитает ваша сестра.")
			n=5
			print("(1)Пойти на кухню. \n(2)Пойти в свою комнату. \n(3)Пойти в комнату родителей. \n(4)Пойти в комнату сестры. \n(5)Выйти из дома.")
			
			inp()
				
			if gt=="5":
				gt="выйти"
				print("Вы вышли из дома")
				time.sleep(2)
			
			if gt=="2":
				print("Вы идете к себе в комнату")
				time.sleep(2)
				gt="себе"
				gb=gt	
			if chest==1:
				gt=gz
				chest=0
			while gt=="себе":
				gz="ж"
				date(d)
				n=2
				print("Вы у себя в комнате. Вы можете поспать на своей кровати. Вы можете выйти из комнаты.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Поспать.")
				n+=1
				a2=str(n)
				print("("+str(n)+")Сундук.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Выйти.")
				
				inp()
					
				if gt==a1:
					ustal-=25
					golod+=10
					print("\nВы поспали пару часов.")
					d+=timedelta(hours=2)
					time.sleep(2)
					gt="себе"
					
				if gt==a2:
					gz="себе"
					print("Вы подходите к сундуку.")
					time.sleep(2)
					chest()
					
				if gt==a9:
					perehod()
					print("Вы вышли из комнаты.")
					time.sleep(2)
					gt="дом"
				
			if gt=="1":
				print("Вы идете на кухню.")
				time.sleep(2)
				gt="кухня"
				gb=gt
			while gt=="кухня":
				date(d)
				print("Вы стоите посреди большой, светлой кухни. Мама успевает поддерживать ее в чистоте, хоть и проводит все время в таверне.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Поесть.")
				if d.hour==6:
					n+=1
					a2=str(n)
					print("("+str(n)+")Поговорить с мамой.")
				if d.hour==7:
					n+=1
					a3=str(n)
					print("("+str(n)+")Поговорить с отцом.")
				if d.hour==8:
						n+=1
						a4=str(n)
						print("("+str(n)+")Поговорить с сестрой.")
				if fish>=1:
					n+=1
					a5=str(n)
					print("("+str(n)+")Оставить еду дома.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Выйти.")
				
				
				inp()
				
				if gt==a1:
					gt="поесть"
					if eda_dom>=1 or (d.hour>=6 and d.hour<=12) or (d.hour>=18 and d.hour<=23):
						eda()
						eda_dom-=1
						if eda_dom<=0:
							eda_dom=0
						print("\nВы пеерекусили свежей, домашней едой.")
						time.sleep(2)
						gt="кухня"
					else:
						print("\nЕды не осталось. Можно подождать вечера или добыть еду самому. ")
						perehod()
						time.sleep(2)
						gt="кухня"
					
					
				if gt==a9:
					gt="выйти"
					perehod()
					print("\nВы вышли из кухни.")
					time.sleep(2)
					gt="дом"
					
				if gt==a2 or gt==a3 or gt==a4:
					if d.hour==6:
						print("Мама приготовила вкусный завтрак перед тем как отправиться спать. \n-Как дела милый? \n-Все отлично мам, а как ты? \nДа тоже хорошо. ")
						mother_p+=1
						time.sleep(2)
						input()
						gt="кухня"
						for i in rande(3):
							perehod()
					if d.hour==7:
						print("Папа после завтрака отправляется работать на поле. там он пробудет до самого вечера. \n-Привет парень. Как оно? \n-Все в порядке отец, как ты? \n-Да ничего. Работа делается. Кстати я жду тебя на поле. Заглядывай.")
						father_p+=1
						time.sleep(2)
						input()
						for i in range(3):
							perehod()
						gt="кухня"
					if d.hour==8:
						print("Моя старшая сестра, она никуда никогда не спешит Завтракает она тоже медленно и размеренно. \n-Привет братец, как спалось? \n-Пойдет. А ты как спала. \n-Просто замечательно... И снились мне тоже, замечательные вещи.")
						sister_p+=1
						time.sleep(2)
						input()
						for i in range(3):
							perehod()
						gt="кухня"
						
				if gt==a5:
					print("Вы переложили рыбу из дорожной сумки в бочку для рыбы.")
					eda_dom+=fish
					fish-=fish
					time.sleep(2)
					gt="кухня"
				
			
			if gt=="3":
				gt="родители"
				gb=gt		
			while gt=="родители":
				date(d)
				if d.hour >23 and d.hour <6:
					print("Кажется дверь заперта.")
					perehod()
					time.sleep(2)
					gt="дом"
				else:
					print("Вы находитесь в спальне своих родителей.")
					n=0
					if d.hour==7:
						n+=1
						a1=str(n)
						print("("+str(n)+")Поговорить с матушкой.")
					if d.hour>=8 and d.hour<=16:
						n+=1
						a2=str(n)
						print("("+str(n)+")Разбудить маму.")
					if d.hour==22:
						a3=str(n)
						n+=1
						print("("+str(n)+")Поговорить с отцом.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Выйти.")
					
					inp()
					
					if gt==a1:
						date(d)
						if d.hour==7:
							print("Обычно по утрам мама подсчитывает выручка из таверны за прошедший день. Потом она ложится спать. \n-Ты что-то хотел, сынок?")
							n=3
							print("(1)Поболтать. \n(2)Комплимент. \n(3)Выйти.")
							inp()
							
							if gt=="1":
								print("Да просто хотел поболтать с тобой.")
								mother_p+=1
								time.sleep(2)
								gt="родители"
								
							if gt=="2":
								if mother_p>=30:
									print("Да просто хотел сказать комплимент.")
									mother_lp+=1
									time.sleep(2)
									gt="родители"
								else:
									print("Да что ты себе позволяешь, пошляк!!")
									mother_p-=1
									time.sleep(2)
									gt="родители"
							if gt=="3":
								print("Да ничего мам, не буду тебя отвлекать.")
								time.sleep(2)
								gt="родители"
							
					if gt==a2 and d.hour>=8 and d.hour<=16:
						if mother_lp>=30:
							print("Продолжай будить.")
							mother_lp+=1
							time.sleep(2)
							gt="родители"
						else:
							print("Не сейчас малыш, не мешай спать.")
							time.sleep(2)
							gt="родители"
								
					if gt==a3:
						if d.hour==22:
							print("После тяжелого трудового дня, отец готовится ко сну.")
							n=2
							print("(1)Поговорить. \n(2)Выйти.")
							inp()
							
							if gt=="1":
								print("-Как прошел день, отец? \n-В поле сын. Вечером посидел в трактире, да домой. Эх рутина. А вот раньше...")
								for i in range(3):
									perehod()
									time.sleep(2)
									father_p+=1
									gt="родители"
							if gt=="2":
								print("Ладно па, в другой раз.")
								perehod()
								gt="родители"
								time.sleep(2)
							
					
					if gt==a9:
						print("\nВы вышли из родительской спальни.")
						time.sleep(2)
						perehod()
						gt="дом"
					
			if gt=="4":
				gt="сестра"	
			while gt=="сестра":
				date(d)
				if d.hour >23 and d.hour <8:
					if agil>=5:
						print("Кажется дверь заперта. Но вы можете ее вскрыть.")
						n=2
						print("(1)Взломать. (2)Отойти.")
						inp()
						if gt=="1":
							gt="sis_n"
							gb=gt
							while gt=="sis_n":
								print("Вы открываете дверь.")
								print("Ваша сестра мирно спит. Когда она спит она намного милее.")
								n=2
								print("(1)Разбудить. \n(2)Выйти.")
								inp()
								if gt=="1":
									if sister_lp>=30:
										print("Продолжай будить.")
										for i in range(4):
											perehod()
										sister_lp+=1
										time.sleep(2)
										gt="дом"
									else:
										print("Уйди отсюда, грязный извращенец!")
										perehod()
										sister_p-=5
										time.sleep(2)
										gt="дом"
					else:
						print("Кажется дверь заперта.")
						perehod()
						time.sleep()
						gt="дом"
				else:
					print("Вы находитесь в спальне своей сестры.")
					n=0
					print("(1)Выйти.")
					if d.hour==9:
						n+=1
						a1=str(n)
						print("("+str(n)+")Поговорить с сестрой.")
					if d.hour==22:
						n+=1
						a2=str(n)
						print("("+str(n)+")Поговорить с сестрой.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Выйти из комнаты сестры.")
					inp()
					
					if gt==a9:
						print("Вы вышли из спальни сестры.")
						perehod()
						time.sleep(2)
						gt="дом"
					
					if gt==a1:
						gt="говор"
						gb=gt
						if d.hour==9:
							print("Ваша сестра сидит за уроками. Какой бы оторвой она не казалась, она пытается поступить в университет.")
							n=2
							print("(1)Помочь.\n(2)Выйти.")
							
							inp()
							if gt=="1":
								print("Эмми, давай я тебе помогу. \n-Да чем ты мне поможешь шкет?")
								if intel>=5:
									print("-Ну вообще-то я кое что знаю. То что ты сейчас проходишь, элементарно. Давай я тебе покажу...")
									for i in range(6):
										perehod()
									sister_p+=1
									time.sleep(2)
									gt="сестра"
								else:
									print("-Ты права, прости.")
									perehod()
									gt="сестра"
									timesleep(2)
					if gt==a2:		
						if d.hour==22:
							print("Ваша сестра готовится ко сну.")
							n=3
							print("(1)Поговорить. \n (2)Комплимент. \n(3)Выйти.")
							
							inp()
							if gt=="1":
								print("Эмми, как у тебя дела?")
								sister_p+=1
								for i in range(3):
									perehod()
								time.sleep(2)
								gt="сестра"
							if gt=="2":
								if sister_lp>=10:
									print("Сестренка, просто хотел сказать что ты хорошо выглядишь.")
									sister_lp+=1
									for i in range(3):
										perehod()
									time.sleep(2)
									gt="сестра"
								else:
									print("Что это ты удумал извращенец?")
									perehod()
									time.sleep(2)
									gt="сестра"
								
	#хиден
	
	#проселочная дорога
	
	
	while place=="проселочная дорога":
		date(d)
		print("Вы стоите на проселочной дороге. Тропки ведут в разные стороны. Одна тропка ведет к дому вашего друга Филипа Тетчера. Вторая ведёт к дому Митчимов. Третья ведет к дому вдовы Кеннет. И четвертая тропка ведет к лесу.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")К дому Тетчеров.")
		n+=1
		a2=str(n)
		print("("+str(n)+")К дому Митчимов.")
		n+=1
		a3=str(n)
		print("("+str(n)+")К дому вдовы Кеннет.")
		n+=1
		a4=str(n)
		print("("+str(n)+")В лес.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Вернуться на деревенскую площадь.")
		inp()
		
		if gt==a1:
			print("Вы направляетесь к дому Тетчеров.")
			perehod()
			time.sleep(2)
			place="дом тетчеров"
			gt="ж"
		if gt==a2:
			print("Вы направляетесь к дому Митчимов.")
			perehod()
			time.sleep(2)
			place="дом митчимов"
			gt="ж"
		if gt==a3:
			print("Вы направляетесь к дому вдовы Кеннет.")
			perehod()
			time.sleep(2)
			place="дом вдовы кеннет"
			gt="ж"
		if gt==a4:
			print("Вы направляетесь к лесу.")
			perehod()
			time.sleep(2)
			place="лес хиден"
			gt="ж"
		if gt==a9:
			print("Вы возвращаетесь на деревенскую площадь.")
			perehod()
			time.sleep(2)
			place="двор"
			gt="ж"
	
	#проселочная дорога
	
	#лес хиден
	
	
	while place=="лес хиден":
		date(d)
		print("Вы стоите на опушке хиденского леса. Днем дровосеки валят деревья. А ночью здесь тишь и благодать. Неподалеку от опушки, находится сруб лесничего.")
		if d.hour==12:
			print("Вы видите как Люси, тренируется в стрельбе из лука.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Зайти в дом лесничего.")
		if d.hour>=7 and d.hour<=19:
			n+=1
			a2=str(n)
			print("("+str(n)+")Пойти на звуки топора.")
		if d.hour==12:
			n+=1
			a3=str(n)
			print("("+str(n)+")Подойти к Люси.")
		n+=1
		a4=str(n)
		print("("+str(n)+")Пойти в глубь леса.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Вернуться на проселочную дорогу.")
		
		inp()
		if gt==a1:
			print("Вы идете к дому лесничего.")
			perehod()
			time.sleep(2)
			if d.hour >=23 and d.hour<=6:
				print("Дверь закрыта.")
			else:
				gt="дом лесничего"
				while gt=="дом лесничего":
					date(d)
					print("Вы стоите внутри маленького сруба лесничего Хантера. \nНа стене весят головы зверей, на полу у камина шкура медведя, а над каминов весит длинный лук. Хантер сидит в кресле-качалке и курит трубку.")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Поговорить.")
					n+=1
					a2=str(n)
					print("("+str(n)+")Покупки.")
					if hunter_les==0:
						pole_rand=random.int(1,5)
					if pole_rand==2:
						n+=1
						a3=str(n)
						print("("+str(n)+")Напроситься с Хантером на вылозку.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Выйти.")
					inp()
					if gt==a3 and pole_rand==3:
						print("Хантер, а возьми меня с собой на вылозку в лес. \n-Ладно малой, но выполняй все в точности как я тебе скажу.")
						time.sleep(2)
						print("Вместе с Хантером вы выходите на лесную опушку. \n-Давай я покажу тебе как нужно выслеживать кролика. Следуй за мной.")
						time.sleep(2)
						print("Вы следуете за Хантером и слушаете хитрлсти охотника, как вдруг он остановился. \n-Замри. Замри и стой здесь. Я скоро вернусь. \nОн оставляет вас стоять в замешательстве.")
						time.sleep(2)
						print("Вдруг, вы замечаете кролика, о котором было столько разговоров. Вы собираетесь его поймать. \nВы подкрадываетесь ближе и выйдя на просвет вам открывается карьина Хантера и дриады.")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Смотреть.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Выстрелить в кролика.")
						inp()
						if gt==a1:
							print("Вы решили оставить кролика в покое и понаблюдать за действиями лесничего.")
							time.sleep(2)
							print("Закончив дриада растворяется среди листвы, к вам подходит Хантер. \n-Ну вот парень тебе еще один урок. Опасно ходить в лесу, потомц что тут обитают дриады, и если ты нарушишь правила их драгоценного леса, они тебя просто убьют в назидание другим. К ним нужен особый подход. Ладно парень. Пойдем обратно. Жаль конечно что ни одного кролика мы так и не поймали.")
							hunter_les="complete"
							perehod()
							time.sleep(2)
							gt="лес"
							
						if gt==a9:
							print("Вы выстреливаете в кролика. Дриада громко вскрикивает. Ее лицо искажает злобная гримасса. Она расцарапывает лесничему бок и убегает. Хантер храмает к вам. \nЧерт подери парень. Когда лриада рядом ты убиваешь создание леса. Ты вообще в своем уме? А если бы она была не олна? Они бы нас быстро тут выпотрошили и оставили сохнуть на солнце в назидание другим. К ним другой подход нужен. Ну все, уроки окончены. Пойдем обратно.")
							hunter_les="complete"
							food+=1
							perehod()
							time.sleep(2)
							gt="лес"
						
					if gt==a1:
						print("-Хантер, ты ж с моим отцом воевал. Расскажешь о тех временах? \n-Может быть позже, парень... Может позже...")
						perehod()
						time.sleep(2)
						gt="дом лесничего"
					
					if gt==a2:
						print("-Хантер, можно посмотреть, что у тебя есть? \n-Конечно парень, смотри на здоровье.")
						time.sleep(2)
						gt="покупки"
						while gt=="покупки":
							date(d)
							print("В закромах у Хантера вы нашли необработанные шкуры животных, лук со стрелами и инструменты для выделки кожи.")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Лук и стрелы.")
							n+=1
							a2=str(n)
							print("("+str(n)+")Необработанная кожа.")
							n+=1
							a3=str(n)
							print("("+str(n)+")Инструменты.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Ничего не нужно.")
							inp()
							
							if gt==a1:
								if bow==1:
									print("Не, второй лук мне не нужен.")
									perehod()
									time.sleep(2)
									gt="покупки"
								else:
									if money>=150:
										print("Вы покупаете лук и стрелы.")
										money-=150
										bow=1
										perehod()
										time.sleep(2)
										gt="покупки"
									else:
										print("Нужно больше золота.")
										perehod()
										time.sleep(2)
										gt="покупки"
									
							
							if gt==a2:
								if money>=50:
									print("Вы покупаете необработанную кожу.")
									money-=50
									neob_skin+=1
									perehod()
									time.sleep(2)
									gt="покупки"
								else:
									print("Нужно больше золота.")
									perehod()
									time.sleep(2)
									gt="покупки"
							
							if gt==a3:
								if money>=150:
									print("Вы приобретаете инструмент для обработки кожи.")
									money-=150
									instr_skin=1
									perehod()
									time.sleep(2)
									gt="покупки"
								else:
									print("Нужно больше золота.")
									perehod()
									time.sleep(2)
									gt="покупки"
							
							if gt==a9:
								print("Пока вам ничего не нужно.")
								time.sleep(2)
								perehod()
								gt="дом лесничего"
					
					if gt==a9:
						print("Вы выходите обратно на улицу.")
						perehod()
						time.sleep(2)
						gt="ж"
		
		if gt==a2 and d.hour>=7 and d.hour<=19:
			print("Вы идете к дровосекам.")
			perehod()
			time.sleep(2)
			gt="дровосеки лес"
			while gt=="дровосеки лес":
				date(d)
				print("Вы выходите на участок леса где дровосеки валят деревья. Трудная и пыльная работа.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Помочь.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Уйти.")
				inp()
				if gt==a1:
					print("-Мужики, помощь нужна? \n-Привет парень. Да, помощь всегда нужна. Работы не початый край. Бери топор и дуй рубить лес. Оплата почасовая. ")
					time.sleep(2)
					print("Вы работали в течении часа. Все тело ломит. Вы очень устали, но заработали несколько монет.")
					for i in range(12):
						perehod()
					time.sleep(2)
					money+=3
					gt="дровосеки лес"
				
				if gt==a9:
					print("Вы возвращаетесь на полянку.")
					perehod()
					time.sleep(2)
					gt="ж"
		
		if gt==a3 and d.hour==12:
			print("Вы подходите к Люси.")
			perehod()
			time.sleep(2)
			gt="люси лес"
			while gt=="люси лес":
				date(d)
				print("-Люси привет, как дела? \n-Ох это ты. Напугал. Да вот тренируюсь что бы не потерять форму. Папа раньше часто водил меня в лес на охоту.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Научишь стрелять?")
				n+=1
				a2=str(n)
				print("("+str(n)+")Посоревнуемся?")
				n+=1
				a9=str(n)
				print("("+str(n)+")Уйти.")
				inp()
				
				if gt==a1:
					if bow==1:
						print("-Люси, научи меня лучше стрелять.")
						if hunting<30:
							print("Конечно, научу. Смотри все просто...")
							for i in range(12):
								perehod()
							time.slerp(2)
							hunting+=1
							gt="ж"
						else:
							print("Ты уже и так отлично стреляешь, дальше, только практика.")
							perehod()
							time.sleep(2)
							gt="ж"
					else:
						print("Раздобудь сначала лук, а потом посмотрим.")
						perehod()
						time.sleep(2)
						gt="люси лес"
				
				if gt==a2:
					if bow==1:
						print("-Ну давай посоревнуемся.")
						time.sleep(2)
						print("-Стреляем три раза. \n-Кто наберет больше очков, тот победил. \n-И так... Начали.")
						catch=3
						while catch!=0:
							print("Вы делаете выстрел.")
							if hunting<=10:
								pole_rand=random.int(1,10)
								print("Вы попали в: "+str(pole_rand))
							if hunting<=20:
								pole_rand=random.int(5,10)
								print("Вы попали в: "+str(pole_rand))
							if hunting<=10:
								pole_rand=random.int(7,10)
								print("Вы попали в: "+str(pole_rand))
							result+=pole_rand
							catch-=1
							time.sleep(2)
						for i in range(3):
							pole_rand=random.randint(5,10)
							l_result+=pole_rand
						print("И так. Смотрим результат. \nТы набрал: "+result+"\nЯ набрала: "+l_result)
						if result>l_result:
							print("Ты победил!!!")
						elif result<l_result:
							print("Я победила!!!") 
						elif result==l_result:
							print("Хмм... Ничья.")
						time.sleep(2)
						print("Ну если что, приходи еще.")
						time.sleep(2)
						gt="ж"
					else:
						print("Раздобудь сначала лук, а потом посмотрим.")
						perehod()
						time.sleep(2)
						gt="люси лес"
				
				if gt==a9:
					print("Ну ладно Люси, не буду тебя отвлекать.")
					perehod()
					time.sleep(2)
					gt="ж"
		
		if gt==a4:
			print("Вы углубляетесь в лес.")
			perehod()
			time.sleep(2)
			gt="глубь леса"
			gb=gt
			while gt=="глубь леса":
				date(d)
				print("Вы забрались глубоко в лес. Вокруг нет ни души. Ну быть может только зверье бегает, по своим звериным делам.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Поохотиться.")
				n+=1
				a2=str(n)
				print("("+str(n)+")Побегать.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Вернуться на опушку.")
				inp()
				
				if gt==a1:
					print("Вы отправляетесь на охоту.")
					time.sleep(2)
					hunt()
				
				if gt==a2:
					print("Вы решаете побегать часок.")
					time.sleep(2)
					pole_rand=random.randint(1,4)
					if pole_rand!=4:
						print("Пробежка прошла без происшествий.")
						time.sleep(2)
						gt="глубь леса"
					else:
						print("Вы натыкаетесь на дикого зверя.")
						pole_rand=random.randint(1,4)
						if pole_rand!=4:
							print("Вы натыкаетесь на волка.")
							enemy=wolf
							e_weapon=claws
							enemy.weapon=e_weapon
							enemy.damage+=e_weapon.damage
						else:
							print("Вы натыкаетесь на медведя!!!")
							enemy=bear
							e_weapon=claws
							enemy.weapon=e_weapon
							enemy.damage+=e_weapon.damage
							
				
				if gt==a9:
					print("Вы возвращаетесь на лесную опушку.")
					perehod()
					time.sleep(2)
					gt="ж"
		
		if gt==a9:
			print("Вы возвращаетесь на проселочную дорогу.")
			perehod()
			time.sleep(2)
			place="проселочная дорога"
			gt="ж"
	
	#лес хиден
	
	#дом вдовы кеннет
	
	while place=="дом вдовы кеннет":
		date(d)
		print("Перед вами раскинулся огромный особняк с большим прудом. \nВ нем живет вдова бывшего мэра со своей дочерью. После смерти мужа миссис Кеннет не растеряло нажитое мужем богатство, а наоборот приумножила его. У этой женщины всегда была коммерческая жилка.")
		if d.hour==13:
			print("Миссис Кеннет плавает в пруду.")
		if d.hour==19:
			print("Люси куда-то собирается.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Зайти в дом Кеннет.")
		if d.hour==13:
			n+=1
			a2=str(n)
			print("("+str(n)+")Поговорить с миссис Кеннет.")
		if d.hour==19:
			n+=1
			a3=str(n)
			print("("+str(n)+")Подойти к Люси.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Вернуться на проселочную дорогу.")
		catch=1
		if catch==1:
			inp()
			if gt==a1:
				print("Вы идете к дому Кеннет.")
				time.sleep(2)
				if d.hour>=23 and d.hour<=6:
					print("Дом закрыт.")
					perehod()
					time.sleep(2)
					gt="ж"
				else:
					gt="дом кеннет"
					while gt=="дом кеннет":
						date(d)
						print("Вы стоите в огромной прихожей. Коридоры ведут во всевозможные стороны. Лестницы ведут вверх и вниз. Глаза просто разбегаются.")
						if d.hour not in ([8, 12, 13, 18]):
							print("Миссис Кеннет, лежит на софе в прихожей и читает книгу.")
						n=0
						if d.hour not in ([8, 12, 13, 18]):
							n+=1
							a1=str(n)
							print("("+str(n)+")Поговорить с миссис Кеннет.")
						n+=1
						a2=str(n)
						print("("+str(n)+")На кухню.")
						n+=1
						a3=str(n)
						print("("+str(n)+")В спальню миссис Кеннет.")
						n+=1
						a4=str(n)
						print("("+str(n)+")В спальню Люси.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти на улицу.")
						inp()
						if gt ==a1 and d.hour not in ([8, 12, 13, 18]):
							print("Вы подходите к миссис Кеннет.")
							time.sleep(2)
							gt="кеннет корридор"
							while gt=="кеннет корридор":
								date(d)
								print("-Здравствуй, мой мальчик. Ты что-то хотел?")
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Поговорить.")
								n+=1
								a2=str(n)
								print("("+str(n)+")Помочь.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Ничего.")
								inp()
								if gt==a1:
									print("-Просто хотел с вами поговорить.")
									for i in range(6):
										perehod()
									time.sleep(2)
									mis_kennet_p+=1
									gt="дом кеннет"
								
								if gt==a2:
									print("-Миссис Кеннет, могу ли я чем-нибудь вам помочь?")
									time.sleep(2)
									pole_rand=random.randint(1,4)
									if pole_rand==1:
										print("-О да, твоя помощь просто необходима. Не мог бы ты помочь мне с уборкой дома.")
										time.sleep(2)
										print("В течении часа вы драили полы, вытирали пыль и мыли окна. Миссис Кеннет не смотря на свой статус богатой леди не чуралась работы и драила дом на ровне с вами. В перерывах она рассказывала вам истории о купцах и их умении убеждать людей. Вы весело провели время, еще и заработали.")
										for i in range(12):
											perehod()
										time.sleep(2)
										money+=5
										charisma_p+=1
										mis_kennet_p+=1
										gt="дом кеннет"
										
									if pole_rand==2:
										print("-О да, твоя помощь просто необходима. Не мог бы ты помочь мне с чисткой пруда.")
										time.sleep(2)
										print("В течении часа вы чистили пруд у дома миссис Кеннет. Миссис Кеннет же загорала на берегу. Отличный же вид. На озеро я имею ввиду.")
										for i in range(12):
											perehod()
										time.sleep(2)
										money+=5
										mis_kennet_p+=1
										mis_kennet_lp+1
										gt="дом кеннет"
										
									if pole_rand==3:
										print("-О да, твоя помощь просто необходима. Не мог бы ты помочь мне с приготовлением пищи.")
										time.sleep(2)
										print("В течении часа вы крутились на кухне вместе с миссис Кеннет. Вы обсуждали интересные мысли и идеи. Иногда вы начинали жаркий спор, что порой забывали о кипящих кастрюлях.")
										for i in range(12):
											perehod()
										time.sleep(2)
										money+=5
										intel_p+=1
										mis_kennet_p+=1
										mis_kennet_lp+1
										gt="дом кеннет"
										
									if pole_rand==4:
										print("-Прости дорогой, пока помощь не требуется, но ты садись рядом. Давай поговорим.")
										time.sleep(2)
										print("Вы проболтали целый час. Хоть поработать и не удалось, вы хорошо провели время.")
										for i in range(12):
											perehod()
										time.sleep(2)
										mis_kennet_p+=2
										gt="дом кеннет"
									
								if gt==a9:
									print("Извините за беспокойство миссис Кеннет.")
									perehod()
									time.sleep(2)
									gt="дом кеннет"
						
						if gt==a2:
							print("Вы идете на кухню.")
							time.sleep(2)
							perehod()
							gt="кухня кеннет"
							while gt=="кухня кеннет":
								date(d)
								print("Вы стоите в центре большой, светлой кухни. Все сияет чистотой. Конечно миссис Кеннет не сама занимается уборкой, она приглашает уборщиц. Все выглядит идеально.")
								if d.hour in([8,12,18]):
									print("Миссис Кеннет и ее дочь Люси, трапезничают. \n-Здравствуй, мой мальчик, прошу, раздели с нами трапезу.")
									n=0
									if d.hour in([8,12,18]):
										n+=1
										a1=str(n)
										print("("+str(n)+")Поесть.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Уйти с кухни.")
									inp()
									if gt==a1 and d.hour in([8,12,18]):
										print("-Благодарю за приглашение. \nВы садитесь кушать вместе с ними.")
										for i in range(2):
											eda()
										time.sleep(2)
										gt="кухня кеннет"
									
									if gt==a9:
										print("Вы выходите с кухни.")
										perehod()
										time.sleep(2)
										gt="дом кеннет"
						
						if gt==a3:
							print("Вы идете в спальню миссис Кеннет.")
							perehod()
							time.sleep(2)
							gt="комната кеннет"
							while gt=="комната кеннет":
								date(d)
								print("Вы стоите в огромной хозяйской спальне. Из окна открывается шикарный вид на озеро.")
								if d.hour in ([20, 21, 22]):
									print("Миссис Кеннет сидит в большом удобном кресле и читает книгу.")
								n=0
								if d.hour in ([20, 21, 22]):
									n+=1
									a1=str(n)
									print("("+str(n)+")Подойти к миссис Кеннет.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Выйти из спальни миссис Кеннет.")
								inp()
								if gt==a1 and d.hour in ([20, 21, 22]):
									print("Вы подходите к миссис Кеннет. \nОна откладывает книгу и поднимает на вас взгляд.")
									time.sleep(2)
									print("-Здравствуйте миссис Кеннет. Как у вас дела? Хорошо, мой мальчик. Ты что-то хотел?")
									n=0
									n+=1
									a1=str(n)
									print("("+str(n)+")Поговорить.")
									n+=1
									a1=str(n)
									print("("+str(n)+")Комплимент.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Ничего.")
									inp()
									if gt==a1:
										print("-Просто хотел с вами поговорить.")
										mis_kennet_p+=1
										for i in range(6):
											perehod()
										time.sleep(2)
										gt="комната кеннет"
											
									if gt==a2:
										if mis_kennet_p>=10:
											print("Мисс Кеннет, вы великолепны.")
											mis_kennet_p+=1
											mis_kennet_lp+=1
											for i in range(6):
												perehod()
											time.sleep(2)
											gt="комната кеннет"
										else:
											print("-Что это ты удумал?")
											perehod()
											time.sleep(2)
											gt="комната кеннет"
										
									if gt==a9:
										print("-Да ничего, простите. Я пожалуй пойду.")
										perehod()
										time.sleep(2)
										gt="комната кеннет"
								
								if gt==a9:
									print("Вы выходите из спальни миссис Кеннет.")
									perehod()
									time.sleep(2)
									gt="дом кеннет"
									
						
						if gt==a4:
							print("Вы идете в спальню к Люси.")
							time.sleep(2)
							if d.hour>=23 and d.hour<=6:
								print("Комната закрыта.")
							else:
								gt="комната люси"
								while gt=="комната люси":
									date(d)
									print("Вы стоите в огромной, шикарно обставленной девичьей спальне. Наверное так живут принцессы.")
									if d.hour not in ([8, 12, 13, 18, 19, 20, 21]):
										print("Люси развалилась на своей широкой кровати и что-то увлеченно записывает в дневник.")
									n=0
									if d.hour not in ([8, 12, 13, 18, 19, 20, 21]):
										n+=1
										a1=str(n)
										print("("+str(n)+")Подойти к Люси.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Выйти.")
									inp()
									if gt==a1 and d.hour not in ([8, 12, 13, 18, 19, 20, 21]):
										print("Вы приближаетесь к Люси.")
										time.sleep(2)
										print("-Привет Люси. Как дела? \n-Пойдет. Ты что-то хотел?")
										n=0
										n+=1
										a1=str(n)
										print("("+str(n)+")Поговорить.")
										n+=1
										a1=str(n)
										print("("+str(n)+")Комплимент.")
										n+=1
										a9=str(n)
										print("("+str(n)+")Ничего.")
										inp()
										if gt==a1:
											print("-Люси, давай поболтаем.")
											lucy_p+=1
											for i in range(6):
												perehod()
											time.sleep(2)
											gt="комната люси"
											
										if gt==a2:
											if lucy_p>=10:
												print("Люси, ты великолепна.")
												lucy_p+=1
												lucy_lp+=1
												for i in range(6):
													perehod()
												time.sleep(2)
												gt="комната люси"
											else:
												print("-Что это ты удумал?")
												perehod()
												time.sleep(2)
												gt="комната люси"
										
										if gt==a9:
											print("-Да ничего, прости. Я пожалуй пойду.")
											perehod()
											time.sleep(2)
											gt="комната люси"
										
									if gt==a9:
										print("Вы выходите из комнаты Люси.")
										perehod()
										time.sleep(2)
										gt="дом кеннет"
						
						if gt==a9:
							print("Вы выходите обратно на улицу.")
							perehod()
							time.sleep(2)
							gt="ж"
						
			if gt==a2 and d.hour==13:
				print("Вы подходите к краю озера, увидев вас миссис Кеннет подплывает ближе.")
				if mis_kennet_p>=10:
					print("-Ты что-то хотел, мой мальчик?")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Поговорить.")
					n+=1
					a2=str(n)
					print("("+str(n)+")Поплавать.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Ничего.")
					inp()
					if gt==a1:
						print("-Просто хотел с вами поговорить миссис Кеннет.")
						perehod()
						time.sleep(2)
						gt="ж"
					
					if gt==a2:
						print("Миссис Кеннет, можно с вами поплавать?")
						time.sleep(2)
						if mis_kennet_p>=20:
							print("-Конечно мой мальчик. Пойдем, вдвоем плавать куда веселее.")
							for i in range(12):
								perehod()
							time.sleep(2)
							mis_kennet_p+=2
							mis_kennet_lp+=1
							gt="ж"
						else:
							print("-Пожалуй нет, может быть когда-нибудь потом.")
							perehod()
							time.sleep(2)
							gt="ж"
					
					if gt==a9:
						print("-Ничего миссис Кеннет, простите что потревожил.")
						perehod()
						time.sleep(2)
						gt="ж"
				else:
					print("-Прошу меня не отвлекать. \nПосле этих слов она отвернулась от вас и отплыла подальше.")
					perehod()
					time.sleep(2)
					gt="ж"
			
			if gt==a3 and d.hour==19:
				print("Вы подходите к Люси. \n-Люси ты куда-то собралась? \n-Ой не строй из себя мою матушку. Гулять я иду.")
				if lucy_p>=10:
					print("Хочешь, пойдем со мной.")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Конечно пойдем.")
					n+=1
					a9=str(n)
					print("("+str(n)+")В другой раз.")
					inp()
					
					if gt==a1:
						print("И так, куда пойдем?")
						pole_rand=random.randint(1,4)
						if pole_rand==1:
							print("-Пойдем к реке.")
							time.sleep(2)
							print("Вы отправляетесь к реке.")
							print("Люси поворачивается к вам и откуда-то достает бутылку вина. \n-Может я открою бутылочку, а ты пока поймаешь рыбу и мы устроим славный пикничок?")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Конечно сейчас поймаю.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Давай в другой раз.")
							inp()
							if gt==a1:
								print("-Хорошо, только дождись меня. Я скоро! \nВы отправляетесь к реке чтоб поймать рыбу.")
								time.sleep(2)
								if udochka==1:
									print("Вы достаете удочку и забрасываете крючок в воду.")
									time.sleep(2)
									catch=random.randint(1,4)
									if catch!=3:
										print("Вам удалось поймать рыбу")
										time.sleep(2)
										catch="отлично"
									else:
										catch=random.randint(1,4)
										if catch!=3:
											print("Вам удалось поймать рыбу")
											time.sleep(2)
											catch="хорошо"
										else:
											catch="неудача"
										
								else:
									print("Мда, с удочкой было бы удобней, но что поделать. Нельзя же ударить в грязь лицом.")
									time.sleep(2)
									catch=random.randint(1,4)
									if catch==3:
										print("О чудо!!! Вам удалось поймать рыбу голыми руками.")
										time.sleep(2)
										catch="отлично"
									else:
										print("Не мудрено, что вы ничего не поймали. Нужно попробовать еще раз.")
										time.sleep(2)
										catch=random.randint(1,4)
										if catch!=3:
											print("О чудо!!! Вам удалось поймать рыбу голыми руками.")
											time.sleep(2)
											catch="хорошо"
										else:
											catch="неудача"
								if catch=="отлично":
									print("Вы быстро поймали рыбу и вернулись к Люси, она только открыла бутылку и устроилась на пледе(откуда только он у нее взялся?) \nВы разводите костер и готовите рыбу, при этом мило беседуя с Люси вы передаете бутылку вина друг другу. Когда солнце совсем скрывается за горизонтом, вы сидите рядом друг с другом прижавшись плечами. Люси смотрит на вас и тянется к вам с поцелуем. Да это был отличный вечер.")
									for i in range(4):
										eda()
									drunk+=20
									lucy_p+=3
									lucy_lp+=3
									gt="ж"
								if catch=="хорошо":
									print("Вы чуть задержались, поэтому Люси выпила уже пол бутылки и была на веселе. Вы все же развели костер и пожарили рыбу, но толком пообщаться вам не удалось, потому что Люси постоянно болтала и смеялась. Она хорошо провела время , чего нельзя сказать о вас.")
									for i in range(4):
										eda()
									drunk+=20
									lucy_p+=3
									gt="ж"
								if catch=="неудача":
									print("Вы жутко задержались, поэтому когда вы вернулись к Люси, бутылка вина была пуста, а сама Люси спала завернувшись в плед.")
									n=0
									n+=1
									a1=str(n)
									print("("+str(n)+")Не относить Люси.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Отнести Люси.")
									inp()
									if gt==a1:
										print("Вы не относите Люси домой.")
										time.sleep(2)
										for i in range(4):
											eda()
										lucy_angry=1
										gt="ж"
									if gt==a9:
										print("Вы относите Люси домой.")
										time.sleep(2)
										for i in range(4):
											eda()
										lucy_p+=1
										gt="ж"
										
							if gt==a9:
								print("-Как-то нет для этого настроения. \nЛюси понуро опускает плечи, убирает бутылку за пазуху. Вы пытаетесь поднять ей настроение, но у вас не больно-то и выходит. ")
								for i in range(12):
									perehod()
								time.sleep(2)
								gt="ж"
								
						if pole_rand==2:
							print("-Пойдем в лес.")
							time.sleep(2)
							print("На закате вы отправляетесь в лес.\n Здесь тихо и спокойно. вдруг Люси поворачивается к вам. \n-Давай поохотимся. Всегда любила ночную охоту, мой покойный па, иногда выводил меня на ночную охоту, это так будоражит, чувствуешь себя диким хищником.")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Давай.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Давай в другой раз.")
							inp()
							if gt==a1:
								if luk==1:
									print("-И так какие правила? \n-Кто принесет больше кроликов, тот победил, а проигравший будет должен одно желание. На все про все час. Встречаемся здесь. Удачи. \nИ она убежала в глубь леса, оставив вас хлопать глазами.")
									time.sleep(2)
									print("И так, вы присьупаете к охоте.")
									time.sleep(2)
									pole_rand=4
									while pole_rand>=4:
										catch=random.randint(1,4)
										if catch!=4:
											print("Вы добыли зайца.")
											food+=1
											pole_rand-=1
											a8+=1
											time.sleep(2)
										else:
											print("Вам не удалось никого поймать.")
											pole_rand-=1
											time.sleep(2)
									catch=random.randint(0,4)
									print("Спустя час вы встретились на опушке. \n-И так охотник, сколько ты добыл? \n-Я поймал "+str(a8)+"шт. \n-Ха, а у меня " +str(catch)+". \n-Это значит победил:")
									if a8>catch:
										print("Ты! И я должна тебе одно желание.")
										n=0
										n+=1
										a1=str(n)
										print("("+str(n)+")Поцелуй.")
										n+=1
										a9=str(n)
										print("("+str(n)+")Танец.")
										inp()
										if gt==a9:
											if lucy_lp>=10:
												print("Люси улыбнулась и станцевала для вас при свете луны. \nПосле этого вы отправляетесь домой, держась за руки.")
												for i in range(24):
													perehod()
												time.sleep(2)
												lucy_p+=3
												lucy_lp+=2
												gt="ж"
											else:
												print("-Не будя я этого делать. Все, пойдем домой, уже поздно.")
												for i in range(24):
													perehod()
												time.sleep(2)
												lucy_p+=1
												gt="ж"
										if gt==a1:
											if lucy_lp>=10:
												print("Люси засмеялась, подбежала к вам, прыгнула в ваши объятья и поцеловала. \nПосле этого вы отправляетесь домой, держась за руки.")
												for i in range(24):
													perehod()
												time.sleep(2)
												lucy_p+=3
												lucy_lp+=2
												gt="ж"
											else:
												print("-Не будя я этого делать. Все, пойдем домой, уже поздно.")
												for i in range(24):
													perehod()
												time.sleep(2)
												lucy_p+=1
												gt="ж"
											
										
									elif a8==catch:
										print("Хм... Ничья. Ладно, иди сюда, ты все равно это заслужил. \nВы подходите к Люси, а она встаёт на цыпочки и целует вас в щеку. После этого вы идете вместе домой.")
										for i in range(24):
											perehod()
										time.sleep(2)
										lucy_p+=2
										gt="ж"
										
									elif catch>a8:
										print("Я!!! Победила я!!! И ты должен мне желание... Так, чего же я хочу...")
										time.sleep(2)
										if lucy_lp>=20:
											print("Поцелуй меня... \nВы приближаетесь к Люси, обнимаете ее целуете. Крепко, страстно. \n-Воу, это было нечто, а теперь, проводи меня домой мой охотник.")
										else:
											print("Пробегись по лесу голышем.")
											time.sleep(2)
											print("Делать нечего, долг, дело святое. Вы скидываете с себя все вещи. Люси давится от смеха, прикрывая рот, что бы не сильно хохотать. Вы пускаетесь в путь. Хоть бы не было ночной детской экскурсии.")
											catch=random.randint(1,4)
											if catch!=4:
												print("Ваш голый забег прошел без происшествий, вы вернулись к Люси на опушку. Она похлопала вам и похвалила за смелость. Одевшись вы проводили ее домой.")
												for i in range(24):
													perehod()
												time.sleep(2)
												lucy_p+=2
												gt="ж"
											else:
												print("О нет!!! Ночная детская экскурсия. Куча мелких детей и училка. А вы голый. Училка завизжала, а дети начали смеяться. Так быстро вы не убегали даже от медведя. \nВернувшись на опушку к Люси, вы застали ее катающуюся по полу от смеха. \nКогда вы оделись, она все еще смеялась. \n-Ох и насмешил. Ладно пойдем теперь домой, ночной бегун.")
												for i in range(12):
													perehod()
												time.sleep(2)
												lucy_p+=2
												gt="ж"
										
								else:
									print("И как ты собрался охотиться без лука? Ладно, спасибо хотя бы за то что согласился. Ладно, пойдем просто погуляем.")
									for i in range(12):
										perehod()
									time.sleep(2)
									lucy_p+=1
									gt="ж"
							if gt==a9:
								print("Люси грустно вздыхает и идет дальше в лес, вы догоняете ее, пока она или вы не заблудились.")
								for i in range(12):
									perehod()
								time.sleep(2)
								gt="ж"
							
						if pole_rand==3:
							print("-Пойдем в таверну.")
							time.sleep(2)
							print("Вы отправляетесь в местную таверну.")
							time.sleep(2)
							print("В таверне к вечеру собирается много народу.")
							if money>=20:
								print("Вы заказываете столик на двоих и кое-какие закуски. \nОфициантка принимает ваш заказ, а Люси светится от счастья.")
								catch=1
								lucy_p+=2
							else:
								print("Денег у вас в кошельке шаром покати, так что вы просто пристраиваетесь у стеночки.")
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Пойти танцевать.")
								if mother_p>=30:
									n+=1
									a2=str(n)
									print("("+str(n)+")Споить Люси.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Просто поболтать.")
								inp()
								if gt==a1:
									print("Вы зовете Люси на танцы.")
									time.sleep(2)
									if dance<=9:
										print("Люси смеется, гляди как вы танцуете. Пару раз вы даже наступили ей на ногу. \nВ общем танцы прошли не очень удачно.")
										lucy_p+=1
									if dance>=10 and dance<=19:
										print("Хоть и неуклюже, но вы все же изредка попадали в такт. И сильно пытались не отдавить ноги Люси")
										lucy_p+=2
										lucy_lp+=1
									if dance>=20:
										print("Вы хорошо двигаетесь. У Люси на лице довольная улыбка. Она наплясались в сласть и во время медленного танца, подарила вам поцелуй.")
										lucy_p+=3
										lucy_lp+=2
									if catch==1:
										for i in range(4):
											eda()
									else:
										for i in range(24):
											perehod()
										time.sleep(2)
										gt="ж"
								if gt==a2:
									print("Вы заказываете у мамы пару стаканчиков горячительного. Выпив еще и еще, Люси уже плохо стоит на ногах. Она икает и глупо улыбается.")
									n=0
									n+=1
									a1=str(n)
									print("("+str(n)+")Зажать в углу.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Отвести ее домой.")
									inp()
									if gt==a1:
										print("Вы решили воспользоваться состоянием Люси и зажали ее в углу. Ее глаза расширились от страха, она бьет вас в пах и со слезами выбегает из таверны.")
										if catch==1:
											for i in range(4):
												eda()
										else:
											for i in range(24):
												perehod()
											lucy_angry=1
											time.sleep(2)
											place="двор"
											gt="ж"
									if gt==a9:
										print("Вы поддерживаете Люси под руки и доводите ее до дома. Там вы выслушиваете лекцию от ее матери, но Люси лишь глупо улыбается. Когда миссис Кеннет затаскивала ее в дом, Люси обернулась к вам и сказала спасибо.")
										if catch==1:
											for i in range(4):
												eda()
										else:
											for i in range(24):
												perehod()
										lucy_p+=2
										time.sleep(2)
										gt="ж"
									
								if gt==a9:
									print("Вы просто болтаете весь вечер. Не то что бы Люси была недовольна, но ей хотелось большего.  \nСпустя пару часов вы провожаете ее домой.")
									if catch==1:
										for i in range(4):
											eda()
									else:
										for i in range(24):
											perehod()
									lucy_p+=1
									time.sleep(2)
									gt="ж"
									
						if pole_rand==4:
							print("-Пойдем просто погуляем.")
							time.sleep(2)
							pole_rand=random.randint(1,3)
							if pole_rand!=3:
								print("Вы отлично погуляли на свежем воздухе.")
								lucy_p+=1
								lucy_lp+=1
								for i in range(12):
									perehod()
								time.sleep(2)
								print("Вы проводили Люси домой.")
								time.sleep(2)
								gt="ж"
							else:
								print("Вдруг за спиной вы слышите свист. \nОбернувшись вы видите, как к вам приближается местная шпана. \n -Опа, опа, какая краля, нука малой подвинься.")
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Договориться.")
								n+=1
								a2=str(n)
								print("("+str(n)+")Вступиться.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Оставить им Люси")
								
								inp()
								if gt==a2:
									print("Сейчас вы у меня по щам, получите.")
									enemy=shpana
									e_weapon=random.choice([noj, hands])
									enemy.weapon=e_weapon
									enemy.damage+=e_weapon.damage
									time.sleep(2)
									lucy_fight=1
									fight()
								
								
								if gt==a9:
									print("-Да пожалуйста, как говорила мама, баб много, а я у нее один. \nВы быстро убегаете в закат, слыша позади себя крики Люси.")
									lucy_angry=1
									for i in range(12):
										perehod()
									time.sleep(2)
									place="хиден"
									gt="ж"
					
					if gt==a9:
						print("Прости Люська, давай в другой раз.")
						perehod()
						time.sleep(2)
						gt="ж"
				else:
					print("И сопровождающий мне не нужен.")
					time.sleep(2)
					perehod()
					gt="ж"
				
			
			if gt==a9:
				print("Вы возвращаетесь на проселочную дорогу.")
				perehod()
				time.sleep(2)
				place="проселочная дорога"
				gt="ж"
	
	
	#дом вдовы кеннет
	
	#дом митчимов
	
	
	while place=="дом митчимов":
		date(d)
		print("Вы стоите у дома семьи Митчимов. Митч Митчим повар в местной таверне. Вы знаете его с самого детства, а так же трех его дочерей. Старших близняшек Фили и Гили и вашу ровесницу Лили. Дочери тоже помогают отцу, так что они работают посменно.")
		if d.hour==16:
			print("Фили сидит на лавочке перед домом и болтает с вашей сестрой.")
		if d.hour==23:
			print("Вы видите свет в окне Лили.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Зайти в дом Митчимов.")
		if d.hour==16:
			n+=1
			a2=str(n)
			print("("+str(n)+")Поговорить с Фили.")
		if d.hour==23:
			n+=1
			a3=str(n)
			print("("+str(n)+")Подойти к окну Лили.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Вернуться на проселочную дорогу.")
		catch=1
		if catch==1:
			inp()
			
			if gt==a1:
				if d.hour>=23 and d.hour<=5:
					print("Дверь закрыта. Уже поздно для гостей.")
					perehod()
					time.sleep(2)
					gt="ж"
				else:
					print("Вы заходите домой к Митчимам.")
					gt="дом лили"
					gb=gt
					time.sleep(2)
					perehod()
					while gt=="дом лили":
						date(d)
						print("Вы стоите внутри маленького дома. Хоть Митч и работает много все свои деньги он откладывает на приданное своим дочерям.")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")В комнату Митча.")
						n+=1
						a2=str(n)
						print("("+str(n)+")В комнату близняшек.")
						n+=1
						a3=str(n)
						print("("+str(n)+")В комнату Лили.")
						n+=1
						a4=str(n)
						print("("+str(n)+")На кухню.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти.")
						inp()
						
						if gt==a1:
							print("Вы идете в комнату Митча.")
							perehod()
							time.sleep(2)
							gt="комната митча"
							gb=gt
							while gt=="комната митча":
								date(d)
								print("Вы находитесь в крохотной комнатушке. Митч живет в спартанских условиях. Кроме кровати и небольшой полки с книгами в его комнате ничего больше нет.")
								if d.hour== 19:
									print("Митч сидит на кровати и читает книгу перед сном.")
									n=0
									n+=1
									a1=str(n)
									print("("+str(n)+")Поговорить.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Выйти.")
									inp()
									if gt==a1:
										print("Просто хотел немного с тобой поболтать старик.")
										mitch_p+=1
										for i in range(6):
											perehod()
										time.sleep(2)
										gt="дом лили"
									if gt==a9:
										print("Вы выходите из комнаты.")
										perehod()
										time.sleep(2)
										gt="дом лили"
								else:
									print("Комната закрыта.")
									perehod()
									time.sleep(2)
									gt="дом лили"
						
						if gt==a2:
							print("Вы идете в комнату близняшек.")
							perehod()
							time.sleep(2)
							gt="комната близняшек"
							gb=gt
							while gt=="комната близняшек":
								date(d)
								print("Вы стоите в большой комнате, которую делят две близняшки Фили и Гили. Они души не чают в своем старике и их младшей сестре Лили.")
								if d.hour==17:
									print("На пуфике у комода сидит стройная девушка, она расчесывает свои волосы. Гили так похожа на свою близняшку Фили, но только внешне, характер у них совершенно разный.")
									n=0
									n+=1
									a1=str(n)
									print("("+str(n)+")Поговорить.")
									n+=1
									a2=str(n)
									print("("+str(n)+")Флиртовать.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Выйти.")
									inp()
									if gt==a1:
										print("Просто хотел немного с тобой поболтать.")
										lily_p+=1
										for i in range(6):
											perehod()
										time.sleep(2)
										gt="дом лили"
									
									if gt==a2:
										if lily_p>=10:
											print("Флиртовать.")
											lily_lp+=1
											for i in range(6):
												perehod()
											time.sleep(2)
											gt="дом лили"
										else:
											print("Что ты себе позволяешь?")
											perehod()
											time.sleep(2)
											gt="дом лили"
									
									if gt==a9:
										print("Вы выходите из комнаты близняшек.")
										perehod()
										time.sleep(2)
										gt="дом лили"
								else:
									print("Комната закрыта.")
									perehod()
									time.sleep(2)
									gt="дом лили"
						
						if gt==a3:
							print("Вы идете в комнату Лили.")
							perehod()
							time.sleep(2)
							gt="комната лили"
							gb=gt
							while gt=="комната лили":
								date(d)
								print("Вы находитесь в маленькой комнате, которую на первый взгляд и не назовешь девчачьей. Здесь нет ни оборочек, ни рюшек, ни зеркал. Стоит лишь кровать и полка с книгами.")
								if d.hour==20:
									print("На кровати сидит коротко стриженная Лили. Она увлеченно читает книгу.")
									n=0
									n+=1
									a1=str(n)
									print("("+str(n)+")Поговорить.")
									n+=1
									a2=str(n)
									print("("+str(n)+")Флиртовать.")
									n+=1
									a9=str(n)
									print("("+str(n)+")Выйти.")
									inp()
									if gt==a1:
										print("Просто хотел немного с тобой поболтать.")
										lily_p+=1
										for i in range(6):
											perehod()
										time.sleep(2)
										gt="дом лили"
									
									if gt==a2:
										if lily_p>=10:
											print("Флиртовать.")
											lily_lp+=1
											for i in range(6):
												perehod()
											time.sleep(2)
											gt="дом лили"
										else:
											print("Что ты себе позволяешь?")
											perehod()
											time.sleep(2)
											gt="дом лили"
									
									if gt==a9:
										print("Вы выходите из комнаты Лили.")
										perehod()
										time.sleep(2)
										gt="дом лили"
								else:
									print("Комната закрыта.")
									perehod()
									time.sleep(2)
									gt="дом лили"
									
						if gt==a4:
							date(d)
							print("Вы стоите в крошечной кухоньке. Где-где, а у Митчимов всегда можно найти что-нибудь перекусить.")
							if d.hour==7:
								print("Митч и Лили завтракают.")
							if d.hour==17:
								print("Фили и Гили едят перед сменой.")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Поесть.")
							if d.hour==7:
								n+=1
								a2=str(n)
								print("("+str(n)+")Поболтать с Лили.")
							if d.hour==17:
								n+=1
								a3=str(n)
								print("("+str(n)+")Поболтать с близняшками.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Выйти.")
							inp()
							if gt==a1:
								print("Вы славно перекусили вкусной едой.")
								eda()
								time.sleep(2)
								gt="дом лили"
							
							if gt==a2 and d.hour==7:
								print("Вы подходите к Лили. Митч неодобрительно косится на вас, но все же двигается и уступает вам место рядом с собой. Лили становится удивительно молчаливой когда находится рядом с отцом. И почему-то постоянно краснеет. Вы поболтали с ними о всяких мелочах и даже перекусили.")
								mitch_p+=1
								lily_p+=1
								eda()
								time.sleep(2)
								gt="дом лили"
							
							if gt==a3:
								print("Вы подходите к близняшкам, они прерывают трапезу и смотрят на вас. Вы болтаете с пол часа и даже перекусили вместе с ними.")
								gily_p+=1
								phily_p+=1
								eda()
								time.sleep(2)
								gt="дом лили"
								
							
							if gt==a9:
								print("Вы выходите с кухни.")
								perehod()
								time.sleep(2)
								gt="дом лили"
							
						
						if gt==a9:
							print("Вы выходите во двор.")
							perehod()
							time.sleep(2)
							gt="дом митчимов"
						
					
			if gt==a3:
				print("Вы подходите к окну Лили и заглядываете в него. Вам плохо что видно через шторы. Все что вы можете рассмотреть, это очертания Лили, лежащей на кровати с книгой в руках.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Постучать в окно.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Уйти.")
				inp()
				if gt==a1:
					print("Вы слегка стучите в окно. Лили вздрагивает захлопывает книгу и испугано смотрит в окно. Увидев вас, она вскакивает на ноги, подходит к окну и распахивает ставни. \n-Что ты так пугаешь, дурак?")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Пустишь к себе?")
					n+=1
					a9=str(n)
					print("("+str(n)+")Ничего.")
					inp()
					
					if gt==a1:
						print("Лили, пустишь к себе?")
						time.sleep(2)
						if lily_p>=20:
							print("-Ладно проныра, залазь.")
							time.sleep(2)
							perehod()
							gt="комната лили ночь"
							while gt=="комната лили ночь":
								date(d)
								print("Вы находитесь в маленькой уютной комнатушке. Если бы вы не знали что это комната Лили вы бы подумали что она принадлежит какому-нибудь мальчишке. От девчачьей комнаты здесь только что сама Лили. Она уперла руки в боки и смотрит на вас выжидающе. \n-И так, ты чего хотел?")
								if d.hour<=2:
									print("Так полуночник, мне уже спать пора, завтра с отцом на смену. Так что давай, обратно через окно, только по-тихому.")
									time.sleep(2)
									perehod()
									gt="дом митчимов"
								n=0
								n+=1
								a1=str(n)
								print("("+str(n)+")Поболтать.")
								n+=1
								a2=str(n)
								print("("+str(n)+")Флирт.")
								n+=1
								a9=str(n)
								print("("+str(n)+")Выйти.")
								inp()
								if gt==a2:
									if lily_lp>=10:
										print("Успех")
										time.sleep(2)
										lily_lp+=1
										for i in range(12):
											perehod()
									else:
										print("Ты чей-то удумал? Давай дуй отсюдова.")
										perehod()
										time.sleep(2)
										gt="дом митчимов"
										
								if gt==a9:
									print("-Да просто хотел сказать привет. \n-Привет? Привет?! ты сумасшедший? Ночью. В окно. Привет?! Давай лезь обратно.")
									perehod()
									time.sleep(2)
									gt="дом митчимов"
								if gt==a1:
									print("Да просто хотел поболтать, чего расскажешь? \n-И ради этого ты отвлекал меня от книги. Ну ладно давай поболтаем.")
									time.sleep(2)
									lily_p+=2
									for i in range(12):
										perehod()
									gt="комната лили ночь"
						else:
							print("Конечно нет, ты что, сдурел? \nЛили закрывает перед вами ставни и возвращается к чтению книги.")
							perehod()
							time.sleep(2)
							gt="дом митчимов"
							
					
			if gt==a2 and d.hour==16:
				print("Вы подходите поболтать с Фили. \n-Привет Фили, привет Эмми. Как дела? \n-Ты что-то хотел малой? Иначе ты нам мешаешь.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")Да, я хотел поговорить с Фили.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Ничего.")
				inp()
				
				if gt==a1:
					print("-Вообще-то да. Я хотел поговорить с Фили. Ты не против? \nВы болтаете с Фили не обращая внимания на свою сестру.")
					phily_p+=2
					sister_p-=1
					for i in range(6):
						perehod()
					time.sleep(2)
					gt="дом митчимов"
				if gt==a9:
					print("-Да ничего я не хотел. Уже ухожу.")
					perehod()
					time.sleep(2)
					gt="дом митчимов"
				
			if gt==a9:
				print("Вы выходите обратно на проселочную дорогу.")
				perehod()
				time.sleep(2)
				gt="ж"
				place="проселочная дорога"
	
	#дом митчимов
	
	
	#дом тетчеров

	
	while place=="дом тетчеров":
		date(d)
		print("Это дом вашего друга Филипа. Вы с ним одного возраста. Его семья тоже возделывает поля. Филип иногда помогает семье, когда не успевает дать стрекоча, что б ухлестывать за девчонками.")
		n=0
		n+=1
		a1=str(n)
		print("("+str(n)+")Зайти к Тетчерам.")
		n+=1
		a2=str(n)
		print("("+str(n)+")Пойти на поле Тетчеров.")
		n+=1
		a9=str(n)
		print("("+str(n)+")Вернуться на проселочную дорогу.")
		
		inp()
		
		if gt==a1:
			if d.hour>=23 and d.hour<=5:
				print("Дом закрыт.")
			else:
				print("Вы идете к Филипу домой.")
				gt="дом филипа"
				gb=gt
			while gt=="дом филипа":
				date(d)
				print("Внутри дом Филипа такой же чистый и ухоженный, как и ваш. Мисс Тетчер следит за чистотой.")
				n=0
				n+=1
				a1=str(n)
				print("("+str(n)+")В спальню Филипа.")
				n+=1
				a2=str(n)
				print("("+str(n)+")В спальню родителей Филипа.")
				n+=1
				a3=str(n)
				print("("+str(n)+")На кухню Тэтчеров.")
				n+=1
				a9=str(n)
				print("("+str(n)+")Выйти на улицу.")
				inp()
				if gt==a2:
					reb()
					if d.hour>=23 and d.hour<=5:
						print("Комната заперта.")
					else:
						print("Вы идете в хозяйскую спальню.")
						time.sleep(2)
						date(d)
						print("Вы стоите в хозяйской спальне.")
						n=0
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти из спальни.")
						inp()
						if gt==a9:
							reb()
							print("Вы выходите обратно в коридор.")
							perehod()
							time.sleep(2)
							gt="дом филипа"
				
				if gt==a3:
					print("Вы идете на кухню.")
					time.sleep(2)
					reb()
					date(d)
					if d.hour==6 or d.hour==12 or d.hour==18:
						print("Семья Тетчеров сидит и трапезничает. \n-Здравствуй мой мальчик, садись, поешь вместе с нами")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Согласиться.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти в корридор.")
						inp()
						if gt==a1:
							reb()
							print("Вы присоединяетесь к трапезе Тетчеров.")
							eda()
							time.sleep(2)
							reb()
							gt="дом филипа"
						
						if gt==a9:
							reb()
							print("Вы выходите обратно в коридор.")
							perehod()
							reb()
							time.sleep(2)
							gt="дом филипа"
					else:
						date(d)
						print("Большая и светлая кухня Тетчеров.")
						n=0
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти в корридор.")
						inp()
						if gt==a9:
							print("Вы выходите с кухни.")
							perehod()
							time.sleep(2)
							gt="дом филипа"
				
				if gt==a1:
					print("Вы идете в спальню Филипа.")
					time.sleep(2)
					gt="комната филипа"
					while gt=="комната филипа":
						date(d)
						print("Вы стоите в спальне своего друга Филипа. В отличии от всего дома, тут сущий бардак.")
						if d.hour==20:
							print("Филип лежит у себя на кровати и смотрит в потолок.")
						n=0
						if d.hour==20:
							n+=1
							a1=str(n)
							print("("+str(n)+")Поговорить с Филипом.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Выйти из комнаты.")
						inp()
						if gt==a1 and d.hour==20:
							print("-Эй Филип, как жизнь? Не хочешь прошвырнуться по окрестностям? \n -Да давай, а то я заскучал.")
							time.sleep(2)
							pole_rand=random.randint(1,4)
							if pole_rand==1:
								print("Вы выходите на улицу и идете гулять по окрестностям. На пути вам попадаются Близняшки Фили и Гили, они идут в таверну сменить своего отца. Вы присоединяетесь к ним и провожаете их до таверны.")
								for i in range(6):
									perehod()
									place="двор"
									gt="ж"
							if pole_rand==2:
								print("Вы вышли из дома, когда во всех окнах погасли огни, один за одним. Вы видели как уезжает последняя бричка. Вы просто гуляли и болтали с другом.")
								philip_p+=2
								for i in range(12):
									perehod()
								time.sleep(2)
								gt="дом тетчеров"
								
								
							if pole_rand==3:
								print("Вы решили прогуляться до соседней улицы, как сзади вас окликнули местные хулиганы.")
								print("Вы нарываетесь на драку.")
								enemy=shpana
								e_weapon=random.choice([noj, hands])
								enemy.weapon=e_weapon
								enemy.damage+=e_weapon.damage
								time.sleep(2)
								gb="дом тетчеров"
								fight()
							if pole_rand==4:
								print("Ничего интересного не происходило.")
								philip_p+=1
								for i in range(6):
									perehod()
								time.sleep(2)
								gt="дом тетчеров"
								
						if gt==a9:
							print("Вы выходите из спальни Филипа.")
							gt="дом филипа"
							reb()
							perehod()
							time.sleep(2)
				if gt==a9:
					print("Вы выходите из дома во двор.")
					perehod()
					reb()
					time.sleep(2)
					place="дом тетчеров"
					gt="ж"
						
		
		if gt==a2:
			gt="поле тетчеров"
			print("Вы идете к полю семьи Тетчер.")
			time.sleep(2)
			gb=gt
			while gt=="поле тетчеров":
				date(d)
				if d.hour>21 or d.hour<7:
					print("В такое время на поле делать нечего.")
					pole_rand=random.randint(1,3)
					if pole_rand==3:
						print("Но в ночи вы слышите звуки доносящиеся с поля. Вряд ли это Тетчеры.")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Пойти узнать.")
						n=0
						n+=1
						a9=str(n)
						print("("+str(n)+")Уйти с поля.")
						inp()
						if gt==a1:
							print("Вы решаете пойти на звук и узнать, что там происходит.")
							pole_rand=random.randint(1,3)
							if pole_rand==1:
								print("Вы нарываетесь на драку.")
								enemy=shpana
								e_weapon=random.choice([noj, hands])
								enemy.weapon=e_weapon
								enemy.damage+=e_weapon.damage
								time.sleep(2)
								fight()
							elif pole_rand==2:
								print("Вы натыкаетесь на детей леса.")
								perehod()
								time.sleep(2)
								gt="ж"
							else:
								print("Видимо вам показалось.")
								perehod()
								time.sleep(2)
								gt="ж"
						
						if gt==a9:
							print("Вы решаете уйти по добру по здорову.")
							perehod()
							time.sleep(2)
							gt="ж"
					else:
						time.sleep(2)
						perehod()
						gt="ж"
				else:
					print("Семья тетчеров работает в поле. Быть может стоит найти Филипа?")
					n=0
					n+=1
					a1=str(n)
					print("("+str(n)+")Найти Филипа.")
					n+=1
					a2=str(n)
					print("("+str(n)+")Помочь мисс Тетчер.")
					if miss_tetcher_p>=20:
						n+=1
						a9=str(n)
						print("("+str(n)+")Флиртовать с мисс Тетчер.")
					n+=1
					a9=str(n)
					print("("+str(n)+")Уйти с поля Тетчеров.")
					inp()
					if gt==a1:
						print("Вы ищите Филипа по всему полю. Спустя некоторое время вы нашли его спящим в тени под деревом.")
						n=0
						n+=1
						a1=str(n)
						print("("+str(n)+")Разбудить Филипа.")
						n+=1
						a9=str(n)
						print("("+str(n)+")Оставить Филипа в покое.")
						inp()
						if gt==a1:
							print("Вы будите Филипа. Он смотрит на вас недовольным взглядом. \n-Ну что тебе нужно? ")
							n=0
							n+=1
							a1=str(n)
							print("("+str(n)+")Поговорить с Филипом.")
							n+=1
							a9=str(n)
							print("("+str(n)+")Уйти.")
							inp()
							if gt==a1:
								print("Да так, хотел просто поболтать. Как дела?")
								for i in range(3):
									perehod()
								philip_p+=1
								time.sleep(2)
								gt="поле тетчеров"
							
							if gt==a9:
								print("Да ничего, прости что потревожил.")
								perehod()
								time.sleep(2)
								gt="поле тетчеров"
							
						if gt==a9:
							print("Вы решили не беспокоить Филипа.")
							perehod()
							time.sleep(2)
							gt="поле тетчеров"
					
						
					if gt==a2:
						print("-Мисс Тетчер, давайте я вам помогу. \n-Ах "+player_name+", большое спасибо. Помощь действительно нужна.")
						time.sleep(2)
						print("Вы проработали на поле Тетчеров час. При этом вы беседовали с мисс Тетчер.")
						miss_tetcher_p+=1
						for i in range(12):
							perehod()
						time.sleep(2)
						gt="поле тетчеров"
						
					if gt==a3:
						print("-Мисс Тетчер, вы прекрасно выглядите. \n-Ах "+player_name+", перестань. Лучше помоги мне.")
						time.sleep(2)
						print("Вы проработали на поле Тетчеров час. При этом вы любезничали с мисс Тетчер.")
						miss_tetcher_p+=1
						miss_tetcher_lp+=1
						for i in range(12):
							perehod()
						time.sleep(2)
						gt="поле тетчеров"
						
					if gt==a9:
						print("Вы уходите с поля Тетчеров.")
						perehod()
						time.sleep(2)
						gt="ж"
		
		if gt==a9:
			print("Вы возвращаетесь на проселочную дорогу.")
			perehod()
			time.sleep(2)
			place="проселочная дорога"
			gt="ж"
		
		
		
		
	#город
		
	while place=="город":
		date(d)
		print("Вы стоите по среди улицы. Рядом вы видите МАГАЗИН, КАФЕ, ГОСТИНИЦУ. Дальше улица ведет в ПОРТ. Куда вы отправитесь?")
		gt=input()
		if gt=="магазин":
			perehod()
			
		while gt=="магазин":
			date(d)
			print("Вы стоите в магазине. Что вы хотите? КУПИТЬ или ВЫЙТИ?")
			
			gt=input()
			while gt=="купить":
				print("У вас в кошельке " + str(money) + " монет.")
				print("Что вы хотите купить? ЗЕЛЬЕ(5), ЕДА(5), или вы передумали и хотите ВЫЙТИ?")
				
				gt=input()
				if gt=="выйти":
					time.sleep(2)
					gt="магазин"
				
				if gt=="зелье":
					money-=5
					potion+=1
					print("Вы купили зелье.")
					time.sleep(2)
					gt="купить"
				
				if gt=="еда":
					money-=5
					food+=1
					print("Вы купили еду.")
					time.sleep(2)
					gt="купить"
			
			if gt=="выйти":
				perehod()
				print("Вы вышли из магазина.")
				time.sleep(2)
				#gt больше не "магазин" и поэтому цикл прерывается.
		
		if gt=="кафе":
			perehod()
		while gt=="кафе":
			date(d)
			print("Вы зашли в маленькое уютное кафе. Вы пожете ПОЕСТЬ, вы моэете ВЫЙТИ  из кафе.")
			
			gt=input()
			
			if gt=="поесть":
				d=d + timedelta (minutes =30)
				ustal+=6
				golod-=100
				print("\nВы славно поели.")
				time.sleep(2)
				gt=="кафе"
		
		if gt=="гостиница":
			perehod()
		while gt=="гостиница":
			date(d)
			print("Вы зашли в холл гостиницы. Что вы хотите? Вы можете заказать номер и ПОСПАТЬ(5) или ВЫЙТИ.")
			
			gt=input()
			if gt not in (["поспать", "выйти"]):
				gt== "гостиница"
				
				
			if gt=="поспать":
				d=d + timedelta (minutes =120)
				ustal-=25
				print("\nВы поспали пару часов.")
				time.sleep(2)
				gt=="гостиница"
			
			if gt=="выйти":
				perehod()
				print("\nВы вышли в город.")
				time.sleep(2)
				
		if gt=="порт":
			for i in range(2):
				perehod()
			place="порт"
			
	while place=="порт":
		date(d)
		print("Вы стоите на пристани, вокруг вас снуют портовые рабочие. они чем-то сильно заняты, так что на вас они не обращают ни малейшего внимания. Куда пойти? Можно вернуться обратно в ГОРОД или зайти в портовый КАБАК")
		
		gt=input()
		if gt not in (["город", "кабак"]):
			gt="ж"
		else:
			perehod()
		
		while gt=="кабак":
			print("Вы зашли в портовый кабак.")
			
		if gt=="город":
			print("\nВы пошли обратно в город.")
			time.sleep(2)
			place="город"
	#город