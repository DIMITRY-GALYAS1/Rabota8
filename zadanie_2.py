#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = {
        1: 'a',
        2: 'b',
        3: 'c'
    }
    dict_items = s.items()
    s1 = dict(zip(s.values(), s.keys()))
    print(s1)
