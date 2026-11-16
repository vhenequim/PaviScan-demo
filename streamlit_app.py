"""Entrada do Streamlit Community Cloud: poe src/ no caminho e roda o painel."""

import runpy
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ / "src"))
runpy.run_path(str(RAIZ / "src" / "paviscan" / "painel" / "app.py"), run_name="__main__")
