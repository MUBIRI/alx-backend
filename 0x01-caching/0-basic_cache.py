#!/usr/bin/env python3

'''a class BasicCache that inherits from BaseCaching and is a caching system
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
'''BasicCache'''

    def put(self, key, item):
        '''assigning a dict to a function'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''getting the function'''

        return self.cache_data.get(key, None)
