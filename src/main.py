def add(a, b):
    return a + b


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Add two numbers")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    args = parser.parse_args()
    print(add(args.a, args.b))


if __name__ == "__main__":
    main()
