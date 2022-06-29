from cProfile import label
import prefect
from prefect import task, Flow
from prefect.run_configs import KubernetesRun
from prefect.storage import GitHub

IMAGE='prefecthq/prefect:latest-python3.8'
REPO='RichardDoDeal/prefect_datalearn'
PATH='simple_flow/k8_flow.py'

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello!")


with Flow("hello-docker-flow",
		storage=GitHub(repo=REPO, path=PATH),
		run_config=KubernetesRun(image=IMAGE,
		labels=['k'])) as flow:   
    hello_task()

flow.register(project_name="proj", labels=['k'])