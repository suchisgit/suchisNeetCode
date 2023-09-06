#WILL SOLVE THE FIRST 2 LEVELS
import re
def solution(queries):
    data = list(dict())
    mappingKeyToIndx = {}
    indx = 0
    res = []
    for q in queries:
        if q[0] == "SET":
            res.append("")
            timeStamp = q[1]
            key = q[2]
            field = q[3]
            value = int(q[4])
            if key not in mappingKeyToIndx:
                mappingKeyToIndx[key] = indx
                d = { "keySuchi" : key , field : value}
                data.append(d)
                indx+=1
            else:
                data[mappingKeyToIndx[key]][field]=value
        if q[0] == "COMPARE_AND_SET":
            timeStamp = q[1]
            key = q[2]
            field = q[3]
            expectedValue = int(q[4])
            newValue = int(q[5])
            if key in mappingKeyToIndx:
                if field in data[mappingKeyToIndx[key]]:
                    if data[mappingKeyToIndx[key]][field] == expectedValue:
                        data[mappingKeyToIndx[key]][field] = newValue
                        res.append("true")
                    else:
                        res.append("false")
                else:
                    res.append("false")
            else:
                res.append("false")
        if q[0] == "COMPARE_AND_DELETE":
            timeStamp = q[1]
            key = q[2]
            field = q[3]
            expectedValue = int(q[4])
            if key in mappingKeyToIndx:
                if field in data[mappingKeyToIndx[key]]:
                    if data[mappingKeyToIndx[key]][field] == expectedValue:
                        del data[mappingKeyToIndx[key]][field]
                        res.append("true")
                    else:
                        res.append("false")
                else:
                        res.append("false")
            else:
                        res.append("false")
        if q[0] == "GET":
            timeStamp = q[1]
            key = q[2]
            field = q[3]
            if key in mappingKeyToIndx:
                if field in data[mappingKeyToIndx[key]]:
                    res.append(str(data[mappingKeyToIndx[key]][field]))
                else:
                    res.append("")
            else:
                    res.append("")
        if q[0] == "SCAN":
            timeStamp = q[1]
            key = q[2]
            filteredList=[]
            if key in mappingKeyToIndx:
                for field in data[mappingKeyToIndx[key]]:
                    if field!="keySuchi":
                        filteredList.append(field+"("+str(data[mappingKeyToIndx[key]][field])+"), ")
            else:
                res.append("")
                continue
            filteredList.sort()
            res1=""
            for x in filteredList:
                res1+=x
            res.append(res1[:-2])
        if q[0] == "SCAN_BY_PREFIX":
            timeStamp = q[1]
            key = q[2]
            prefix = q[3]
            filteredList=[]
            if key in mappingKeyToIndx:
                for field in data[mappingKeyToIndx[key]]:
                    if field!="keySuchi":
                        filteredList.append(field+"("+str(data[mappingKeyToIndx[key]][field])+"), ")
            else:
                res.append("")
                continue
            filteredList.sort()
            # print(filteredList)
            pattern = re.compile(f"^{prefix}")
            filteredList1 = [s for s in filteredList if pattern.match(s)]
            res2=""
            for x in filteredList1:
                res2+=x
            res.append(res2[:-2])
            
    return res