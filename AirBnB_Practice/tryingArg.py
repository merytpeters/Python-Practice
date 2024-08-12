#!/usr/bin/env python3
def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

if __name__ == '__main__':
    my_fct("School", 12, name="Best", number=89)
