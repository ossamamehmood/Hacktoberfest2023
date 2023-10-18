def hello():
    print("Hello World\n\n")


def hello_one_param(name):
    print("Hello {}\n\n".format(name))


def hello_two_params(name1, name2):
    print("Hello {} and {}\n\n".format(name1, name2))


def hello_list(list_of_names):
    for name in list_of_names:
        print("Hello {}".format(name))
    print("\n\n")


def hello_list2(list_of_names):
    string_of_names = ", ".join(list_of_names[:-1])
    print("Hello {}, and {}\n\n".format(string_of_names, list_of_names[-1]))


def hello_n_params(*names):
    hello_list(names)


def hello_n_params2(*names):
    hello_list2(names)


if __name__ == "__main__":
    name1 = "Yums"
    name2 = "Dexter"
    name3 = "Alice"
    name4 = "Daniel"
    list_of_names = ["Yums", "Dexter", "Alice", "Daniel"]

    hello()
    hello_one_param(name1)
    hello_two_params(name1, name2)
    hello_list(list_of_names)
    hello_list2(list_of_names)
    hello_n_params(name1, name2, name3, name4)
    hello_n_params2(name1, name2, name3, name4)
