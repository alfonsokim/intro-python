
import urllib2
from collections import defaultdict

def world_count(url):
    counts = defaultdict(int)
    for line in urllib2.urlopen(url).readlines():
        line = line.replace('\r\n', '')
        for world in line.split(' '):
            counts[world] += 1
    return counts

def to_csv(counts):
    csv_file = open('quixote_world_count.csv', 'w')
    for world, freq in counts.iteritems():
        print >> csv_file, '%s,%i' % (world, freq)
    csv_file.close()


if __name__ == '__main__':
    counts = world_count('http://www.gutenberg.org/cache/epub/996/pg996.txt')
    sorted_keys = sorted(counts, key=counts.get, reverse=True)
    print 'top 10 worlds:'
    for i, key in enumerate(sorted_keys):
        if i < 10:
            print '%s: %s' % (key, counts[key])
    to_csv(counts)
