import shutil
from pathlib import Path

from ploomber import DAGConfigurator, SourceLoader
from ploomber.tasks import NotebookRunner, PythonCallable
from ploomber.products import File


def CreatePipeline(clean_up=True):

    # create any top level folders
    # we will save all output here
    out = Path("myPipeline", "output")
    if clean_up and out.exists():
        shutil.rmtree(str(out))
    out.mkdir(exist_ok=True)

    # then configure the pipeline/dag
    cfg = DAGConfigurator()
    cfg.params.hot_reload = True
    myPipelineDag = cfg.create()

    # source loaders allows us to easily load files from modules
    loader = SourceLoader(
        path="myPipeline/tasks",
        # module="ploomber_basic",
    )

    # # our first task is a Python function, it outputs a csv file
    # load = PythonCallable(functions.load, product=File(out / "data.csv"), dag=dag, name="load")

    # Our second task is a Python script. Since we are using the NotebookRunner
    # task, it will convert it to a Jupyter notebook before execution (you can
    # still pass a .ipynb file). We recommend using .py files as they are
    # easier to merge with git
    taskCommonFunctions = NotebookRunner(
        source=loader["CommonFunctions.py"],
        # this task generates two files, the .ipynb
        # output notebook and another csv file
        product={
            "nb": File(out / "CommonFunctions.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        # you can run any language supported by Jupyter
        # by specifying which kernel to use
        kernelspec_name="python3",
        # by enabling this option, a few checks are
        # performed on your code before running the
        # notebook. Given that jupyter notebooks are run
        # cell by cell, something as simple as a syntax
        # error will be discovered until such cell is run,
        # this gives you immediate feedback
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskConstantsFromFilePaths = NotebookRunner(
        source=loader["ConstantsFromFilePaths.py"],
        product={
            "nb": File(out / "ConstantsFromFilePaths.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskConstantsFromEnvFileParams = NotebookRunner(
        source=loader["ConstantsFromEnvFileParams.py"],
        product={
            "nb": File(out / "ConstantsFromEnvFileParams.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskDocumentationPdfOfFaq = NotebookRunner(
        source=loader["DocumentationPdfOfFaq.py"],
        product={
            "nb": File(out / "DocumentationPdfOfFaq.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskDocumentationPdfOfStepbyStepGuide = NotebookRunner(
        source=loader["DocumentationPdfOfStepbyStepGuide.py"],
        product={
            "nb": File(out / "DocumentationPdfOfStepbyStepGuide.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskIngestData1 = NotebookRunner(
        source=loader["IngestData1.py"],
        product={
            "nb": File(out / "IngestData1.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskIngestData2 = NotebookRunner(
        source=loader["IngestData2.py"],
        product={
            "nb": File(out / "IngestData2.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    return myPipelineDag
