import os
import random

way = 'images/stars'
pictures = os.listdir(way)
picture = random.choice(pictures)
print(picture)