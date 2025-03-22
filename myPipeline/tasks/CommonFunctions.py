# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %%
# your code here...

# %%
from pathlib import Path
import cloudpickle


# %%
def FUNC_1():
    return 1


# pickle/store stuff to use later
Path(str(product["FUNC_1"])).parent.mkdir(exist_ok=True, parents=True)
Path(str(product["FUNC_1"])).write_bytes(cloudpickle.dumps(FUNC_1))
# print output
FUNC_1


# %%
def FUNC_2():
    return "func 2"


# pickle/store stuff to use later
Path(str(product["FUNC_2"])).parent.mkdir(exist_ok=True, parents=True)
Path(str(product["FUNC_2"])).write_bytes(cloudpickle.dumps(FUNC_2))
# print output
FUNC_2
