import pygame
import time
import sys

lyrics = [
    "NigahHooon Mein Dekhoo",
    "Meri Jo Haai Bas Gaya.........",
    "WohHai Milta Tumseaa HoobBahu.....",
    ".........Ooooooooo................",
    "Jane Teri ..AankhenThi ya",
    "BaateinThi Wajah........",
    "Huye Tum Jo Dil Kiie AArEzooo........"
]

timestamps = [0.0 , 2.99 , 8.19 , 13.49 , 16.66 , 20.65 , 25.27 , 29.8]

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/UMER ISLAM/OneDrive/Pictures/BeSt FrIEndS FoREveR_320kbps.mp3.mpeg")
pygame.mixer.music.play()
start = time.time()

def type_line(line, next_ts, start_ts):
    duration = next_ts - start_ts
    delay = duration / max(len(line), 1)

    for ch in line:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

i = 0
while i < len(lyrics):
    now = time.time() - start

    if now >= timestamps[i]:
        next_ts = timestamps[i+1] if i+1 < len(timestamps) else now + 3
        type_line(lyrics[i], next_ts, timestamps[i])
        i += 1

    time.sleep(0.005)
