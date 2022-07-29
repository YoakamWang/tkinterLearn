from tkinter import *


def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w


class Calculator(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calc1")
        display = StringVar()
        Entry(self, relief=SUNKEN,
              textvariable=display).pack(side=TOP, expand=YES,
                                         fill=BOTH)

        for key in ("123", "456", "789", "-0."):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char,
                       lambda w=display, s=' %s ' % char: w.set(w.get() + s))
        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char,
                             lambda w=display, c=char: w.set(w.get() + ' ' + c + ' '))
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except ValueError:
            display.set("ERROR")


if __name__ == '__main__':
    Calculator().mainloop()

# from tkinter import *
# root = Tk()
# root.title('Simple Plot - Version 1')
#
# canvas = Canvas(root, width=450, height=300, bg = 'white')
# canvas.pack()
# Button(root, text='Quit', command=root.quit).pack()
# canvas.create_line(100,250,400,250, width=2)
# canvas.create_line(100,250,100,50, width=2)
# for i in range(11):
#     x = 100 + (i * 30)
#     canvas.create_line(x,250,x,245, width=2)
#     canvas.create_text(x,254, text='%d'% (10*i), anchor=N)
# for i in range(6):
#     y = 250 - (i * 40)
#     canvas.create_line(100,y,105,y, width=2)
#     canvas.create_text(96,y, text='%5.1f'% (50.*i), anchor=E)
# for x,y in [(12, 56), (20, 94), (33, 98), (45, 120), (61, 180),
# (75, 160), (98, 223)]:
#     x = 100 + 3*x
#     y = 250 - (4*y)/5
#     canvas.create_oval(x-6,y-6,x+6,y+6, width=1,
#     outline='black', fill='SkyBlue2')
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# # # 设置主窗口区的背景颜色以区别画布区的颜色
# root.config(bg='#8DB6CD')
# root.title("test")
# #root.geometry('500x300')
# #root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# # # 将画布设置为白色
# cv = Canvas(root,width=2200,height=1500, bg='white')
# # # tkinter 提供的内置位图名称
# # bitmaps = ["error", "gray75", "gray50", "gray25", "gray12",
# #            "hourglass", "info", "questhead", "question", "warning"]
# # # 列出所有的位图样式
# # for i in range(len(bitmaps)):
# #     # 前两个参数指定一个位图的位置，后续依次排列
# #     cv.create_bitmap((i + 1) * 30, 30, bitmap=bitmaps[i])
# # 并在画布上添加文本
# # 参数说明，前两个参数（x0，y0）参照点，指定文字字符串的左上角坐标
# # anchor 指定了文本的对于参照点的相对位置，以方位来指定,比如 W/E/N/S等
# #cv.create_text(30, 80, text="tkinter内置位图预览", fill='#7CCD7C', anchor=W, font=('微软雅黑', 15, 'bold'))
# # 展示图片，使用 PhotoImage()来加载图片
# img = PhotoImage(file="office.pgm")
# cv.create_image(10,510,image=img, anchor=W)
# #cv.create_text(30, 220, text="图片预览", fill='#7CCD7C', anchor=W, font=('微软雅黑', 15, 'bold'))
# cv.pack()
# mainloop()
