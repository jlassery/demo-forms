## Sobre
 
Este repositório hospeda uma aplicação Python em forma de formulário, integrada com Banco de dados MongoDB, ambos para serem usado nos Openshift. 

-Utilizado:
* Python3.6
* Flask - Framework Web
* PyMongo - MongoDB Interface
* ContainerImage MongoExpress - Interface Web MongoDB (https://hub.docker.com/_/mongo-express)
* Atom como plataforma de código e integração com git
* Openshift 4.4
* Inspirado na app Python desenvolvida por Davi Garcia


## Capacidades

* Criação de um aplicativo Python usando Source-to-Image
* Criação de um database a partir do Catálogo do OCP
* Uso de Secret para personalizar o comportamento do aplicativo em relação ao BD
* Escalabilidade horizontal do componente de frontend (web), sem afetar o componente de backend (db)
* Uso de Webhook(em fase de teste)

## Roteiro de Demonstração

1. Crie um projeto para hospedar o aplicativo e seus recursos:
```
$ oc new-project "nome do projeto"
```
2. Crie o componente de frontend (web) do aplicativo:
```
Pode ser usada a interface Web do OCP e escolher fazer o deploy por S2I(puxando do github) (não esqueça de selecionar a opção "DeploymentConfig")
```
3. Exponha uma rota pública para o componente web e teste-o:
```
Ao fazer deploy da app, selecione expor a rota.
```
4. Crie o componente Banco de dados:
```
Na aba de "Developer" selecione "Database", em seguida selecione "MongoDB(persistent storage)
```

5. Conecte o Banco com a aplicação
```
Na aba de "Developer" selecione "Database", em seguida selecione "MongoDB(persistent storage)
```

continua...em fase de desenvolvimento...
