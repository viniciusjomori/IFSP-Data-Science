"""Executa os notebooks do projeto, em ordem, usando kernels limpos."""

import asyncio
from pathlib import Path
import sys
import warnings

import nbformat
from nbclient import NotebookClient


if sys.platform == "win32":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


NOTEBOOKS = [
    Path("01_normalize.ipynb"),
    Path("02_clustering.ipynb"),
    Path("03_supervised.ipynb"),
]


for notebook_path in NOTEBOOKS:
    print(f"Executando {notebook_path}...")
    notebook = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(Path.cwd())}},
    )
    client.execute()
    nbformat.write(notebook, notebook_path)
    print(f"Concluído: {notebook_path}")
