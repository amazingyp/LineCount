import tkinter as tk
import function
from tkinter import filedialog

window = tk.Tk()
window.title('字符统计')
window.geometry('800x500')

# 打开文件按钮
paths = []


def selectPath():
    paths.clear()
    filenames = filedialog.askopenfilenames()
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0, len(filenames)):
            string_filename += str(filenames[i]) + "\n"
            paths.append(str(filenames[i]))
        filelable.config(text="您选择的文件是：" + string_filename)
    else:
        filelable.config(text="您没有选择任何文件");


tk.Button(window, text="选择一组文件", font=('Arial', 12), command=selectPath).pack()
filelable = tk.Label(window, text='')
filelable.pack()
# 功能选择
fun = 4


def one_selection():
    global fun
    fun = var.get()


var = tk.IntVar()
r1 = tk.Radiobutton(window, variable=var, text='字符数', value=0, command=one_selection)
r1.pack()
r2 = tk.Radiobutton(window, variable=var, text='词数', value=1, command=one_selection)
r2.pack()
r3 = tk.Radiobutton(window, variable=var, text='行数', value=2, command=one_selection)
r3.pack()
r4 = tk.Radiobutton(window, variable=var, text='特殊数据', value=3, command=one_selection)
r4.pack()


# 计算结果
def count():
    result = ''
    if fun == 0:
        for file in paths:
            result += function.printCharNumber(file)
            result += '\n'
    elif fun == 1:
        for file in paths:
            result += function.printWordNumber(file)
            result += '\n'
    elif fun == 2:
        for file in paths:
            result += function.printLineNumber(file)
            result += '\n'
    elif fun == 3:
        for file in paths:
            result += function.printSpecialLine(file)
            result += '\n'
    else:
        resultlable.config(text="请选择功能")
        return
    resultlable.config(text=result)


tk.Button(window, text="确认", font=('Arial', 12), command=count).pack()
resultlable = tk.Label(window, text='')
resultlable.pack()

def showWindow():
    window.mainloop()
