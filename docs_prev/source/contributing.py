# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3.9
#     language: python
#     name: py39
# ---

# %% [markdown]
# ## Writing documentation and user guides
#
# We use [Sphinx](https://www.sphinx-doc.org/en/master/), and a few add-ons, most importantly [nbsphinx](https://nbsphinx.readthedocs.io/) so we can write using Jupyter notebooks.

# %% [markdown]
# ### Organisation
#
# The documentation mainly lives in the docs/source folder. This is the "relevant" high-level folder structure for the documentation:
#
# ```
# ├── docs                      <- Documentation folder.
# │   ├── build                 <- Placeholder for built docs.
# │   ├── source                <- Documentation scripts.
# │   │   ├── api               <- Files to render docstrings.
# │   │   ├── basics / websites <- Walkthrough notebooks.
# │   │   ├── index.rst         <- Main file.
# │   │   ├── contributing...   <- How to docs.
# │   │   └── etc.
# │   └── etc.                  <- Other necessary files.
# │
# └── etc.
# ```

# %% [markdown]
# ### Serving documentation locally
#
# It can be helpful to build and serve the documentation locally in order to QA any changes. 
#
# To do so:
#
# 1. Clone the repository
#    ```
#    git clone git@github.com:cmagovuk/selene-core.git
#    ```
# 2. Activate your relevant environment
#    ```
#    conda activate py39
#    ```
# 3. Navigate to the docs directory (the one with the Makefile), install requirements, pull submodules and build the html
#    ```
#    cd selene-core/docs
#    make requirements
#    make html
#    ```
# 4. Run the docker image which serves the documentation
#    ```
#    make serve-start
#    ```
# 5. For CMA users, in the browser URL, navigate to https://data.cma.gov.uk/leda/user/USERNAME/INSTANCENAME/proxy/80/index.html
# 6. Update the documentation, re-run `make html` and refresh the page.
# 7. To stop the container, run 
#    ```
#    make serve-stop
#    ````
