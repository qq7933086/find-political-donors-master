## Approach
Generating two output files (generate medianvals_by_zip.txt and medianvals_by_date.txt) shares a common process. The records belonging to the same CMTE_ID/ZIP_CODE and CMTE_ID/TRANSACTION_DT are stored in seperate dictionaries. So that when a new record comes, we can add the new amount to the corresponding array directly without any search. 
To calculate median, we need to efficiently maintain a sorted array. We can insert the new amount in the sorted array using a bisection search, which has log(n) complexity. 
medianvals_by_zip will require streaming out the running median into files. medianvals_by_date file is written out when all records (for certain period of time) have been processed.

## Dependencies
Python library:
sys
bisect
math

## Run instructions
In the project directory, using python command:
python ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt

or directly run "run.sh"

#use test to check formatting
#write own additional tests

* Put any comments in the README inside your project repo, not in the submission box
