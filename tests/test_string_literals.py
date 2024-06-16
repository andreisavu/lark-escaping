import pytest
from lark import Lark
import os
from mydsl.evaluator import MyEvaluator

def load_grammar():
    grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar.lark')
    with open(grammar_path) as grammar_file:
        return grammar_file.read()

def test_string_literal_parsing():
    grammar = load_grammar()
    parser = Lark(grammar, start='string', parser='lalr', transformer=MyEvaluator())
    test_cases = [
        ('"hello"', "hello"),
        ('"hello\\nworld"', "hello\nworld"),
        ('"hello\\tworld"', "hello\tworld"),
        ('"hello\\"world\\""', 'hello"world"'),
        ("'hello'", "hello"),  # Single quotes test case
        ("'hello\\'world\\''", "hello'world'"),  # Single quotes with escaped single quote
        ('"hello\\\'world\\\'"', "hello\'world\'"),  # Double quotes with escaped single quote
        ("'hello\\\"world\\\"'", 'hello"world"'),  # Single quotes with escaped double quote
        ('"hello\'world\'"', "hello'world'"),  # Double quotes with single quote inside
        ("'hello\"world\"'", 'hello"world"'),  # Single quotes with double quote inside
        ('"hello\\u1234world"', "hello\u1234world"),  # Double quotes with unicode character
        ("'hello\\uABCDworld'", "hello\uABCDworld"),  # Single quotes with unicode character
        ('"\\nNew\\tLine\\u1234"', "\nNew\tLine\u1234"),  # New line, tab, and unicode character
        ("'\\nNew\\tLine\\uABCD'", "\nNew\tLine\uABCD")  # New line, tab, and unicode character in single quotes
    ]
    for test_string, expected in test_cases:
        result = parser.parse(test_string)
        assert result == expected

def test_get_expression_parsing():
    grammar = load_grammar()
    parser = Lark(grammar, start='get_expression', parser='lalr', transformer=MyEvaluator())
    test_cases = [
        ('GET(User, "dsf223d")', {'collection_name': 'User', 'key': 'dsf223d'}),
        ('GET(User, \'123d423\')', {'collection_name': 'User', 'key': '123d423'}),
    ]
    for test_string, expected in test_cases:
        result = parser.parse(test_string)
        assert result == expected
