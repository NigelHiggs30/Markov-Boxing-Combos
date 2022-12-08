from itertools import chain
import matplotlib.pyplot as plt
from random import randrange
from random import choices
from collections import Counter


def calc_len_combo_probs(data):
    # create list of the length of each element in data
    all_lengths = [len(x) for x in data]

    # count the number of occurrences of each length
    counts = Counter(all_lengths)

    # extract keys and values of count into lists
    keys, values = list(counts.keys()), list(counts.values())

    # calculate probabilities and round to three decimal places
    final_list = [round(x/len(all_lengths),3) for x in values]

    # return final_list and keys
    return final_list, keys

def punch_bin_counts(result):
    # create empty bin to count each instance of each punch
    empty_bin = [0] * len(result)

    # count instances of each punch in data
    for x in data:
        for y in x:
            for list_len in range(len(empty_bin)):
                if result[list_len] == y:
                    empty_bin[list_len] += 1

    # calculate probability distribution of each punch
    prob_dist = [round(z/sum(empty_bin), 2) for z in empty_bin]

    # return probability distribution
    return prob_dist

def Markov_Matrix(result,data):

    #now lets create probabilities of certain punches being thrown
    #after each categorical punch. should be in n * n matrix
    matrix =  [[float(0) for col in range(len(result)+1)] for row in range(len(result))]

    count = 0

    while count < len(result):
        check = result[count]
        for x in range(len(data)):
            #print(x)
           
            for y in range(len(data[x])):
                #print(y)
                if data[x][y] == check:
                    try:
                        #see if there is an element 1 place over in the
                        #list if not go to exception
                        test = data[x][y+1]
                        for i in range(len(result)):
                            if test == result[i]:
                                matrix[count][i] += 1
                            else:
                                continue
                    except:
                        #if
                        matrix[count][-1]+=1
        count+=1

    #now we run through each list in the matrix find its sum, round
    #than insert every index with a prob where neccesary.
    for x in range(len(matrix)):
        sum_list = sum(matrix[x])
        for y in range(len(matrix[x])):
            if matrix[x][y] > 0.0:
                calc_prob = round(matrix[x][y]/sum_list,2)
                matrix[x][y] = calc_prob
            else:
                continue
    result.append("Empty") 

    return matrix,count

def combo_generator(result,data,matrix):
    #lets create a first punch vector that we will randomly select and
    #use to feed into are combo generator
    first_punch_list = [0.0] * len(result)

    #lets all calculate the len at which we should be running the max combo len
    len_combo,names = calc_len_combo_probs(data)
    len_combo = choices(names,len_combo)

    for i in data:
        for x in range(len(result)):
            if i[0] == result[x]:
                first_punch_list[x]+=1.0
            else:
                continue
           
    divide_by = sum(first_punch_list)
    for y in range(len(first_punch_list)):
        first_punch_list[y] = round(first_punch_list[y]/divide_by,2)

    first_punch = choices(result,first_punch_list)
    first_index = result.index(first_punch[0])


    punch = choices(result,matrix[first_index])
    print(first_punch[0])
    print(punch[0])

    if len_combo[0] >2:
        #while punch[0] != "Empty":

        for x in range(int(len_combo[0]-2)):
            try:
                #print(punch)
                next_index = result.index(punch[0])
                punch = choices(result,matrix[next_index])
                if punch[0]!= "Empty":
                    print(punch[0])
                elif punch[0]=="Empty":
                    break
                
                else:
                    print("\n")
                    break
            except:
                break
    else:
        pass
    
    return len_combo

if __name__ == "__main__":
    #2d list which contains each combo I preform for boxing.
    #we can use this to create are probs etc.
    data = [
       
            ["LHJab","LHJab"],["LHJab","LHJab","LBHook","LHHook"]
            ,["LHJab","LHJab","RHStraight"],["LHJab","LHJab","RBStraight"]
            ,["LHJab","LHJab","RHStraight","LHHook","RHStraight"]
            ,["LHJab","LHJab","RHStraight","LHHook","RHStraight","LBHook","LHHook"]
            ,["RHStraight","LHHook","RHStraight"],["RHStraight","LHHook","RHStraight","LBHook","LHHook"]
            ,["LHStraight","RHStraight"],["LHStraight","RHStraight","LBHook","LHHook"]
            ,["LHStraight","RHStraight","LHStraight","RHStraight"]
            ,["LHJab","LHJab","RBStraight","LHHook","RHStraight","LBHook","LHHook"]
            ,["LHJab","LHJab","RBStraight","LHHook","RHStraight"]
            
        ]



    #this result equals a list that contains all the categories of punches from the
    #above data set.
    punch_categories = list(set(chain(*data)))


    #probabilities of each punch_categories occuring
    Total_Punch_Probs = punch_bin_counts(punch_categories)

    ##now we return Markov matrix and count

    matrix, count = Markov_Matrix(punch_categories,data)

        
    output = combo_generator(punch_categories,data,matrix)
