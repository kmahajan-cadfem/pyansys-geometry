"""Sphinx documentation configuration file."""
from datetime import datetime
import os
from pathlib import Path

from ansys_sphinx_theme import (
    ansys_favicon,
    ansys_logo_white,
    ansys_logo_white_cropped,
    get_autoapi_templates_dir_relative_path,
    get_version_match,
    latex,
    pyansys_logo_black,
    watermark,
)
from sphinx.builders.latex import LaTeXBuilder

from ansys.geometry.core import __version__

LaTeXBuilder.supported_image_types = ["image/png", "image/pdf", "image/svg+xml"]


# Project information
project = "ansys-geometry-core"
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = "ANSYS, Inc."
release = version = __version__
cname = os.getenv("DOCUMENTATION_CNAME", default="geometry.docs.pyansys.com")
switcher_version = get_version_match(__version__)

# Select desired logo, theme, and declare the html title
html_logo = pyansys_logo_black
html_theme = "ansys_sphinx_theme"
html_short_title = html_title = "PyAnsys Geometry"

# specify the location of your github repo
html_context = {
    "github_user": "ansys",
    "github_repo": "pyansys-geometry",
    "github_version": "main",
    "doc_path": "doc/source",
}
html_theme_options = {
    "switcher": {
        "json_url": f"https://{cname}/versions.json",
        "version_match": switcher_version,
    },
    "check_switcher": False,
    "github_url": "https://github.com/ansys/pyansys-geometry",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "collapse_navigation": True,
    "use_edit_page_button": True,
    "additional_breadcrumbs": [
        ("PyAnsys", "https://docs.pyansys.com/"),
    ],
    "icon_links": [
        {
            "name": "Support",
            "url": "https://github.com/ansys/pyansys-geometry/discussions",
            "icon": "fa fa-comment fa-fw",
        },
    ],
}

# Sphinx extensions
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "nbsphinx",
    "myst_parser",
    "jupyter_sphinx",
    "sphinx_design",
    "sphinx_jinja",
    "autoapi.extension",
    "numpydoc",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "pyvista": ("https://docs.pyvista.org/version/stable", None),
    "grpc": ("https://grpc.github.io/grpc/python/", None),
    "pint": ("https://pint.readthedocs.io/en/stable", None),
    "beartype": ("https://beartype.readthedocs.io/en/stable/", None),
    "docker": ("https://docker-py.readthedocs.io/en/stable/", None),
    "pypim": ("https://pypim.docs.pyansys.com/version/stable", None),
    "ansys.geometry.core": (f"https://geometry.docs.pyansys.com/version/{switcher_version}", None),
}

# numpydoc configuration
numpydoc_show_class_members = False
numpydoc_xref_param_type = True

# Consider enabling numpydoc validation. See:
# https://numpydoc.readthedocs.io/en/latest/validation.html#
numpydoc_validate = True
numpydoc_validation_checks = {
    "GL06",  # Found unknown section
    "GL07",  # Sections are in the wrong order.
    # "GL08",  # The object does not have a docstring
    "GL09",  # Deprecation warning should precede extended summary
    "GL10",  # reST directives {directives} must be followed by two colons
    "SS01",  # No summary found
    "SS02",  # Summary does not start with a capital letter
    # "SS03", # Summary does not end with a period
    "SS04",  # Summary contains heading whitespaces
    # "SS05", # Summary must start with infinitive verb, not third person
    "RT02",  # The first line of the Returns section should contain only the
    # type, unless multiple values are being returned"
}

# static path
html_static_path = ["_static"]

html_css_files = [
    "custom.css",
]

html_favicon = ansys_favicon

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".mystnb": "jupyter_notebook",
    ".md": "markdown",
}

# The master toctree document.
master_doc = "index"

# Configuration for Sphinx autoapi
autoapi_type = "python"
autoapi_dirs = ["../../src/ansys"]
autoapi_root = "api"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
]
autoapi_template_dir = get_autoapi_templates_dir_relative_path(Path(__file__))
suppress_warnings = ["autoapi.python_import_resolution"]
autoapi_python_use_implicit_namespaces = True
autoapi_keep_files = True
autoapi_render_in_single_page = ["class", "enum", "exception"]

# Examples gallery customization
nbsphinx_execute = "always"
nbsphinx_custom_formats = {
    ".mystnb": ["jupytext.reads", {"fmt": "mystnb"}],
}
nbsphinx_thumbnails = {
    "examples/01_getting_started/01_math": "_static/thumbnails/101_getting_started.png",
    "examples/01_getting_started/02_units": "_static/thumbnails/101_getting_started.png",
    "examples/01_getting_started/03_sketching": "_static/thumbnails/101_getting_started.png",
    "examples/01_getting_started/04_modeling": "_static/thumbnails/101_getting_started.png",
    "examples/01_getting_started/05_plotter_picker": "_static/thumbnails/101_getting_started.png",  # noqa: E501
    "examples/02_sketching/basic_usage": "_static/thumbnails/basic_usage.png",
    "examples/02_sketching/dynamic_sketch_plane": "_static/thumbnails/dynamic_sketch_plane.png",
    "examples/02_sketching/advanced_sketching_gears": "_static/thumbnails/advanced_sketching_gears.png",  # noqa: E501
    "examples/03_modeling/add_design_material": "_static/thumbnails/add_design_material.png",
    "examples/03_modeling/plate_with_hole": "_static/thumbnails/plate_with_hole.png",
    "examples/03_modeling/tessellation_usage": "_static/thumbnails/tessellation_usage.png",
    "examples/03_modeling/design_organization": "_static/thumbnails/design_organization.png",
    "examples/03_modeling/boolean_operations": "_static/thumbnails/boolean_operations.png",
}
nbsphinx_epilog = """
----

.. admonition:: Download this example

    Download this example as a `Jupyter Notebook <{cname_pref}/{ipynb_file_loc}>`_
    or as a `Python script <{cname_pref}/{py_file_loc}>`_.

""".format(
    cname_pref=f"https://{cname}/version/{switcher_version}",
    ipynb_file_loc="{{ env.docname }}.ipynb",
    py_file_loc="{{ env.docname }}.py",
)

nbsphinx_prolog = """

.. admonition:: Download this example

    Download this example as a `Jupyter Notebook <{cname_pref}/{ipynb_file_loc}>`_
    or as a `Python script <{cname_pref}/{py_file_loc}>`_.

----
""".format(
    cname_pref=f"https://{cname}/version/{switcher_version}",
    ipynb_file_loc="{{ env.docname }}.ipynb",
    py_file_loc="{{ env.docname }}.py",
)

typehints_defaults = "comma"
simplify_optional_unions = False

# additional logos for the latex coverpage
latex_additional_files = [watermark, ansys_logo_white, ansys_logo_white_cropped]

# change the preamble of latex with customized title page
# variables are the title of pdf, watermark
latex_elements = {"preamble": latex.generate_preamble(html_title)}

linkcheck_exclude_documents = ["index", "getting_started/local/index"]

# -- Declare the Jinja context -----------------------------------------------
exclude_patterns = []
BUILD_API = True if os.environ.get("BUILD_API", "true") == "true" else False
if not BUILD_API:
    exclude_patterns.append("autoapi")

BUILD_EXAMPLES = True if os.environ.get("BUILD_EXAMPLES", "true") == "true" else False
if not BUILD_EXAMPLES:
    exclude_patterns.append("examples/**")
    exclude_patterns.append("examples.rst")

jinja_contexts = {
    "main_toctree": {
        "build_api": BUILD_API,
        "build_examples": BUILD_EXAMPLES,
    },
    "linux_containers": {
        "add_windows_warnings": False,
    },
    "windows_containers": {
        "add_windows_warnings": True,
    },
}


def prepare_jinja_env(jinja_env) -> None:
    """
    Customize the jinja env.

    Notes
    -----
    See https://jinja.palletsprojects.com/en/3.0.x/api/#jinja2.Environment
    """
    jinja_env.globals["project_name"] = project


autoapi_prepare_jinja_env = prepare_jinja_env
nitpick_ignore_regex = [
    # Ignore typing
    (r"py:.*", r"optional"),
    (r"py:.*", r"beartype.typing.*"),
    (r"py:.*", r"ansys.geometry.core.typing.*"),
    (r"py:.*", r"Real.*"),
    (r"py:.*", r"SketchObject"),
    # Ignore API package
    (r"py:.*", r"ansys.api.geometry.v0.*"),
    (r"py:.*", r"GRPC.*"),
    (r"py:.*", r"method"),
    # Python std lib errors
    (r"py:obj", r"logging.PercentStyle"),
]
