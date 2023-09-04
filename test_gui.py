import tkinter as tk
from test import *
from tkinter.filedialog import askopenfilename


root = tk.Tk()

glob_lable = tk.Label(root, text=None)

root.title('KODE')
root.geometry('1000x700+500+200')
root.minsize(300, 400)

root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=10)
root.columnconfigure(2, minsize=10)
root.columnconfigure(3, minsize=10)
root.columnconfigure(4, minsize=300)
root.columnconfigure(5, minsize=10)
root.columnconfigure(6, minsize=10)

lable = tk.Label(root, text='Тестовое задание', 
                 font=('Arial', 20, 'bold'),
                 padx=10
                 ).grid(row=0, column=4)


def getFileName():
    fileName = askopenfilename(filetypes=[('TXT', '*.txt')], title="Выберите файл...")
    return fileName

fileName = getFileName()

def printObjects(fileName):
    global glob_lable
    glob_lable.config(text='')
    text = ''
    objects = readObjects(fileName)
    for object in objects:
        text = text + f"{object}\n"
    # text = [f'{object}\n'for object in objects]
    tk.Label(root, text='Имя объекта X Y Тип обекта Время создания').grid(row=11, column=4)
    glob_lable.config(text=text)
    glob_lable.grid(row=14, column=4, rowspan=100)
    return objects

objects = printObjects(fileName)

def submit():
    global glob_lable
    global objects
    sub_name = name.get()
    sub_x = x.get()
    sub_y = y.get()
    sub_type = type.get()
    text = ''
    try:
        objects.append(MyObject(sub_name, sub_x, sub_y, sub_type))
        for object in objects:
            text = text + f"{object}\n"
        glob_lable.config(text=text)
        glob_lable.grid(row=14, column=4, rowspan=100)
    except:
        tk.Label(root, text="Введите валидные координаты (Например 12.11)").grid(row=15, column=0)


def groupDist():
    global glob_lable
    global objects
    text = ''
    grp = groupByDistance(objects)
    for k, v in grp.items():
        text = text + "{}:\n".format(k)
        for val in v:
            text = text + "{}\n".format(val)
    glob_lable.config(text=text)
    glob_lable.grid(row=14, column=4, rowspan=100)


def groupName():
    global glob_lable
    global objects
    text = ''
    grp = groupByName(objects)
    for k, v in grp.items():
        text = text + "{}:\n".format(k)
        for val in v:
            text = text + "{}\n".format(val)
    glob_lable.config(text=text)
    glob_lable.grid(row=14, column=4, rowspan=100)


def groupTime():
    global glob_lable
    global objects
    text = ''
    grp = groupByTime(objects)
    for k, v in grp.items():
        text = text + "{}:\n".format(k)
        for val in v:
            text = text + "{}\n".format(val)
    glob_lable.config(text=text)
    glob_lable.grid(row=14, column=4, rowspan=100)


def groupType():
    global glob_lable
    global objects
    text = ''
    grp = groupByType(objects, 2)
    for k, v in grp.items():
        text = text + "{}:\n".format(k)
        for val in v:
            text = text + "{}\n".format(val)
    glob_lable.config(text=text)
    glob_lable.grid(row=14, column=4, rowspan=100)


def saveResult():
    global glob_lable
    file = askopenfilename(filetypes=[('TXT', '*.txt')], title="Выберите файл...")
    save(glob_lable.cget("text"), file)

lable_add = tk.Label(root,
                    text='Добавить объект в список').grid(row=2, column=0)

lable_name = tk.Label(root, text='Имя объекта').grid(row=10, column=0, sticky='nwse')
name = tk.Entry(root)
name.grid(row=10, column=1)

lable_x = tk.Label(root, text='Координата X').grid(row=11, column=0)
x = tk.Entry(root)
x.grid(row=11, column=1)

lable_y = tk.Label(root, text='Координата Y').grid(row=12, column=0)
y = tk.Entry(root)
y.grid(row=12, column=1)

lable_type = tk.Label(root, text='Тип объекта').grid(row=13, column=0)
type = tk.Entry(root)
type.grid(row=13, column=1)

lable_submit = tk.Button(root, text='Добавить', command=submit).grid(row=14, column=0)

btn_group_dist = tk.Button(root,
                text='Сгруппировать по расстоянию',
                command=groupDist
                ).grid(row=20, column=0)

btn_group_name = tk.Button(root,
                text='Сгруппировать по имени',
                command=groupName
                ).grid(row=21, column=0)

btn_group_time = tk.Button(root,
                text='Сгруппировать по времени',
                command=groupTime
                ).grid(row=22, column=0)

btn_group_type = tk.Button(root,
                text='Сгруппировать по типу объекта',
                command=groupType
                ).grid(row=23, column=0)

btn_save = tk.Button(root,
                text='Сохранить результаты в файл',
                command=saveResult
                ).grid(row=24, column=0)
    

root.mainloop()