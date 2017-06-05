import random


def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def mean2(numbers, occurrences):
    if occurrences >= len(numbers):
        return mean(numbers)
    return mean(numbers[-occurrences:])

def task_1():
    tstr = raw_input("input several numbers separated by commas ");
    return mean([float(x) for x in tstr.split(',')]);

def task_2():
    tstr = raw_input("input several numbers separated by commas ");
    occurrences = input("occurrences ");
    listOfNumbers = [float(x) for x in tstr.split(',')]
    return mean2(listOfNumbers, occurrences);

def task_3():
    r = random.randint(1, 100)
    print r
    if(r >= 1 and r <= 50):
        return "Loss";
    if(r > 50 and r < 100):
        return "Win";
    if(r == 100):
        return "Draw";


def task_4():
    pass

def task_5():
    pass

