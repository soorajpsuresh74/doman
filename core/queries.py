PYTHON_QUERY = """
(function_definition
        name: (identifier) @function_name
        parameters: (parameters) @parameters
        body: (block
            (expression_statement
                (string) @function_docstring
            )?
        ) @function_block)

(class_definition
        name: (identifier) @class_name
        body: (block
            (function_definition
                name: (identifier) @function_name
                body: (block
                    (expression_statement
                        (string) @class_docstring
                    )?
                )
            )*
        ) @class_block
    )
"""
