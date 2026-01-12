from locust import HttpUser, task, between

class TenForceLoadTester(HttpUser):
    wait_time = between(1, 2)

    @task
    def check_api_reliability(self):
        with self.client.get("/api/v1/careers", catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                # Integrity Check: Ensure load doesn't cause data truncation 
                if not data.get("jobs"):
                    response.failure("Data Integrity Failure: 'jobs' array is empty under load")
            else:
                response.failure(f"System Degradation: Status {response.status_code}")