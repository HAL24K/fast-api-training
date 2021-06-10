# How to demo the sequence generator

1. > docker-compose -f docker-compose-v1.yml up --build
2. Visit browser page http://localhost:8501 and experiment adding and submitting numbers to the sequence.
3. ```CTRL-C to exit docker-compose```
4. > docker-compose -f docker-compose-v1.yml up --build --scale web_api=3
5. Revist the browser and repeat the experiment - inconsistencies should be evident
6. > docker-compose -f docker-compose-v2.yml up --build --scale web_api=3
7. Repeat the expeiment again and you should see the REDIS database solves the problem

## Tidying up

### Remove any leftover containers
> docker rm $(docker ps --filter status=exited -q)

### Remove all dangling images
> docker system prune