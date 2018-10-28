# pycon

![picon](https://images-na.ssl-images-amazon.com/images/I/51ekKN9T7rL.jpg)

> A `python` script to convert a `NASTRAN` `GPWG` `.f06` MO Matrix output to a `.conm2`

## Usage

``` bash
python pycon.py a.f06
```
In order to release from `NASTRAN` `GPWG` `.f06` Table (from MO Rigid body mass Matrix as per  [1] nomenclature) a `NASTRAN` `CONM2` Card. The latter is written into `a.conm2`. Default is to write a `CONM2` with id 1000 at `GRID` 9000 in Coordinate System Id 9999 (MO Matrix `.f06` is to be inline with this data).

## Reference

[1]	[A Verification Procedure for MSC/NASTRAN Finite
Element Models](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.81.951&rep=rep1&type=pdf), NASA Contractor Report 4675 - 1995.
