#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, shoe_size):
        self.brand = brand
        self._size = shoe_size

    def check_size(self):
        return self._size

    def set_size(self, shoe_size):
        if isinstance (shoe_size, int):
            return shoe_size
        else:
            raise ValueError("shoe size must bean integer") 
        
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as mew")
    
    _size = property(check_size, set_size)
