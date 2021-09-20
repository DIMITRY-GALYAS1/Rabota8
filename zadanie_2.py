#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    z = {
         1: 'a',
         2: 'b',
         3: 'c'
         }
    x = dict(zip(z.values(), z.keys()))
    print(x)
