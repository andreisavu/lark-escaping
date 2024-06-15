import pytest
from pypika import Query, Table, Field

def test_pypika_encoding_string_literals():
    # Define a table
    users = Table('users')
    
    # Construct a query with string literals containing both single and double quotes
    query = Query.from_(users).select('*').where(
        (Field('name') == "O'Reilly") & (Field('comment') == 'He said "Hello, World!"')
    )
    
    # Expected SQL query
    expected_query = "SELECT * FROM \"users\" WHERE \"name\"='O''Reilly' AND \"comment\"='He said \"Hello, World!\"'"
    
    # Assert the generated SQL query matches the expected output
    assert str(query) == expected_query

def test_pypika_encoding_with_new_lines():
    # Define a table
    users = Table('users')
    
    # Construct a query with string literals containing new lines
    query = Query.from_(users).select('*').where(
        Field('bio') == 'Line1\nLine2'
    )
    
    # Expected SQL query
    expected_query = "SELECT * FROM \"users\" WHERE \"bio\"='Line1\\nLine2'"
    
    # Assert the generated SQL query matches the expected output
    assert str(query) == expected_query

def test_pypika_encoding_with_tabs():
    # Define a table
    users = Table('users')
    
    # Construct a query with string literals containing tabs
    query = Query.from_(users).select('*').where(
        Field('preferences') == 'Tab\tSeparated'
    )
    
    # Expected SQL query
    expected_query = "SELECT * FROM \"users\" WHERE \"preferences\"='Tab\\tSeparated'"
    
    # Assert the generated SQL query matches the expected output
    assert str(query) == expected_query

def test_pypika_encoding_with_arbitrary_unicode():
    # Define a table
    users = Table('users')
    
    # Construct a query with string literals containing arbitrary unicode characters
    query = Query.from_(users).select('*').where(
        Field('emoji') == 'Unicode Character \u1234'
    )
    
    # Expected SQL query
    expected_query = "SELECT * FROM \"users\" WHERE \"emoji\"='Unicode Character \u1234'"
    
    # Assert the generated SQL query matches the expected output
    assert str(query) == expected_query
