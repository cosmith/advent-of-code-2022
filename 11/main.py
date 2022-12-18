from functools import reduce


class Monkey:
    def __init__(self, items, operation, divisible_by, test_true, test_false):
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0


# test
# monkeys = [
#     Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
#     Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
#     Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
#     Monkey([74], lambda x: x + 3, 17, 0, 1),
# ]

# input
monkeys = [
    Monkey([99, 67, 92, 61, 83, 64, 98], lambda x: x * 17, 3, 4, 2),
    Monkey([78, 74, 88, 89, 50], lambda x: x * 11, 5, 3, 5),
    Monkey([98, 91], lambda x: x + 4, 2, 6, 4),
    Monkey([59, 72, 94, 91, 79, 88, 94, 51], lambda x: x * x, 13, 0, 5),
    Monkey([95, 72, 78], lambda x: x + 7, 11, 7, 6),
    Monkey([76], lambda x: x + 8, 17, 0, 2),
    Monkey([69, 60, 53, 89, 71, 88], lambda x: x + 5, 19, 7, 1),
    Monkey([72, 54, 63, 80], lambda x: x + 3, 7, 1, 3),
]

multiple = reduce(lambda x, y: x * y, [m.divisible_by for m in monkeys], 1)


def do_round():
    for monkey in monkeys:
        for item in monkey.items:
            item = item % multiple
            item = monkey.operation(item)
            monkey.inspected += 1
            monkey.items = monkey.items[1:]
            if item % monkey.divisible_by == 0:
                throw_to = monkey.test_true
            else:
                throw_to = monkey.test_false
            monkeys[throw_to].items.append(item)


for x in range(1, 10001):
    do_round()
    if x % 1000 == 0:
        print("Round {x}".format(x=x))
        for m, monkey in enumerate(monkeys):
            print("Monkey {m}: {monkey.inspected}".format(m=m, monkey=monkey))
        print("")

result = sorted([m.inspected for m in monkeys], reverse=True)
print(result[0] * result[1])
