def count_lines(name):
    print("The count of lines is:", len(name.readlines()))


def count_chars(name):
    print("Number of characters:", len(name.read()))


def test(name):
    return count_lines(open(name)), count_chars(open(name))


test("state.txt")
