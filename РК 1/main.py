class HardDrive:
    def __init__(self, hard_drive_id, capacity, computer_id):
        self.hard_drive_id = hard_drive_id
        self.capacity = capacity
        self.computer_id = computer_id

class Computer:
    def __init__(self, computer_id, model):
        self.computer_id = computer_id
        self.model = model

class ComputerHardDrives:
    def __init__(self, hard_drive_id, computer_id):
        self.hard_drive_id = hard_drive_id
        self.computer_id = computer_id

hard_drives = [
    HardDrive(1, 500, 1),
    HardDrive(2, 1000, 1),
    HardDrive(3, 250, 2),
    HardDrive(4, 750, 3),
]

computers = [
    Computer(1, "Lenovo Computer"),
    Computer(2, "HP"),
    Computer(3, "Dell Computer"),
]

relations = [
    ComputerHardDrives(1, 1),
    ComputerHardDrives(2, 1),
    ComputerHardDrives(3, 2),
    ComputerHardDrives(4, 3),
]

print("List of hard drives and their corresponding computers:")
for computer in sorted(computers, key=lambda x: x.model):
    drives_for_computer = [drive for drive in hard_drives if drive.computer_id == computer.computer_id]
    print(f"Computer: {computer.model}")
    for drive in drives_for_computer:
        print(f"  Hard Drive (Capacity): {drive.capacity} GB")

print("\nList of computers with total hard drive capacity:")
total_capacities = {}
for computer in computers:
    total_capacity = sum(drive.capacity for drive in hard_drives if drive.computer_id == computer.computer_id)
    total_capacities[computer.model] = total_capacity

for computer, capacity in sorted(total_capacities.items(), key=lambda item: item[1], reverse=True):
    print(f"Computer: {computer}, Total Capacity: {capacity} GB")

print("\nComputers with 'computer' in their model name and their hard drives:")
for computer in computers:
    if "computer" in computer.model.lower():
        drives_for_computer = [drive for drive in hard_drives if drive.computer_id == computer.computer_id]
        print(f"Computer: {computer.model}")
        for drive in drives_for_computer:
            print(f"  Hard Drive (Capacity): {drive.capacity} GB")
