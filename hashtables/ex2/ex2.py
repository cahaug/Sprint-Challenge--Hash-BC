#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    print('length ' + str(length))
    """
    Store all the tickets in the hash table, with key = source, then retrieve source=null, set that to the route[0], then traverse the rest of the length of the inputs and order them
    """
    # loop through the tickets
    for ticket in tickets:
        # store in hash table with source being the key
        print(f's:{ticket.source}   d:{ticket.destination}')
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # origin flight has a source of none, set to route[0]
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    print('route[0] '+ route[0])
    # order the next flights
    for i in range(1, length):
        # follow the bread crumb trail, logging the destinations into the route array
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    
    # verify the route array looks correct
    print(route[0:length-1])

    # remove the extra none at the end, remembering that the final destination is none
    route = route[0:length-1]
    return route




