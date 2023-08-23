#!/usr/bin/env python3

class Book:
    def __init__(self,title, page_count):
        self.title = title
        self._page_count = page_count

    def check_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            return page_count
        else :
            raise ValueError("page count must be an integer")
    _page_count = property(check_count,set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    
    
        