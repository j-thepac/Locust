# locust -u 1 -r 1 -t 5s --only-summary -f performance.py #--headless 
# locust -u 1 -r 1 -t 5s --headless --only-summary -f performance.py
from locust import SequentialTaskSet,HttpUser,task,constant

class AllTasks(SequentialTaskSet):

    def on_start(self): #on_stop
        print("setup")  #teardown

    @task
    def get_india(self):
        resp=self.client.get("/india")
        print(resp.status_code, resp.text , resp.json())
        print('india')
        
    @task
    def get_china(self):
        self.client.get("/china")
        print('china') 

class Loadtest(HttpUser):
    host,tasks,wait_time="https://restcountries.com/v3.1/name",[AllTasks],constant(1)


