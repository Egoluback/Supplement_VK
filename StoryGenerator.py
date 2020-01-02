from const import *

import requests, json, random, sys

class StoryGenerator:
    def __init__(self, start, mode = "default", countIter = 10):
        self.start = start
        self.mode = mode
        self.countIter = countIter

        if (self.mode == "g_onyourown"):
            self.start = -1
            data = self.readDataset()
            if (data):
                self.start = data
    
    def readDataset(self):
        result = ""
        with open(random.choice(DATASETS), "r", encoding="utf-8") as file:
            try:
                text = file.readlines()
            except:
                return False
            while result == "" or len(result) < 20:
                result = random.choice(text)
        
        print(result)
        
        return result.rstrip()
        
    
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
        if (self.start == -1): return
        result_arr = [self.start]

        for i in range(self.countIter):
            print("iteration " + str(i))
            continue_str = get_sample(self.join(result_arr))
            result_arr.append(continue_str)

        return ''.join(result_arr)