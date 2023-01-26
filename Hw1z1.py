
from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt
from dirty_main import *
import text_to_image
from PIL import Image
import random

if __name__ == "__main__":
    i_remember_time = dt.datetime.now()
    calculate_salary()
    get_employees()
    print(dt.datetime) # 3
    print(dt.datetime.now())
    print("format", dt.datetime.now().strftime('%Y yrs %m moths %d days %H hours %M minutes %S seconds'))
    print("today", dt.date.today(), "time", dt.datetime.now().time(), "and it is")
    print(dt.datetime.now() - i_remember_time)
    print("seconds elapsed")
    print()
    with open("Hw1z1.py", "r") as f: # 4
        text = f.read()
    img = text_to_image.encode(text, "image.png")
    print(img, text_to_image.decode("image.png"))
    img = Image.new('RGBA', (64, 64), 'white')
    for x in range(64):
        for y in range(64):
            c = random.randint(0, 255)
            img.putpixel((x, y), (x*4, y*4, c))
    img.save("image2.png")
    img.show()





