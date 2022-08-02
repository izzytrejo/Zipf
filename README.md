# Zipf
A project to test Zipf's law in quantum linguistics. Why would we need to test for Zipf's law? How is it used in everyday life? Do certain languages follow his law better than others?


## Installation
Make a copy of this repository (go to the green button at the top right that says code). 

```
pip install -e
```
## Folders
This project is divided into five folders:

    zipf: contains the main module code that runs the analysis
    scripts: contains scripts to glue the module code
    data: contains the text for the analysis
    results: will contain the output of the analysis


## Running the code

The simplest run might look like this:

```
cd scripts
python3 run_analysis.py --in_folder ../data --out_folder .
```
## Data sets
I've already added the texts needed for this project in the data folder. These are the books I used from Project Gutenberg (https://www.gutenberg.org/):

Latin Iliad: https://www.gutenberg.org/files/52692/52692-0.txt
Latin Odyssey: https://www.gutenberg.org/files/52693/52693-0.txt
Spanish Odyssey: https://www.gutenberg.org/files/58221/58221-0.txt
Spanish Iliad: https://www.gutenberg.org/files/57654/57654-0.txt
French Odyssey: https://www.gutenberg.org/files/52927/52927-0.txt
French Iliad: https://www.gutenberg.org/cache/epub/14285/pg14285.txt
Greek Iliad: https://www.gutenberg.org/files/36248/36248-0.txt
English Odyssey: https://www.gutenberg.org/cache/epub/1727/pg1727.txt
English Iliad: https://www.gutenberg.org/cache/epub/6130/pg6130.txt
