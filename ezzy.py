import pygame

import pygame

active = False

def init():
    pygame.init()
    active = True

# Precisamos retornar a tela para usá-la depois
def execute(width, height, title):
    pygame.display.set_caption(title)
    return pygame.display.set_mode((width, height))

def end():
    active = False
    pygame.quit()

class time():
    @staticmethod
    def Clock():
        return pygame.time.Clock()

class event():
    @staticmethod
    def get():
        return pygame.event.get()

    @staticmethod
    def quit():
        return pygame.QUIT

def fill(screen, color):
    screen.fill(color)

def display():
    pygame.display.flip()

# Adicionado o return
def v2(x=0.0, y=0.0):
    return pygame.Vector2(x, y)

def getWidth(screen):
    return screen.get_width()

def getHeight(screen):
    return screen.get_height()

class draw():
    @staticmethod
    def circle(screen, color, pos, radius):
        pygame.draw.circle(screen, color, pos, radius)

class key():
    @staticmethod
    def get_keydown():
        return pygame.key.get_pressed()

#parte 2

def isRunning():
    return active

class keys():
    key_esc = pygame.K_ESCAPE
    key_f1 = pygame.K_F1
    key_f2 = pygame.K_F2
    key_f3 = pygame.K_F3
    key_f4 = pygame.K_F4
    key_f5 = pygame.K_F5
    key_f6 = pygame.K_F6
    key_f7 = pygame.K_F7
    key_f8 = pygame.K_F8
    key_f9 = pygame.K_F9
    key_f10 = pygame.K_F10
    key_f11 =  pygame.K_F11
    key_f12 = pygame.K_F12
    key_printscreen =  pygame.K_PRINT
    key_scrolllock = pygame.K_SCROLLOCK
    key_pausebreak = pygame.K_PAUSE
    key_backquote = pygame.K_BACKQUOTE  # Tecla ~ / `
    key_1 = pygame.K_1
    key_2 = pygame.K_2
    key_3 = pygame.K_3
    key_4 = pygame.K_4
    key_5 = pygame.K_5
    key_6= pygame.K_6
    key_7 = pygame.K_7
    key_8 = pygame.K_8
    key_9 = pygame.K_9
    key_0 = pygame.K_0
    key_minus = pygame.K_MINUS
    key_equals = pygame.K_EQUALS
    key_backspace = pygame.K_BACKSPACE

        # Linha do Tab
    key_tab = pygame.K_TAB
    key_q = pygame.K_q
    key_w = pygame.K_w
    key_e = pygame.K_e
    key_r = pygame.K_r
    key_t = pygame.K_t
    key_y = pygame.K_y
    key_u = pygame.K_u
    key_i = pygame.K_i
    key_o = pygame.K_o
    key_p = pygame.K_p
    key_leftbracket = pygame.K_LEFTBRACKET  # [
    key_rightbracket = pygame.K_RIGHTBRACKET # ]
    key_backslash = pygame.K_BACKSLASH      # \

        # Linha do CapsLock
    key_capslock = pygame.K_CAPSLOCK
    key_a = pygame.K_a
    key_s = pygame.K_s
    key_d = pygame.K_d
    key_f = pygame.K_f
    key_g = pygame.K_g
    key_h = pygame.K_h
    key_j = pygame.K_j
    key_k = pygame.K_k
    key_l = pygame.K_l
    key_semicolon = pygame.K_SEMICOLON    # ;
    key_quote = pygame.K_QUOTE            # '
    key_enter = pygame.K_RETURN

        # Linha do Shift
    key_lshift = pygame.K_LSHIFT
    key_z = pygame.K_z
    key_x = pygame.K_x
    key_c = pygame.K_c
    key_v = pygame.K_v
    key_b = pygame.K_b
    key_n = pygame.K_n
    key_m = pygame.K_m
    key_comma = pygame.K_COMMA
    key_period = pygame.K_PERIOD
    key_slash = pygame.K_SLASH
    key_rshift = pygame.K_RSHIFT

        # Linha de baixo / Modificadores
    key_lctrl = pygame.K_LCTRL
    key_lalt = pygame.K_LALT
    key_space = pygame.K_SPACE
    key_ralt = pygame.K_RALT
    key_rctrl = pygame.K_RCTRL

        # Setas e Comandos Centrais
    key_insert = pygame.K_INSERT
    key_home = pygame.K_HOME
    key_pageup = pygame.K_PAGEUP
    key_delete = pygame.K_DELETE
    key_end = pygame.K_END
    key_pagedown = pygame.K_PAGEDOWN

    key_up = pygame.K_UP
    key_down = pygame.K_DOWN
    key_left = pygame.K_LEFT
    key_right = pygame.K_RIGHT

        # Teclado Numérico (Opcional)
    key_numlock = pygame.K_NUMLOCK
    key_kp0 = pygame.K_KP0
    key_kp1 = pygame.K_KP1
    key_kp2 = pygame.K_KP2
    key_kp3 = pygame.K_KP3
    key_kp4 = pygame.K_KP4
    key_kp5 = pygame.K_KP5
    key_kp6 = pygame.K_KP6
    key_kp7 = pygame.K_KP7
    key_kp8 = pygame.K_KP8
    key_kp9 = pygame.K_KP9


def loadImg(path):
    return pygame.image.load(path)
    

def blit(screen, img, pos):
    return screen.blit(img, pos)

class cursors():
    arrow = pygame.SYSTEM_CURSOR_ARROW
    ibeam = pygame.SYSTEM_CURSOR_IBEAM
    def compile():
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        