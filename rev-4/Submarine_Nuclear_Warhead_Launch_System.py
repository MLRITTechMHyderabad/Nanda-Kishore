
import json
import logging
from authorization import LaunchAuthorizationSystem


logging.basicConfig(level=logging.INFO)


class Warhead:

    def __init__(self, warhead_id, type, yield_kt):
        self.warhead_id = warhead_id
        self.type = type
        self.yield_kt = yield_kt  # Yield in kilotons

    def get_info(self):
        return f"Type: {self.type}, Yield: {self.yield_kt}kt"


class Submarine:

    def __init__(self, name, warhead_data):
        self.name = name
        self.warheads = [Warhead(**w) for w in warhead_data]
        self.unauthorized_attempts = 0

    def authorize_launch(self, auth_code):
        if self.unauthorized_attempts >= 3:
            logging.error("Self-destruct triggered due to 3 unauthorized attempts.")
            return

        if LaunchAuthorizationSystem.validate_code(auth_code):
            logging.info(f"Launch authorized for {self.name}. Preparing to launch SLBM...")
            self.launch_missile()
        else:
            self.unauthorized_attempts += 1
            logging.error("Launch Authorization Failed! Access Denied.")

    def launch_missile(self):
        warhead = self.warheads[0]
        logging.info(f"🚀 Missile launched carrying Warhead {warhead.warhead_id}: {warhead.get_info()}!")


warhead_json = '''
[
    {"warhead_id": "W001", "type": "Thermonuclear", "yield_kt": 1000},
    {"warhead_id": "W002", "type": "Tactical", "yield_kt": 300}
]
'''

warhead_data = json.loads(warhead_json)

submarine = Submarine("USS Trident", warhead_data)

submarine.authorize_launch("INVALID-123")

submarine.authorize_launch("AUTH-XYZ123-4567-SECURE")

submarine.authorize_launch("INVALID-456")
submarine.authorize_launch("INVALID-789")
submarine.authorize_launch("INVALID-012")
