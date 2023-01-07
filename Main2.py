
### Thư viện đồ họa
import pygame

### khai báo tiêu đề
import menu

### Sử dụng dialog win32
import ctypes
from ctypes.wintypes import HWND, LPWSTR, UINT

### Hiển thị bảng để lấy địa chỉ file
from tkinter import filedialog

### Khai báo bảng cài đătk
import MainCaidai
### Khai báo file hỗ trợ vẽ
import HoTroVeDuongDi as draw
### Khai báo biến
from declare import *
#Khai báo các hàm hỗ trợ tính toán
import funcition as fun

# dialog
_user32 = ctypes.WinDLL('user32', use_last_error=True)
_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT  # default return type is c_int, this is not required
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

MB_OK = 0
MB_OKCANCEL = 1
MB_YESNOCANCEL = 3
MB_YESNO = 4
MB_ICONWARNING = 30
IDOK = 1
IDCANCEL = 2
IDABORT = 3
IDYES = 6
IDNO = 7


def MessageBoxW(hwnd, text, caption, utype):
    result = _MessageBoxW(hwnd, text, caption, utype)
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return result

### Khởi tạo pygame
pygame.init()

# function
def show_edge(start, end, color, FlagHuongDoThi):
    global pygame
    global screen
    global adjaGraph
    x1 = listVetex[start].x
    y1 = listVetex[start].y
    x2 = listVetex[end].x
    y2 = listVetex[end].y
    if FlagHuongDoThi:
        if fun.find_edge(end, start) == INF or start < end:
            draw.induongnoi(screen, x1, y1, x2, y2,
                            color, fun.find_edge(start, end))
        else:
            draw.drawCurvedLine(screen, x1, y1, x2, y2,
                                color, fun.find_edge(start, end))
    else:
        draw.induongnoiVoHuong(screen, x1, y1, x2, y2,
                            color, fun.find_edgeVoHuong(start, end))


def renameVetexFuntion():
    if isEmptyGraph():
        return
    global pygame
    global screen
    global isSaved
    done = True
    title = draw.Label(screen, "Chọn vào đỉnh để đổi tên!", 500, 510, 28)
    while done:
        for event in pygame.event.get():
            (mousex, mousey) = pygame.mouse.get_pos()
            tmp = fun.ischooseVetex(mousex, mousey)
            if tmp == -1:
                fun.setColorAllVetex(nomalVetexColor)
            if event.type == pygame.QUIT:
                try:
                    result = MessageBoxW(
                        None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                    if result == IDYES:
                        fun.pygame_quit()
                    elif result == IDNO:
                        continue
                except:
                    fun.pygame_quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    (x, y) = pygame.mouse.get_pos()
                    if ((x >= 250 + RADIUS_VALUE) and (x <= 1280 - RADIUS_VALUE) and (y >= 0 + RADIUS_VALUE) and (y <= 500 - RADIUS_VALUE)):
                        index = fun.ischooseVetex(x, y)
                        if (index != -1):
                            draw.input_box1.active = True
                            draw.input_box1.color = draw.COLOR_ACTIVE
                            a = renameVetext(listVetex[index])
                            if a == 1:
                                listVetex[index].color = nomalVetexColor
                                isSaved = False
                            elif a == 2:
                                done = False
                            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
            pygame.display.flip()
        draw.showAllVetex(screen)
        reTextZone()
        pygame.display.flip()
    fun.setColorAllVetex(nomalVetexColor)
    labels.remove(title)
    rescreen()
    pygame.display.flip()


def addEdegsFuntion():
    if isEmptyGraph():
        return
    start = -1
    end = -1
    weight = 0.0
    index = -1
    global pygame
    global screen
    global adjaGraph
    global isSaved
    done = True
    dragging = False
    global FlagHuongDoThi
    title = draw.Label(
        screen, "Nối hai đỉnh để thêm hoặc xóa cung!", 500, 510, 28)
    while done:
        for event in pygame.event.get():
            (mousex, mousey) = pygame.mouse.get_pos()
            tmp = fun.ischooseVetex(mousex, mousey)
            if tmp == -1 and index != -1:
                listVetex[index].color = nomalVetexColor
            index = tmp
            if event.type == pygame.QUIT:
                try:
                    result = MessageBoxW(
                        None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                    if result == IDYES:
                        fun.pygame_quit()
                    elif result == IDNO:
                        continue
                except:
                    fun.pygame_quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    (tmp1, tmp2) = pygame.mouse.get_pos()
                    start = fun.ischooseVetex(tmp1, tmp2)
                    x = listVetex[start].x
                    y = listVetex[start].y
                    dragging = True
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                (mousex, mousey) = pygame.mouse.get_pos()
                end = fun.ischooseVetex(mousex, mousey)
                if end == -1 or end == start:
                    listVetex[start].color = nomalVetexColor
                    reWorkingZone()
                    continue
                text1 = draw.Label(
                    screen, "Nhập trọng số (xóa cung nhập 'd/D)", 500, 540, 28)
                text2 = draw.Label(screen, "Trọng số:", 500, 600, 28)
                input_Weight = draw.InputBox(600, 600, 140, 32)
                draw.input_boxes.append(input_Weight)
                pygame.display.flip()
                done1 = True
                deleteFlag = False
                draw.induongnoi(screen, x, y, mousex, mousey,
                                nomalLineColor, weight)
                escape = False
                while done1:
                    for event in pygame.event.get():
                        tmp_weight = None
                        for box in draw.input_boxes:
                            tmp_weight = box.handle_event(event)
                        if (tmp_weight != None):
                            try:
                                weight = float(tmp_weight)
                                done1 = False
                            except:
                                try:
                                    result = MessageBoxW(
                                        None, "Vui Lòng nhập số", "Thông báo lỗi", MB_OKCANCEL)
                                    if result == IDOK:
                                        continue
                                    elif result == IDCANCEL:
                                        listVetex[start].color = nomalVetexColor
                                        listVetex[end].color = nomalVetexColor
                                        start = -1
                                        end = -1
                                        labels.clear()
                                        draw.input_boxes.remove(input_Weight)
                                        rescreen()
                                        return
                                    else:
                                        return
                                except WindowsError as win_err:
                                    return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                escape = True
                                done1 = False
                            if event.key == pygame.K_d:
                                if FlagHuongDoThi:
                                    if fun.find_edge(start, end) != INF:
                                        try:
                                            result = MessageBoxW(
                                                None, "Bạn có muốn xóa cung không", "Thông báo xác nhận", MB_YESNO)
                                            if result == IDYES:
                                                egde = fun.find_edgeTrue(
                                                    start, end)
                                                adjaGraph.remove(egde)
                                                deleteFlag = True
                                                rescreen()
                                                done1 = False
                                            elif result == IDNO:
                                                continue
                                            else:
                                                pass
                                        except:
                                            return
                                    else:
                                        try:
                                            result = MessageBoxW(
                                                None, "Nếu bạn chọn nhầm cạnh ấn \"yes\", còn bạn ấn nhầm (d/D) ấn \"no\"", "Lỗi không tìm thấy cạnh để xóa", MB_YESNO)
                                            if result == IDYES:
                                                listVetex[start].color = nomalVetexColor
                                                listVetex[end].color = nomalVetexColor
                                                start = -1
                                                end = -1
                                                labels.remove(text1)
                                                labels.remove(text2)
                                                draw.input_boxes.remove(
                                                    input_Weight)
                                                rescreen()
                                                addEdegsFuntion()
                                                return
                                            elif result == IDNO:
                                                continue
                                            else:
                                                pass
                                            break
                                        except WindowsError as win_err:
                                            pass
                                else:
                                    if fun.find_edgeVoHuong(start, end) != INF:
                                        try:
                                            result = MessageBoxW(
                                                None, "Bạn có muốn xóa cung không", "Thông báo xác nhận", MB_YESNO)
                                            if result == IDYES:
                                                egde = fun.find_edgeVoHuong_true(
                                                    start, end)
                                                adjaGraphVoHuong.remove(egde)
                                                egde = fun.find_edgeVoHuong_true(
                                                    start, end)
                                                if egde != INF:
                                                    adjaGraphVoHuong.remove(
                                                        egde)
                                                egde1 = fun.find_edgeTrue(
                                                    start, end)
                                                egde2 = fun.find_edgeTrue(
                                                    end, start)
                                                if egde1 != INF:
                                                    adjaGraph.remove(egde1)
                                                if egde2 != INF:
                                                    adjaGraph.remove(egde2)
                                                deleteFlag = True
                                                rescreen()
                                                done1 = False
                                            elif result == IDNO:
                                                continue
                                            else:
                                                pass
                                        except:
                                            return
                    reTextZone()
                    pygame.display.flip()
                if escape:
                    labels.remove(text1)
                    labels.remove(text2)
                    draw.input_boxes.remove(input_Weight)
                    reTextZone()
                    draw.showAllVetex(screen)
                    reWorkingZone()
                    continue
                if deleteFlag:
                    pass
                elif fun.find_edge(start, end) != INF and FlagHuongDoThi:
                    egde = fun.find_edgeTrue(start, end)
                    egde[2] = weight
                elif fun.find_edgeVoHuong(start, end) != INF and FlagHuongDoThi == False:
                    fun.update_egdeVoHuong(start, end,weight)
                else:
                    adjaGraph.append([start, end, weight])
                    if FlagHuongDoThi == False:
                        for edge in adjaGraph:
                            adjaGraphVoHuong.append(
                                [edge[0], edge[1], edge[2]])
                            adjaGraphVoHuong.append(
                                [edge[1], edge[0], edge[2]])
                listVetex[start].color = nomalVetexColor
                listVetex[end].color = nomalVetexColor
                start = -1
                end = -1
                labels.remove(text1)
                labels.remove(text2)
                draw.input_boxes.remove(input_Weight)
                isSaved = False
                rescreen()
            elif event.type == pygame.MOUSEMOTION and dragging:
                if start == -1:
                    continue
                reWorkingZone()
                (mousex, mousey) = pygame.mouse.get_pos()
                end = fun.ischooseVetex(mousex, mousey)
                if (end != -1):
                    listVetex[end].color = nomalVetexColor
                draw.induongnoi(screen, x, y, mousex, mousey,
                                nomalLineColor, weight)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
        reTextZone()
        draw.showAllVetex(screen)
    reWorkingZone()
    labels.remove(title)


def deleteVetexFuntion():
    if isEmptyGraph():
        return
    global pygame
    global screen
    global adjaGraph
    global isSaved
    index = -1
    done = True
    title = draw.Label(screen, "Chọn đỉnh cần xóa", 500, 510, 28)
    while done:
        for event in pygame.event.get():
            (mousex, mousey) = pygame.mouse.get_pos()
            tmp = fun.ischooseVetex(mousex, mousey)
            if tmp == -1 and index != -1:
                listVetex[index].color = nomalVetexColor
            index = tmp
            if event.type == pygame.QUIT:
                try:
                    result = MessageBoxW(
                        None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                    if result == IDYES:
                        fun.pygame_quit()
                    elif result == IDNO:
                        continue
                except:
                    fun.pygame_quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    (x, y) = pygame.mouse.get_pos()
                    if ((x >= 250 + RADIUS_VALUE) and (x <= 1280 - RADIUS_VALUE) and (y >= 0 + RADIUS_VALUE) and (y <= 500 - RADIUS_VALUE)):
                        index = fun.ischooseVetex(x, y)
                        if (index != -1):
                            try:
                                result = MessageBoxW(
                                    None, "Bạn có chắc xóa đỉnh không?", "Thông báo xác nhận", MB_YESNO)
                                if result == IDYES:
                                    fun.deleteEdge(index)
                                    listVetex.pop(index)
                                    isSaved = False
                                    index = -1
                                    if FlagHuongDoThi == False:
                                        adjaGraphVoHuong.clear()
                                        for edge in adjaGraph:
                                            adjaGraphVoHuong.append(
                                                [edge[0], edge[1], edge[2]])
                                            adjaGraphVoHuong.append(
                                                [edge[1], edge[0], edge[2]])
                                    reWorkingZone()
                                elif result == IDNO:
                                    listVetex[index].color = nomalVetexColor
                                else:
                                    listVetex[index].color = nomalVetexColor
                            except WindowsError as win_err:
                                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
            pygame.display.flip()
        reTextZone()
        draw.showAllVetex(screen)
    labels.remove(title)
    reTextZone()
    pygame.display.flip()


def moveFunciton():
    if isEmptyGraph():
        return
    global pygame
    global screen
    global adjaGraph
    global isSaved
    done = True
    dragging = False
    title = draw.Label(screen, "Chọn đỉnh cần di chuyển", 500, 510, 28)
    text1 = draw.Label(
        screen, "Dùng thao tác kéo thả để di chuyển từng đỉnh", 500, 550, 16)
    text2 = draw.Label(
        screen, "Hoặc dùng Crtl + kéo thả để di chuyển toàn bộ đồ thị", 500, 580, 16)
    index = -1
    check = False
    reTextZone()
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    result = MessageBoxW(
                        None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                    if result == IDYES:
                        fun.pygame_quit()
                    elif result == IDNO:
                        continue
                except:
                    fun.pygame_quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    (x, y) = pygame.mouse.get_pos()
                    index = fun.ischooseVetex(x, y)
                    if (index != -1):
                        dragging = True

            elif event.type == pygame.MOUSEMOTION and dragging:
                (x, y) = pygame.mouse.get_pos()
                if (check == True):
                    dx = x - listVetex[index].x
                    dy = y - listVetex[index].y
                    oldx = listVetex[index].x
                    oldy = listVetex[index].y
                    for i in range(len(listVetex)):
                        listVetex[i].x += dx
                        listVetex[i].y += dy
                        listVetex[index].x = x
                        listVetex[index].y = y
                        if ((listVetex[i].x < 250 + RADIUS_VALUE) or (listVetex[i].x > 1280 - RADIUS_VALUE) or (listVetex[i].y < 0 + RADIUS_VALUE) or (listVetex[i].y > 500 - RADIUS_VALUE)):
                            for j in range(i+1):
                                listVetex[j].x -= dx
                                listVetex[j].y -= dy
                            listVetex[index].x = oldx
                            listVetex[index].y = oldy
                            break
                    reWorkingZone()
                else:
                    oldx = listVetex[index].x
                    oldy = listVetex[index].y
                    listVetex[index].x = x
                    listVetex[index].y = y
                    if ((listVetex[index].x < 250 + RADIUS_VALUE) or (listVetex[index].x > 1280 - RADIUS_VALUE) or (listVetex[index].y < 0 + RADIUS_VALUE) or (listVetex[index].y > 500 - RADIUS_VALUE)):
                        listVetex[index].x = oldx
                        listVetex[index].y = oldy
                    reWorkingZone()
            elif event.type == pygame.MOUSEBUTTONUP:
                listVetex[index].color = nomalVetexColor
                dragging = False
                isSaved = False
                rescreen()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
                if event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL:
                    check = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RCTRL or event.key == pygame.K_LCTRL:
                    check = False
    labels.remove(title)
    labels.remove(text1)
    labels.remove(text2)
    rescreen()


def removeAllGraph():
    global isSaved
    if isEmptyGraph():
        return
    try:
        result = MessageBoxW(
            None, "Bạn có chắc xóa toàn bộ đồ thị không?", "Thông báo xác nhận", MB_YESNO)
        if result == IDYES:
            listVetex.clear()
            adjaGraph.clear()
            isSaved = True
        elif result == IDNO:
            pass
        else:
            pass
    except WindowsError as win_err:
        pass


def saveFileFuntion():
    global isSaved
    if isEmptyGraph():
        return
    global adjaGraph
    file_path = filedialog.asksaveasfilename(
        filetypes=(("Graph", ".txt"),   ("All Files", "*.*")))
    if file_path == '':
        print("sadsa")
        return
    if FlagHuongDoThi == False:
        for edge in adjaGraph:
            edge[2] = fun.find_edgeVoHuong(edge[0],edge[1])
    f = open(file_path, 'w')
    f.write(str(len(listVetex)) + "\n")
    for i in range(len(listVetex)):
        text = str(listVetex[i].x) + " " + str(listVetex[i].y) + \
            " " + str(listVetex[i].name) + '\n'
        f.write(text)
    f.write(str(len(adjaGraph)) + "\n")
    for i in range(len(adjaGraph)):
        text = str(adjaGraph[i][0]) + " " + str(adjaGraph[i]
                                                [1]) + " " + str(adjaGraph[i][2]) + '\n'
        f.write(text)
    f.close()
    isSaved = True


def loadFileFuntion():
    global FlagHuongDoThi
    global adjaGraph
    global adjaGraphVoHuong
    global isSaved
    file_path = filedialog.askopenfilename(
        filetypes=(("Graph", ".txt"),   ("All Files", "*.*")))
    if file_path == '':
        return
    if len(listVetex) != 0 and isSaved == False:
        try:
            result = MessageBoxW(
                None, "Hiện đang có đồ thị bạn vẫn muốn tiếp tục load file?", "Thông báo", MB_YESNO)
            if result == IDYES:
                pass
            elif result == IDNO:
                return
            else:
                pass
        except WindowsError as win_err:
            pass
    listVetex.clear()
    adjaGraph.clear()
    f = open(file_path, 'r')
    length = int(f.readline())
    if (length < 0):
        try:
            result = MessageBoxW(
                None, "Lỗi trong quá trình load file", "Thông báo lỗi", MB_OKCANCEL)
            if result == IDOK:
                return
            elif result == IDCANCEL:
                return
            else:
                pass
        except WindowsError as win_err:
            pass
    for i in range(length):
        s1 = f.readline()
        arr = s1.split()
        x = int(arr[0])
        y = int(arr[1])
        name = str(arr[2])
        vetex = draw.Vetex(screen, x, y, nomalVetexColor, name)
        listVetex.append(vetex)
    length = int(f.readline())
    if (length >= 0):
        for i in range(length):
            s1 = f.readline()
            arr = s1.split()
            x = int(arr[0])
            y = int(arr[1])
            z = float(arr[2])
            adjaGraph.append([x, y, z])
    if not FlagHuongDoThi:
        if fun.checkChyenDoiQuaVoHuong():
            for edge in adjaGraph:
                adjaGraphVoHuong.append(
                    [edge[0], edge[1], edge[2]])
                adjaGraphVoHuong.append(
                    [edge[1], edge[0], edge[2]])
        else:
            try:
                result = MessageBoxW(
                    None, "Trong file có cạnh có 2 giá trị trọng số. Bạn có muốn chuyển sang đồ thị có hướng?", "Thông báo lỗi", MB_YESNO)
                if result == IDYES:
                    FlagHuongDoThi = True
                elif result == IDNO:
                    adjaGraph.clear()
                    listVetex.clear()
                    return False
                else:
                    adjaGraph.clear()
                    listVetex.clear()
                    return False
            except WindowsError as win_err:
                FlagHuongDoThi = True
    return True


def chooseTwoVertices():
    if isEmptyGraph():
        return
    text1 = draw.Label(screen, "Chọn đỉnh xuất phát: ", 500, 510, 16)
    text2 = draw.Label(screen, "", 500, 550, 16)
    global pygame
    global adjaGraph
    pygame.display.flip()
    done = True
    index = -1
    start = -1
    stop = -1
    first = True
    while done:
        for event in pygame.event.get():
            (mousex, mousey) = pygame.mouse.get_pos()
            tmp = fun.ischooseVetex(mousex, mousey)
            if tmp == -1 and index != -1:
                listVetex[index].color = nomalVetexColor
            index = tmp
            if event.type == pygame.QUIT:
                if not isSaved:
                    try:
                        result = MessageBoxW(
                            None, "Bạn có muốn thoát không?", "Thông báo chưa lưu", MB_YESNO)
                        if result == IDYES:
                            fun.pygame_quit()
                        elif result == IDNO:
                            continue
                    except:
                        pass
                else:
                    fun.pygame_quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    (x, y) = pygame.mouse.get_pos()
                    tmp1 = fun.ischooseVetex(x, y)
                    if tmp1 != -1:
                        if first:
                            text1.change_text(
                                "Chọn đỉnh xuất phát: " + str(listVetex[tmp].name))
                            text2.change_text("Chọn đỉnh kết thúc: ")
                            first = False
                            start = tmp1
                        else:
                            text2.change_text(
                                "Chọn đỉnh kết thúc: " + str(listVetex[tmp].name))
                            stop = tmp1
                if start != -1 and stop != -1:
                    rescreen()
                    return (start, stop)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return (-1, -1)
            reTextZone()
            draw.showAllVetex(screen)
    rescreen()


def showDijkstra(dist, trace, start, stop):
    global pygame
    global screen
    global adjaGraph
    global FlagHuongDoThi
    text3 = draw.Label(screen, "", 500, 590, 16)

    if dist[stop] == INF:
        text3.change_text("Không tồn tại đường đi")
    else:
        ans = []
        text3.change_text("Tổng trọng số là:" + str(dist[stop]))
        text4 = draw.Label(screen, "Đường đi ngắn nhất là:", 500, 630, 16)
        f = stop
        while not f == start:
            ans.append(f)
            f = trace[f]

        ans.append(start)
        ans.reverse()
        for i in range(len(ans)):
            listVetex[ans[i]].color = moveVetextColor
            text4.addText(str(listVetex[ans[i]].name))
            draw.showAllVetex(screen)
            if i != len(ans)-1:
                text4.addText("->", textColor)
                show_edge(ans[i], ans[i+1], moveLineColor, FlagHuongDoThi)
                pygame.time.delay(delay)
            pygame.display.flip()
        reTextZone()
        pygame.display.flip()


def print_result_to_file(flag,dist, trace, start, stop):
    file_path = filedialog.asksaveasfilename(filetypes=(("Graph", ".txt"),   ("All Files", "*.*")))
    if file_path == '':
            return
    f = open(file_path, 'w', encoding='utf-8')
    if (flag == 1):
        f.write("Thuật toán Dijkstra\n")
        if dist[stop] == INF:
            f.write("Không tồn tại đường đi\n")
        else:
            ans = []
            f.write("Tổng trọng số là:" + str(dist[stop]) + "\n")
            f.write("Đường đi ngắn nhất là:")
            tmp = stop
            while not tmp == start:
                ans.append(tmp)
                tmp = trace[tmp]
            ans.append(start)
            ans.reverse()
            for i in range(len(ans)):
                f.write(str(listVetex[ans[i]].name))
                if i != len(ans)-1:
                    f.write("->")
            f.close()
    else:
        f.write("Thuật toán Bellman-ford\n")
        if dist[stop] == INF:
            f.write("Không tồn tại đường đi\n")
        else:
            ans = []
            f.write("Tổng trọng số là:" + str(dist[stop]) + "\n")
            f.write("Đường đi ngắn nhất là:")
            tmp = stop
            while not tmp == start:
                ans.append(tmp)
                tmp = trace[tmp]
            ans.append(start)
            ans.reverse()
            for i in range(len(ans)):
                f.write(str(listVetex[ans[i]].name))
                if i != len(ans)-1:
                    f.write("->")
            f.close()
        
    

def Dijkstra(FlagHuongDoThi):
    if isEmptyGraph():
        return
    runDijkstra = True
    while runDijkstra:  
        done = False
        (start, stop) = chooseTwoVertices()
        if (start == -1 or stop == -1):
            labels.clear()
            fun.setColorAllVetex(nomalVetexColor)
            rescreen()
            pygame.display.flip()
            return
        visited = [False for _ in range(len(listVetex) + 1)]
        dist = [INF for _ in range(len(listVetex) + 1)]
        trace = [-1 for _ in range(len(listVetex) + 1)]
        dist[start] = 0
        if FlagHuongDoThi:
            while True:
                min_d = INF
                min_index = -1
                for v in range(len(listVetex)):
                    if not visited[v]:
                        if dist[v] < min_d:
                            min_d = dist[v]
                            min_index = v
                if (min_index == -1 or min_index == stop):
                    break

                visited[min_index] = True
                for v in range(len(listVetex)):
                    if not visited[v]:
                        if round(dist[min_index] + fun.find_edge(min_index, v),10) < dist[v]:
                            dist[v] = round(dist[min_index] + fun.find_edge(min_index, v),10)
                            trace[v] = min_index
        else:
            while True:
                min_d = INF
                min_index = -1
                for v in range(len(listVetex)):
                    if not visited[v]:
                        if dist[v] < min_d:
                            min_d = dist[v]
                            min_index = v
                if (min_index == -1 or min_index == stop):
                    break

                visited[min_index] = True
                for v in range(len(listVetex)):
                    if not visited[v]:
                        if round(dist[min_index] + fun.find_edgeVoHuong(min_index, v),10) < dist[v]:
                            dist[v] = round(dist[min_index] + fun.find_edgeVoHuong(min_index, v),10)
                            trace[v] = min_index
        showDijkstra(dist, trace, start, stop)
        text5 = draw.Label(screen, "Tiếp tục ấn enter!", 500, 680, 16)
        reTextZone()
        pygame.draw.rect(screen,"#F8F8FF",[650,670,100,30])
        textAdd = smallfont.render("In ra file", True, textColor)
        screen.blit(textAdd, textAdd.get_rect(
            center=pygame.Rect(650, 670, 100, 30).center))
        pygame.display.update()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        result = MessageBoxW(
                            None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                        if result == IDYES:
                            fun.pygame_quit()
                        elif result == IDNO:
                            continue
                    except:
                        fun.pygame_quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        labels.clear()
                        fun.setColorAllVetex(nomalVetexColor)
                        rescreen()
                        done = False
                        runDijkstra = False
                    elif event.key == pygame.K_RETURN:
                        labels.clear()
                        fun.setColorAllVetex(nomalVetexColor)
                        done = False
                        rescreen()
                elif event.type == pygame.MOUSEMOTION:
                    tmp = fun.is_print_to_file()
                    if tmp == 1:
                        pygame.draw.rect(screen,"#3CB371",[650,670,100,30])
                        textAdd = smallfont.render("In ra file", True, textColor)
                        screen.blit(textAdd, textAdd.get_rect(
                            center=pygame.Rect(650, 670, 100, 30).center))
                        pygame.display.update()
                    else:
                        pygame.draw.rect(screen,"#F8F8FF",[650,670,100,30])
                        textAdd = smallfont.render("In ra file", True, textColor)
                        screen.blit(textAdd, textAdd.get_rect(
                            center=pygame.Rect(650, 670, 100, 30).center))
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = pygame.mouse.get_pos()
                    if (x >= 650 and x <= 650+100) and (y >= 670 and y <= 670+30):     
                          print_result_to_file(1,dist,trace,start,stop)
    rescreen()


def Bellman_Ford(FlagHuongDoThi):
    if isEmptyGraph():
        return
    runBellman_Ford = True
    while runBellman_Ford:
        (start, stop) = chooseTwoVertices()
        if (start == -1 or stop == -1):
            labels.clear()
            fun.setColorAllVetex(nomalVetexColor)
            rescreen()
            pygame.display.flip()
            return
        visited = [False for _ in range(len(listVetex) + 1)]
        dist = [INF for _ in range(len(listVetex) + 1)]
        trace = [-1 for _ in range(len(listVetex) + 1)]
        dist[start] = 0
        if FlagHuongDoThi:
            for _ in range(len(listVetex) - 1):
                for u, v, w in adjaGraph:
                    if dist[u] != INF and round(dist[u] + w,10) < dist[v]:
                        dist[v] = round(dist[u] + w,10)
                        trace[v] = u
            for u, v, w in adjaGraph:
                if dist[u] != INF and round(dist[u] + w,10) < dist[v]:
                    try:
                        result = MessageBoxW(
                            None, "Đồ thị có chứa chu trình âm", "Thông báo lỗi", MB_OKCANCEL)
                        if result == IDOK:
                            labels.clear()
                            rescreen()
                            fun.setColorAllVetex(nomalVetexColor)
                            return
                        elif result == IDCANCEL:
                            labels.clear()
                            rescreen()
                            fun.setColorAllVetex(nomalVetexColor)
                            return
                        else:
                            labels.clear()
                            rescreen()
                            fun.setColorAllVetex(nomalVetexColor)
                            return

                    except WindowsError as win_err:
                        pass
        else:
            for _ in range(len(listVetex) - 1):
                for u, v, w in adjaGraphVoHuong:
                    if dist[u] != INF and round(dist[u] + w,10) < dist[v]:
                        dist[v] = round(dist[u] + w,10)
                        trace[v] = u
            for u, v, w in adjaGraphVoHuong:
                if dist[u] != INF and round(dist[u] + w,10) < dist[v]:
                    try:
                        result = MessageBoxW(
                            None, "Đồ thị có chứa chu trình âm", "Thông báo lỗi", MB_OKCANCEL)
                        if result == IDOK:
                            labels.clear()
                            rescreen()
                            fun.setColorAllVetex(nomalVetexColor)
                            return
                        elif result == IDCANCEL:
                            labels.clear()
                            rescreen()
                            fun.setColorAllVetex(nomalVetexColor)
                            return
                        else:
                            labels.clear()
                            rescreen()
                            fun.setColorAllVetex(nomalVetexColor)
                            return

                    except WindowsError as win_err:
                        pass
        showDijkstra(dist, trace, start, stop)
        text5 = draw.Label(screen, "Tiếp tục ấn enter!", 500, 680, 16)
        reTextZone()
        pygame.draw.rect(screen,"#F8F8FF",[650,670,100,30])
        textAdd = smallfont.render("In ra file", True, textColor)
        screen.blit(textAdd, textAdd.get_rect(
            center=pygame.Rect(650, 670, 100, 30).center))
        pygame.display.update()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        result = MessageBoxW(
                            None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                        if result == IDYES:
                            fun.pygame_quit()
                        elif result == IDNO:
                            continue
                    except:
                        fun.pygame_quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        labels.clear()
                        fun.setColorAllVetex(nomalVetexColor)
                        rescreen()
                        done = False
                        runBellman_Ford = False
                    elif event.key == pygame.K_RETURN:
                        labels.clear()
                        fun.setColorAllVetex(nomalVetexColor)
                        rescreen()
                        done = False
                elif event.type == pygame.MOUSEMOTION:
                    tmp = fun.is_print_to_file()
                    if tmp == 1:
                        pygame.draw.rect(screen,"#3CB371",[650,670,100,30])
                        textAdd = smallfont.render("In ra file", True, textColor)
                        screen.blit(textAdd, textAdd.get_rect(
                            center=pygame.Rect(650, 670, 100, 30).center))
                        pygame.display.update()
                    else:
                        pygame.draw.rect(screen,"#F8F8FF",[650,670,100,30])
                        textAdd = smallfont.render("In ra file", True, textColor)
                        screen.blit(textAdd, textAdd.get_rect(
                            center=pygame.Rect(650, 670, 100, 30).center))
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = pygame.mouse.get_pos()
                    if (x >= 650 and x <= 650+100) and (y >= 670 and y <= 670+30):     
                          print_result_to_file(0,dist,trace,start,stop)
    rescreen()


def helpFloyd():
    color1 = "#F8F8FF"
    color2 = "#3CB371"
    txtNotify1 = draw.Label(
        screen, "Bạn muốn sử dụng Floyd để tìm đường đi ngắn nhất giữa hay giữa các cặp đỉnh(xuất ra file)", 500, 510, 16)
    reTextZone()
    pygame.draw.rect(screen, color1, [550, 550, 100, 50])
    content = smallfont.render("Tìm 2 đỉnh", True, textColor)
    screen.blit(content, content.get_rect(
        center=pygame.Rect([550, 550, 100, 50]).center))
    pygame.draw.rect(screen, color1, [750, 550, 100, 50])
    content = smallfont.render("Xuất ra File", True, textColor)
    screen.blit(content, content.get_rect(
        center=pygame.Rect([750, 550, 100, 50]).center))
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    result = MessageBoxW(
                        None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                    if result == IDYES:
                        fun.pygame_quit()
                    elif result == IDNO:
                        continue
                except:
                    fun.pygame_quit()
            elif event.type == pygame.MOUSEMOTION:
                tmp = fun.isHelpFloydchoose()
                if tmp == -1:
                    pygame.draw.rect(screen, color1, [550, 550, 100, 50])
                    content = smallfont.render("Tìm 2 đỉnh", True, textColor)
                    screen.blit(content, content.get_rect(
                        center=pygame.Rect([550, 550, 100, 50]).center))
                    pygame.draw.rect(screen, color1, [750, 550, 100, 50])
                    content = smallfont.render("Xuất ra File", True, textColor)
                    screen.blit(content, content.get_rect(
                        center=pygame.Rect([750, 550, 100, 50]).center))
                elif tmp == 0:
                    pygame.draw.rect(screen, color2, [550, 550, 100, 50])
                    content = smallfont.render("Tìm 2 đỉnh", True, textColor)
                    screen.blit(content, content.get_rect(
                        center=pygame.Rect([550, 550, 100, 50]).center))
                elif tmp == 1:
                    pygame.draw.rect(screen, color2, [750, 550, 100, 50])
                    content = smallfont.render("Xuất ra File", True, textColor)
                    screen.blit(content, content.get_rect(
                        center=pygame.Rect([750, 550, 100, 50]).center))
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    labels.remove(txtNotify1)
                    return 2
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if (x >= 550 and x <= 550+100) and (y >= 550 and y <= (550 + 50)):
                    labels.remove(txtNotify1)
                    return 0
                elif (x >= 750 and x <= 750+100) and (y >= 550 and y <= (550 + 50)):
                    labels.remove(txtNotify1)
                    return 1



def print_result_to_file_floyd(arr2d,trace,stop,start):
    file_path = filedialog.asksaveasfilename(filetypes=(("Graph", ".txt"),   ("All Files", "*.*")))
    if file_path == '':
            return
    f = open(file_path, 'w', encoding='utf-8')
    f.write("Thuật toán Floyd\n")
    if arr2d[start][stop] == INF:
        f.write("Không có đường đi")
    else:
        ans = []
        ans.append(start)
        f.write("Đường đi ngắn nhất từ " + str(listVetex[start].name) + " đến " + str(listVetex[stop].name) + " có độ dài là: " + str(arr2d[start][stop]) + "\n")
        while start != stop:
            start = trace[start][stop]
            ans.append(start)
            f.write("Đường đi: ")
        for i in range(len(ans)):
            f.write(str(listVetex[ans[i]].name))
            if i != len(ans)-1:
                f.write("->")
        f.close()


def Floyd(FlagHuongDoThi):
    if isEmptyGraph():
        return
    Flag = False
    check = helpFloyd()
    if check == 0:
        Flag = False
    elif check == 1:
        Flag = True
    elif check == 2:
        return
    arr2d = [[INF for j in range(len(listVetex))]
            for i in range(len(listVetex))]
    trace = [[-1 for j in range(len(listVetex))]
            for i in range(len(listVetex))]
    if FlagHuongDoThi:
        for egde in adjaGraph:
            arr2d[egde[0]][egde[1]] = egde[2]
            trace[egde[0]][egde[1]] = egde[1]
        for i in range(len(listVetex)):
            arr2d[i][i] = 0
            trace[i][i] = i
        for k in range(len(listVetex)):
            for i in range(len(listVetex)):
                for j in range(len(listVetex)):
                    if arr2d[i][j] > round(arr2d[i][k] + arr2d[k][j],10):
                        arr2d[i][j] = round(arr2d[i][k] + arr2d[k][j],10)
                        trace[i][j] = trace[i][k]
    else:
        for egde in adjaGraphVoHuong:
            arr2d[egde[0]][egde[1]] = egde[2]
            trace[egde[0]][egde[1]] = egde[1]
        for i in range(len(listVetex)):
            arr2d[i][i] = 0
            trace[i][i] = i
        for k in range(len(listVetex)):
            for i in range(len(listVetex)):
                for j in range(len(listVetex)):
                    if arr2d[i][j] > round(arr2d[i][k] + arr2d[k][j],10):
                        arr2d[i][j] = round(arr2d[i][k] + arr2d[k][j],10)
                        trace[i][j] = trace[i][k]
    for i in range(len(listVetex)):
        if arr2d[i][i] < 0:
            try:
                result = MessageBoxW(
                    None, "Đồ thị có chứa chu trình âm", "Thông báo lỗi", MB_OKCANCEL)
                if result == IDOK:
                    labels.clear()
                    rescreen()
                    fun.setColorAllVetex(nomalVetexColor)
                    return
                elif result == IDCANCEL:
                    labels.clear()
                    rescreen()
                    fun.setColorAllVetex(nomalVetexColor)
                    return
                else:
                    labels.clear()
                    rescreen()
                    fun.setColorAllVetex(nomalVetexColor)
                    return
            except WindowsError as win_err:
                pass
    # In Kết Quả Ra fiLe
    if Flag:
        file_path = filedialog.asksaveasfilename(
            filetypes=(("Graph", ".txt"),   ("All Files", "*.*")))
        if file_path == '':
            return
        f = open(file_path, 'w', encoding='utf-8')
        for i in range(len(listVetex)):
            f.write("Đường đi từ đỉnh " +
                    str(listVetex[i].name) + " đến tất cả các đỉnh" + "\n")
            for j in range(len(listVetex)):
                if i != j:
                    batdau = i
                    ketthuc = j
                    tmp = []
                    tmp.append(batdau)
                    if arr2d[i][j] == INF:
                        f.write("Không có đường đi từ đỉnh " +
                                str(listVetex[i].name) + "->" + str(listVetex[j].name) + "\n")
                        continue
                    f.write("Đường đi từ đỉnh " + str(listVetex[i].name) + "->" + str(
                        listVetex[j].name) + " có độ dài là: " + str(arr2d[i][j]) + "\n")
                    while batdau != ketthuc:
                        batdau = trace[batdau][ketthuc]
                        tmp.append(batdau)
                    f.write("Đường đi: ")
                    for t in range(len(tmp)):
                        f.write(str(listVetex[tmp[t]].name))
                        if t != len(tmp)-1:
                            f.write("->")
                    f.write("\n")
            f.write("\n")
        f.close()
        return
    else:
        run_Floyd = True
        while run_Floyd:
            (start, stop) = chooseTwoVertices()
            start_for_print_file = start
            stop_for_print_file = stop
            if (start == -1 or stop == -1):
                labels.clear()
                fun.setColorAllVetex(nomalVetexColor)
                draw.showAllVetex(screen)
                pygame.display.flip()
                return
            if arr2d[start][stop] == INF:
                try:
                    result = MessageBoxW(
                        None, "Không có đường đi bạn có muốn tiếp tục lựa chọn đỉnh khác", "Thông báo", MB_YESNO)
                    if result == IDYES:
                        labels.clear()
                        rescreen()
                        Floyd(FlagHuongDoThi)
                        return
                    elif result == IDNO:
                        labels.clear()
                        rescreen()
                        fun.setColorAllVetex(nomalVetexColor)
                        return
                    else:
                        labels.clear()
                        rescreen()
                        fun.setColorAllVetex(nomalVetexColor)
                except WindowsError as win_err:
                    pass
            else:
                ans = []
                ans.append(start)
                text3 = draw.Label(screen, "Đường đi ngắn nhất từ" + str(listVetex[start].name) + " đến " + str(
                    listVetex[stop].name) + "có độ dài là: " + str(arr2d[start][stop]), 500, 590, 16)
                while start != stop:
                    start = trace[start][stop]
                    ans.append(start)
                text4 = draw.Label(screen, "Đường đi:", 500, 630, 16)
                for i in range(len(ans)):
                    listVetex[ans[i]].color = moveVetextColor
                    text4.addText(str(listVetex[ans[i]].name))
                    draw.showAllVetex(screen)
                    if i != len(ans)-1:
                        text4.addText("->", textColor)
                        show_edge(ans[i], ans[i+1], moveLineColor, FlagHuongDoThi)
                        pygame.time.delay(delay)
                    reTextZone()
                    pygame.display.flip()
            text5 = draw.Label(screen, "Tiếp tục ấn enter!", 500, 680, 16)
            reTextZone()
            pygame.draw.rect(screen,"#F8F8FF",[650,670,100,30])
            textAdd = smallfont.render("In ra file", True, textColor)
            screen.blit(textAdd, textAdd.get_rect(
                center=pygame.Rect(650, 670, 100, 30).center))
            pygame.display.update()
            done = True
            while done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        try:
                            result = MessageBoxW(
                                None, "Bạn có muốn thoát không?", "Thông báo", MB_YESNO)
                            if result == IDYES:
                                fun.pygame_quit()
                            elif result == IDNO:
                                continue
                        except:
                            fun.pygame_quit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            labels.clear()
                            fun.setColorAllVetex(nomalVetexColor)
                            rescreen()
                            done = False
                            run_Floyd = True
                        elif event.key == pygame.K_RETURN:
                            labels.clear()
                            fun.setColorAllVetex(nomalVetexColor)
                            rescreen()
                            done = False
                    elif event.type == pygame.MOUSEMOTION:
                        tmp = fun.is_print_to_file()
                        if tmp == 1:
                            pygame.draw.rect(screen,"#3CB371",[650,670,100,30])
                            textAdd = smallfont.render("In ra file", True, textColor)
                            screen.blit(textAdd, textAdd.get_rect(
                                center=pygame.Rect(650, 670, 100, 30).center))
                            pygame.display.update()
                        else:
                            pygame.draw.rect(screen,"#F8F8FF",[650,670,100,30])
                            textAdd = smallfont.render("In ra file", True, textColor)
                            screen.blit(textAdd, textAdd.get_rect(
                                center=pygame.Rect(650, 670, 100, 30).center))
                            pygame.display.update()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        (x,y) = pygame.mouse.get_pos()
                        if (x >= 650 and x <= 650+100) and (y >= 670 and y <= 670+30):     
                            print_result_to_file_floyd(arr2d,trace,stop_for_print_file,start_for_print_file)
    rescreen()


def isEmptyGraph():
    if (len(listVetex) == 0):
        try:
            result = MessageBoxW(
                None, "Đồ thị của bạn đang trống", "Thông báo", MB_OKCANCEL)
            if result == IDOK:
                pass
            elif result == IDNO:
                pass
            else:
                pass
        except WindowsError as win_err:
            pass
        return True
    else:
        return False


def renameVetext(Vetex):
    global pygame
    global screen
    done = True
    reWorkingZone()
    while done:
        for event in pygame.event.get():
            name = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
                    return 2
            elif event.type == pygame.QUIT:
                if not isSaved:
                    try:
                        result = MessageBoxW(
                            None, "Bạn có muốn thoát không?", "Thông báo chưa lưu", MB_YESNO)
                        if result == IDYES:
                            fun.pygame_quit()
                        elif result == IDNO:
                            continue
                    except:
                        pass
                else:
                    fun.pygame_quit()
            for box in draw.input_boxes:
                name = box.handle_event(event)
            if (name != None):
                if fun.findNameVetext(name):
                    try:
                        result = MessageBoxW(
                            None, "Trùng tên", "Thông báo lỗi", MB_OKCANCEL)
                        if result == IDOK:
                            continue
                        elif result == IDCANCEL:
                            return 0
                        else:
                            return 0
                    except WindowsError as win_err:
                        pass
                Vetex.name = name
                reTextZone()
                done = False
                return 1
            draw.showAllVetex(screen)
            reTextZone()
            pygame.display.flip()


def printMenu():
    global pygame
    global screen
    for i in menu.Button:
        # self.rect = pygame.Rect(x, y, w, h)
        pygame.draw.rect(screen, i[1], i[0])
        textAddVetex = smallfont.render(i[2], True, textColor)
        screen.blit(textAddVetex, textAddVetex.get_rect(
            center=pygame.Rect(i[0][0], i[0][1], i[0][2], i[0][3]).center))


def isMenuchoose():
    global pygame
    (x, y) = pygame.mouse.get_pos()
    for i in range(len(menu.Button)):
        if (x >= menu.Button[i][0][0] and x <= menu.Button[i][0][0]+menu.Button[i][0][2]) and (y >= menu.Button[i][0][1] and y <= (menu.Button[i][0][1] + menu.Button[i][0][3])):
            menu.Button[i][1] = activeMenuColor
            return i
    return -1


# Quan lý screen
def reOptionZone():
    pygame.draw.rect(screen, optionZoneColor, [0, 0, 250, 500], 0)
    printMenu()
    pygame.display.flip()


def reWorkingZone():
    pygame.draw.rect(screen, workingZoneColor, [250, 0, 1280, 500], 0)
    draw.showAllVetex(screen)
    for edge in adjaGraph:
        show_edge(edge[0], edge[1], nomalLineColor, FlagHuongDoThi)
    pygame.display.flip()


def reTextZone():
    pygame.draw.rect(screen, textZoneColor, [0, 500, 1280, 720], 0)
    draw.show_labels()
    for box in draw.input_boxes:
        box.update()
    for box in draw.input_boxes:
        box.draw(screen)
    pygame.display.flip()


def rescreen():
    global adjaGraph
    global delay
    global FlagHuongDoThi
    pygame.draw.rect(screen, workingZoneColor, [250, 0, 1280, 500], 0)
    pygame.draw.rect(screen, optionZoneColor, [0, 0, 250, 500], 0)
    pygame.draw.rect(screen, textZoneColor, [0, 500, 1280, 720], 0)
    draw.Label(screen, "Tên đỉnh: ", 10, 510, 28)
    draw.Label(screen, "Nhấn Esc để thoát hoặc hủy chức năng", 10, 700, 16)
    draw.show_labels()
    draw.showAllVetex(screen)
    printMenu()
    for box in draw.input_boxes:
        box.update()
    draw.show_all_input(screen)
    for edge in adjaGraph:
        show_edge(edge[0], edge[1], nomalLineColor, FlagHuongDoThi)
    pygame.display.flip()
    FPS_CLOCK.tick(200)


def setAllMenuColor(color):
    for i in range(len(menu.Button)):
        menu.Button[i][1] = color


def loadConfigFile():
    global nomalVetexColor
    global chooseVetexColor
    global moveVetextColor
    global nomalLineColor
    global moveLineColor
    global nomalMenuColor
    global activeMenuColor
    global textColor
    global workingZoneColor
    global optionZoneColor
    global textZoneColor
    global FlagHuongDoThi
    try:
        f = open("ConfigSetting.txt", 'r')
        a = f.readlines()
        if str(a[0].rstrip()) == "2":
            FlagHuongDoThi = True
        else:
            FlagHuongDoThi = False
        nomalVetexColor = str(a[1].rstrip())
        chooseVetexColor = str(a[2].rstrip())
        moveVetextColor = str(a[3].rstrip())
        nomalLineColor = str(a[4].rstrip())
        moveLineColor = str(a[5].rstrip())
        nomalMenuColor = str(a[6].rstrip())
        activeMenuColor = str(a[7].rstrip())
        textColor = str(a[8].rstrip())
        workingZoneColor = str(a[9].rstrip())
        optionZoneColor = str(a[10].rstrip())
        textZoneColor = str(a[11].rstrip())
        f.close()
    except:
        try:
            result = MessageBoxW(
                None, "Có lỗi trong quá trình load file", "Thông báo lỗi", MB_OKCANCEL)
            if result == IDOK:
                return
            elif result == IDCANCEL:
                return
            else:
                return
        except WindowsError as win_err:
            return

# chọn nút thoát trong hướng dẫn
def helpHuongDan():
    global pygame
    (x, y) = pygame.mouse.get_pos()
    if (x >= 10 and x <= 10+100) and (y >= 10 and y <= (10 + 100)):
        pygame.draw.rect(screen, activeMenuColor, [10, 10, 100, 100])
        textAddVetex = smallfont.render("Thoát", True, textColor)
        screen.blit(textAddVetex, textAddVetex.get_rect(
            center=pygame.Rect(10, 10, 100, 100).center))
        pygame.display.flip()
        return True
    return False

if __name__ == "__main__":
    # Main
    loadConfigFile()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    FPS_CLOCK = pygame.time.Clock()
    runnning = True
    smallfont = pygame.font.SysFont('Corbel', 16)
    pygame.draw.rect(screen, textZoneColor, [0, 500, 1280, 220], 0)
    draw.Label(screen, "Tốc độ: " + str(delay), 10, 450, 16)
    rescreen()
    while runnning:
        # screen
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                tmp = isMenuchoose()
                if tmp == -1:
                    setAllMenuColor(nomalMenuColor)
                printMenu()
                pygame.display.flip()
            elif event.type == pygame.QUIT:
                if not isSaved:
                    try:
                        result = MessageBoxW(
                            None, "Bạn có muốn thoát không?", "Thông báo chưa lưu đồ thị", MB_YESNO)
                        if result == IDYES:
                            runnning = False
                        elif result == IDNO:
                            runnning = True
                    except:
                        pass
                else:
                    runnning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if delay != 1000:
                        delay += 100
                        labels.clear()
                        speed = draw.Label(screen, "Tốc độ: " +
                                        str(delay), 10, 450, 16)
                        reOptionZone()
                        speed.draw()
                        pygame.display.flip()
                elif event.key == pygame.K_DOWN:
                    if delay != 0:
                        delay -= 100
                        labels.clear()
                        speed = draw.Label(screen, "Tốc độ: " +
                                        str(delay), 10, 450, 16)
                        reOptionZone()
                        speed.draw()
                        pygame.display.flip()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    (x, y) = pygame.mouse.get_pos()
                    if isMenuchoose() == 0:
                        reOptionZone()
                        renameVetexFuntion()
                        menu.Button[0][1] = nomalMenuColor
                    elif isMenuchoose() == 1:
                        reOptionZone()
                        addEdegsFuntion()
                        menu.Button[1][1] = nomalMenuColor
                    elif isMenuchoose() == 2:
                        reOptionZone()
                        deleteVetexFuntion()
                        menu.Button[2][1] = nomalMenuColor
                    elif isMenuchoose() == 3:
                        reOptionZone()
                        moveFunciton()
                        menu.Button[3][1] = nomalMenuColor
                    elif isMenuchoose() == 4:
                        reOptionZone()
                        removeAllGraph()
                        menu.Button[4][1] = nomalMenuColor
                    elif isMenuchoose() == 5:
                        reOptionZone()
                        saveFileFuntion()
                        menu.Button[5][1] = nomalMenuColor
                    elif isMenuchoose() == 6:
                        reOptionZone()
                        if loadFileFuntion() == True:
                            isSaved = True
                        else:
                            pass
                        menu.Button[6][1] = nomalMenuColor
                    elif isMenuchoose() == 7:
                        reOptionZone()
                        if (fun.checkDijkstra() == False and FlagHuongDoThi) or (fun.checkDijkstraVoHuong() == False  and FlagHuongDoThi == False):
                            try:
                                result = MessageBoxW(
                                    None, "Có giá trị âm không thể sử dụng thuật toán này!", "Thông báo lỗi", MB_OKCANCEL)
                                if result == IDOK:
                                    menu.Button[7][1] = nomalMenuColor
                                    reOptionZone()
                                    break
                                elif result == IDCANCEL:
                                    menu.Button[7][1] = nomalMenuColor
                                    reOptionZone()
                                    break
                                else:
                                    menu.Button[7][1] = nomalMenuColor
                                    reOptionZone()
                                    break
                            except WindowsError as win_err:
                                pass
                        else:
                            Dijkstra(FlagHuongDoThi)
                            menu.Button[7][1] = nomalMenuColor
                    elif isMenuchoose() == 8:
                        reOptionZone()
                        Bellman_Ford(FlagHuongDoThi)
                        menu.Button[8][1] = nomalMenuColor
                    elif isMenuchoose() == 9:
                        reOptionZone()
                        Floyd(FlagHuongDoThi)
                        menu.Button[9][1] = nomalMenuColor
                    elif isMenuchoose() == 10:
                        (a, b, c, d, e, f, g, h, j, k, l, m) = MainCaidai.main(FlagHuongDoThi, nomalVetexColor, chooseVetexColor, moveVetextColor,
                                                                            nomalLineColor, moveLineColor, nomalMenuColor, activeMenuColor, textColor, workingZoneColor, optionZoneColor, textZoneColor)
                        thaydoi = False
                        if a == '1':
                            if FlagHuongDoThi:
                                thaydoi = True
                            FlagHuongDoThi = False
                        else:
                            if FlagHuongDoThi == False:
                                thaydoi = True
                            FlagHuongDoThi = True
                        if FlagHuongDoThi == False and thaydoi:
                            if fun.checkChyenDoiQuaVoHuong():
                                adjaGraphVoHuong.clear()
                                for edge in adjaGraph:
                                    adjaGraphVoHuong.append(
                                        [edge[0], edge[1], edge[2]])
                                    adjaGraphVoHuong.append(
                                        [edge[1], edge[0], edge[2]])
                            else:
                                try:
                                    result = MessageBoxW(
                                        None, "Có cạnh có 2 giá trị trọng số", "Thông báo lỗi", MB_OKCANCEL)
                                    if result == IDOK:
                                        FlagHuongDoThi = True
                                    elif result == IDCANCEL:
                                        FlagHuongDoThi = True
                                    else:
                                        FlagHuongDoThi = True
                                    break
                                except WindowsError as win_err:
                                    FlagHuongDoThi = True
                        if FlagHuongDoThi == True and thaydoi:
                            for edge in adjaGraph:
                                edge[2] = fun.find_edgeVoHuong(edge[0],edge[1])
                                
                        nomalVetexColor = b
                        chooseVetexColor = c
                        moveVetextColor = d
                        nomalLineColor = e
                        moveLineColor = f
                        nomalMenuColor = g
                        activeMenuColor = h
                        textColor = j
                        workingZoneColor = k
                        optionZoneColor = l
                        textZoneColor = m
                        fun.setColorAllVetex(nomalVetexColor)
                    elif isMenuchoose() == 11:
                        labels.clear()
                        done1 = True
                        screen.fill("#C0C0C0")
                        pygame.draw.rect(screen, "White", [10, 10, 100, 100])
                        textAddVetex = smallfont.render("Thoát", True, textColor)
                        screen.blit(textAddVetex, textAddVetex.get_rect(
                            center=pygame.Rect(10, 10, 100, 100).center))
                        draw.Label(
                            screen, "Tạo đỉnh chọn trong vùng làm việc(ở bên phải màn hình) và đặt tên cho đỉnh", 10, 150, 28)
                        draw.Label(
                            screen, "Các chức năng sẽ có tác như tên button", 10, 200, 28)
                        draw.Label(
                            screen, "Thay đổi tốc độ ấn phím mũi tên lên hoặc xuống", 10, 250, 28)
                        draw.Label(
                            screen, "Ý tưởng thuật toán sử dụng trên Vnoi (Nguồn: https://vnoi.info/wiki/algo/graph-theory/shortest-path.md)", 10, 300, 28)
                        draw.Label(
                            screen, "Tác giả: Hà Xuân Thanh, Nguyễn Văn Trường", 10, 350, 28)
                        draw.show_labels()
                        pygame.display.flip()
                        while done1:
                            for event in pygame.event.get():
                                tmp = helpHuongDan()
                                if tmp == False:
                                    pygame.draw.rect(screen, "White", [
                                                    10, 10, 100, 100])
                                    textAddVetex = smallfont.render(
                                        "Thoát", True, textColor)
                                    screen.blit(textAddVetex, textAddVetex.get_rect(
                                        center=pygame.Rect(10, 10, 100, 100).center))
                                    pygame.display.flip()
                                if event.type == pygame.QUIT:
                                    if not isSaved:
                                        try:
                                            result = MessageBoxW(
                                                None, "Bạn có muốn thoát không?", "Thông báo chưa lưu", MB_YESNO)
                                            if result == IDYES:
                                                fun.pygame_quit()
                                            elif result == IDNO:
                                                continue
                                        except:
                                            pass
                                    else:
                                        fun.pygame_quit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        done1 = False
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_presses = pygame.mouse.get_pressed()
                                    if mouse_presses[0]:
                                        tmp = helpHuongDan()
                                        if tmp:
                                            done1 = False

                        labels.clear()
                        draw.Label(screen, "Tốc độ: " + str(delay), 10, 450, 16)
                        rescreen()
                    if ((x >= 250 + RADIUS_VALUE) and (x <= 1280 - RADIUS_VALUE) and (y >= 0 + RADIUS_VALUE) and (y <= 500 - RADIUS_VALUE)):
                        index = fun.ischooseVetex(x, y)
                        if (index != -1):
                            try:
                                result = MessageBoxW(
                                    None, "Nơi bạn chọn đã có đỉnh", "Thông báo lỗi", MB_OKCANCEL)
                                if result == IDOK:
                                    listVetex[index].color = nomalVetexColor
                                elif result == IDCANCEL:
                                    listVetex[index].color = nomalVetexColor
                                else:
                                    listVetex[index].color = nomalVetexColor
                                break
                            except WindowsError as win_err:
                                pass
                            listVetex[index] = nomalVetexColor
                            break
                        else:
                            vetex = draw.Vetex(screen, x, y, chooseVetexColor, "")
                            listVetex.append(vetex)
                            draw.input_box1.active = True
                            draw.input_box1.color = draw.COLOR_ACTIVE
                            reTextZone()
                            vetex.color = chooseVetexColor
                            if renameVetext(vetex) == 1:
                                vetex.color = nomalVetexColor
                                isSaved = False
                            else:
                                listVetex.remove(vetex)
                    rescreen()
        for box in draw.input_boxes:
            box.handle_event(event)
        pygame.display.flip()
        FPS_CLOCK.tick(200)

    pygame.quit