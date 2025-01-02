from core.docman import Docman
import asyncio


async def start_docman():
    docman = Docman(r"C:\Users\bornd\Desktop\New folder")
    # docman = Docman(r"core")
    await docman.process_directory()


async def main():
    await start_docman()


if __name__ == "__main__":
    asyncio.run(main())
