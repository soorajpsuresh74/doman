import logging
from tree_sitter import Tree
from core.generator.docstringGenarator import docstring_generator_function

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class PYAnalyzer:
    @staticmethod
    async def generate_and_insert_docstring(tree, node, block_type):
        pass

    @staticmethod
    async def iterate_to_find_the_functions(root_node, query, code):
        payload = code
        for match_tuple in query.matches(root_node):
            node_dict = match_tuple[1]

            class_name_node = node_dict.get('class_name', [None])[0]
            function_name_node = node_dict.get('function_name', [None])[0]

            class_docstring_node = node_dict.get('class_docstring', [None])[0]
            function_docstring_node = node_dict.get('function_docstring', [None])[0]

            class_block_node = node_dict.get('class_block', [None])[0]
            function_block_node = node_dict.get('function_block', [None])[0]

            if function_name_node:
                function_name = payload[function_name_node.start_byte:function_name_node.end_byte]
                if function_block_node:
                    function_start = function_name_node.start_byte
                    function_end = function_block_node.end_byte
                    full_function_code = payload[function_start:function_end]

                    if full_function_code:
                        if not function_docstring_node:
                            generated_docstring = await docstring_generator_function(full_function_code)
                            first_line = full_function_code.splitlines()[0]
                            indentation = len(first_line) - len(first_line.lstrip())

                            # Format docstring with indentation
                            docstring_with_indentation = " " * indentation + "'''\n"
                            for line in generated_docstring.splitlines():
                                docstring_with_indentation += " " * indentation + line + "\n"
                            docstring_with_indentation += " " * indentation + "'''\n"

                            # Insert docstring into the code
                            lines = full_function_code.splitlines()
                            for i, line in enumerate(lines):
                                if line.strip() and i > 0:  # Find the first non-empty line after the signature
                                    indentation_level = len(line) - len(line.lstrip())
                                    break
                            else:
                                indentation_level = indentation  # If no non-empty line found, use signature indentation

                            docstring_lines = docstring_with_indentation.splitlines()
                            docstring_with_indentation = '\n'.join(
                                [' ' * indentation_level + line for line in docstring_lines])

                            updated_function_code = full_function_code.replace("):",
                                                                               f"):\n{docstring_with_indentation}")

                            updated_payload = payload[:function_start] + updated_function_code + payload[function_end:]
                            print(f"Updated code with the new docstring:\n{updated_payload}")

            if class_name_node:
                class_name = payload[class_name_node.start_byte:class_name_node.end_byte]
                if class_block_node:
                    class_start = class_name_node.start_byte
                    class_end = class_block_node.end_byte
                    full_class_code = payload[class_start:class_end]

                    if full_class_code:
                        if not class_docstring_node:
                            prompt = f"Generate a docstring for the following Python function:\n\n{full_class_code}"
                            generated_docstring = "This is a sample docstring.\nIt spans multiple lines.\n"
                            first_line = full_class_code.splitlines()[0]
                            indentation = len(first_line) - len(first_line.lstrip())

                            docstring_with_indentation = " " * indentation + "'''\n"
                            for line in generated_docstring.splitlines():
                                docstring_with_indentation += " " * indentation + line + "\n"
                            docstring_with_indentation += " " * indentation + "'''\n"

                            lines = full_class_code.splitlines()
                            for i, line in enumerate(lines):
                                if line.strip() and i > 0:  # Find the first non-empty line after the signature
                                    indentation_level = len(line) - len(line.lstrip())
                                    break
                            else:
                                indentation_level = indentation

                            docstring_lines = docstring_with_indentation.splitlines()
                            docstring_with_indentation = '\n'.join(
                                [' ' * indentation_level + line for line in docstring_lines])

                            updated_function_code = full_class_code.replace(":",
                                                                            f"):\n{docstring_with_indentation}")
                            updated_payload = payload[:class_start] + updated_function_code + payload[class_end:]
                            print(f"Updated code with the new docstring:\n{updated_payload}")


async def analyse_tree(tree: Tree, query, code, language):
    root_node = tree.root_node
    if language == '.py':
        analyser = PYAnalyzer()
        logging.info("Starting the analysis process...")
        await analyser.iterate_to_find_the_functions(root_node, query, code)
        logging.info("Analysis process complete.")
