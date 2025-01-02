from core.treeSitter.treeSitterParser import DocmanParsers

LANGUAGE_PARSERS = {
    '.py': DocmanParsers.parse_python,
    '.kt': DocmanParsers.parse_kotlin,
    '.java': DocmanParsers.parse_java,
    '.html': DocmanParsers.parse_html,
}