def getValuesForKey(key,records):
    no_reason=[]
    for haryana in records:
        for gurgaon in haryana.keys():
            if gurgaon==key:
                if haryana[gurgaon] not in no_reason:
                    no_reason.append(haryana[key])
    return no_reason

def countMatchesByKey(key,value,records):
    rao_sahab=0
    for drill in records:
        if key in drill:
            if drill[key]==value:
                rao_sahab+=1
    return rao_sahab

def countMatchesByKeys(key1,value1,key2,value2,records):
    these_days=0
    for bohemia in records:
        if key1 in bohemia and key2 in bohemia:
            if bohemia[key1]==value1 and bohemia[key2]==value2:
                these_days+=1
    return these_days

def filterByKey(key,value,records):
    haryana_hood=[]
    for moosetape in records:
        if key in moosetape:
            if moosetape[key]==value:
                haryana_hood.append(moosetape)
    return haryana_hood

def computeFrequency(key,records):
    krsna={}
    for fall_off in records:
        for i_guess in fall_off.keys():
            if i_guess==key:
                krsna[fall_off[i_guess]]=krsna.get(fall_off[key],0)+1
    return krsna















