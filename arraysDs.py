'''
    An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index, (where ), that can be referenced as (you may also see it written as ).

    Given an array, , of integers, print each element in reverse order as a single line of space-separated integers.

    Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    ry = [] #tampungan untuk array baru yang akan direverse
    for r in range(len(a)-1, -1, -1):   #len(a)-1 adalah batas awal iterasi
                                        #len(a)-1 artinya panjang array dikurangi 1, sehingga didapatkan index terakhir dari array
                                        # -1 adalah index ke -1 sebagai batas akhir, yg mana dalam hal ini tidak diikutsertakan ke dalam iterasi (exclude)
                                        # -1 yg terakhir adalah iterasinya, -1 artinya dia looping mundur dari index akhir ke index awal.
                                        #sehingga, jika inputnya [1,2,3,4], maka batas awal iterasinya adalah index ketiga yaitu 4
                                        #batas akhirnya adalah index -1 yaitu 4, artinya angka 4 tidak ikut serta, hanya sampai index ke 0
        ry.append(a[r]) #masukkan array a dengan index r ke dalam arrray ry
    return ry #balikin nilai ry
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()