# Visualizing Kubernetes Clusters with Weave Scope
To visualize inbound and outbound connections to a Kubernetes cluster,
you can use [Weave Scope](https://www.weave.works/oss/scope/).

## Limitations
* It doesn't visualize east-west traffic within the cluster at the pod level. The container level seems to have this view.
* It doesn't show inbound requests from outside the cluster if it is passed through a load balancer.
* You can't export it. It's served on a web page.

## Instructions
1. Connect to your Kubernetes cluster.
1. Download the [Weave Scope manifest](https://cloud.weave.works/k8s/scope.yaml). Note: While the tool is produced by Weave 
   Networks, it still works for Calico.
1. Once you've downloaded the scope manifest, apply it to the Kubernetes cluster. This will create all of the agents to scrape 
   the information.
   ```
   kubectl apply -f scope.yaml
   ```
1. Now that the agents are running, you need to port-forward to see the dashboard.
   ```
   kubectl port-forward -n weave "$(kubectl get -n weave pod --selector=weave-scope-component=app -o jsonpath='{.items..metadata.name}')" 4040
   ```
1. Go to http://localhost:4040 and you will see a dashboard.

## Dashboard
You can change up the views to see the connections at the container level,
which give far more granularity in which connections are happening.
In particular, check out Containers → by DNS Name.

You can also show dependencies on the process level by
switching to Process → by name.

## Clean-up
To clean up, delete the resources.

```
kubectl delete -f scope.yaml
```

## References
* https://www.weave.works/docs/scope/latest/installing/#k8s
* https://www.projectcalico.org/calico-and-weave-scope/