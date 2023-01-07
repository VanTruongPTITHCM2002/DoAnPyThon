import math
import pygame
import declare
import re
smallfont = declare.pygame.font.SysFont('Corbel', 16)
def printWeight(screen,x, y, w):
    if w.is_integer():
        weight = smallfont.render(str(int(w)), True, declare.textColor)
        screen.blit(weight, (x, y))
    else:
        weight = smallfont.render(str(w), True, declare.textColor)
        screen.blit(weight, (x, y))
    # Label(screen, str(w), x, y, 16)


def drawTrianle(screen,x1, y1, x2, y2, color):
    global pygame

    tmp = []
    a1 = (x1 + y2 - y1)
    b1 = (y1 + x1 - x2)
    a2 = (x1 - y2 + y1)
    b2 = (y1 - x1 + x2)
    a3 = x2
    b3 = y2
    a4 = a1
    b4 = b1
    tmp.append((a1, b1))
    tmp.append((a2, b2))
    tmp.append((a3, b3))
    tmp.append((a4, b4))
    pygame.draw.polygon(screen, color, tmp)
    pygame.display.flip()
    pygame.display.update()


def induongnoi(screen,x1, y1, x2, y2, color, w):
    global pygame
    if (x1 - x2 == 0):
        return
    corner = math.atan(float(abs(y1 - y2)) / abs(x1 - x2))
    Rsin = declare.RADIUS_VALUE * math.sin(corner)
    Rcos = declare.RADIUS_VALUE * math.cos(corner)
    x11 = x1 + Rcos
    y11 = y1 + Rsin
    x22 = x2 - Rcos
    y22 = y2 - Rsin
    if x1 > x2:
        x11 = x1 - Rcos
        x22 = x2 + Rcos

    if y1 > y2:
        y11 = y1 - Rsin
        y22 = y2 + Rsin
    pygame.draw.line(screen, color, (x11, y11), (x22, y22), 3)
    drawTrianle(screen,2*x22-(x2+x22)/2, 2*y22-(y22+y2)/2, x22, y22, color)
    printWeight(screen,(x1+x2)/2, (y1+y2)/2, w)
    pygame.display.flip()
    pygame.display.update()


def drawCurvedLine2(screen,x1, y1, x2, y2, color, w):
    xO = (x1 + x2) / 2 + (y1 - y2) / math.sqrt(2)
    yO = (y1 + y2) / 2 + (x2 - x1) / math.sqrt(2)
    r = math.sqrt(pow(xO - x1, 2) + pow(yO - y1, 2))
    d = math.sqrt(pow(x1 - xO, 2) + pow(y1 - yO, 2))
    a = (pow(r, 2) - pow(declare.RADIUS_VALUE, 2) + pow(d, 2)) / (2 * d)
    h = math.sqrt(r * r - a * a)
    tmpx1 = xO + a * (x1 - xO) / d
    tmpx2 = xO + a * (x2 - xO) / d
    tmpy1 = yO + a * (y1 - yO) / d
    tmpy2 = yO + a * (y2 - yO) / d
    x3 = tmpx1 - h * (y1 - yO) / d
    x4 = tmpx2 + h * (y2 - yO) / d
    y3 = tmpy1 + h * (x1 - xO) / d
    y4 = tmpy2 - h * (x2 - xO) / d
    angle1 = float(x1 - xO) / r
    angle2 = 1 - float(pow(declare.RADIUS_VALUE, 2)) / (2 * pow(r, 2))
    if (angle1 < -1 or angle1 > 1):
        angle1 = int(angle1)
    if (angle2 < -1 or angle2 > 1):
        angle2 = int(angle2)
    angle1 = math.acos(angle1) * 180 / math.pi
    angle2 = math.acos(angle2) * 180 / math.pi
    if y1 >= yO:
        angle1 = 360-angle1
    stangle = angle1 + angle2
    angle1 = math.acos(
        1 - pow(math.sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2)), 2) / (2 * pow(r, 2)))
    angle1 = angle1 * 180 / math.pi
    stangle = stangle - angle1 - 2 * angle2
    endangle = stangle + angle1
    theta = math.atan2((y1 + y2) / 2 - yO, (x1 + x2) / 2 - xO)
    xT = xO + r * math.cos(theta)
    yT = yO + r * math.sin(theta)
    stangle = stangle*math.pi/180
    endangle = endangle*math.pi/180
    pygame.draw.arc(screen, color, [xO-r, yO-r,
                    2*r, 2*r], stangle, endangle, 3)
    drawTrianle(screen,2 * x4 - (x2 + x4) / 2, 2 * y4 - (y2 + y4) / 2, x4, y4, color)
    printWeight(screen,xT, yT, w)


def drawCurvedLine(screen,x1, y1, x2, y2, color, w):
    xO = (x1 + x2) / 2 + (y1 - y2) / -math.sqrt(2)
    yO = (y1 + y2) / 2 + (x2 - x1) / -math.sqrt(2)
    r = math.sqrt(pow(xO - x1, 2) + pow(yO - y1, 2))
    d = math.sqrt(pow(x1 - xO, 2) + pow(y1 - yO, 2))
    a = (pow(r, 2) - pow(declare.RADIUS_VALUE, 2) + pow(d, 2)) / (2 * d)
    h = math.sqrt(r * r - a * a)
    tmpx1 = xO + a * (x1 - xO) / d
    tmpx2 = xO + a * (x2 - xO) / d
    tmpy1 = yO + a * (y1 - yO) / d
    tmpy2 = yO + a * (y2 - yO) / d
    x3 = tmpx1 + h * (y1 - yO) / d
    x4 = tmpx2 - h * (y2 - yO) / d
    y3 = tmpy1 - h * (x1 - xO) / d
    y4 = tmpy2 + h * (x2 - xO) / d
    angle1 = float(x1 - xO) / r
    angle2 = 1 - float(pow(declare.RADIUS_VALUE, 2)) / (2 * pow(r, 2))
    if (angle1 < -1 or angle1 > 1):
        angle1 = int(angle1)
    if (angle2 < -1 or angle2 > 1):
        angle2 = int(angle2)
    angle1 = (math.acos(angle1) * 180) / math.pi
    angle2 = (math.acos(angle2) * 180) / math.pi
    if y1 >= yO:
        angle1 = 360-angle1
    stangle = angle1 + angle2
    angle1 = math.acos(
        1 - pow(math.sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2)), 2) / (2 * pow(r, 2)))
    angle1 = angle1 * 180 / math.pi
    endangle = stangle + angle1
    theta = math.atan2((y1 + y2) / 2 - yO, (x1 + x2) / 2 - xO)
    xT = xO + r * math.cos(theta)
    yT = yO + r * math.sin(theta)
    if (xT <= 250 or xT >= 1280 or yT <= 0 or yT >= 500):
        drawCurvedLine2(screen,x1, y1, x2, y2, color, w)
    else:
        stangle = stangle*math.pi/180
        endangle = endangle*math.pi/180
        pygame.draw.arc(
            screen, color, [xO-r, yO-r, 2*r, 2*r], stangle, endangle, 3)
        drawTrianle(screen,2 * x4 - (x2 + x4) / 2, 2 *
                    y4 - (y2 + y4) / 2, x4, y4, color)
        printWeight(screen,xT, yT, w)


# Vẽ Cho Đồ Thị Vô Hướng
def induongnoiVoHuong(screen,x1, y1, x2, y2, color, w):
    global pygame
    if (x1 - x2 == 0):
        return
    corner = math.atan(float(abs(y1 - y2)) / abs(x1 - x2))
    Rsin = declare.RADIUS_VALUE * math.sin(corner)
    Rcos = declare.RADIUS_VALUE * math.cos(corner)
    x11 = x1 + Rcos
    y11 = y1 + Rsin
    x22 = x2 - Rcos
    y22 = y2 - Rsin
    if x1 > x2:
        x11 = x1 - Rcos
        x22 = x2 + Rcos

    if y1 > y2:
        y11 = y1 - Rsin
        y22 = y2 + Rsin
    pygame.draw.line(screen, color, (x11, y11), (x22, y22), 3)
    printWeight(screen,(x1+x2)/2, (y1+y2)/2, w)
    pygame.display.flip()
    pygame.display.update()


def drawCurvedLine2VoHuong(screen,x1, y1, x2, y2, color, w):
    xO = (x1 + x2) / 2 + (y1 - y2) / math.sqrt(2)
    yO = (y1 + y2) / 2 + (x2 - x1) / math.sqrt(2)
    r = math.sqrt(pow(xO - x1, 2) + pow(yO - y1, 2))
    d = math.sqrt(pow(x1 - xO, 2) + pow(y1 - yO, 2))
    a = (pow(r, 2) - pow(declare.RADIUS_VALUE, 2) + pow(d, 2)) / (2 * d)
    h = math.sqrt(r * r - a * a)
    tmpx1 = xO + a * (x1 - xO) / d
    tmpx2 = xO + a * (x2 - xO) / d
    tmpy1 = yO + a * (y1 - yO) / d
    tmpy2 = yO + a * (y2 - yO) / d
    x3 = tmpx1 - h * (y1 - yO) / d
    x4 = tmpx2 + h * (y2 - yO) / d
    y3 = tmpy1 + h * (x1 - xO) / d
    y4 = tmpy2 - h * (x2 - xO) / d
    angle1 = float(x1 - xO) / r
    angle2 = 1 - float(pow(declare.RADIUS_VALUE, 2)) / (2 * pow(r, 2))
    if (angle1 < -1 or angle1 > 1):
        angle1 = int(angle1)
    if (angle2 < -1 or angle2 > 1):
        angle2 = int(angle2)
    angle1 = math.acos(angle1) * 180 / math.pi
    angle2 = math.acos(angle2) * 180 / math.pi
    if y1 >= yO:
        angle1 = 360-angle1
    stangle = angle1 + angle2
    angle1 = math.acos(
        1 - pow(math.sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2)), 2) / (2 * pow(r, 2)))
    angle1 = angle1 * 180 / math.pi
    stangle = stangle - angle1 - 2 * angle2
    endangle = stangle + angle1
    theta = math.atan2((y1 + y2) / 2 - yO, (x1 + x2) / 2 - xO)
    xT = xO + r * math.cos(theta)
    yT = yO + r * math.sin(theta)
    stangle = stangle*math.pi/180
    endangle = endangle*math.pi/180
    pygame.draw.arc(screen, color, [xO-r, yO-r,
                    2*r, 2*r], stangle, endangle, 3)
    printWeight(screen,xT, yT, w)


def drawCurvedLineVoHuong(screen,x1, y1, x2, y2, color, w):
    xO = (x1 + x2) / 2 + (y1 - y2) / -math.sqrt(2)
    yO = (y1 + y2) / 2 + (x2 - x1) / -math.sqrt(2)
    r = math.sqrt(pow(xO - x1, 2) + pow(yO - y1, 2))
    d = math.sqrt(pow(x1 - xO, 2) + pow(y1 - yO, 2))
    a = (pow(r, 2) - pow(declare.RADIUS_VALUE, 2) + pow(d, 2)) / (2 * d)
    h = math.sqrt(r * r - a * a)
    tmpx1 = xO + a * (x1 - xO) / d
    tmpx2 = xO + a * (x2 - xO) / d
    tmpy1 = yO + a * (y1 - yO) / d
    tmpy2 = yO + a * (y2 - yO) / d
    x3 = tmpx1 + h * (y1 - yO) / d
    x4 = tmpx2 - h * (y2 - yO) / d
    y3 = tmpy1 - h * (x1 - xO) / d
    y4 = tmpy2 + h * (x2 - xO) / d
    angle1 = float(x1 - xO) / r
    angle2 = 1 - float(pow(declare.RADIUS_VALUE, 2)) / (2 * pow(r, 2))
    if (angle1 < -1 or angle1 > 1):
        angle1 = int(angle1)
    if (angle2 < -1 or angle2 > 1):
        angle2 = int(angle2)
    angle1 = (math.acos(angle1) * 180) / math.pi
    angle2 = (math.acos(angle2) * 180) / math.pi
    if y1 >= yO:
        angle1 = 360-angle1
    stangle = angle1 + angle2
    angle1 = math.acos(
        1 - pow(math.sqrt(pow(x3 - x4, 2) + pow(y3 - y4, 2)), 2) / (2 * pow(r, 2)))
    angle1 = angle1 * 180 / math.pi
    endangle = stangle + angle1
    theta = math.atan2((y1 + y2) / 2 - yO, (x1 + x2) / 2 - xO)
    xT = xO + r * math.cos(theta)
    yT = yO + r * math.sin(theta)
    if (xT <= 250 or xT >= 1280 or yT <= 0 or yT >= 500):
        drawCurvedLine2(screen,x1, y1, x2, y2, color, w)
    stangle = stangle*math.pi/180
    endangle = endangle*math.pi/180
    pygame.draw.arc(screen, color, [xO-r, yO-r,
                    2*r, 2*r], stangle, endangle, 3)
    printWeight(screen,xT, yT, w)



class Label:

    ''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''

    def __init__(self, screen, text, x, y, size=16, color=declare.textColor):
        if size != 20:
            self.font = declare.fontsize(size)
        else:
            self.font = declare.font_default
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        declare.labels.append(self)

    def addText(self, text, color=declare.textColor):
        self.text += text
        self.image = self.font.render(self.text, 1, color)

    def change_text(self, newtext, color=declare.textColor):
        self.image = self.font.render(newtext, 1, color)

    def change_font(self, font, size, color=declare.textColor):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)

    def draw(self):
        self.screen.blit(self.image, (self.rect))

# Quản lý label


def show_labels():
    for _ in declare.labels:
        _.draw()




### inputbox

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        global screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    txt = self.text
                    self.text = ''
                    self.txt_surface = FONT.render("", True, self.color)
                    self.active = False
                    return txt
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                a = re.findall('[a-zA-Z0-9 -_.]+', self.text)
                self.text = ''.join(a)
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def setText(self, text):
        self.text = text

# Quản lý inputbox
input_box1 = InputBox(150, 510, 100, 30)
input_boxes = [input_box1]

def show_all_input(screen):
    for box in input_boxes:
        box.draw(screen)


# Vetex
class Vetex:
    def __init__(self, screen, x, y, color, name):
        self.x = x
        self.y = y
        self.color = color
        self.name = name
        self.screen = screen

    def draw_name(self,screen):
        if (len(self.name) <= 3):
            #  screen.blit(textAddVetex,textAddVetex.get_rect(center = pygame.Rect(i[0][0],i[0][1],i[0][2],i[0][3]).center))
            font = pygame.font.SysFont("Corbel", 16)
            nameVetex = font.render(self.name, True, declare.textColor)
            text_rect = nameVetex.get_rect(center=pygame.Rect(
                self.x-declare.RADIUS_VALUE, self.y-declare.RADIUS_VALUE, 2*declare.RADIUS_VALUE, 2*declare.RADIUS_VALUE).center)
            screen.blit(nameVetex, text_rect)
        elif len(self.name) <= 5:
            nameVetex = smallfont.render(self.name, True, declare.textColor)
            text_rect = nameVetex.get_rect(center=pygame.Rect(
                self.x-declare.RADIUS_VALUE, self.y-declare.RADIUS_VALUE, 2*declare.RADIUS_VALUE, 2*declare.RADIUS_VALUE).center)
            screen.blit(nameVetex, text_rect)
        else:
            font = pygame.font.SysFont("Corbel", 6)
            nameVetex = font.render(self.name, True, declare.textColor)
            text_rect = nameVetex.get_rect(center=pygame.Rect(
                self.x-declare.RADIUS_VALUE, self.y-declare.RADIUS_VALUE, 2*declare.RADIUS_VALUE, 2*declare.RADIUS_VALUE).center)
            screen.blit(nameVetex, text_rect)

    def create_vetex(self, x, y,screen):
        self.x = x
        self.y = y
        pygame.draw.circle(screen, self.color, (x, y), declare.RADIUS_VALUE)

    def drawVetex(self,screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), declare.RADIUS_VALUE)
        self.draw_name(screen)

# Quan lý Vetex
def showAllVetex(screen):
    for i in declare.listVetex:
        i.drawVetex(screen)
