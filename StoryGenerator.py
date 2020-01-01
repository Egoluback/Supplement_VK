from const import *

import requests, json, random, sys

class StoryGenerator:
    def __init__(self, start, mode = "default", countIter = 10):
        self.start = start
        self.mode = mode
        self.countIter = countIter

        if (self.mode == "g_onyourown"):
            self.start = self.readDataSet()
    
    def readDataSet(self):
        result = ""
        with open(random.choice(DATASETS), "r", encoding="utf-8") as file:
            text = file.readlines()
            print("text", len(text))
            while result == "" or len(result) < 20:
                result = random.choice(text)
        
        print(result)
        
        return result
        
    
    def load(self):
        with open("result.txt", "r") as file:
            data = file.readlines()
            if (len(data) > 0):
                self.start = data[0]
                print(self.start)

    def join(self, arr):
        if (len(arr) <= 10):
            return ''.join(arr)
        else:
            return ''.join(arr[len(arr) - 10 : len(arr)])
    
    def Generate(self):
        result_arr = [self.start]

        for i in range(self.countIter):
            print("iteration " + str(i))
            continue_str = get_sample(self.join(result_arr))
            result_arr.append(continue_str)

        return ''.join(result_arr)


if __name__ == "__main__":
    countIter = 5
    start = "Жил да был"

    isLoad = False

    for i in range(len(sys.argv)):
        if (i == 1):
            if (sys.argv[i] == "y"):
                isLoad = True
        elif (i == 2):
            countIter = sys.argv[i]
        elif (i == 3):
            start = ' '.join(sys.argv[i].split("-"))
        
    
    storyGenerator = StoryGenerator(start, int(countIter))
    if (isLoad): storyGenerator.load()

    print("let's get started...")
    with open("result.txt", "w") as file:
        file.write(storyGenerator.Generate())
    
