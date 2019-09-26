import itertools
import sys
import time
import os
from tqdm.auto import tqdm  # pip install tqdm

os.system('clear')

'''
########################################################################
####### Wordlist Generator : Compitable For All Operating Systems ######
########################################################################
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# usages Example:>>
#        Please enter here all characters for combination :>> ABCabc123';./
#        Please enter here lengh of words :>> 4
#        Please enter here sequental character exclution:>> 2
#        Please enter here name of Wordlist :>> pass.txt
# **********************************************************************
# **********************************************************************
'''

chrs = input("\n[+] Enter Here All Characters For Combination :> ")

l = int(input("\n[+] Enter Minimum Lenth Of Words  :>  "))
k = l
j = int(input("\n[+] Enter Maximum Lenth Of Words  :>  "))
n = j + 1

# Number that is enterd is include.
# (ex: 2 means AA, AAA, AAAA, AAAAA, etc are exclude in you file)
v = int(input("\n[+] Enter Sequential Charachter Exclution :> "))

## This function (just to come up with the right number for the progress bar despite input given by the user)
## should be a generator expression with the right math equations to calculate that number on the fly.
## That way it won't store anything on the memory of the computer

def tline(chrs, k, n, v):
    ''' NOW ADD THE MATH FOR THE EXCLUTION (J)'''
    tline = []
    for line in range(k, n):
        if k == j:  # <--
            # This line DOES give the correct number if k and j are equal!
            tline.append(line**len(chrs))
        else: # <--
            # This line doesn't give the correct number.
            tline.append((line**len(chrs)) - ((k - line)**len(chrs)))
            # tline.append(len(chrs)**(((int(chrs[:n])) + 1) - line))
        
    return(sum(tline))


if k == j:
    tline=tline(chrs, k, n, v)
    print('\n\nThis number IS correct for "total=tline" in TQDM.\ntline =', tline, "You'll see the progress bar now.")
else:
    tline=tline(chrs, k, n, v)
    print('\n\nThis number is NOT correct for "total=tline" in TQDM.\ntline =', tline, "You'll NOT see the progress bar now.")


zt=input("\n[+] Enter Name Of Wordlist File :> ")


input('\n\n[+] Are You Ready ?\t[Press Enter]')


print('\n\n++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++\n\n')

# tline should might be a factorial mathematical equation.
# tline = int(tline(k, n, chrs, v))

time1=time.asctime()
start=time.time()

loop=tqdm(total=tline, position=0)

psd=open(zt, 'a')
for i in range(k, n):
    r=i * 100 / n
    l=str(r) + ' percent '

    for xs in itertools.product(chrs, repeat=i):
        if v > 0:
            cnts=[sum(1 for i in grp[1])
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
end=time.time()
print('\t [+] Process Completed                    :   ', time.asctime())
totaltime=end - start
print('\t [+] Total Time Consumed                  :   ', totaltime, 'second')
rate=tline / totaltime
print('\t [+] Rate Of Words Generating Per Seconds :   ', rate)

print('\n+++++++++++++++++++++++++ Please Wait +++++++++++++++++++++++++\n')


print('''
\t***************************************************
\t*       Successfully created thanks for using     *
\t***************************************************

''')
print('\n')
input("[*] Press Enter For Exit")
