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

def get_hard_drives_by_computer(computers, hard_drives):
    result = {}
    for computer in sorted(computers, key=lambda x: x.model):
        drives_for_computer = [drive for drive in hard_drives if drive.computer_id == computer.computer_id]
        result[computer.model] = drives_for_computer
    return result

def get_total_capacity_by_computer(computers, hard_drives):
    total_capacities = {}
    for computer in computers:
        total_capacity = sum(drive.capacity for drive in hard_drives if drive.computer_id == computer.computer_id)
        total_capacities[computer.model] = total_capacity
    return total_capacities

def get_computers_with_keyword(computers, hard_drives, keyword="computer"):
    result = {}
    for computer in computers:
        if keyword.lower() in computer.model.lower():
            drives_for_computer = [drive for drive in hard_drives if drive.computer_id == computer.computer_id]
            result[computer.model] = drives_for_computer
    return result
