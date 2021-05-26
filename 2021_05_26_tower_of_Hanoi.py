from typing import TextIO


def move_tower(disks, source, middle, destination):
    if disks == 0:
        print(f"Move disk {disks} from {source} to {destination}")
        return
    move_tower(disks-1, source, destination, middle)
    print(f"Move disk {disks} from {source} to {destination}")
    move_tower(disks-1, middle, source, destination)


move_tower(5, "A", "B", "C")
