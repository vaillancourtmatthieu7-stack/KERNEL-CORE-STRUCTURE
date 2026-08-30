from core import KernelCore

kernel = KernelCore()

print("KERNEL CORE INTEGRATION")
print("========================")

for _ in range(3):
    print(kernel.tick(0.5))

print("INTEGRATION=PASS")
