from DocmanLogger.docmanLogger import setup_logger
from core.generator.docstringGenarator import docstring_generator_function_for_kotlin

logger = setup_logger(name="KTAnalyzer", log_file="logs/KTAnalyzer.log")


class KTAnalyzer:
    @staticmethod
    async def iterate_to_find_the_functions(root_node, query, code):
        contents = code
        for match_tuple in query.matches(root_node):
            node_dict = match_tuple[1]

            class_name_node = node_dict.get('class_name', [None])[0]
            function_name_node = node_dict.get('function_name', [None])[0]

            class_docstring_node = node_dict.get('class_docstring', [None])[0]
            function_docstring_node = node_dict.get('function_docstring', [None])[0]

            class_block_node = node_dict.get('class_body', [None])[0]
            function_block_node = node_dict.get('function_body', [None])[0]

            if class_name_node:
                class_name = contents[class_name_node.start_byte:class_name_node.end_byte]
                logger.info(class_name)

                if class_block_node:
                    class_start = class_name_node.start_byte
                    logger.info(class_start)

                    class_end = class_block_node.end_byte
                    logger.info(class_end)

                    full_class_code = contents[class_start:class_end]

                    if full_class_code:
                        if not class_docstring_node:
                            generated_docstring = await docstring_generator_function_for_kotlin(full_class_code)
                            logger.info(generated_docstring)
                            first_line = full_class_code.splitlines()[0]
                            logger.info(first_line)
                            indentation = len(first_line) - len(first_line.lstrip())

                            docstring_with_indentation = " " * indentation + "/*\n"
                            for line in generated_docstring.splitlines():
                                docstring_with_indentation += " " * indentation + line + "\n"
                            docstring_with_indentation += " " * indentation + "*/\n"

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

                            updated_class_code = full_class_code.replace(
                                "{", f"{{\n{docstring_with_indentation}")

                            logger.info(updated_class_code)

            if function_name_node:
                function_name = contents[function_name_node.start_byte:function_name_node.end_byte]
                logger.info(function_name)

                if function_block_node:
                    function_start = function_name_node.start_byte
                    logger.info(function_start)
                    function_end = function_block_node.end_byte
                    logger.info(function_end)

                    full_function_code = contents[function_start:function_end]
                    logger.info(full_function_code)

                    if full_function_code:
                        if not function_docstring_node:
                            generated_docstring = await docstring_generator_function_for_kotlin(full_function_code)
                            logger.info(generated_docstring)
                            first_line = full_function_code.splitlines()[0]
                            logger.info(first_line)
                            indentation = len(first_line) - len(first_line.lstrip())

                            docstring_with_indentation = " " * indentation + "/*\n"
                            for line in generated_docstring.splitlines():
                                docstring_with_indentation += " " * indentation + line + "\n"
                            docstring_with_indentation += " " * indentation + "*/\n"

                            lines = full_function_code.splitlines()
                            logger.info(docstring_with_indentation)
                            for i, line in enumerate(lines):
                                if line.strip() and i > 0:
                                    indentation_level = len(line) - len(line.lstrip())
                                    break
                            else:
                                indentation_level = indentation

                            docstring_lines = docstring_with_indentation.splitlines()
                            docstring_with_indentation = '\n'.join(
                                [' ' * indentation_level + line for line in docstring_lines])

                            updated_function_code = full_function_code.replace(
                                "{", f"{{\n{docstring_with_indentation}")

                            logger.info(updated_function_code)
                            print(updated_function_code)
