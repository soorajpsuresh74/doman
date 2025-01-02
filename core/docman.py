import os

from tree_sitter import Tree

from core.analysis import analyse_tree
from core.treeSitter.treeSitterConfig import LANGUAGE_PARSERS
from core.treeSitter.treeSitterQueryClasses import QUERY_CLASS_MAPPINGS
from DocmanLogger.docmanLogger import setup_logger

logger = setup_logger(name="file_reader", log_file="core.log")


def detect_language_parser_queries(file_path):
    _, ext = os.path.splitext(file_path)
    return LANGUAGE_PARSERS.get(ext.lower()), QUERY_CLASS_MAPPINGS.get(ext.lower()), ext.lower()


def make_syntax_tree(code: str, language_parser) -> Tree:
    return language_parser(code)


class Docman:
    def __init__(self, directory):
        self.directory = directory
        self.process_directory()

    async def process_directory(self):
        if not os.path.exists(self.directory):
            logger.error(f"Directory does not exist: {self.directory}")
            raise Exception(f"Directory does not exist: {self.directory}")

        logger.info(f"Processing directory: {self.directory}")

        for root, dirs, files in os.walk(self.directory):
            if not files:
                continue

            for file_name in files:
                file_path = os.path.join(root, file_name)
                language_parser, query, language = detect_language_parser_queries(file_path)

                if language_parser and query:
                    try:
                        logger.info(f"Processing file: {file_path}")
                        with open(file_path, 'r', encoding="utf-8") as file:
                            code = file.read()

                            tree = make_syntax_tree(code, language_parser)

                            await analyse_tree(tree, query.query, code, language)

                            logger.info(f"Successfully processed file: {file_path}")
                    except Exception as e:
                        logger.error(f"An exception occurred while processing {file_path}: {e}")
                        print(f"An exception occurred in the process directory function as {e}")
