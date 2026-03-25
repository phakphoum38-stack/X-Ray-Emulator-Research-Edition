from system_controller import XRaySystem

system = XRaySystem()

image = system.start_scan()

print("Image generated")
print(len(image), "x", len(image[0]))
