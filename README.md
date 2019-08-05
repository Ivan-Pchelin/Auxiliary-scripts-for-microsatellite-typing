# Auxiliary-scripts-for-microsatellite-typing 
Here one can find python scripts for conversion of haploid microsatellite or SSR typing data from GeneMapper format to a table (incrustator.py) and back (tabletogenemapper.py).
The script incrustator.py writes a sum of new haploid microsatellite typing data in GeneMapper format (Addition.txt) and an existing table with samples' names (Mainfile.txt) to a new file.

The script tabletogenemapper.py transforms a TAB-delimited table with microsatellite polymorphism data into GeneMapper file format.
By the moment, it is very slow when dealing with multiple measurements of particular alleles.