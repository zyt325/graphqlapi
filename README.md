# GraphQLAPI

```bazaar
git clone https://xxx/graphqlapi.git
cd graphqlapi
gunicorn gpapi.wsgi -c gunicorn_config.py
```


```
cd graphqlapi
docker build -t graphiql:2.2.3 .
docker-compose up -d
```