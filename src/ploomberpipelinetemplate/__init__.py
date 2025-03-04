from importlib.metadata  import version as __v

__version__ = __v(__name__)

def hello() -> str:
    return "Hello from ploomberpipelinetemplate!"
