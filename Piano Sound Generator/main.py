import pygame
import piano_list as pl
from pygame import mixer

pygame.init()
pygame.mixer.set_num_channels(45)

font = pygame.font.Font('resources/Dreaming Christmas.otf', 62)
med_font = pygame.font.Font('resources/selawksb.ttf', 16)
small_font = pygame.font.Font('resources/Crumble Bakery.otf', 18)
smallest_font = pygame.font.Font('resources/Crumble Bakery.otf', 14)
fps = 60
timer = pygame.time.Clock()
width = 1400
height = 400

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Piano Bajaoo!!')

k_whites = []
k_blacks = []
white_sounds = []
black_sounds = []

left_hand= pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels

for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'resources\\notes\\{white_notes[i]}.wav'))

for i in range(len(black_notes)):
    black_sounds.append(mixer.Sound(f'resources\\notes\\{black_notes[i]}.wav'))

left_octave = 4
right_octave = 5

def make_piano(whites, blacks):   #making a piano
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white', [i*35, height - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i*35, height - 300, 35, 300], 2, 2)
        key_labels = small_font.render(pl.white_notes[i], True, 'black')
        screen.blit(key_labels, (i*35 + 3, height - 20))

    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, 'black', [23 + (i*35) + (skip_count * 35), height - 300, 24, 200], 0, 2)
        for j in range(len(blacks)):
            if blacks[j][0] == i:
                if blacks[j][1]>0:
                    pygame.draw.rect(screen, 'blue', [23 + (i*35) + (skip_count * 35), height - 300, 24, 200], 2, 2)
                    blacks[j][1] -= 1

        key_labels = smallest_font.render(pl.black_labels[i], True, 'white')
        screen.blit(key_labels, (25 + (i*35) +(skip_count * 35), height - 120))
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    for i in range (len(whites)):
        if whites[i][1]>0:
            k = whites[i][0]
            pygame.draw.rect(screen, 'blue', [k * 35, height - 100, 35, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks

def disp_title():
    t_name = font.render('Press and Enjoy!', True, 'black',)
    screen.blit(t_name,(158, 18))
    t_name = font.render('Press and Enjoy!', True, 'blue', )
    screen.blit(t_name, (156, 16))
    left_keys_text = med_font.render('LEFT OCTAVE: S, D, G, H, J for black keys & Z, X, C, V, B, N, M for white keys', True, 'black')
    screen.blit(left_keys_text, (width - 580, 10))
    left_keys_text = med_font.render('RIGHT OCTAVE: 5, 6, 8, 9, 0 for black keys & R, T, Y, U, I, O, P for white keys', True, 'black')
    screen.blit(left_keys_text, (width - 580, 38))

active = True
while active:
    left_dict = {
                 'Z': f'C{left_octave}',
                 'S': f'C#{left_octave}',
                 'X': f'D{left_octave}',
                 'D': f'D#{left_octave}',
                 'C': f'E{left_octave}',
                 'V': f'F{left_octave}',
                 'G': f'F#{left_octave}',
                 'B': f'G{left_octave}',
                 'H': f'G#{left_octave}',
                 'N': f'A{left_octave}',
                 'J': f'A#{left_octave}',
                 'M': f'B{left_octave}'
                 }

    right_dict = {'R': f'C{right_octave}',
                  '5': f'C#{right_octave}',
                  'T': f'D{right_octave}',
                  '6': f'D#{right_octave}',
                  'Y': f'E{right_octave}',
                  'U': f'F{right_octave}',
                  '8': f'F#{right_octave}',
                  'I': f'G{right_octave}',
                  '9': f'G#{right_octave}',
                  'O': f'A{right_octave}',
                  '0': f'A#{right_octave}',
                  'P': f'B{right_octave}'}



    timer.tick(fps)
    screen.fill('grey')
    white_keys, black_keys, k_whites, k_blacks = make_piano(k_whites, k_blacks)
    disp_title()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.TEXTINPUT:
            if event.text.upper() in left_dict:
                if left_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(left_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    k_blacks.append([index, 30])
                else:
                    index = white_notes.index(left_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    k_whites.append([index, 30])
            if event.text.upper() in right_dict:
                if right_dict[event.text.upper()][1] == '#':
                    index = black_labels.index(right_dict[event.text.upper()])
                    black_sounds[index].play(0, 1000)
                    k_blacks.append([index, 30])
                else:
                    index = white_notes.index(right_dict[event.text.upper()])
                    white_sounds[index].play(0, 1000)
                    k_whites.append([index, 30])


    pygame.display.flip()
pygame.quit()