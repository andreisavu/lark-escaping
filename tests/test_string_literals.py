import pytest
from lark import Lark, Transformer
import os

class StringTransformer(Transformer):
    def string(self, s):
        # Remove the surrounding quotes and unescape
        return s[0][1:-1].encode().decode('unicode_escape')

def test_string_literal_parsing():
    grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar.lark')
    with open(grammar_path) as grammar_file:
        grammar = grammar_file.read()
    parser = Lark(grammar, start='string', parser='lalr', transformer=StringTransformer())
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
