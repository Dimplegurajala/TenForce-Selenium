from locust import HttpUser, task, between

class TenForceApiUser(HttpUser):
    wait_time = between(1, 2) # Simulating human-like pauses with 1 to 2 sec pacing

    @task
    def check_careers_api(self):
        self.client.get("/api/careers", name="Get Careers List")