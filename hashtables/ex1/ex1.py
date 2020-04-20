#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Iterate through the weights and store the difference between weight and limit as the key of the hash table. then traverse the hash table to match up the values
    """
    print('running with limit:' + str(limit))
    
    #iterate through the weights and calculate the difference between each weight and the limit
    for i in range(0, length):
        print('running with weight '+str(weights[i]))
        # store the difference between the weight and the limit
        difference = limit - weights[i]
        print('difference ' + str(difference))
        # check if there's a entry for the corresponding limit-weight (using limit like a mirror)
        mirrored_perfectly = hash_table_retrieve(ht, difference)
        print(f'{mirrored_perfectly} mirror perfectly')
        # we know from the instructions this will return none if there is no value
        if mirrored_perfectly is not None:
            # found a flush match, return them in largest to smallest order
            print(str(i), str(mirrored_perfectly))
            return (i, mirrored_perfectly)
        # if no flush match found, store the value in the hash table
        hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
