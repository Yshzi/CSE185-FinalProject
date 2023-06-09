# Benchmarking
Multiple Sequence Alignement was inspired by `MAFFT` and so we will be benchmarking using `MAAFT`. In this directory, you will find a benchmarking fasta file that contains three protein sequences that can be used as input for benchmarking. Additionally we have included the Multiple Sequence Alignment python code so the code can be run in the same directory as the files.

## Installing `MAAFT`
First, we have to install `MAAFT`. To install `MAFFT` follow the instructions on this [website](https://mafft.cbrc.jp/alignment/software/). Ensure that you are using the correct download instructions for your operating system.

## Benchmarking 


### Windows `MAAFT`
For windows we downloaded the `All-In-One version`. After downloading the `.zip` file. We extracted its contents per the instructions from the `MAAFT` website. Then we opened the terminal with powershell, and changed the directory until we were in the `mafft-win` folder. After, we ran `MAAFT` on the `benchmark.fasta` file by using 
```
Measure-Command {.\mafft.bat <filepath to benchmark.fasta> --ep 0 --op 0}
``` 
The command `Measure-Command` is a cmdlet for powershell that allows us to see how long it take to execute the code in the curly brackets.

### MacOS `MAAFT`
For Mac we downloaded the `Standard package`. After downloading and following the installation instructions. Then we opened the terminal and ran 
```
time /usr/local/bin/mafft <filepath to benchmark.fasta>
```
`time` is command-line utility that allows us to see how long it takes to execute the code. 

### Alignment Score
The output of `MSA.py` includes an alignment score that counts the number of matches between the sequences. In order for us to measure the alignment score from `MAAFT` we redirected the output of `MAAFT` using the `>` operator and redirected the output into `.txt` files. We also modified the format of the output so that it would work with `ScoreCalculator.py`. See `Alignments` directory for specifications in format.

 For example: 

```
/usr/local/bin/mafft benchmark.fasta > example.txt
```

Now that we have the output of `MAAFT` in a `.txt` file we can use `ScoreCalculator.py` on it.
### MSA.py
Now we will benchmark `MSA.py`. Using the timing tool for your specific operating system as specified as above we will look at the runtimes for `MSA.py`. To reiterate, windows will use `Measure-Command` and mac will use `time`. Ensure that you are in the benchmarking directory in this repository.
Windows users will use:

```
Measure-Command {python3 MSA.py benchmark.fasta}
```
and mac users will use:

```
time python3 MSA.py benchmark.fasta
```

The output should be the time it took for the code to run. Now we have both the benchmark times for `MAAFT` and `MSA.py` that we can now compare.
