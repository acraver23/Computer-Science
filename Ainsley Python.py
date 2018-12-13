import webbrowser as wb
import pyautogui as pg
import time as t
points = 0
show = pg.prompt ("What is your favorite show? ")
if show == "friends":
    pg.alert("My favorite character is Joey!")
    wb.open("https://www.youtube.com/watch?v=34172ltXqw8")
    t.sleep(5)
    points += 15
elif show == "the office":
    pg.alert("I love Dwight!")
    wb.open("https://www.youtube.com/watch?v=bqgVB6Vl-lI")
    t.sleep(5)
    points += 5
elif show == "stranger things":
    pg.alert("Max is the best!")
    t.sleep(5)
    points += 10
elif show == "how i met your mother":
    pg.alert("The ending was so sad!")
    wb.open("https://www.youtube.com/watch?v=C19US6rqqAo")
    t.sleep(5)
    points += 7
elif show == "90210":
    pg.alert("I love that show! So sad they took it off Netflix.")
    wb.open("https://www.youtube.com/watch?v=ITI-2dDyiBc")
    t.sleep(5)
    points += 3
elif show == "gossip girl":
    pg.alert ("I liked gossip girl but I stopped watching after they all went to college.")
    wb.open("https://www.youtube.com/watch?v=vxi6NlFoj-o")
    t.sleep(5)
    points -= 5
else:
    pg.alert("Your favorite show is " + show)
food = pg.prompt ("What is your favorite food? ")
if food == "pizza":
    pg.alert ("That's a popular answer.")
    wb.open("https://www.youtube.com/watch?v=0O16-V_JtYs")
    t.sleep(5)
    points += 2
elif food == "tacos":
    pg.alert ("I love tacos! Especially from Tomatillos!")
    wb.open("https://www.youtube.com/watch?v=npjF032TDDQ")
    t.sleep(5)
    points += 10
elif food == "hambuger":
    pg.alert ("My favorite is a buger with fries and a milkshake!")
    t.sleep(5)
    points += 15
elif food == "ice cream":
    pg.alert ("I love ice cream! My favorite flavor is chocolate and caramel.")
    wb.open("https://www.gogogogourmet.com/vanilla-rainbow-ice-cream/")
    t.sleep(5)
    points += 8
elif food == "popcorn":
    pg.alert ("That's my favorite salty snack.")
    wb.open("https://www.landolakes.com/recipe/17299/chunky-caramel-popcorn/")
    t.sleep(5)
    points += 6
elif food == "salad":
    pg.alert ("Eww. So healthy!")
    t.sleep(5)
    points -= 5
else:
    pg.alert ("That's a good choice!")
sport = pg.prompt ("What is your favorite sport? ")
if sport == "soccer":
    pg.alert ("Most of my friends play soccer, too!")
    wb.open("https://www.youtube.com/watch?v=K-U1ZgrsGGg")
    t.sleep(5)
    points += 0
elif sport == "dance":
    pg.alert ("Me too! I love turning!")
    wb.open("https://www.youtube.com/watch?v=50lAMbJUXfc")
    t.sleep(5)
    points += 15
elif sport == "football":
    pg.alert ("Our football team this year is not that good.")
    t.sleep(5)
    points += 5
elif sport == "hockey":
    pg.alert ("Cool! I haven't skated in a while.")
    wb.open("https://www.youtube.com/watch?v=fx7Qba7p6pY")
    t.sleep(5)
    points += 3
elif sport == "field hockey":
    pg.alert ("I used to play field hockey but I haven't since last year.")
    t.sleep(5)
    points += 7
elif sport== "lax":
    pg.alert ("Most of my friends play lax, too.")
    wb.open("https://www.youtube.com/watch?v=LbPFmgl7igY")
    t.sleep(5)
    points -= 2
else:
    pg.alert ("I've never done " + sport + "!")
animal = pg.prompt ("What is your favorite animal? ")
if animal == "dog":
    pg.alert("Same! I have a yellow lab.")
    wb.open("https://www.youtube.com/watch?v=vvppaufeD3Q")
    t.sleep(5)
    points += 15
elif animal == "cat":
    pg.alert("I hate cats! They are so mean and creepy.")
    wb.open("https://www.youtube.com/watch?v=1Wh8RzcQZr4")
    t.sleep(5)
    points -= 20
elif animal == "horse":
    pg.alert("Cool! Do you ride horses?")
    wb.open("https://www.google.com/search?q=smiling+horses&rlz=1C1GCEA_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjox9yalMXeAhVMmuAKHdGgBawQ_AUIEygB&biw=619&bih=578#imgrc=clIix4wE7uUzdM:")
    t.sleep(5)
    points += 10
elif animal == "dolphin":
    pg.alert("I wish I coukld swim with them one day.")
    t.sleep(5)
    points += 5
elif animal == "elephant":
    pg.alert("I love elephants! I saw a bunch when I was on safari in Africa.")
    t.sleep(5)
    points += 5
elif animal == "bunny":
    pg.alert ("I don't like bunnies. One time my friend's pet bunny bit me.")
    wb.open("https://www.youtube.com/watch?v=14KTu4i27j8")
    t.sleep(5)
    points -= 10
else:
    pg.alert("Your favorite animal is " + animal)
place = pg.prompt ("What is your favorite place? ")
if place == "new york":
    pg.alert("Same! I love the city!")
    wb.open("https://www.youtube.com/watch?v=ae8_-GTf3UY")
    t.sleep(5)
    points += 15
elif place == "anywhere warm":
    pg.alert("The beach is the best place to be!")
    t.sleep(5)
    points += 10
elif place == "bahamas":
    pg.alert("Cool! I've never been!")
    wb.open("https://www.google.com/search?q=bahamas&rlz=1C1GCEA_enUS752US752&tbm=isch&source=lnms&sa=X&ved=0ahUKEwiEpoH6muPeAhUKTt8KHeqKBgcQ_AUICygC&biw=619&bih=578&dpr=1.1")
    t.sleep(5)
    points -= 5
elif place == "colorado":
    pg.alert("I love skiing there!")
    wb.open("https://www.youtube.com/watch?v=CnJfIONbJF4")
    t.sleep(5)
    points += 7
elif place == "england":
    pg.alert("Would you like spot of tea?")
    wb.open("https://www.youtube.com/watch?v=5jB4kU_ip7U")
    t.sleep(5)
    points += 5
elif place == "south america":
    pg.alert ("Cool! I've never been!")
    t.sleep(5)
    points -= 5
else:
    pg.alert("Your favorite place is " + place)
pg.alert ("You earned " + str(points) + " points!")
