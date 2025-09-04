################################### Synopsis

Bootstrapping is a powerful and useful method of error estimation and propagation.
The principal idea was introduced by Efron.
(B. Efron. "Bootstrap Methods: Another Look at the Jackknife." Ann. Statist. 7 (1) 1 - 26, January, 1979. https://doi.org/10.1214/aos/1176344552)

Here we provide python command line tools that implement the sampling of a CrystFEL streamfile for the purpose of error estimation in crystallographic data
as described in "Discerning best practices in XFEL-based biological crystallography – standards for nonstandard experiments",Gorel, A., Schlichting, I. & Barends, T. R. M. (2021). IUCrJ 8, 532-543.


################################### Installation

These scripts come as standalone python modules. The required python version is 3.5 or newer.


################################### Usage

Provided that you obtained a CrystFEL stream file from indexing with the CrystFEL software suite, bootstrapping the dataset can be achieved in two steps.

0) Find out how many indexed images your stream had:

$>fgrep "Reflection" something.stream|wc -l

This will return the number of indexed chunks in the stream file (provided that you did not use the multi option for indexing).
You can select a number smaller or equal to this number for the stream files that you want to sample for bootstrapping.

1) Cut down the dataset to a number of indexed images:

$>python3 indexed_substream_num.py -s something.stream -o something-1000.stream -n 1000

This will take the first 1000 indexed chunks from the stream file and write them into something-1000.stream that will serve as the source for the bootstraps.

2) Bootstrap (sample) the dataset multiple times to obtain your set of bootstrapped streams:

$>python3 bootstrap_stream.py -s something-1000.stream -o something-1000-bootstrapped-1.stream
$>python3 bootstrap_stream.py -s something-1000.stream -o something-1000-bootstrapped-2.stream
...
$>python3 bootstrap_stream.py -s something-1000.stream -o something-1000-bootstrapped-100.stream

Each of the individual output streams will have a different sampled set of indexed chunks.

3) Process the 100 bootsrapped streams:

Here you need to implement your own pipeline that processes the bootstrapped stream files and generates a structure or calculates a statistic.
By calculating the standard deviation on this ensemble of the statistic of interest (e.g. bond length) you estimate the error.
