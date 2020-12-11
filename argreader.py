#!/usr/bin/env python

import sys


DEBUG = False
#DEBUG = True

def debug(s):
    if DEBUG:
        print('DEBUG: %s' % s)

def parse_cli(values, defaults=None):
    """ Simple option/argument parsing.

        Args:
            values: sequence of str giving command-line, i.e. usually sys.argv[1:]
            defaults: dict. Define all options in here - any element of `values` which is not a key in `defaults` is assumed to be an argument.
                      If a value in `defaults` is a bool, the option takes no argument, otherwise it does.

        Returns (options, arguments) where the former is a dict giving options and the latter is a sequence giving arguments.
    """

    options = {} if defaults is None else defaults.copy()
    args = []
    idx = 0
    while idx < len(values):
        v = values[idx]
        if v in defaults: # is option
            if isinstance(defaults[v], bool): # is flag
                options[v] = True
            else:
                options[v] = values[idx + 1] # TODO: length check, check doesn't start with '-'?
                idx += 1
        else:
            args.append(v)
        idx += 1
    return (options, args)



if __name__ == '__main__':

    tests = [
        ('-v --option foo arg1 arg2'.split(), {'-v':False, '--option':'bar'}),
        ('--option foo arg1'.split(), {'-v':True, '--option':'bar'}),
        ('--option foo'.split(), {'-v':True, '--option':'bar'}),
        (''.split(), {'-v':True, '--option':'bar'}),
        ('-v'.split(), {'-v':False, '--option':'bar'}),
    ]

    for t in tests:
        print(parse_cli(*t))
