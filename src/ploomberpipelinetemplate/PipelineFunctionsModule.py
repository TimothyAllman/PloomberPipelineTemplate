import shutil
from pathlib import Path

from ploomber import DAGConfigurator, SourceLoader
from ploomber.tasks import NotebookRunner, PythonCallable
from ploomber.products import File

from ploomberpipelinetemplate.ConstantsForFilePathsDataModule import _NOTEBOOKS_FOLDER_NAME, _OUTPUT_FOLDER_NAME, _SHARED_VARIABLES_FOLDER_NAME
from ploomberpipelinetemplate.EnvFileDataModule import EnvFileData


def CreatePipeline(
    envParams: EnvFileData,
    clean_up=False,
):

    # create any top level folders
    outputFolderPath = Path("myPipeline", _OUTPUT_FOLDER_NAME)
    if clean_up and outputFolderPath.exists():
        shutil.rmtree(str(outputFolderPath))
    outputFolderPath.mkdir(exist_ok=True)

    myFolderName = envParams.MY_FOLDER

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
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "CommonFunctions.ipynb"),
            "FUNC_1": File(outputFolderPath / myFolderName / _SHARED_VARIABLES_FOLDER_NAME / "FUNC_1.pkl"),
            "FUNC_2": File(outputFolderPath / myFolderName / _SHARED_VARIABLES_FOLDER_NAME / "FUNC_2.pkl"),
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

    taskConstantsFromEnvFileParams = NotebookRunner(
        source=loader["ConstantsFromEnvFileParams.py"],
        params=envParams.__dict__,
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "ConstantsFromEnvFileParams.ipynb"),
            "THING_1": File(outputFolderPath / myFolderName / _SHARED_VARIABLES_FOLDER_NAME / "THING_1.pkl"),
            "THING_2": File(outputFolderPath / myFolderName / _SHARED_VARIABLES_FOLDER_NAME / "THING_2.pkl"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # documentation tasks
    taskDocumentationPdfOfFaq = NotebookRunner(
        source=loader["DocumentationPdfOfFaq.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "DocumentationPdfOfFaq.ipynb"),
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
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "DocumentationPdfOfStepbyStepGuide.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # ingestation/fetch raw data tasks
    taskIngestData1 = NotebookRunner(
        source=loader["IngestData1.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "IngestData1.ipynb"),
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
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "IngestData2.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # transformation/process tasks
    taskProcessToDoCalc1 = NotebookRunner(
        source=loader["ProcessToDoCalc1.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "ProcessToDoCalc1.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskProcessToDoCalc2 = NotebookRunner(
        source=loader["ProcessToDoCalc2.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "ProcessToDoCalc2.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # tasks to create graphs/tables
    taskQuantifyAndSaveLineGraph = NotebookRunner(
        source=loader["QuantifyAndSaveLineGraph.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "QuantifyAndSaveLineGraph.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskQuantifyAndSaveMyTable1 = NotebookRunner(
        source=loader["QuantifyAndSaveMyTable1.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "QuantifyAndSaveMyTable1.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # tasks to build report paga by page
    taskReportMyThingInitiate = NotebookRunner(
        source=loader["ReportMyThingInitiate.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "ReportMyThingInitiate.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    askReportMyThingAddLineGraphPage = NotebookRunner(
        source=loader["ReportMyThingAddLineGraphPage.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "ReportMyThingAddLineGraphPage.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    taskReportMyThingAddTablePage = NotebookRunner(
        source=loader["ReportMyThingAddTablePage.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "ReportMyThingAddTablePage.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # tasks to upload data
    taskTurnResultIntoExcel = NotebookRunner(
        source=loader["TurnResultIntoExcel.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "TurnResultIntoExcel.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    #
    #
    #
    #
    #
    #
    #
    #
    #
    # tasks to upload data
    taskUploadData = NotebookRunner(
        source=loader["UploadData.py"],
        product={
            "nb": File(outputFolderPath / myFolderName / _NOTEBOOKS_FOLDER_NAME / "UploadData.ipynb"),
            # "data": File(out / "clean.csv"),
        },
        dag=myPipelineDag,
        kernelspec_name="python3",
        static_analysis="disable",
        papermill_params={"nest_asyncio": True},
    )

    return myPipelineDag
