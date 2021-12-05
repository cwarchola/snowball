#import turtle
#wn = turtle.Screen()
#Yeah, I thought there would be a better, easier way to
#use images in my program. I googled and discovered PIL
#(pillow). After learning that it was not a built-in
#function, and failing (3 times) to install it,
#I asked my son to walk me through the installation.
#I haven't used the command prompt since 1984 (lol)
import PIL
from PIL import Image

im1 = Image.open("ask_again_later.png")
im2 = Image.open("cannot_predict_now.jpg")
im3 = Image.open("get_milk_bread_eggs.jpg")
im4 = Image.open("it_is_decidedly_so.jpg")
im5 = Image.open("most_likely.jpg")
im6 = Image.open("my_reply_is_no.jpg")
im7 = Image.open("outlook_not_so_good.jpg")
im8 = Image.open("sue_serio_says_get_to_work.jpg")
im9 = Image.open("very_doubtful.jpg")
im10 = Image.open("you_wish.jpg")
im11 = Image.open("go_to_sleep.jpg")
    
def magic_snowball():
    
    #print("How much snow is expected?")
    snowTotal = int(input("How much snow is expected?"))
                
    if snowTotal >= 12:
        im3.show()
    elif snowTotal >= 10 and snowTotal <= 11:
        im4.show()
    elif snowTotal >= 7 and snowTotal <= 9:
        im5.show()
    elif snowTotal == 5 or snowTotal == 6:
        print("When is the snow expected to start? (Use 24-hour format - 1:00pm should read 1300)")
        startSnow = int(input("When is the snow expected to start? (Use 24-hour format - 1:00pm should read 1300)"))
        if startSnow >= 30 and startSnow <= 245:
            im2.show()
        elif startSnow >= 300 and startSnow <= 900:
            print("What is the expected rate (in inches) per hour?")
            rateSnow = float(input("What is the expected rate (in inches) per hour?"))
            if rateSnow >= 0.75:
                im5.show()
            else:
                im7.show()
        elif startSnow >= 901 and startSnow <= 2000:
            im10.show()
        else:
            im11.show()
    elif snowTotal == 3 or snowTotal == 4:
        im6.show()
    else:
        im8.show()

   
magic_snowball()

#I really wanted to feed this program live data from
#NOAA or NWS into this program, but simply didn't have
#time. I am definitely going to keep working on this
#because I don't feel like it's finished and I had
#so much fun working on this. AND snow season is
#upon us!
        



