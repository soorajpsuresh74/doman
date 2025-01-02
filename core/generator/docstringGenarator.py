import logging
import re

import google.generativeai as _genai
from config import KEY

_genai.configure(api_key=KEY)
model = _genai.GenerativeModel('gemini-1.5-flash')


async def docstring_generator_function(full_function_code):
    try:
        prompt = (f"Generate a clean, concise, and properly formatted docstring for the following function:\n\n"
                  f"{full_function_code}\n\nReturn only the docstring as a single line, with no other text or code.")

        response = model.generate_content(prompt)

        docstring = response.candidates[0].content.parts[0].text
        logging.info(f"Generated Docstring: {docstring}")

        match = re.search(r'"""(.*?)"""', docstring, re.DOTALL)

        if match:
            clean_result = match.group(1).strip()
            logging.info(f"Generated cleaned Docstring: {clean_result}")
            return clean_result

    except Exception as e:
        logging.error(f"An error occurred during docstring generation: {e}")
        return "TODO: Add a docstring here."
