# kube-bench

This runs the CIS benchmarks against a Kubernetes cluster by
deploying kube-bench as jobs.

## Instructions
1. Target your Kubernetes cluster.
1. Create the `audit` namespace.
   ```
   kubectl apply -f namespace.yaml
   ```
1. Run the master & node kube-bench jobs.
   ```
   kubectl apply -f master.yaml
   kubectl apply -f node.yaml
   ```
1. To retrieve the log output, you can run the following.
   ```
   kubectl logs job/kube-bench-master -n audit
   kubectl logs job/kube-bench-node -n audit
   ```

## Useful Tasks
Some tasks have been created that handle the save
and comparison of logs. These are located under the
`tasks` directory using the `invoke` task framework.

To save the kube-bench output, run:
```
invoke logs.save kube-bench-[master | node] audit [ output file name ]
```

To compare two output files, run:
```
invoke logs.compare [ desired state file ] [ current state file ]
```

## References
* https://github.com/aquasecurity/kube-bench