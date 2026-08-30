class VRAdapter:
    adapter_type = "vr"

    def capabilities(self):
        return ["vr", "perception", "3d"]

    def connect(self):
        return True

    def disconnect(self):
        return True
