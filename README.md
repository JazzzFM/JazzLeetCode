# JazzLeetCode
Repositorio para entrenar algoritmos y estructuras de datos resolviendo problemas de LeetCode.

<!-- Badges -->
[![CI](https://github.com/tu-usuario/leetcode-playground/actions/workflows/ci.yml/badge.svg)](https://github.com/tu-usuario/leetcode-playground/actions)
[![Coverage](https://codecov.io/gh/tu-usuario/leetcode-playground/branch/main/graph/badge.svg)](https://codecov.io/gh/tu-usuario/leetcode-playground)
[![Docs](https://img.shields.io/readthedocs/leetcode-playground.svg)](https://leetcode-playground.readthedocs.io)
[![Python](https://img.shields.io/pypi/pyversions/leetcode-playground.svg)](https://pypi.org/project/leetcode-playground)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

# leetcode-playground

> Un entorno modular y profesional para resolver y documentar problemas de LeetCode  
> **Autor:** Jaziel Flores | **Tech Lead & ML Engineer @ Banamex**

---

## 📋 Tabla de Contenidos
1. [Demo](#-demo)  
2. [Características](#-características)  
3. [Instalación y Quickstart](#-instalación-y-quickstart)  
4. [Estructura del Proyecto](#-estructura-del-proyecto)  
5. [Flujo de Trabajo](#-flujo-de-trabajo)  
6. [Documentación](#-documentación)  
7. [Contribuir](#-contribuir)  
8. [Licencia](#-licencia)

---

## 🎬 Demo

![docs-screenshot](./assets/docs_screenshot.png)  
_Un peek de la documentación generada con Sphinx + tema Furo, desplegada en GitHub Pages._

---

## ✨ Características

- 🔍 **Soluciones organizadas** por nivel (*easy*, *medium*, *hard*).  
- 📑 **Documentación viva** con Sphinx + [Furo theme](https://pradyunsg.me/furo/).  
- 🧪 **Tests automáticos** con pytest y 95 %+ de coverage.  
- ⚙️ **CI/CD** listo para GitHub Actions: lint, tests, docs deploy.  
- 📦 **Packageable**: instala tu propio entorno con `pip install .`.  
- 🛠 **Calidad de código**: configurado con Black, Flake8 y MyPy.

---

## 🚀 Instalación y Quickstart

```bash
git clone https://github.com/tu-usuario/leetcode-playground.git
cd leetcode-playground
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Lanzar CI local (lint + tests)
make ci

### Generar docs en local
make -C docs html
### -> Abre docs/_build/html/index.html en tu navegador

## 🗂 Estructura del Proyecto

```bash
JazzLeetCode/
├── .github/
│   └── workflows/ci.yml       # CI: lint, tests, coverage, deploy docs
├── assets/                    # Capturas, diagramas, logos
├── docs/                      # Sphinx + Furo theme
├── problems/
│   ├── easy/                  # Problemas fáciles
│   ├── medium/                # Problemas medios
│   └── hard/                  # Problemas difíciles
├── tests/                     # pytest: parallelizable via xdist
├── leetcode_playground/       # Código reusable como package
├── .flake8
├── .githubpages.yml           # Config para GitHub Pages
├── .gitignore
├── LICENSE
├── Makefile                   # comandos: `make ci`, `make docs`
├── README.md
├── requirements.txt
└── setup.py
```


## 🔄 Flujo de Trabajo
Abrir un Issue describiendo el problema.
**Branch feature/**nombre para aislar cambios.
Agregar solución en problems/{nivel}/.
Escribir tests en tests/{nivel}/.
Actualizar docs si corresponde.
Crear PR: CI correrá lint, tests y build de docs.


## 📖 Documentación
Sitio en: https://JazzLeetCode.readthedocs.io

Basado en Sphinx + extensión sphinx-autodoc-typehints + tema Furo.

Demo de estructura:

```bash
rst
Copiar
Editar
.. toctree::
   :maxdepth: 2
   :caption: Problemas:

   problems.easy
   problems.medium
   problems.hard
```

## 🤝 Contribuir
Haz fork y branch.
Sigue el flujo de trabajo.
Asegúrate de pasar make ci antes de PR.
¡Conecta tu PR con un Issue para trazabilidad!


### 3. Mejoras adicionales

- **Temas y CSS**: en `docs/conf.py`, añade:
```python
  html_theme = "furo"
  html_theme_options = {"light_css_variables": {"color-brand-primary": "#0055A4"}}
```  

Badges generados automáticamente por CI: en el workflow ci.yml exper la URL de cobertura (Codecov) y despliegue de docs en GitHub Pages.
Diagramas embebidos: instala sphinxcontrib-mermaid y añade diagramas de flujo o arquitectura (por ejemplo, mermaid para mostrar la estructura de carpetas).
Capturas y GIFs: en assets/, guarda screenshots y GIFs de “resolver un problema + correr tests” y enzalar en el README.
