import os
import pytest
from lark import Lark, Transformer, v_args

# Correct the file path to locate grammar.lark within the project structure
grammar_file_path = os.path.join(os.path.dirname(__file__), '..', 'grammar.lark')
with open(grammar_file_path) as file:
    grammar = file.read()

class EvalConcat(Transformer):
    @v_args(inline=True)
    def string_literal(self, s):
        return s[1:-1]  # strip quotes

    def concat(self, s1, s2):
        return s1 + s2

@pytest.fixture
def parser():
    return Lark(grammar, parser='lalr', transformer=EvalConcat())

def test_string_literal(parser):
    assert parser.parse('"hello"') == "hello"

def test_concatenation(parser):
    assert parser.parse('"hello" + " world"') == "hello world"

def test_concatenation_with_multiple_terms(parser):
    assert parser.parse('"hello" + " beautiful" + " world"') == "hello beautiful world"

def test_concatenation_with_spaces(parser):
    assert parser.parse('"hello" + " world"') == "hello world"
