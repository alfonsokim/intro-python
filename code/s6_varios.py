
# =============================================================================
class Magic():

    def __init__(self, **props):
        self.props = props

    def __getattr__(self, attr):
        if attr in self.props:
            return self.props.get(attr)
        raise Exception('No existe: %s' % attr)

    def __call__(self, *args, **keywords):
        print 'call con args: %s y keywords: %s' % (str(args), str(keywords))


# =============================================================================
m = Magic(**{'hello': 1, 'world': range(10)})

print m.hello
print m.world
# print m.no_existe

m()
m(1, 'dos', False)
m(1, dos=2, tres='tres')

# =============================================================================
def timer(f):
    import time
    def proxy(*args):
        start = time.time()
        val = f(*args)
        print 'tiempo: %f' % (time.time() - start)
        return val
    return proxy

import math

@timer
def test_function(test_f, n):
    return [test_f(x) for i in range(n) for x in range(i)]

test1 = lambda x: x**0.5
test2 = lambda x: math.log(x+1, 3)
test3 = lambda x: x / 2

test_function(test1, 1000)
test_function(test2, 1000)
test_function(test3, 1000)


