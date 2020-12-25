# GraphQLAPI

## docker
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

如图issue01所示,
## nginx
```
server {
        server_name  itd-api.base-fx.com;

    rewrite ^(.*)$  https://$host$1 permanent;
        # Load configuration files for the default server block.

    }

server {
        server_name  itd-api.base-fx.com;
        listen       443 ssl  ;
        ssl_certificate certs/base-fx.com.pem;
        ssl_certificate_key certs/base-fx.com.key;
        ssl_session_timeout  10m;
	location / {
	    root /docker_data/graphqlapi/www;
	    index index.html;
	}
        location /graphql/ {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header host $host;
            proxy_pass http://127.0.0.1:8086/graphql/;
            client_max_body_size  100M;
        }
        location /admin/ {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header host $host;
            proxy_pass http://127.0.0.1:8086/admin/;
            client_max_body_size  100M;
        }
        location /static/ {
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header host $host;
            proxy_pass http://127.0.0.1:8086/static/;
            client_max_body_size  100M;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }
        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
        access_log  /var/log/nginx/itd-api.access.log  main;
        error_log /var/log/nginx/itd-api.error.log;
    }
```