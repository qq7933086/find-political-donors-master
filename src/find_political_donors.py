import sys
import bisect

def calcuateMedian(arr):
    arrLen = len(arr)
    median = -1
    if arrLen % 2 < 1e-6:
        median = round((arr[int(arrLen/2 - 1)] + arr[int(arrLen / 2)]) / 2, 0)    #if array has even numbers
    else:
        median = arr[int((arrLen-1)/2)]    #if array has odd numbers
    return int(median)

# update dictionary of CMTE_ID and dim (ZIP_CODE or TRANSACTION_DT) with TRANSACTION_AMT as amount
def updateCMTEDict(dic, key, dim, amount):
    if key not in dic.keys():
        dic[key] = {}
    if key in dic.keys() and dim in dic[key].keys():
        dic[key][dim][-1] = dic[key][dim][-1] + amount # add new value to total amount
        bisect.insort_left(dic[key][dim],amount)    # using bisection algorithm to search for the position to insert
    else:
        dic[key][dim] = [amount,amount]

    arr = dic[key][dim] # remove the total in the array
    median = calcuateMedian(arr[:-1])
    arrLen = len(arr) - 1
    return [median, arrLen, int(arr[-1])]

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFileZip = sys.argv[2]
    outputFileDate = sys.argv[3]
    
    CMTE_ZIPDICT = {}    #dictionary to store an sorted array for CMTE_ID and ZIP_CODE
    CMTE_DTDICT = {}    #dictionary to store an sorted array for CMTE_ID and TRANSACTION_DT
    with open(inputFile) as file, open(outputFileZip, 'w') as zipFile:
        lines = [line.rstrip('\n') for line in file]
    
        for line in lines:
            values = line.split("|")
            try:
                CMTE_ID = values[0]
                ZIP_CODE = values[10][0:5]
                TRANSACTION_DT = values[13]
                TRANSACTION_AMT = float(values[14])
                OTHER_ID = values[15]
                if len(OTHER_ID) < 1e-6:
                    [zipMedian, zipCount, zipTotal] = updateCMTEDict(CMTE_ZIPDICT, CMTE_ID, ZIP_CODE, TRANSACTION_AMT)
                    zipFile.write(CMTE_ID+'|'+ZIP_CODE+'|'+str(zipMedian)+'|'+str(zipCount)+'|'+str(zipTotal)+'\n')
                    updateCMTEDict(CMTE_DTDICT, CMTE_ID, TRANSACTION_DT, TRANSACTION_AMT)
            except:
                pass
    file.close()
    zipFile.close()
    
    with open(outputFileDate, 'w') as dtFile:
        for key in CMTE_DTDICT.keys():
            for dt in CMTE_DTDICT[key].keys():
                arr = CMTE_DTDICT[key][dt]
                dtMedian = calcuateMedian(arr[:-1])
                dtCount = len(arr) - 1
                dtTotal = int(arr[-1])
                dtFile.write(CMTE_ID+'|'+TRANSACTION_DT+'|'+str(dtMedian)+'|'+str(dtCount)+'|'+str(dtTotal)+'\n')
    dtFile.close()