import argparse, os




# Get a dic of all the tests we have on hand
def get_tests():
    tests = {}
    for (root, dir, files) in os.walk('./tests'):
        # print(root)
        # print(dir)
        # print(files)
        if root == './tests':
            dir.sort()
            for item in dir:
                tests.update({item: []})

        else:
            tests.update( {root.split('/')[len(root.split('/'))-1]: files} )
        # print('-------------')
    return tests



# Print out the tests/test pacakages we have on hand
def show_tests(tests, test_package = False):
    print('\n\n')
    if not test_package:
        print('Test packages: ')
        for test in tests:
            print(f"- {test}")
    elif test_package in tests:
        print(test_package)
        for test in tests[test_package]:
            print(f"- {test}")
    else:
        print(f"{test_package} is not in: ")
        for test in tests:
            print(f"- {test}")



def main():
    print('Welcome to the prototype DSAT \'Dynamic Application Security Scanning Tool\'')

    tests = get_tests()

    parser = argparse.ArgumentParser(description='DSAT Prototype')
    subparsers = parser.add_subparsers(dest = 'mode')

    run_parser = subparsers.add_parser('run', help = 'run some tests')
    run_parser.add_argument('-r', required = True, help = 'test pacakge to use')

    list_parser = subparsers.add_parser('list', help = 'list the test packages')
    list_parser.add_argument('-r', help = 'list test for given package')

    args = parser.parse_args()
    print(args)


    if args.mode == 'list':
        show_tests(tests, args.r)






if __name__ == "__main__":
    main()
