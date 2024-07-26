from celery import shared_task
import time  # Simulating a time-consuming task

@shared_task
def process_data(data):
    # Simulate processing time (e.g., saving to the database)
    time.sleep(15)  # Simulating a long-running task
    print(f"Processed data: {data}")
    return f"Processed data: {data}"  # This return value can be logged or used elsewhere
