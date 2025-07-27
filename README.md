event hooks
custom events
    1. Decoupling Logic from Tasks
    2. Centralized Control
    3. Integration with Locust’s Reporting
    4. Async
    5. Support Plugins
logging ,parameterisation - Use Python packages
Config
Command Line(headless)
Sequentials Task
support Distributed Load testing Master-slave (Eg: Spark )
docker run -it -d -p 8089:8089 -v $PWD:/home/apps -w /home/apps locustio/locust -f test.py\
-- html result.html -r 1 -u 1 -t 10s --headless --only-summary
# localhost:8089
#docker ps 
# docker exec -it container_id bash