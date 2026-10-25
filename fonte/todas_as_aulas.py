# -*- coding: utf-8 -*-
"""Os `conteudo_aN.py` que existem, na ordem. Um lugar so, para os guardas e o
build nunca olharem para listas diferentes (antes cada um importava a Aula 1 e
mais nada, e uma aula nova passava sem guarda nenhum)."""
import glob, importlib, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))


def modulos():
    ns = sorted(int(re.search(r"conteudo_a(\d+)\.py", p).group(1))
                for p in glob.glob(os.path.join(AQUI, "conteudo_a*.py")))
    return [importlib.import_module(f"conteudo_a{n}") for n in ns]


def aulas():
    return [m.AULA for m in modulos()]
