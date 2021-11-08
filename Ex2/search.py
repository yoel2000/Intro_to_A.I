import state
import frontier


def search(n):
    s = state.create(n)
    # s = [[4, 3, 7, 5, 8, 6, 1, 0, 2], '']
    print(s)
    f = frontier.create(s)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if state.is_target(s):
            return [len(s[1]), f[3]]  # The len(s[1] is corresponding to the depth and f[3] to the max number of items.
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f, i)
    return 0


# max_depth=0
# sum_item=0

# print("search(3):")
# for i in range(100):
#     x = search(3)
#     max_depth += x[0]
#     sum_item += x[1]
# print("Average depth", max_depth/100)
# print("Average items", sum_item/100)
#
#
# max_depth=0
# sum_item=0
#
# print("search(4):")
# for i in range(3):
#     x = search(4)
#     max_depth += x[0]
#     sum_item += x[1]
# print("Average depth", max_depth/3)
# print("Average items", sum_item/3)


max_depth=0
sum_item=0

print("search(3):")

x = search(3)
max_depth += x[0]
sum_item += x[1]
print("Average depth", max_depth)
print("Average items", sum_item)

# max_depth=0
# sum_item=0

# print("search(3):")
# for i in range(100):
#     x = search(3)
#     max_depth += x[0]
#     sum_item += x[1]
# print("Average depth", max_depth/100)
# print("Average items", sum_item/100)
#
#
# max_depth=0
# sum_item=0
#
# print("search(4):")
# for i in range(3):
#     x = search(4)
#     max_depth += x[0]
#     sum_item += x[1]
# print("Average depth", max_depth/3)
# print("Average items", sum_item/3)

"""
The answer to the question 4 is in the "state.py" file.
"""




