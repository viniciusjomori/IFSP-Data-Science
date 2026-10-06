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


PROJECT_ROOT = Path(__file__).resolve().parent
NOTEBOOKS = [
    PROJECT_ROOT / "notebooks" / "01_data_preparation.ipynb",
    PROJECT_ROOT / "notebooks" / "02_kmeans_clustering.ipynb",
    PROJECT_ROOT / "notebooks" / "03_decision_tree_classification.ipynb",
]


for notebook_path in NOTEBOOKS:
    print(f"Executando {notebook_path.relative_to(PROJECT_ROOT)}...")
    notebook = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(PROJECT_ROOT)}},
    )
    client.execute()
    nbformat.write(notebook, notebook_path)
    print(f"Concluído: {notebook_path.relative_to(PROJECT_ROOT)}")
