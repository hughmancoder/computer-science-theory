class Cloud:
    def __init__(self, location, ip, capacity):
        self.location = location
        self.ip = ip
        self.capacity = capacity
        self.id = 0
        self.current_users = 0 # added

class CloudConnector:
    def __init__(self):
        self.clouds = []
        self.cloud_id = {}
        self.current_id = 1
        self.user_cloud = {} # added

    def add_cloud(self, new_cloud):
        new_cloud.id = self.current_id
        self.cloud_id[new_cloud.location] = self.current_id - 1
        self.clouds.append(new_cloud)
        self.current_id += 1

    def connect(self, user_name, user_location):
        if user_location in self.cloud_id:
            id = self.cloud_id[user_location]
            if self.clouds[id].current_users < self.clouds[id].capacity:
                self.clouds[id].current_users += 1
                self.user_cloud[user_name] = id
                return self.clouds[id]
            
        # Find the index of the cloud with the maximum available capacity.
        # The available capacity of a cloud is its total capacity minus the current number of users.
        max_capacity_cloud_id = max(range(len(self.clouds)), key=lambda index: self.clouds[index].capacity - self.clouds[index].current_users)
        if self.clouds[max_capacity_cloud_id].current_users < self.clouds[max_capacity_cloud_id].capacity:
            self.clouds[max_capacity_cloud_id].current_users += 1
            self.user_cloud[user_name] = max_capacity_cloud_id
            return self.clouds[max_capacity_cloud_id]
        return None

    def disconnect(self, user_name):
        if user_name in self.user_cloud:
            cloud_id = self.user_cloud[user_name]
            self.clouds[cloud_id].current_users -= 1
            del self.user_cloud[user_name]