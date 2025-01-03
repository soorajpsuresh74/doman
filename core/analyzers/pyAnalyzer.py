from DocmanLogger.docmanLogger import setup_logger
from core.generator.docstringGenarator import docstring_generator_function_for_python

logger = setup_logger(name="PYAnalyzer", log_file="logs/PYAnalyzer.log")


class PYAnalyzer:

    @staticmethod
    async def iterate_to_find_the_functions(root_node, query, code):
        payload = code
        for match_tuple in query.matches(root_node):
            node_dict = match_tuple[1]

            class_name_node = node_dict.get('class_name', [None])[0]
            logger.info(class_name_node)
            function_name_node = node_dict.get('function_name', [None])[0]
            logger.info(function_name_node)

            class_docstring_node = node_dict.get('class_docstring', [None])[0]
            logger.info(class_docstring_node)
            function_docstring_node = node_dict.get('function_docstring', [None])[0]
            logger.info(function_docstring_node)

            class_block_node = node_dict.get('class_block', [None])[0]
            logger.info(class_block_node)
            function_block_node = node_dict.get('function_block', [None])[0]
            logger.info(function_block_node)

            if function_name_node:
                function_name = payload[function_name_node.start_byte:function_name_node.end_byte]
                logger.info(function_name)

                if function_block_node:
                    function_start = function_name_node.start_byte
                    logger.info(function_start)
                    function_end = function_block_node.end_byte
                    logger.info(function_end)
                    full_function_code = payload[function_start:function_end]
                    logger.info(full_function_code)

                    if full_function_code:
                        if not function_docstring_node:
                            generated_docstring = await docstring_generator_function_for_python(full_function_code)
                            logger.info(generated_docstring)
                            first_line = full_function_code.splitlines()[0]
                            indentation = len(first_line) - len(first_line.lstrip())

                            docstring_with_indentation = " " * indentation + "'''\n"
                            for line in generated_docstring.splitlines():
                                docstring_with_indentation += " " * indentation + line + "\n"
                            docstring_with_indentation += " " * indentation + "'''\n"

                            lines = full_function_code.splitlines()
                            for i, line in enumerate(lines):
                                if line.strip() and i > 0:
                                    indentation_level = len(line) - len(line.lstrip())
                                    break
                            else:
                                indentation_level = indentation

                            docstring_lines = docstring_with_indentation.splitlines()
                            docstring_with_indentation = '\n'.join(
                                [' ' * indentation_level + line for line in docstring_lines])

                            updated_function_code = full_function_code.replace("):",
                                                                               f"):\n{docstring_with_indentation}")
                            logger.info(updated_function_code)

                            updated_payload = payload[:function_start] + updated_function_code + payload[function_end:]
                            logger.info(updated_payload)
                            print(f"Updated code with the new docstring:\n{updated_payload}")

            if class_name_node:
                class_name = payload[class_name_node.start_byte:class_name_node.end_byte]
                logger.info(class_name)
                if class_block_node:
                    class_start = class_name_node.start_byte
                    logger.info(class_start)
                    class_end = class_block_node.end_byte
                    logger.info(class_end)
                    full_class_code = payload[class_start:class_end]
                    logger.info(full_class_code)

                    if full_class_code:
                        if not class_docstring_node:
                            generated_docstring = await docstring_generator_function_for_python(full_class_code)
                            logger.info(generated_docstring)
                            first_line = full_class_code.splitlines()[0]
                            logger.info(first_line)
                            indentation = len(first_line) - len(first_line.lstrip())

                            docstring_with_indentation = " " * indentation + "'''\n"
                            for line in generated_docstring.splitlines():
                                docstring_with_indentation += " " * indentation + line + "\n"
                            docstring_with_indentation += " " * indentation + "'''\n"

                            logger.info(docstring_with_indentation)

                            lines = full_class_code.splitlines()
                            for i, line in enumerate(lines):
                                if line.strip() and i > 0:
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
                            logger.info(updated_payload)
                            print(f"Updated code with the new docstring:\n{updated_payload}")
