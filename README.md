# Docstring Generator

This project aims to automatically generate docstrings for Python and Kotlin functions or classes that do not already have one. It uses predefined templates to add docstrings where they are missing.

## Features

- Automatically generates docstrings for functions in **Python** and **Kotlin**.
- Supports generation of class-level docstrings as well.
- Works by scanning the code for functions or classes that lack docstrings.
- Ensures proper indentation for Kotlin and Python functions.

Note: - Code replacement from files is not yet implemented due to code file security may cause further issues in the code

## Prerequisites

Ensure you have the following prerequisites before setting up the project:

- **Python 3.6+** (for the Python component)
- **Kotlin** (for Kotlin code processing)
- **Google API Key** (for interacting with Google APIs, if necessary)

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   cd repositoryname
