from ploomberpipelinetemplate.EnvFileDataModule import EnvFileData
from ploomberpipelinetemplate.PipelineFunctionsModule import CreatePipeline


myEnvDictionary = EnvFileData(
    env_thing_1="this_thing",
    env_thing_2="prod",
)

dag = CreatePipeline(
    envParams=myEnvDictionary,
)

dag.build(
    force=True,
)
