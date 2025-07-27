[Locust Tutorial Video](https://www.youtube.com/playlist?list=PLJ9A48W0kpRKMCzJARCObgJs3SinOewp5)


### Import Topics
1. event hooks
2. custom events
        1. Decoupling Logic from Tasks
        2. Centralized Control
        3. Integration with Locust’s Reporting
        4. Async
        5. Support Plugins
3. logging ,parameterisation - Use Python packages
4. Configuration Files
5.  Command Line(headless)
6.  Sequentials Task
7.  support Distributed Load testing Master-slave (Eg: Spark )


    docker run -it -d -p 8089:8089 -v $PWD:/home/apps -w /home/apps locustio/locust -f test.py\
    -- html result.html -r 1 -u 1 -t 10s --headless --only-summary
    # localhost:8089
    #docker ps 
    # docker exec -it container_id bash