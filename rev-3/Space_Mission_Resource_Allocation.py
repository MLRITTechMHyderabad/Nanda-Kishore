import numpy as np


resources = np.array([
    [15, 40, 32],
    [20, 42, 35],
    [25, 38, 30],
    [18, 50, 40],
    [22, 37, 36],
    [28, 45, 33]
])

total_resources = np.sum(resources, axis=0)

max_monthly_consumption = np.max(resources, axis=0)
max_resource_idx = np.argmax(max_monthly_consumption)
max_overall = np.max(resources)
month, resource = np.unravel_index(np.argmax(resources), resources.shape)

std_dev = np.std(resources, axis=0)

transposed_resources = resources.T


print(f"Total resources needed (tons): Oxygen: {total_resources[0]}, Water: {total_resources[1]}, Food: {total_resources[2]}")
print(f"Highest consumption in a month: {['Oxygen', 'Water', 'Food'][resource]} ({max_overall} tons in month {month+1})")
print(f"Standard deviation of consumption: Oxygen: {std_dev[0]:.1f}, Water: {std_dev[1]:.1f}, Food: {std_dev[2]:.1f}")
print("Transposed matrix:")
print(transposed_resources)
