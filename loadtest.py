''''Load Test Script for the Flask App'''
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    ''' Test load test for the API '''
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        ''' Test load test for the API '''
        self.client.get("/")
