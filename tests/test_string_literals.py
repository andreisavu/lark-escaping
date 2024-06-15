import pytest
from lark import Lark, Transformer
import os

class MyEvaluator(Transformer):
    def string(self, s):
        # Remove the surrounding quotes and unescape
        return s[0][1:-1].encode().decode('unicode_escape')
    
    def collection_name(self, s):
        return s[0]

    def get_expression(self, items):
        # Extract the collection name and the key from the get_expression
        collection_name, key = items
        return {'collection_name': collection_name, 'key': key}

def test_string_literal_parsing():
    grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar.lark')
    with open(grammar_path) as grammar_file:
        grammar = grammar_file.read()
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
        ("'hello\"world\"'", 'hello"world"')  # Single quotes with double quote inside
    ]
    for test_string, expected in test_cases:
        result = parser.parse(test_string)
        assert result == expected

def test_get_expression_parsing():
    grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar.lark')
    with open(grammar_path) as grammar_file:
        grammar = grammar_file.read()
    parser = Lark(grammar, start='get_expression', parser='lalr', transformer=MyEvaluator())
    test_cases = [
        ('GET(User, "dsf223d")', {'collection_name': 'User', 'key': 'dsf223d'}),
        ('GET(User, \'123d423\')', {'collection_name': 'User', 'key': '123d423'}),
    ]
    for test_string, expected in test_cases:
        result = parser.parse(test_string)
        assert result == expected
