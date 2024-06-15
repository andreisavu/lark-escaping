import pytest
from lark import Lark
import os

def test_string_literal_parsing():
    grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar.lark')
    with open(grammar_path) as grammar_file:
        grammar = grammar_file.read()
    parser = Lark(grammar, start='string')
    test_string = '"hello"'
    parse_tree = parser.parse(test_string)
    assert str(parse_tree) == "Tree('string', [Token('STRING', '\"hello\"')])"
