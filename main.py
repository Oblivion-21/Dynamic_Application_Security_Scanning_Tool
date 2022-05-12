import argparse
import os

from tests import ssl, http

"""
TODO:
    - be able to show test description when list test (i.e. test_name -- description of test)
"""


# Get a dic of all the tests we have on hand
def get_tests():
    tests = {}

    for (root, dir, files) in os.walk('./tests'):
        if root == './tests':
            dir.sort()
            for item in dir:
                tests.update({item: []})
        else:
            tests.update({root.split('/')[len(root.split('/')) - 1]: files})

    return tests


# Print out the tests/test packages we have on hand
def show_tests(tests, test_package=False):
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


# Run some tests
def run_tests(tests, chosen_package, url):
    # Break if non-valid package is chosen
    if chosen_package not in tests:
        print(f"{chosen_package} is not in:")
        for test in tests:
            print(f"- {test}")
        return

    print(f"Running {chosen_package} tests against {url}")
    if chosen_package == "ssl":
        ssl.__runTests.run(url)
    elif chosen_package == "http":
        http.__runTests.run(url)


def main():
    print('Welcome to the prototype DSAT \'Dynamic Application Security Scanning Tool\'\n\n')

    tests = get_tests()

    parser = argparse.ArgumentParser(description='DSAT Prototype')
    subparsers = parser.add_subparsers(dest='mode')

    run_parser = subparsers.add_parser('run', help='run some tests')
    run_parser.add_argument('-r', required=True, help='test pacakge to use')
    run_parser.add_argument('-w', required=True, help='website to test aginst')

    list_parser = subparsers.add_parser('list', help='list the test packages')
    list_parser.add_argument('-r', help='list test for given package')

    args = parser.parse_args()
    # print(args)

    # Basic menu
    if args.mode == 'list':
        show_tests(tests, args.r)
    elif args.mode == 'run':
        run_tests(tests, args.r, args.w)


if __name__ == "__main__":
    main()
