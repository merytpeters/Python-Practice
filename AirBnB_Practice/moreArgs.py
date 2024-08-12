#!/usr/bin/env python3
def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

a_dict = { 'name': "Best", 'age': 89 }

if __name__ == '__main__':
    my_fct(a_dict)
    my_fct(*a_dict)
    my_fct(**a_dict)
