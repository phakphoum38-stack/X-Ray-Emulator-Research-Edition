from core.system_controller import XRaySystem

system = XRaySystem()

img = system.start_scan()

print("Image size:",img.shape)
