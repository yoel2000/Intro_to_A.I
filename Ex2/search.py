import state
import frontier


def search(n):
    s = state.create(n)
    print(s)
    f = frontier.create(s)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if state.is_target(s):
            return [len(s[1]), f[2]]
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f, i)
    return 0


max_depth=0
sum_item=0

print("search(3):")
for i in range(100):
    x = search(3)
    max_depth += x[0]
    sum_item += x[1]
print("Average depth", max_depth/100)
print("Average items", sum_item/100)


max_depth=0
sum_item=0

# print("search(4):")
# for i in range(10):
#     x = search(4)
#     max_depth += x[0]
#     sum_item += x[1]
# print("Average depth", max_depth/10)
# print("Average items", sum_item/10)

# print(search(3))
