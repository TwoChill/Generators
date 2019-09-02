# Word_List_Generator
A wordlist generator. (For pentesting purposes)


## Getting Started

* run ``` git clone http:// ***.git ```

# Wordlist Generator

* Run ``` (YOUR PATCH)/ *** .py

Instructions on how to use the wordlist script

```
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
```

### Prerequisites

Progress bar module named: TQDM

### Installing

* Run ``` pip install tqdm ``` to install the module.


## Using the generator

1. Enter here all characters for combination:
```
[+] Please Enter Here All Characters For Combination :> qwerty
```

2. Enter here min/max lengh of words:
```
[+] Please Enter Minimum Lenth Of Words  :>  2

[+] Please Enter Maximum Lenth Of Words  :>  6
```

3. Enter here sequental character exclution

(If you want to skip lines with certain sequental characters in them)
```
[+] Please Enter Sequential Charachter Exclution :> 3
```
Example:
```
1. ('q','q','q','q') = 4 sequental characters --> EXCLUDED 
2. ('q','q','q','w') = 3 sequental characters --> EXCLUDED
3. ('q','q','q','e') = 3 sequental characters --> EXCLUDED
4. ('q','q','q','r') = 3 sequental characters --> EXCLUDED
5. ('q','q','w','q') = 2 sequental characters
6. ('q','q','w','w') = 2 sequental characters
7. ('q','q','w','e') = 2 sequental characters
8. ('q','q','w','r') = 2 sequental characters
```

4.Enter path and filename of wordlist file (Incl. your file extention)
```
[+] Please Enter Name Of Wordlist File :> test.txt
```

5. Press Enter/Return to start the generator
```
[+] Numbers Of Total Lines :  50826


[+] Are You Ready ?	[Press Enter]
```

6. ```++++++++++++++++++++++++ Please Wait ++++++++++++++++++++++++


100%|█████████████████████████████████| 50826/50826 [00:00<00:00, 109521.63it/s]

	Done Sucessfully

++++++++++++++++++++++++ Process Report ++++++++++++++++++++++++

	 [+] Process Started                      :    Mon Sep  2 15:02:41 2019
	 [+] Process Completed                    :    Mon Sep  2 15:02:42 2019
	 [+] Total Time Consumed                  :    0.7232437133789062 second
	 [+] Rate Of Words Generating Per Seconds :    70275.06642615273

+++++++++++++++++++++++++ Please Wait +++++++++++++++++++++++++


	***************************************************
	*       Successfully created thanks for using     *
	***************************************************




[*] Press Enter For Exit
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
