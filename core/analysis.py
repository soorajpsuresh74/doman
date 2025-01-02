from tree_sitter import Tree
from DocmanLogger.docmanLogger import setup_logger
from core.analyzers.KTAnalyzer import KTAnalyzer
from core.analyzers.pyAnalyzer import PYAnalyzer

logger = setup_logger(name="analysis", log_file="logs/analysis.log")


async def analyse_tree(tree: Tree, query, code, language):
    root_node = tree.root_node
    if language == '.py':
        analyser = PYAnalyzer()
        logger.info("Starting the analysis process...")
        await analyser.iterate_to_find_the_functions(root_node, query, code)
        logger.info("Analysis process complete.")

    if language == '.kt':
        analyser = KTAnalyzer()
        logger.info("Starting the analysis process...")
        await analyser.iterate_to_find_the_functions(root_node, query, code)
        logger.info("Analysis process complete.")
