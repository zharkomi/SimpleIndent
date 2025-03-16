from apply_indention import apply_indention


def demonstrate_indention_example(test_name):
    test_cases = {
        "test_java_output": {
            "content": "Node{id=1, name='Root', children=[Node{id=2, name='Child 1', children=[Node{id=4, name='Grandchild 1.1', children=[]}, Node{id=5, name='Grandchild 1.2', children=[]}]}, Node{id=3, name='Child 2', children=[]}]}",
            "open_brackets": "{[(",
            "close_brackets": "}])",
            "newline_chars": ",",
            "tab_str": "  ",
            "expected": "Node{\n  id=1,\n   name='Root',\n   children=[\n    Node{\n      id=2,\n       name='Child 1',\n       children=[\n        Node{\n          id=4,\n           name='Grandchild 1.1',\n           children=[]\n        },\n         Node{\n          id=5,\n           name='Grandchild 1.2',\n           children=[]\n        }\n      ]\n    },\n     Node{\n      id=3,\n       name='Child 2',\n       children=[]\n    }\n  ]\n}"
        },
        "test_basic_curly_brackets": {
            "content": "{hello world}",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "{\n    hello world\n}"
        },
        "test_nested_curly_brackets": {
            "content": "{outer{inner}content}",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "{\n    outer{\n        inner\n    }content\n}"
        },
        "test_empty_brackets": {
            "content": "{}",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "{}"
        },
        "test_multiple_bracket_types": {
            "content": "{curly[square(round)]}",
            "open_brackets": "{[(",
            "close_brackets": "}])",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "{\n    curly[\n        square(\n            round\n        )\n    ]\n}"
        },
        "test_with_semicolons": {
            "content": "{statement1;statement2;}",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": ";",
            "tab_str": "    ",
            "expected": "{\n    statement1;\n    statement2;\n}"
        },
        "test_tab_string_variation": {
            "content": "{level1{level2}}",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "\t",
            "expected": "{\n\tlevel1{\n\t\tlevel2\n\t}\n}"
        },
        "test_code_like_content": {
            "content": "function() {if (condition) {return true;} else {return false;}}",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": ";",
            "tab_str": "    ",
            "expected": "function() {\n    if (condition) {\n        return true;\n    } else {\n        return false;\n    }\n}"
        },
        "test_json_structure": {
            "content": '{"name":"John","data":{"age":30,"active":true}}',
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": ",",
            "tab_str": "    ",
            "expected": '{\n    "name":"John",\n    "data":{\n        "age":30,\n        "active":true\n    }\n}'
        },
        "test_no_brackets": {
            "content": "Plain text without brackets.",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": ";",
            "tab_str": "    ",
            "expected": "Plain text without brackets."
        },
        "test_unbalanced_brackets": {
            "content": "{unclosed bracket",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "{\n    unclosed bracket"
        },
        "test_xml_like_content": {
            "content": "<root><child>text</child></root>",
            "open_brackets": "<",
            "close_brackets": ">",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "<\n    root\n><\n    child\n>text<\n    /child\n><\n    /root\n>"
        },
        "test_empty_input": {
            "content": "",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": ""
        },
        "test_all_whitespace": {
            "content": "   \n\t  ",
            "open_brackets": "{",
            "close_brackets": "}",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "   \n\t  "
        },
        "test_multiple_bracket_types_extended": {
            "content": "{[(<text>)]}",
            "open_brackets": "{[(<",
            "close_brackets": "}])>",
            "newline_chars": "",
            "tab_str": "    ",
            "expected": "{\n    [\n        (\n            <\n                text\n            >\n        )\n    ]\n}"
        }
    }

    # Get the test case
    test_case = test_cases.get(test_name)
    if not test_case:
        print(f"Test case '{test_name}' not found.")
        return False

    # Extract the parameters
    content = test_case["content"]
    open_brackets = test_case["open_brackets"]
    close_brackets = test_case["close_brackets"]
    newline_chars = test_case["newline_chars"]
    tab_str = test_case["tab_str"]
    expected = test_case["expected"]

    # Print the input
    print(f"\n=== {test_name} ===")
    print(f"INPUT:")
    print(f"Content: {repr(content)}")
    print(f"Open brackets: {repr(open_brackets)}")
    print(f"Close brackets: {repr(close_brackets)}")
    print(f"Newline chars: {repr(newline_chars)}")
    print(f"Tab string: {repr(tab_str)}")

    # Call the function and get the result
    result = apply_indention(content, open_brackets, close_brackets, newline_chars, tab_str)

    # Print the output
    print(f"\nOUTPUT:")
    print(f"Result: {repr(result)}")
    print("\nActual output:")
    print(result)
    print("\nExpected output:")
    print(expected)

    # Check if the result matches the expected
    if result == expected:
        print("\nTest PASSED ✓")
        return True
    else:
        print("\nTest FAILED ✗")
        return False


# Example usage:
if __name__ == "__main__":
    # List of all test names
    test_names = [
        "test_java_output",
        "test_basic_curly_brackets",
        "test_nested_curly_brackets",
        "test_empty_brackets",
        "test_multiple_bracket_types",
        "test_with_semicolons",
        "test_tab_string_variation",
        "test_code_like_content",
        "test_json_structure",
        "test_no_brackets",
        "test_unbalanced_brackets",
        "test_xml_like_content",
        "test_empty_input",
        "test_all_whitespace",
        "test_multiple_bracket_types_extended"
    ]

    # Run all tests and track results
    total_tests = len(test_names)
    passed_tests = 0
    failed_tests = []

    for test_name in test_names:
        if demonstrate_indention_example(test_name):
            passed_tests += 1
        else:
            failed_tests.append(test_name)

    # Print summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print(f"Total tests:  {total_tests}")
    print(f"Passed tests: {passed_tests}")
    print(f"Failed tests: {total_tests - passed_tests}")

    if failed_tests:
        print("\nFailed test cases:")
        for test in failed_tests:
            print(f"- {test}")

    if passed_tests == total_tests:
        print("\nALL TESTS PASSED! ✓")
    else:
        print(f"\n{passed_tests}/{total_tests} TESTS PASSED")
