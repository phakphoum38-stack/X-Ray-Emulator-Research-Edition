from hardware.xray_tube import XRayTube
from hardware.detector_panel import DetectorPanel
from imaging.exposure_engine import ExposureEngine

class XRaySystem:

    def __init__(self):

        self.tube = XRayTube()
        self.detector = DetectorPanel()
        self.exposure = ExposureEngine(self.tube,self.detector)

    def start_scan(self):

        print("Initializing X-ray system")

        self.tube.warmup()

        image = self.exposure.capture()

        print("Scan complete")

        return image
