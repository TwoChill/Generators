# Wordlist Generator
## I'm Stuck

The maximum number (tline) of TQDM should be correctly calculated no matter what input is given into this generator.

The function on line 35 -46 should be replaced by a "simple" mathmatical equation which has been explained [here on reddit](https://www.reddit.com/r/askmath/comments/cslrbd/im_trying_to_find_an_equation_where_i_can_exclude/exfnpmk?utm_source=share&utm_medium=web2x).

What makes this equation hard is the *sequential excusion rule* I buildt in this verion of Suraj Singh original word generator.



## Getting Started

Get the file by cloning the repro:
* Run ``` git clone http://https://github.com/MdeFrance/Generators.git ```


# Wordlist Generator

To run the script:
* Run ```(YOUR PATCH)/Wordlist_generator.py```


### Prerequisites

Progress bar module named: TQDM


### Installing
To install the progress bar module (TQDM)
* Run ``` pip install tqdm ``` 


## Using the generator

1.
Enter here all characters for combination:
```
[+] Please Enter Here All Characters For Combination :> qwerty
```

2.
Enter here min/max lengh of words:
```
[+] Please Enter Minimum Lenth Of Words  :>  2

[+] Please Enter Maximum Lenth Of Words  :>  6
```

3.
Enter here sequental character exclution:
```
[+] Please Enter Sequential Charachter Exclution :> 3
```
Example:
```
1. ('q','q','q','q') = 4 sequental characters --> EXCLUDED and SKIPED
2. ('q','q','q','w') = 3 sequental characters --> EXCLUDED and SKIPED
3. ('q','q','q','e') = 3 sequental characters --> EXCLUDED and SKIPED
4. ('q','q','q','r') = 3 sequental characters --> EXCLUDED and SKIPED
5. ('q','q','w','q') = 2 sequental characters
6. ('q','q','w','w') = 2 sequental characters
7. ('q','q','w','e') = 2 sequental characters
8. ('q','q','w','r') = 2 sequental characters
```

4.
Enter path and filename of wordlist file (Incl. your file extention)
```
[+] Please Enter Name Of Wordlist File :> test.txt
```

5.
Press Enter/Return to start the generator
```
[+] Numbers Of Total Lines :  50826


[+] Are You Ready ?	[Press Enter]
```

6. 
```
100%|█████████████████████████████████| 50826/50826 [00:00<00:00, 109521.63it/s]

	Done Sucessfully

	***************************************************
	*       Successfully created thanks for using     *
	***************************************************
```

## Built With

* [Python]


## Author

* **MdeFrance** * - *Initial work* - [MdeFrance](https://github.com/MdeFrance) // [TwoChill](https://github.com/TwoChill)

## Acknowledgments

### Original code and creator:

* **Suraj Singh** - *Initial work* - [Suraj Singh](http://bitforestinfo.blogspot.in/) 

