from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}")
    print(f"Script Name: {argv[0]}")

else:
    print(
        "Hello, world"
    )
    print(f"Script Name: {argv[0]}")
