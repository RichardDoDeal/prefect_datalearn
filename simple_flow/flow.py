import prefect
from prefect import task, Flow

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello DA!")

with Flow("hello-flow") as flow:
    hello_task()

# flow.run()
flow.register(project_name="da_proj")