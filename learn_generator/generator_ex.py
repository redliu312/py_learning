from inspect import isgenerator
from itertools import chain, izip_longest


# HINT: because python2 not support `yield from`
# http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html


def _remove_repeat_search_results(generator):
    keys = set()
    for i in generator:
        if i.key in keys:
            continue
        yield i
        keys.add(i.key)


def iter_over(generators):
    for i in generators:
        if isgenerator(i):
            for j in iter_over(i):
                yield j
        else:
            yield i


def iter_over_batch(generators, batch_size=5):
    def _batch(batch_size):
        batch = []
        for g in generators:
            if not g:
                continue

            batch.append(g)

            if len(batch) == batch_size:
                yield batch
                batch = []

        yield batch

    for batch in _batch(batch_size):
        for group in izip_longest(*batch):
            for i in group:
                if i:
                    yield i
