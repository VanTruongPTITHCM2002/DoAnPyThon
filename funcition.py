from declare import adjaGraph,INF,listVetex,chooseVetexColor,RADIUS_VALUE,adjaGraphVoHuong
from pygame import mouse,quit
import sys
def find_edgeTrue(start, end):
    for edge in adjaGraph:
        if (edge[0] == start and edge[1] == end):
            return edge
    return INF

def find_edge(start, end):
    for edge in adjaGraph:
        if (edge[0] == start and edge[1] == end):
            return edge[2]
    return INF

def find_edgeVoHuong_true(start, end):
    for edge in adjaGraphVoHuong:
        if (edge[0] == start and edge[1] == end) or (edge[0] == end and edge[1] == start):
            return edge
    return INF

def update_egdeVoHuong(start, end, weight):
    for edge in adjaGraphVoHuong:
        if (edge[0] == start and edge[1] == end) or (edge[0] == end and edge[1] == start):
            edge[2] =weight

def find_edgeVoHuong(start, end):
    for edge in adjaGraphVoHuong:
        if (edge[0] == start and edge[1] == end) or (edge[0] == end and edge[1] == start):
            return edge[2]
    return INF

def deleteEdge(index):
    tmp = []
    for i in range(len(adjaGraph)):
        if (adjaGraph[i][0] == index or adjaGraph[i][1] == index):
            tmp.append(i)
    #Xóa từ ngoài vào tránh bị hổng        
    tmp.reverse()
    for i in tmp:
        adjaGraph.pop(i)

    for egde in adjaGraph:
        if egde[0] > index:
            egde[0] = egde[0]-1
        if egde[1] > index:
            egde[1] = egde[1]-1
            
            
def checkDijkstra():
    for i in range(len(adjaGraph)):
        if adjaGraph[i][2] < 0:
            return False
    return True

def checkDijkstraVoHuong():
    for i in range(len(adjaGraphVoHuong)):
        if adjaGraphVoHuong[i][2] < 0:
            print(adjaGraphVoHuong[i][2])
            return False
    return True

def isHelpFloydchoose():
    (x, y) = mouse.get_pos()
    if (x >= 550 and x <= 550+100) and (y >= 550 and y <= (550 + 50)):
        return 0
    elif (x >= 750 and x <= 750+100) and (y >= 550 and y <= (550 + 50)):
        return 1
    return -1

def is_print_to_file():
    (x, y) = mouse.get_pos()
    if (x >= 650 and x <= 650+100) and (y >= 670 and y <= (670 + 30)):
        return 1
    return 0
def ischooseVetex(x, y):
    for i in range(len(listVetex)):
        if ((x >= int(listVetex[i].x) -RADIUS_VALUE and x <= int(listVetex[i].x) +RADIUS_VALUE) and (y >= int(listVetex[i].y) -RADIUS_VALUE and y <= int(listVetex[i].y) +RADIUS_VALUE)):
            listVetex[i].color = chooseVetexColor
            return i
    return -1

def findNameVetext(name):
    return list(filter(lambda x: x.name == name ,listVetex))

def setColorAllVetex(color):
    for vetex in listVetex:
        vetex.color = color

def checkChyenDoiQuaVoHuong():
    for egde in adjaGraph:
        if find_edge(egde[0], egde[1]) != INF and find_edge(egde[1], egde[0]) != INF:
            return False
    return True


def pygame_quit():
    quit()
    sys.exit()