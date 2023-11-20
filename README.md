# Microservices Setup Guide

**Prerequisites:**
- Node.js installed on your machine
- Minikube installed on your machine
- Kubectl installed on your machine

Follow the steps below to set up and run the microservices environment:

1. Start Minikube:
    ```
    minikube start
    ```
2. Configure Docker to use Minikube's Docker daemon:
    ```
    minikube docker-env | Invoke-Expression
    ```
3. Enable Ingress addon for Minikube:
    ```
    minikube addons enable ingress
    ```
4. Build and deploy the weather microservice:
    ```
    cd '.\microservice1 - weather'
    docker build -t weather-service:v1 .
    kubectl apply -f weather-service.yaml
    ```
5. Build and deploy the news microservice:
    ```
    cd '..\microservice2 - news'
    docker build -t news-service:v1 .
    kubectl apply -f news-service.yaml
    ```
6. Build and deploy the random stats microservice:
    ```
    cd '..\microservice3 - randomstats'
    docker build -t stats-service:v1 .
    kubectl apply -f stats-service.yaml
    ```
7. Check the status of all services:
    ```
    kubectl get all
    ```
8. Deploy Ingress for routing:
    ```
    kubectl apply -f ingress.yaml
    ```
9. Get the Ingress external IP address:
    ```
    kubectl get ingress
    ```
10. Start Minikube tunnel to access services locally:
     ```
     minikube tunnel
     ```

11. To clean up and delete the Minikube cluster when you're done:
     ```
     minikube delete
     ```

Now, you can start the user interface (frontend) by running the following commands:

12. Navigate to the stats dashboard directory:
     ```
     cd '.\stats-dashboard\'
     ```

13. Start the frontend application:
     ```
     npm start
     ```

That's it! Your frontend is ready to interact with the microservices. Enjoy! 🚀👩‍💻👨‍💻
