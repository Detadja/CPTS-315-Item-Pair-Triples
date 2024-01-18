
def PA():
    #Reads and cleans data from the file
    browsing_dict = {}
    with open("C:\\Users\\denis\\Desktop\\PA1\\browsing-data.txt", "r") as file:
        # print(file.read())
        data = file.readlines()
        #print(data)
    file.close()

    data = [row[:-2] for row in data]
    #print(data)

    #Places the data into a dictionary
    for row in data: 
        for k in row.split():
            if not k in browsing_dict:
                browsing_dict[k] = 1
            else:
                browsing_dict[k] += 1
        #print(row.split())
    #print(browsing_dict)

    #Determines the frequent items
    support = 100
    freq_item = {} 
    for key in browsing_dict:
        if browsing_dict[key] >= support:
            k, v = key, browsing_dict[key]
            freq_item[k] = v
    #print(freq_item)

    #Determines the total item pairs
    pair_dict = {}
    for row in data:
        split_rows = row.split()
        for item in split_rows:
            if item in freq_item: #If item 1 is a frequent item
                for item2 in split_rows:
                    if item2 in freq_item and item2 != item: #If item 2 is a frequent item and not item 1
                        # comp_key = (item2 + ',' + item)
                        # if comp_key in pair_dict: #If the pair is already in the dictionary
                        #     continue              #Skip it
                        # else:
                        if not (item + ',' + item2) in pair_dict:
                            pair_dict[(item + ',' + item2)] = 1
                        else:
                            pair_dict[(item + ',' + item2)] += 1
    #print(pair_dict)

    #Determines the frequent item pairs
    freq_pair = {}
    for key in pair_dict:
        if pair_dict[key] >= support:
            k, v = key, pair_dict[key]
            freq_pair[k] = v
    #print(freq_pair)

    #Determines the total item triples
    triple_dict = {}
    for row in data:
        split_rows = row.split()
        for item1 in split_rows:
            if item1 in freq_item: #If item 1 is a frequent item
                for item2 in split_rows:
                    if item2 in freq_item and item2 != item1: #If item 2 is a frequent item and not item 1
                        for item3 in split_rows:
                            if item3 in freq_item and item3 != item1 and item3 != item2: #If item 3 is a frequent item and not item 1 or 2
                                # comp_key = [(item1 + ',' + item3 + ',' + item2), (item2 + ',' + item1 + ',' + item3), (item2 + ',' + item3 + ',' + item1), (item3 + ',' + item1 + ',' + item2), (item3 + ',' + item2 + ',' + item1)]
                                # if (comp_key[0] in triple_dict) or (comp_key[1] in triple_dict) or (comp_key[2] in triple_dict) or (comp_key[3] in triple_dict) or (comp_key[4] in triple_dict):
                                #     continue           #If the triple is already in the dicitonary skip it
                                # else:                         
                                if not (item1 + ',' + item2 + ',' + item3) in triple_dict:
                                    triple_dict[(item1 + ',' + item2 + ',' + item3)] = 1
                                else:
                                    triple_dict[(item1 + ',' + item2 + ',' + item3)] += 1
    #print(triple_dict)

    #Determines the frequent triples
    freq_triple = {}
    for key in triple_dict:
        if triple_dict[key] >= support:
            k, v = key, triple_dict[key]
            freq_triple[k] = v
    #print(freq_triple)

    #Determines the conficence scores of the corresponding association rules.
    conf_association = {} # X -> Y
    # conf_association2 = {} # Y -> X
    conf_assoc = {} # (X, Y) -> Z
    # conf_assoc2 = {} # (X, Z) -> Y
    # conf_assoc3 = {} # (Y, Z) -> X

    pairs = list(freq_pair.keys())
    triples = list(freq_triple.keys())
    #print(pairs)
    #print(triples)

    #For Pairs
    for items in pairs:
        item = list(items.split(","))
        x = item[0]
        conf_association[items] = pair_dict[items] / browsing_dict[x]
        #print(item[1])
    #print(conf_association1)
    # for items in pairs:
    #     item = list(items.split(","))
    #     y = item[1]
    #     conf_association2[items] = pair_dict[items] / browsing_dict[y]
    #print(conf_association2)

    #For Triples
    for items in triples:
        item = list(items.split(","))
        xy = str(item[0] + ',' + item[1])
        conf_assoc[items] = triple_dict[items] / pair_dict[xy]
    #print(conf_assoc)
    # for items in triples:
    #     item = list(items.split(","))
    #     XZ = str(item[0] + ',' + item[2])
    #     conf_assoc2[items] = triple_dict[items] / pair_dict[XZ]
    # #print(conf_assoc2)
    # for items in triples:
    #     item = list(items.split(","))
    #     YZ = str(item[1] + ',' + item[2])
    #     conf_assoc3[items] = triple_dict[items] / pair_dict[YZ]
    #print(conf_assoc3)

    sort1 = dict(sorted(conf_association.items(), key=lambda item: item[1],  reverse = True))
    #print(sort1)
    # sort2 = dict(sorted(conf_association2.items()))
    # #print(sort2)

    #sort3 = dict(sorted(conf_assoc.items(), key=lambda item: item[1], reverse = True))
    sort3 = dict(sorted(conf_assoc.items(), key=lambda item:(-item[1], item[0])))
    #print(sort3)
    # sort4 = dict(sorted(conf_assoc2.items()))
    # #print(sort4)
    # sort5 = dict(sorted(conf_assoc3.items()))
    # #print(sort5)

    #Output results into output.txt
    with open("C:\\Users\\denis\\Desktop\\PA1\\output.txt", "w") as ofile:
        ofile.write('OUTPUT A\n')
        count = 0
        for out in sort1:
            if count == 5:
                break
            ofile.write(out.replace(',', ' ') + ' ' + str(sort1[out]) + '\n')
            count += 1
        ofile.write('OUTPUT B\n')
        count = 0
        for out in sort3:
            if count == 5:
                break
            ofile.write(out.replace(',', ' ') + ' ' + str(sort3[out]) + '\n')
            count += 1
    

def main():
    PA()
 

if __name__ == "__main__":
    main()    