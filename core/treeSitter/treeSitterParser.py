from tree_sitter import Parser, Tree

from core.treeSitter.treeSitterLanguage import PYTHON_LANGUAGE, KOTLIN_LANGUAGE, JAVA_LANGUAGE, HTML_LANGUAGE


class DocmanParsers:
    PYTHON_PARSER = Parser(PYTHON_LANGUAGE)
    KOTLIN_PARSER = Parser(KOTLIN_LANGUAGE)
    JAVA_PARSER = Parser(JAVA_LANGUAGE)
    HTML_PARSER = Parser(HTML_LANGUAGE)

    @classmethod
    def parse_python(cls, code: str) -> Tree:
        return cls.PYTHON_PARSER.parse(code.encode(encoding="utf8"))

    @classmethod
    def parse_kotlin(cls, code: str) -> Tree:
        return cls.KOTLIN_PARSER.parse(code.encode(encoding="utf8"))

    @classmethod
    def parse_java(cls, code: str) -> Tree:
        return cls.JAVA_PARSER.parse(code.encode(encoding="utf8"))

    @classmethod
    def parse_html(cls, code: str) -> Tree:
        return cls.HTML_PARSER.parse(code.encode(encoding="utf8"))
