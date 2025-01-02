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

KOTLIN_QUERY = """
(class_declaration
  name: (identifier) @class_name
  (class_body
    (block_comment)? @class_docstring
    (function_declaration
      (block_comment)? @function_docstring
      name: (identifier) @function_name
      (function_body
        (block)? @function_body
      )
    )*
  ) @class_body
)
"""