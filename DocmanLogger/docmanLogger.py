import logging
import logging.handlers
import os


def setup_logger(
        name: str,
        log_file: str,
        console_level: int = logging.WARNING,
        file_level: int = logging.DEBUG,
        fmt: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt: str = "%Y-%m-%d %H:%M:%S",
        max_bytes: int = 5 * 1024 * 1024,  # 5 MB
        backup_count: int = 5
) -> logging.Logger:
    """
    Sets up a logger with both console and rotating file handlers.

    :param name: Name of the logger.
    :param log_file: File path for the log file.
    :param console_level: Logging level for the console handler.
    :param file_level: Logging level for the file handler.
    :param fmt: Log message format.
    :param datefmt: Date format.
    :param max_bytes: Maximum size in bytes before rotating the log file.
    :param backup_count: Number of backup log files to keep.
    :return: Configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(file_level)  # Set to the lowest level to capture all messages
    logger.propagate = False  # Prevent log messages from being propagated to the root logger

    # Create formatters
    formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formatter)

    # File Handler with Rotation
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count, encoding='utf-8'
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(formatter)

    # Avoid adding multiple handlers to the logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


def main():
    # Define log directory and ensure it exists
    LOG_DIR = "logs"
    os.makedirs(LOG_DIR, exist_ok=True)

    # Initialize logger
    logger = setup_logger(
        name="my_application",
        log_file=os.path.join(LOG_DIR, "app.log"),
        console_level=logging.WARNING,
        file_level=logging.DEBUG
    )

    # Example log messages
    logger.debug("Debugging information.")
    logger.info("Informational message.")
    logger.warning("Warning: Something might be wrong.")
    logger.error("Error encountered!")
    logger.critical("Critical issue!")

    # Demonstrate contextual DocmanLogger
    extra = {'user_id': '12345'}
    logger = logging.LoggerAdapter(logger, extra)
    logger.info("User has logged in.")

