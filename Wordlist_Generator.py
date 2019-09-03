import itertools
import sys
import time

 # pip install tqdm
from tqdm.auto import tqdm

info = '''

######################################################
                By S.S.B Group
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.in/

    Note: We Feel Proud To Be Indian
######################################################

#######################################################################
# High Speed Wordlist Generator : Compitable To All Operating Systems #
#######################################################################
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
usages Example:>>
        Please enter here all characters for combination :>> ABCabc123';./
        Please enter here lengh of words :>> 4
        Please enter here sequental character exclution:>> 2
        Please enter here name of Wordlist :>> pass.txt
**********************************************************************
**********************************************************************
'''

chrs = input("\n[+] Please Enter Here All Characters For Combination :> ")

l = int(input("\n[+] Please Enter Minimum Lenth Of Words  :>  "))
k = l
j = int(input("\n[+] Please Enter Maximum Lenth Of Words  :>  "))
n = j + 1
v = int(input("\n[+] Please Enter Sequential Charachter Exclution :> "))

zt = input("\n[+] Please Enter Name Of Wordlist File :> ")

# This function is 'quick fix' to find out the correct iterations of tline
def tline(k, n, chrs, v):
  """ Returns the correct tline number. Including 'exclude sequental characters'."""
    tline = 0
    for i in range(k, n):
        for xs in itertools.product(chrs, repeat=i):
            if v > 0:
                cnts = [sum(1 for i in grp[1])
                        for grp in itertools.groupby(xs)]
                if max(cnts) >= v:
                    continue
                tline += 1
            else:
                tline += 1
    return tline


input('\n\n[+] Are You Ready ?\t[Press Enter]')


print('\n\n++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++\n\n')


time1 = time.asctime()
start = time.time()

# If tline function needs to iterate over a lot of iterations, this will take a while ...
loop = tqdm(total=tline(k, n, chrs, v), position=0)

psd = open(zt, 'a')
for i in range(k, n):
    r = i * 100 / n
    l = str(r) + ' percent '

    for xs in itertools.product(chrs, repeat=i):
        if v > 0:
            cnts = [sum(1 for i in grp[1])
                    for grp in itertools.groupby(xs)]
            if max(cnts) >= v:
                continue
            loop.update()
            psd.write(''.join(xs) + '\n')
        else:
            loop.update()
            psd.write(''.join(xs) + '\n')
psd.close()
loop.close()

sys.stdout.write("\r\n\tDone Sucessfully")


print('\n\n++++++++++++++++++++++++ Process Report ++++++++++++++++++++++++\n')

print('\t [+] Process Started                      :   ', time1)
end = time.time()
print('\t [+] Process Completed                    :   ', time.asctime())
totaltime = end - start
print('\t [+] Total Time Consumed                  :   ', totaltime, 'second')
rate = tline(k, n, chrs, v) / totaltime
print('\t [+] Rate Of Words Generating Per Seconds :   ', rate)

print('\n+++++++++++++++++++++++++ Please Wait +++++++++++++++++++++++++\n')


print('''
\t***************************************************
\t*       Successfully created thanks for using     *
\t***************************************************

''')
print('\n')
input("[*] Press Enter For Exit")
