import sys
import check

package = sys.argv[1]
list = check.check(package)

print(list)
#if percent == 100:
#    print("%d %s %d" % (percent, name, 0))
#elif percent > 90 :
#    print("%d %s %d" % (percent, name, 1))
#else:
#    print("%d %s %d" % (percent, name, 2))
