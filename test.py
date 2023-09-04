import time
import math
import re

class MyObject:

    def __init__(self, name:str, x:float, y:float, obj_type:str, obj_time=time.time()):

        self.name = str(name)
        try:
            float(x)
        except:
            raise Exception
        self.x = x

        try:
            float(y)
        except:
            raise Exception
        self.y = y
        self.obj_type = str(obj_type)
        self.obj_time = f"{float(obj_time):.5f}"

    def __str__(self):
        return f'{self.name} {self.x} {self.y} {self.obj_type} {self.obj_time}'
    
    def __repr__(self):
        return f'{self.name} {self.x} {self.y} {self.obj_type} {self.obj_time}'
            

def sort_dist(value: str):
    _, x, y, _, _ = value.split(' ')
    return math.sqrt(float(x)**2 + float(y)**2)


def groupByDistance(toGroup: list):
    distanceGroups = {
        'До 100 ед.': [],
        'До 1000 ед.': [],
        'До 10000 ед.': [],
        'Слишком далеко': [],
    }

    for element in toGroup:
        x = float(element.x)
        y = float(element.y)
        distance = math.sqrt(x**2 + y**2)

        if distance <= 99:
            distanceGroups['До 100 ед.'].append(str(element))
        elif distance <= 999:
            distanceGroups['До 1000 ед.'].append(str(element))
        elif distance <= 9999:
            distanceGroups['До 10000 ед.'].append(str(element))
        else:
            distanceGroups['Слишком далеко'].append(str(element))
        
    for key in distanceGroups:
        distanceGroups[key].sort(key=sort_dist)

    return distanceGroups


def groupByName(toGroup: list):
    alpha = r'^[А-Яа-я].*'
    alphaGroups = {
        '#': [],
        }

    for element in toGroup:
        if re.match(alpha, element.name):
            first_letter = element.name[0].upper()
            if first_letter in alphaGroups:
                alphaGroups[first_letter].append(str(element))
            else:
                alphaGroups[first_letter] = [str(element)]
        else:
            alphaGroups['#'].append(str(element))
        
        for key in alphaGroups:
            alphaGroups[key].sort(key=lambda x: x.split()[0])
    return alphaGroups

def groupByTime(toGroup: list):
    timeGroups = {
        'Сегодня': [],
        'Вчера': [],
        'На этой неделе': [],
        'В этом месяце': [],
        'В этом году': [],
        'Раннее': [],
    }

    # Время в секундах для каждой группы
    one_day = 24 * 60 * 60
    one_week = 7 * one_day
    one_month = 30 * one_day
    one_year = 365 * one_day

    timestamp = time.time()
    currentTime = f"{timestamp:.5f}"

    for element in toGroup:
        elem_time = element.obj_time
        diff = float(currentTime) - float(elem_time)

        if diff<one_day:
            timeGroups['Сегодня'].append(str(element))
        elif diff<2*one_day:
            timeGroups['Вчера'].append(str(element))
        elif diff<one_week:
            timeGroups['На этой неделе'].append(str(element))
        elif diff<one_month:
            timeGroups['В этом месяце'].append(str(element))
        elif diff<one_year:
            timeGroups['В этом году'].append(str(element))
        else:
            timeGroups['Ранее'].append(str(element))
    for key in timeGroups:
        timeGroups[key].sort(key=lambda x: x.split()[4])
    return timeGroups

def groupByType(toGroup:list, n:int):
    groups = {}
    typeGroups = {}
    sundry = []

    for element in toGroup:
        if element.obj_type in groups:
            groups[element.obj_type].append(str(element))
        else:
            groups[element.obj_type] = [str(element)]
        
    sorted_groups = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
    for obj_type, obj_names in sorted_groups:
        if len(obj_names) >= n:
            typeGroups[obj_type] = obj_names
        else:
            sundry.extend(obj_names)

    if sundry:
        typeGroups['Разное'] = sundry

    for key in typeGroups:
        typeGroups[key].sort(key=lambda x: x.split()[0])
    return typeGroups
    
def readObjects(fileName):
    objects = []
    with open(fileName, 'r') as file:
        for line in file:
            prop_list = []
            prop_list = line.strip().split()
            obj = MyObject(*prop_list)
            objects.append(obj)
    return objects

def save(objects, file):
    with open(file, 'w') as f:
        f.write(objects)