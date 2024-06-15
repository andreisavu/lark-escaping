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
