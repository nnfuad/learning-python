# built-in funtions
print(int("34")+34)
# print is printing(bin func) int is type casting(bin func...:))

#####MODULE funtions....

 # when in a file we save familiar types of variables and funtions thats a module(eg. java.util.Scanner)....#accor. to java
 
import math

print(dir(math))
#print(sqrt(256))    # wouldnt work cuz we havent imported the dir...
from math import sqrt
from math import * ## THIs * imports everything....
print(sqrt(256))

print()











# dont see anything below.....Ignore it
import torch
import pandas as pd
import numpy as np
print()
print("Running Pytorch "+torch.__version__)
scalar = torch.tensor(12)
print(scalar)

