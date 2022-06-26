from cProfile import label
import prefect
from prefect import task, Flow
from prefect.run_configs import DockerRun
from prefect.executors import LocalDaskExecutor

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello DA!")


with Flow("hello-docker-flow",
		run_config=DockerRun(image='prefecthq/prefect:latest', labels=['docker'])) as flow:   
    hello_task()

flow.register(project_name="da_proj", labels=['docker'])