from typing import List


class RAID4:
    def __init__(self, count_of_disks: int, size: int):
        self.__disks: List[List[int]] = [[0 for _ in range(size)] for _ in range(count_of_disks + 1)]

    def __calculate_parity(self, new_block: int, disk_number: int, position: int):
        original_block = self.__disks[disk_number][position]
        original_parity = self.__disks[-1][position]
        return (original_block ^ new_block) ^ original_parity

    def __find_corrupted_disk(self) -> int:
        disk_number: int = -1
        for i, disk in enumerate(self.__disks):
            for value in disk:
                if value == -1:
                    if disk_number != -1:
                        raise RuntimeError("There is more than on corrupted disks")
                    disk_number = i
                    break
        return disk_number

    def write_block(self, block: int, disk_number: int, position: int) -> None:
        new_parity = self.__calculate_parity(block, disk_number, position)

        self.__disks[-1][position] = new_parity
        self.__disks[disk_number][position] = block

    def kill_disk(self, disk_number: int) -> None:
        for i in range(len(self.__disks[disk_number])):
            self.__disks[disk_number][i] = -1

    def recover_disks(self) -> None:
        disk_number: int = self.__find_corrupted_disk()
        if disk_number == -1:
            return
        for position in range(len(self.__disks[0])):
            value = 0
            for i in range(len(self.__disks)):
                if i != disk_number:
                    value ^= self.__disks[i][position]
            self.__disks[disk_number][position] = value

    def print(self):
        for i, disk in enumerate(self.__disks):
            print(f"Disk: {i}", disk)


if __name__ == '__main__':
    raid = RAID4(3, 10)
    raid.write_block(1, 0, 0)
    raid.write_block(2, 0, 1)
    raid.write_block(3, 0, 2)
    raid.write_block(4, 0, 3)
    raid.write_block(9, 0, 9)
    raid.write_block(1, 1, 0)
    raid.write_block(2, 1, 1)
    raid.write_block(3, 1, 2)
    raid.write_block(4, 1, 3)
    raid.write_block(9, 1, 9)
    raid.kill_disk(0)
    raid.recover_disks()
    raid.print()
