# Introduction

NASTRAN&#x2122; is a Finite Element Analysis software package.

>The legend says Structural Analysis for Apollo 11  :rocket: 1969 manned flight to the :waxing_crescent_moon: was lead under NASTRAN&#x2122;.

NASTRAN&#x2122; means __NAS__A&#x2122; __STR__uctural __AN__alysis. The name is a reference to its ground foundation programme layer on FORTRAN (__FOR__mula __TRAN__slation) programming language. Have a look to `github` [nasa/NASTRAN-95](https://github.com/nasa/NASTRAN-95) if you are interested in NASTRAN&#x2122; internal machinery.

NASTRAN&#x2122; is a reliable FEA code but due its more than 50 years live the old-style formatting of input decks are sometimes discouraging for Students to dive into.

The hereuploaded Slides
have been used as a NASTRAN&#x2122; Introduction at [INSA Toulouse](https://www.insa-toulouse.fr/en/index.html) (France) for undergaduate Students (mechanical/systems engineering syllabus) from 2013 to 2017.

The contents is githubed to allow other people interested in the FEA to step into  NASTRAN&#x2122;.

# Table of Contents

## Structural Topics

Lecture Id.     |  githubed | Elements Topology |  Contents
------------ | -------------| -------------| -------------
1 | &#10004; | 1D | linear static structural analysis, nonlinear flavour
2 | &#10004; | 2D | linear static structural analysis, buckling and static Guyan Reduction
3 | &#10004; | 1D & 3D | transcient dynamic analysis, nonlinear structural contact analysis
4 | &#10008; | 3D | modal analysis (Students final exam)

__ Nota : __ Lecture 4 not githubed because not edited (Students Final Exam).

## SOL Coverage

Lecture Id.   |  SOL 101|  SOL 103  | SOL 105|SOL 106 | SOL 112 | SOL 200 |SOL 600
------------ | ------------| -------------
1 | &#x25CF;| &#x25EF; | &#x25EF; |&#x25CF; | &#x25EF; | &#x25CF; | &#x25EF;
2  | &#x25CF;| &#x25EF; | &#x25CF; |&#x25EF; | &#x25EF; | &#x25EF; | &#x25EF;
3  | &#x25CF;| &#x25EF; | &#x25EF; |&#x25EF; | &#x25CF; | &#x25EF; |&#x25CF;
4  | &#x25CF;| &#x25CF; | &#x25EF; |&#x25EF;| &#x25EF; | &#x25EF; | &#x25EF;

__ Nota : __ Only Structured Solution Sequences covered.

# Outcomes

To do list :
- [x] Lectures Slides githubed
- [ ] NASTRAN&#x2122; bulk data files Case Studies of Lectures Githubed
- [ ] Complete README
- [ ] Complete References

# References

Some relevant NASTRAN&#x2122; Materials are quoted hereafter :

[1]	[NASTRAN Level 15 User's Guide](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19750014745.pdf), NASA CR-2504 - 1975.

[2]	[The NASTRAN Theoretical Manual](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19840010609.pdf), NASA SP-221 - 1981.

[3]	NASTRAN Modelling - https://femci.gsfc.nasa.gov/

[4]	Other NASTRAN Manuals - https://ntrs.nasa.gov/
