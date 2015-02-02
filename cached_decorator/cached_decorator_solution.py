"""
Decorator Exercise
------------------

Sometimes performing a computation can be very expensive in terms of the
time or resources taken.  If the same computation needs to be performed
frequently, then this can be a major bottleneck in performance. In these
cases it can be useful to keep a cache of the inputs and corresponding
outputs and then simply look up the value.

A simple implementation of this idea (using only positional arguments) might
look something like::
    
    cache = {}
    
    def cached_call(f, *args):
        global cache
        if (f, args) not in cache:
            cache[(f, args)] = f(*args)
        return cache[(f, args)]

For an illustration of the efficiency that such an approach can gain,
compare computing the nth term in the Fibonacci sequence recursively with
and without this strategy::

    def fibonacci1(n):
        print "Computing fibonacci1(%d)" % n
        if n in {0, 1}:
            return 1
        else:
            return fibonacci1(n-1) + fibonacci1(n-2)

    def fibonacci2(n):
        print "Computing fibonacci2(%d)" % n
        if n in {0, 1}:
            return 1
        else:
            return cached_call(fibonacci2, n-1) + cached_call(fibonacci2, n-2)

However, you'd much prefer to write something like the first and gain the
performance benefits of the second.

Turn the `cached_call` function into a decorator `cached` so that you can
simply write::

    @cached
    def fibonacci(n):
        print "Computing fibonacci(%d)" % n
        if n in {0, 1}:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)

to automatically cache the inputs and outputs.

Bonus
~~~~~

1. Generalize so that this works for keyword arguments as well.

2. If the function is called frequently with different values, the memory used
   by the cache can grow very large.  Modify your solution so that it accepts
   a maximum cache size.  Ideally you might use a "least-recently used"
   strategy (http://en.wikipedia.org/wiki/Cache_algorithms#LRU)
   for determining which cache values to discard, but for your first attempt
   randomly discarding values is sufficient.

"""

from functools import wraps

def cached(f):
    cache = {}
    @wraps(f)
    def cached_f(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return cached_f


@cached
def fibonacci(n):
    print "Computing fibonacci(%d)" % n
    if n in {0, 1}:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(10)

