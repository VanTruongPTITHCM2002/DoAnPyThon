from tkinter import *
from tkinter import ttk
import ctypes
from ctypes.wintypes import HWND, LPWSTR, UINT
WIDTH = 500
HEIGHT= 500
BACKGROUND_COLOR = "#C0C0C0"



### dialog
_user32 = ctypes.WinDLL('user32', use_last_error=True)

_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT  # default return type is c_int, this is not required
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

MB_OK = 0
MB_OKCANCEL = 1
MB_YESNOCANCEL = 3
MB_YESNO = 4

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


distColorBig = {
    "GhostWhite": "#F8F8FF",
    "White": "#FFFFFF",
    "Black": "#000000",
    "DimGray": "#696969",
    "LightGray": "#D3D3D3",
    "Gray": "#BEBEBE",
    "DarkGray": "#A9A9A9",
    "LightSlateGray": "#778899",
    "DarkSlateGray1": "#97FFFF",
    "FloralWhite": "#FFFAF0",
    "LightGoldenrodYellow": "#FAFAD2",
    "SaddleBrown": "#8B4513",
    "Peru": "#CD853F",
    "Snow3": "#CDC9C9",
    "AntiqueWhite": "#FAEBD7",
    "Bisque1": "#FFE4C4",
    "PeachPuff1": "#FFDAB9",
    "NavajoWhite1": "#FFDEAD",
    "LemonChiffon1": "#FFFACD",
    "Cornsilk1": "#FFF8DC",
    "Ivory1": "#FFFFF0",
    "MintCream": "#F5FFFA",
    "Honeydew1": "#F0FFF0",
    "LavenderBlush1": "#FFF0F5",
    "Lavender": "#E6E6FA",
    "MistyRose1": "#FFE4E1",
    "Azure1": "#F0FFFF",
    "AliceBlue": "#F0F8FF",
    "LightSlateBlue": "#8470FF",
    "MediumSlateBlue": "#7B68EE",
    "SlateBlue": "#6A5ACD",
    "DarkSlateBlue": "#483D8B",
    "RoyalBlue": "#4169E1",
    "Blue1": "#0000FF",
    "DarkBlue": "#00008B",
    "NavyBlue": "#000080",
    "MidnightBlue": "#191970",
    "CornflowerBlue": "#6495ED",
    "Mediumblue": "#0000CD",
    "PowderBlue": "#B0E0E6",
    "DodgerBlue1": "#1E90FF",
    "SteelBlue": "#4682B4",
    "DeepSkyBlue1": "#00BFFF",
    "SkyBlue": "#87CEEB",
    "LightSkyBlue": "#87CEFA",
    "LightSteelBlue": "#B0C4DE",
    "LightBlue": "#ADD8E6",
    "LightCyan1": "#E0FFFF",
    "CadetBlue": "#5F9EA0",
    "PaleTurquoise": "#AFEEEE",
    "MediumTurquoise": "#48D1CC",
    "DarkTurquoise": "#00CED1",
    "Cyan1": "#00FFFF",
    "DarkCyan": "#008B8B",
    "Aquamarine1": "#7FFFD4",
    "DarkSeaGreen": "#8FBC8F",
    "SeaGreen": "#2E8B57",
    "PaleGreen": "#98FB98",
    "SpringGreen1": "#00FF7F",
    "Green1": "#00FF00",
    "Navy": "#006400",
    "MediumSeaGreen": "#3CB371",
    "LightSeaGreen": "#20B2AA",
    "LightGreen": "#90EE90",
    "LawnGreen": "#7CFC00",
    "MediumSpringGreen": "#00FA9A",
    "GreenYellow": "#ADFF2F",
    "LimeGreen": "#32CD32",
    "YellowGreen": "#9ACD32",
    "ForestGreen": "#228B22",
    "Chartreuse1": "#7FFF00",
    "OliveDrab": "#6B8E23",
    "DarkOliveGreen": "#556B2F",
    "Khaki1": "#FFF68F",
    "LightGoldenrod": "#EEDD82",
    "LightYellow1": "#FFFFE0",
    "Yellow1": "#FFFF00",
    "Gold1": "#FFD700",
    "Goldenrod": "#DAA520",
    "DarkGoldenrod": "#B8860B",
    "RosyBrown": "#BC8F8F",
    "IndianRed": "#CD5C5C",
    "Sienna1": "#FF8247",
    "Burlywood": "#DEB887",
    "Wheat": "#F5DEB3",
    "Tan": "#D2B48C",
    "Chocolate": "#D2691E",
    "Firebrick": "#B22222",
    "Brown": "#A52A2A",
    "Salmon": "#FA8072",
    "LightSalmon1": "#FFA07A",
    "Orange1": "#FFA500",
    "DarkOrange": "#FF8C00",
    "LightCoral": "#F08080",
    "Coral": "#FF7F50",
    "Tomato1": "#FF6347",
    "OrangeRed1": "#FF4500",
    "Red1": "#FF0000",
    "DarkRed": "#8B0000",
    "Rouge": "#C60000",
    "Crimson": "#DC143C",
    "DeepPink1": "#FF1493",
    "HotPink": "#FF69B4",
    "Pink": "#FFC0CB",
    "LightPink": "#FFB6C1",
    "PaleVioletRed": "#DB7093",
    "Maroon": "#B03060",
    "VioletRed": "#D02090",
    "Magenta1": "#FF00FF",
    "DarkMagenta": "#8B008B",
    "Orchid": "#DA70D6",
    "Plum": "#DDA0DD",
    "MediumOrchid": "#BA55D3",
    "DarkOrchid": "#9932CC",
    "MediumVioletRed": "#C71585",
    "Violet": "#EE82EE",
    "DarkViolet": "#9400D3",
    "BlueViolet": "#8A2BE2",
    "Purple": "#800080",
    "MediumPurple": "#9370DB",
    "thistle": "#D8BFD8",
    "AntiqueGold": "#DDC488",
    "AgedPaper": "#ECAB53",
    "Silver": "#C0C0C0",
    "Dark Cyan": "#008080",
    "Peach-orange": "#FFCC99",
}

def findiIndexColor(color):
    index = 0
    global distColorBig
    for i in distColorBig.keys():
        if i == color:
            return index
        index = index + 1




        



ColorBig =  ('GhostWhite', 'White','Black','DimGray','LightGray','Gray','DarkGray','LightSlateGray','DarkSlateGray1','FloralWhite','LightGoldenrodYellow', 'SaddleBrown', 'Peru','Snow3', 'AntiqueWhite', 'Bisque1', 'PeachPuff1', 'NavajoWhite1', 'LemonChiffon1','Cornsilk1','Ivory1','MintCream','Honeydew1','LavenderBlush1','Lavender','MistyRose1','Azure1','AliceBlue','LightSlateBlue','MediumSlateBlue','SlateBlue','DarkSlateBlue','RoyalBlue','Blue1','DarkBlue','NavyBlue','MidnightBlue','CornflowerBlue','Mediumblue','PowderBlue','DodgerBlue1','SteelBlue','DeepSkyBlue1','SkyBlue','LightSkyBlue','LightSteelBlue','LightBlue','LightCyan1','CadetBlue','PaleTurquoise','MediumTurquoise','DarkTurquoise','Cyan1','DarkCyan','Aquamarine1','DarkSeaGreen','SeaGreen','PaleGreen','SpringGreen1','Green1','Navy','MediumSeaGreen','LightSeaGreen','LightGreen','LawnGreen','MediumSpringGreen','GreenYellow','LimeGreen','YellowGreen','ForestGreen','Chartreuse1','OliveDrab','DarkOliveGreen','Khaki1','LightGoldenrod','LightYellow1','Yellow1','Gold1','Goldenrod','DarkGoldenrod','RosyBrown','IndianRed','Sienna1','Burlywood','Wheat','Tan','Chocolate','Firebrick','Brown','Salmon','LightSalmon1','Orange1','DarkOrange','LightCoral','Coral','Tomato1','OrangeRed1','Red1','DarkRed','Rouge','Crimson','DeepPink1','HotPink','Pink','LightPink','PaleVioletRed','Maroon','VioletRed','Magenta1','DarkMagenta','Orchid','Plum','MediumOrchid','DarkOrchid','MediumVioletRed','Violet','DarkViolet','BlueViolet','Purple','MediumPurple','thistle','AntiqueGold','AgedPaper','Silver','Dark Cyan','Peach-orange')
def main(FlagHuongDoThi,nomalVetexColor,chooseVetexColor,moveVetextColor,nomalLineColor,moveLineColor,nomalMenuColor,activeMenuColor,textColor,workingZoneColor,optionZoneColor,textZoneColor):
    
    
    
    def eventClickbtnResetDefault():
        try:
            result = MessageBoxW(None,"Bạn có muốn khôi phục mặc định không","Thông báo",MB_YESNO)
            if result == IDYES:
                f = open("ConfigDefault.txt", 'r')
                a = f.readlines()
                vetexColorNomal.set(a[0].rstrip())
                vetexColorChoose.set(a[1].rstrip())
                vetexColorMove.set(a[2].rstrip())
                egdeColorNomal.set(a[3].rstrip())
                egdeColorHL.set(a[4].rstrip())
                menuColorNomal.set(a[5].rstrip())
                menuColorActive.set(a[6].rstrip())
                textColorcbx.set(a[7].rstrip())
                workingZoneColorcbx.set(a[8].rstrip())
                optionZoneColorcbx.set(a[9].rstrip())
                textZoneColorcbx.set(a[10].rstrip())
                f.close()
            elif result == IDNO:
                return
            else:
                return
        except:
            return
    
    def eventClickbtnResetCurrentColor():
        try:
            result = MessageBoxW(None,"Bạn có muốn khôi phục cài đặt hiện tại không","Thông báo",MB_YESNO)
            if result == IDYES:
                nomalMenuColor,activeMenuColor,textColor,workingZoneColor,optionZoneColor,textZoneColor
                vetexColorNomal.set(nomalVetexColor)
                vetexColorChoose.set(chooseVetexColor)
                vetexColorMove.set(moveVetextColor)
                egdeColorNomal.set(nomalLineColor)
                egdeColorHL.set(moveLineColor)
                menuColorNomal.set(nomalMenuColor)
                menuColorActive.set(activeMenuColor)
                textColorcbx.set(textColor)
                workingZoneColorcbx.set(workingZoneColor)
                optionZoneColorcbx.set(optionZoneColor)
                textZoneColorcbx.set(textZoneColor)
            elif result == IDNO:
                return
            else:
                return
        except:
            return

    
    def save():
        try:
            result = MessageBoxW(None, "Việc save này sẽ thay đổi trong hệ thông bạn chắc chứ?", "Thông Báo", MB_YESNO)
            if result == IDYES:
                f = open("ConfigSetting.txt", 'w')
                f.write(str(v.get()) + "\n")
                f.write(str(vetexColorNomalval.get()) + "\n")
                f.write(str(vetexColorChooseVal.get()) + "\n")
                f.write(str(vetexColorMoveVal.get()) + "\n")
                f.write(str(egdeColorNomalval.get()) + "\n")
                f.write(str(egdeColorHLval.get()) + "\n")
                f.write(str(menuColorNomalVal.get()) + "\n")
                f.write(str(menuColorActiveVal.get()) + "\n")
                f.write(str(textColorVal.get()) + "\n")
                f.write(str(workingZoneColorVal.get()) + "\n")
                f.write(str(optionZoneColorVal.get()) + "\n")
                f.write(str(textZoneColorVal.get()) + "\n")
                f.close()
            elif result == IDCANCEL:
                return
            else:
                return
        except WindowsError as win_err:
            return
    
    
    
    
    mainFrame = Tk()
    vetexColorNomalval = StringVar()
    vetexColorNomal = ttk.Combobox(mainFrame, width = 27, textvariable = vetexColorNomalval)
    vetexColorNomal['values'] = ColorBig
    vetexColorChooseVal = StringVar()
    vetexColorChoose = ttk.Combobox(mainFrame,width=27,textvariable = vetexColorChooseVal)
    vetexColorChoose['values'] = ColorBig
    vetexColorMoveVal = StringVar()
    vetexColorMove = ttk.Combobox(mainFrame,width=27,textvariable = vetexColorMoveVal)
    vetexColorMove['values'] = ColorBig    
    
    egdeColorNomalval = StringVar()
    egdeColorNomal = ttk.Combobox(mainFrame, width = 27, textvariable = egdeColorNomalval)
    egdeColorNomal['values'] = ColorBig
    egdeColorHLval = StringVar()
    egdeColorHL = ttk.Combobox(mainFrame,width=27,textvariable = egdeColorHLval)
    egdeColorHL['values'] = ColorBig
    
    
    menuColorNomalVal = StringVar()
    menuColorNomal = ttk.Combobox(mainFrame,width=27,textvariable = menuColorNomalVal)
    menuColorNomal['values'] = ColorBig
    
    menuColorActiveVal = StringVar()
    menuColorActive = ttk.Combobox(mainFrame,width=27,textvariable = menuColorActiveVal)
    menuColorActive['values'] = ColorBig
    
    textColorVal = StringVar()
    textColorcbx = ttk.Combobox(mainFrame,width=27,textvariable = textColorVal)
    textColorcbx['values'] = ColorBig
    
    workingZoneColorVal = StringVar()
    workingZoneColorcbx = ttk.Combobox(mainFrame,width=27,textvariable = workingZoneColorVal)
    workingZoneColorcbx['values'] = ColorBig
    
    optionZoneColorVal = StringVar()
    optionZoneColorcbx = ttk.Combobox(mainFrame,width=27,textvariable = optionZoneColorVal)
    optionZoneColorcbx['values'] = ColorBig
    
    textZoneColorVal = StringVar()
    textZoneColorcbx = ttk.Combobox(mainFrame,width=27,textvariable = textZoneColorVal)
    textZoneColorcbx['values'] = ColorBig
    
    
    vetexColorNomal.place(x = 200, y =50)
    vetexColorChoose.place(x = 200,y = 70)
    vetexColorMove.place(x = 200,y = 90)
    egdeColorNomal.place(x = 200 , y = 130)
    egdeColorHL.place(x = 200, y = 150)
    menuColorNomal.place(x = 200,y = 190)
    menuColorActive.place(x = 200,y = 210)
    textColorcbx.place(x = 200,y = 250)
    workingZoneColorcbx.place(x = 200, y = 290)
    optionZoneColorcbx.place(x = 200, y = 310)
    textZoneColorcbx.place(x = 200 , y = 330)
    
    if FlagHuongDoThi:
        v = StringVar(mainFrame, "2")
    else:
        v = StringVar(mainFrame, "1")
    rbtnVoHuong =  Radiobutton(mainFrame, text = "Vô Hướng", variable = v,value = "1").place(x = 120, y = 10)
    rbtnCoHuong =  Radiobutton(mainFrame, text = "Có Hướng", variable = v,value = "2").place(x = 240, y = 10)
    mainFrame.title("Cài đặt")
    mainFrame.geometry('500x500')
    mainFrame.resizable(FALSE, FALSE)
    lblCheDoDoThi = Label(mainFrame, text="Lựa chọn chế độ:" )
    lblCheDoDoThi.place(x = 10, y = 10)
    lblVetex = Label(mainFrame, text="Vetex:" )
    lblVetex.place(x = 10, y = 30)
    lblcolorvetexnomal = Label(mainFrame, text="Màu lúc bình thường:")
    lblcolorvetexnomal.place(x=20, y=50)
    lblcolorvetextChoose = Label(mainFrame, text="Màu lúc được chọn: " )
    lblcolorvetextChoose.place(x=20, y=70)
    lblcolorvetextMove = Label(mainFrame, text= "Màu lúc di chuyển: ")
    lblcolorvetextMove.place(x = 20, y =90)
    lblEgde = Label(mainFrame, text="Edge:" )
    lblEgde.place(x = 10, y = 110)
    lblcoloregdenomal = Label(mainFrame, text="Màu lúc bình thường: " )
    lblcoloregdenomal.place(x=20, y=130)
    lblcoloregdehightlight = Label(mainFrame, text="Màu lúc hight light: " )
    lblcoloregdehightlight.place(x=20, y=150)
    lblColorMenu = Label(mainFrame, text="Menu:" )
    lblColorMenu.place(x = 10, y = 170)
    lblColorMenuNomal = Label(mainFrame, text="Màu lúc bình thường: ")
    lblColorMenuNomal.place(x = 20,y = 190)
    lblColorMenuActive = Label(mainFrame, text = "Màu lúc hoạt động")
    lblColorMenuActive.place(x = 20,y = 210)
    lblText = Label(mainFrame, text="Text:" )
    lblText.place(x = 10,y = 230)
    lblColorText = Label(mainFrame, text="Màu Chữ: ")
    lblColorText.place(x = 20,y = 250)
    lblZone = Label(mainFrame, text="Zone")
    lblZone.place(x = 10, y = 270)
    lblworkingZoneColor = Label(mainFrame, text="Màu working zone:")
    lblworkingZoneColor.place(x = 20,y = 290)
    lbloptionZoneColor = Label(mainFrame, text="Màu option zone:")
    lbloptionZoneColor.place(x = 20, y = 310)
    lbltextZoneColor = Label(mainFrame, text="Màu text zone:")
    lbltextZoneColor.place(x=20, y = 330)
    
    ###Btn
    btnResetDefault = Button(mainFrame, text="Reset Default",foreground="Yellow", bg = "Gray",command= eventClickbtnResetDefault)
    btnResetDefault.place(x = 400, y = 400)
    
    btnResetDefault = Button(mainFrame, text="Reset Current Color",foreground="Yellow", bg = "Gray",command= eventClickbtnResetCurrentColor)
    btnResetDefault.place(x = 200, y = 400)
    
    btnResetDefault = Button(mainFrame, text="save",foreground="Yellow", bg = "Gray",command= save)
    btnResetDefault.place(x = 10, y = 400)
    
     
    vetexColorNomal.current(findiIndexColor(nomalVetexColor))
    vetexColorChoose.current(findiIndexColor(chooseVetexColor))
    vetexColorMove.current(findiIndexColor(moveVetextColor))
    egdeColorNomal.current(findiIndexColor(nomalLineColor))
    egdeColorHL.current(findiIndexColor(moveLineColor))
    
    
    menuColorNomal.current(findiIndexColor(nomalMenuColor))
    menuColorActive.current(findiIndexColor(activeMenuColor))    
    textColorcbx.current(findiIndexColor(textColor))
    
    workingZoneColorcbx.current(findiIndexColor(workingZoneColor))
    optionZoneColorcbx.current(findiIndexColor(optionZoneColor))
    textZoneColorcbx.current(findiIndexColor(textZoneColor))                  
    
    mainFrame.update()
    mainFrame.mainloop()
    return (v.get(),vetexColorNomalval.get(),vetexColorChooseVal.get(),vetexColorMoveVal.get(),egdeColorNomalval.get(),egdeColorHLval.get(),menuColorNomalVal.get(), menuColorActiveVal.get(), textColorVal.get(),workingZoneColorVal.get(),optionZoneColorVal.get(),textZoneColorVal.get())