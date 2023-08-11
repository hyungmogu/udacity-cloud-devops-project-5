#!/bin/bash
# Find ClusterIPs of Redis nodes
export REDIS_NODES=$(kubectl get pods  -l app=redis-cluster -n redis -o json | jq -r '.items | map(.status.podIP) | join(":6379 ")'):6379
# Activate the Redis cluster
kubectl exec -it redis-cluster-0 -n redis -- redis-cli --cluster create --cluster-replicas 1 ${REDIS_NODES}
# Check if all went well
for x in $(seq 0 5); do echo "redis-cluster-$x"; kubectl exec redis-cluster-$x -n redis -- redis-cli role; echo; done