import math
import time

class Generator():
    def __init__(self, current_time=time.time(), multiplier=1664525, increment=1013904223, modulus=math.pow(2, 32)):
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.current_time = current_time

    def lcg(self):
        self.current_time = int(self.increment + self.current_time * self.multiplier) % self.modulus
        value = 0
        value = self.current_time / self.modulus
        return value

    def lcg_to_range(self,min,max):
        lcg = self.lcg()
        value = min + lcg * (max-min)
        return value

if __name__ == "__main__":
    obj = Generator()
    left_list = []
    right_list = []
    final_list = []
    low = int(input("Enter Lower value of range\n"))
    high =int(input("Enter Upper value of range\n"))
    mid_val = (low + high) / 2
    while len(right_list) != 73:
        val = int(obj.lcg_to_range(mid_val+1, high+1))
        right_list.append(val)
        continue
    while len(left_list) != 27:
        val = int(obj.lcg_to_range(low,mid_val-1))
        left_list.append(val)
        continue

    print("Number of values in right_list :" + str(len(right_list)))
    print(right_list)
    print("Number of values in left_list :" + str(len(left_list)))
    print(left_list)
    final_list = left_list+right_list
    print("Final list: ")
    print(final_list)