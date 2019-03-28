from moviepy.editor import *
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

#Use https://video.online-convert.com/convert/gif-to-mp4 to convert gif to mp4 and save to directory

pygame.display.set_caption('GIF Player')

clip = VideoFileClip('giphy.mp4')
for i in range(0,3):
    clip.preview()

pygame.quit()