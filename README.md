# Interview

## Creating environment

The following will install virtualenv and creates environment

```
./create_env.sh
```

## Using environment

- Activating environment

```
. interview/bin/activate
```

- Installing requirements

```
pip install -r requirements.txt
```

## Reading Jupyter Notebook

```
jupyter notebook
```

Open interview.ipnyb


## The ML webservice

```
server.py
```

## Deploying pod

- Installing kubernetes-cli

```
brew install kubernetes-cli
```

- Checking kubectl

```
kubectl version
Client Version: version.Info{Major:"1", Minor:"12", GitVersion:"v1.12.2", GitCommit:"17c77c7898218073f14c8d573582e8d2313dc740", GitTreeState:"clean", BuildDate:"2018-10-30T21:40:58Z", GoVersion:"go1.11.1", Compiler:"gc", Platform:"darwin/amd64"}
```

- Install Minikube

```
brew cask install minikube
```

- Create POD

```
kubectl create -f pods/nginx.yml
```




