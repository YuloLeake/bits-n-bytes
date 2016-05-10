''' Written by Yulo Leake for coding exercise interview. '''

class LRUCache(object):
    ''' Least Recently Used Cache implemented using dictionary and Doubly Linked List.
        The dictionary is used to add and pull up cache data in O(1) time.
        The Doubly LL is used to keep track of order in which the cache item were used (SET and GET) 
         and can delete the least recently used item in O(1) time.
    '''

    def __init__(self, size):
        # implements cache using doubly linked list
        self._cacheHead = None      # Represents the newest item
        self._cacheTail = None      # Represents the oldest item 

        self._cacheDict = {}       # Maps key -> CacheNode 
        self._max_size  = size     # The capacity of the cache
        self._cur_size  = 0        # The current number of item in the cache

    def get_cache(self, key):
        ''' This function returns the node value that corresponds with the given key (None if not found).
            This operation is done in O(1) time.'''
        if key in self._cacheDict:
            # item is in cache, update item's position in LL and return the data
            node = self._cacheDict[key]
            self.__update_node(node)
            return node._data
        else:
            return None

    def set_cache(self, key, value):
        ''' This function adds a new node to the cache with given key and value. 
            If a key -> node pair already exists, it will update the value in the node with given value. 
            If the cache is full, it will delete the oldest used node before adding the new node. 
            This operation is done in O(1) time.'''
        if key in self._cacheDict:
            # key exists, update value and node's position in LL, but don't change current size
            node = self._cacheDict[key]
            node._data = value
            self.__update_node(node)
        else:
            if self._cur_size == self._max_size:
                # current cache capacity is at max, delete oldest node (tail)
                self._cur_size -= 1
                node = self._cacheTail
                self.__remove_node(node)
                self._cacheDict.pop(node._key, None)
            # add new node
            node = CacheNode(key, value)
            self._cacheDict[key] = node
            self.__add_node(node)
            self._cur_size += 1

    def __add_node(self, new_node):
        ''' Helper function to add a new node to the Doubly LL. 
            Function runs in O(1), since it just prepends to the tail. '''
        # basically doubly linked list prepend
        if self._cacheHead is None:
            self._cacheHead = self._cacheTail = new_node
        else:
            new_node._prev = self._cacheHead
            self._cacheHead._next = new_node
            self._cacheHead = new_node

    def __remove_node(self, node):
        ''' Helper function to remove a given node from the Doubly LL. 
            Function runs in O(1), since we already have the node to remove. '''
        # basically doubly linked list remove, but we already have the node
        if node._prev is not None:
            node._prev._next = node._next
        else:
            self._cacheTail = node._next

        if node._next is not None:
            node._next._prev = node._prev
        else:
            self._cacheHead = node._prev

    def __update_node(self, node):
        ''' Removes, then add the same node, hence putting the existing node at the head. '''
        self.__remove_node(node)
        self.__add_node(node)

    def __print_cache(self):
        ''' For debugging purpose; prints cache from oldest to newest item. '''
        node = self._cacheTail
        s = []
        while node != None:
            s.append(str(node)) 
            node = node._next
        print(", ".join(s) + " (cache size = " + str(len(self._cacheDict)) + ")")


class CacheNode(object):
    ''' Node for the Doubly LL used in the LRUCache. '''
    def __init__(self, key, data):
        self._key   = key
        self._data  = data
        self._next = None   # link to newer node
        self._prev = None   # link to older node

    def __str__(self):
        return "%s -> %s" % (self._key, self._data)

    def __repr__(self):
        return self.__str__()

def print_error(msg=""):
    ''' For debugging purpose; was used to print the error message after "ERROR". 
            i.e. "Error Wrong argument length for SIZE"
        It will not just print "ERROR". '''
    # print('ERROR', msg)
    print('ERROR')

def main():
    # Main driver for the Cache program to test it

    # Get size of the cache from user input
    size_set = False
    while not size_set:
        s = raw_input().strip().split(" ")
        if len(s) != 2:
            print_error('Wrong argument length for SIZE: ' + str(len(s)))
        elif s[0] != 'SIZE':
            print_error('Wrong argument for SIZE')
        elif not s[1].isdigit():
            # this takes care of negatives and floating numbers
            print_error('Given size is not a positive int')
        else:
            size = int(s[1])
            if size == 0:
                # Cache of zero makes no sense, so print error
                print_error('Given size is zero')
                continue
            size_set = True
            print('SIZE OK')

    cache = LRUCache(size)

    # Get user input GET, SET, and EXIT
    exit_flag = False
    while not exit_flag:
        s = raw_input().strip().split(" ")
        if s[0] == 'EXIT':
            # User prompts to exit; exit
            exit_flag = True
        elif s[0] == 'GET':
            if len(s) != 2:
                print_error('User may be trying to get multiple items, print error')
            else:
                value = cache.get_cache(s[1])
                if value == None:
                    print('NOTFOUND')
                else:
                    print('GOT ' + str(value))
        elif s[0] == 'SET':
            if len(s) != 3:
                # Key value with spaces, ERROR!
                print_error('Key value with spaces!')
            else:
                cache.set_cache(s[1], s[2])
                print('SET OK')
        else:
            print('ERROR', 'Invalid cache command.')

if __name__ == '__main__':
    main()