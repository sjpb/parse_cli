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
            defaults: dict defining options - any element of `values` which is not a key in `defaults` is assumed to be an argument.
                      If a value in `defaults` is a bool, the option takes no argument, otherwise it does.

        Returns (options, arguments) where the former is a dict giving options and the latter is a sequence giving arguments.

        Examples:
        >>> parse_cli('-v --option foo arg1 arg2'.split(), {'-v':False, '--option':'bar'})
        ({'-v': True, '--option': 'foo'}, ['arg1', 'arg2'])
        >>> parse_cli('--option foo arg1'.split(), {'-v':True, '--option':'bar'})
        ({'-v': True, '--option': 'foo'}, ['arg1'])
        >>> parse_cli('--option foo'.split(), {'-v':True, '--option':'bar'})
        ({'-v': True, '--option': 'foo'}, [])
        >>> parse_cli(''.split(), {'-v':True, '--option':'bar'})
        ({'-v': True, '--option': 'bar'}, [])
        >>> parse_cli('-v'.split(), {'-v':False, '--option':'bar'})
        ({'-v': True, '--option': 'bar'}, [])
        >>> parse_cli('argX'.split(), {})
        ({}, ['argX'])

    """

    options = {} if defaults is None else defaults.copy()
    args = []
    idx = 0
    while idx < len(values):
        v = values[idx]
        if v in options: # is option
            if isinstance(defaults[v], bool): # is flag
                options[v] = True
            else:
                options[v] = values[idx + 1] # TODO: length check, check doesn't start with '-'?
                idx += 1
        else:
            args.append(v)
        idx += 1
    return (options, args)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
