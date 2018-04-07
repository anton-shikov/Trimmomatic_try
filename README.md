# Trimmomatic_try
A simple trimmomatic-like script to trim fastq-files.

## Getting Started

This tool allows you to trim sequences and trimmed file as a result.

### Prerequisites

You need to install python3 with Biopython library to run this tool.

### Installing

To install this tool clone this repository to your PC.

```
~$ git clone https://github.com/anton-shikov/Trimmomatic_try.git
```

## Running and using tool

Using this tool is sa simple as its code is. After downloading repository launch terminal and enter this repository.
Use this following to execute tool:
```
~$ python Trimmomatic_try -isq test.fastq -hd 15 -tl 10 -wn 5 -th 30 -osq test_trimmed.fastq 
```
Information about flags:  
-isq input sequence fastq file  
-hd the size of headcrop (0 for default)  
-tl the size of tailcrop (0 for default)  
-wn the size of sliding clip (5 for default)  
-th  base quality thershold (0 for default)  
-osq output sequence fastq file  
Output format: trimmed sequence in fasq format  

## Author

* **Anton Shikov** - *Initial work* - [anton-shikov](https://github.com/anton-shikov)


## License

This project is free and available for everyone.

## Acknowledgments

Eugene Bakin for python course.
