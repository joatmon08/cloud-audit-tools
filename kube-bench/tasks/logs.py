from invoke import task

@task
def save(ctx, name, namespace, outfile):
    ctx.run("kubectl logs job/{} -n {} > {}".format(name, namespace, outfile))

@task
def compare(ctx, desired_file, actual_file):
    with open(desired_file, 'r') as f:
        desired = f.read()
    with open(actual_file, 'r') as f:
        actual = f.read()
    assert desired == actual, "Current kube-bench state does not match the desired."