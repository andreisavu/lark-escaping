from lark import Transformer

class MyEvaluator(Transformer):
    """
    The MyEvaluator class is responsible for transforming the parsed tree into a more
    useful format that can be easily manipulated and used within the application.
    """
    def string(self, s):
        # Remove the surrounding quotes and unescape
        return s[0][1:-1].encode().decode('unicode_escape')
    
    def collection_name(self, s):
        return s[0]

    def get_expression(self, items):
        # Extract the collection name and the key from the get_expression
        collection_name, key = items
        return {'collection_name': collection_name, 'key': key}
