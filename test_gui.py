import tkinter as tk
from test import *
from tkinter.filedialog import askopenfilename


root = tk.Tk()

glob_lable = tk.Label(root, text=None)

root.title('KODE')
root.geometry('1000x500+500+200')
root.minsize(300, 400)

root.columnconfigure(0, minsize=5)
root.columnconfigure(1, minsize=30)
root.columnconfigure(2, minsize=30)
root.columnconfigure(3, minsize=10)
root.columnconfigure(4, minsize=10)
root.columnconfigure(5, minsize=10)
root.columnconfigure(6, minsize=10)

lable = tk.Label(root, text='Тестовое задание', 
                 font=('Arial', 20, 'bold'),
                 padx=10
                 ).grid(row=0, column=3)


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
    tk.Label(root, text='Имя объекта X Y Тип обекта Время создания').grid(row=4, column=3)
    glob_lable.config(text=text)
    glob_lable.grid(row=14, column=3, rowspan=100)
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
        glob_lable.grid(row=14, column=3, rowspan=100)
    except:
        glob_lable.config(text="Введите валидные данные (Например 12.22)")
        glob_lable.grid(row=14, column=3, rowspan=100)

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
    glob_lable.grid(row=14, column=3, rowspan=100)


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
    glob_lable.grid(row=14, column=3)


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
    glob_lable.grid(row=14, column=3)


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
    glob_lable.grid(row=14, column=3)


def saveResult():
    global glob_lable
    file = askopenfilename(filetypes=[('TXT', '*.txt')], title="Выберите файл...")
    save(glob_lable.cget("text"), file)


lable_name = tk.Label(root, text='Имя объекта').grid(row=20, column=0)
name = tk.Entry(root)
name.grid(row=20, column=1)

lable_x = tk.Label(root, text='Координата X').grid(row=21, column=0)
x = tk.Entry(root)
x.grid(row=21, column=1)

lable_y = tk.Label(root, text='Координата Y').grid(row=22, column=0)
y = tk.Entry(root)
y.grid(row=22, column=1)

lable_type = tk.Label(root, text='Тип объекта').grid(row=23, column=0)
type = tk.Entry(root)
type.grid(row=23, column=1)

lable_submit = tk.Button(root, text='Добавить объект', command=submit).grid(row=24, column=1)

btn_group_dist = tk.Button(root,
                text='Сгруппировать по расстоянию',
                command=groupDist,
                width=25
                ).grid(row=20, column=6, sticky='e')

btn_group_name = tk.Button(root,
                text='Сгруппировать по имени',
                command=groupName,
                width=25
                ).grid(row=21, column=6, sticky='e')

btn_group_time = tk.Button(root,
                text='Сгруппировать по времени',
                command=groupTime,
                width=25
                ).grid(row=22, column=6, sticky='e')

btn_group_type = tk.Button(root,
                text='Сгруппировать по типу',
                command=groupType,
                width=25
                ).grid(row=23, column=6, sticky='e')

btn_save = tk.Button(root,
                text='Сохранить результаты в файл',
                command=saveResult,
                width=25
                ).grid(row=24, column=6, sticky='e')
    

root.mainloop()