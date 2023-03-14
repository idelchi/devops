from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kuberenetes!"
    
import threading
import time
import sys
import logging



def start():
    app.run(host="0.0.0.0", port=9990, debug=False)
    
if __name__ == "__main__":

    logging.basicConfig(format='%(asctime)s %(message)s')

    logging.warning("Starting up!")
    x = threading.Thread(target=start, daemon=True)
    x.start()
    time.sleep(120)
    logging.warning("Exiting badly!")
    sys.exit(1)


# docker compose build 

# minikube image load kubernetes/app:demo

kubectl delete service --all
kubectl delete deployment --all
kubectl delete events --all
kubectl delete pods --all





kubectl create deployment hello-kubernetes --image=kubernetes/app:demo  --replicas=1 -- python3 main.py
# kubectl expose deployment hello-kubernetes --type=LoadBalancer --port=9990
# minikube service hello-kubernetes

# NodePort not working
# kubectl expose deployment hello-kubernetes --type=NodePort --port=9990


# kubectl get pods
# kubectl describe pod


# kubectl get events
# kubectl get services

# curl http://localhost:8001/api/v1/namespaces/default/pods/hello-kubernetes-7556d695cb-fkq55/proxy/