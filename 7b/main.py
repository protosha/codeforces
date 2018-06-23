"""
This code solves task 7B from codeforces.org
link: https://codeforces.com/problemset/problem/7/B
"""
from sys import stdin, stdout

class Block:
    """
    Represents memory block
    """
    def __init__(self, id, offset, size):
        """
        :param id:
        :param offset: Byte number, from which the block starts
        :param size: Block size (in bytes)
        """
        self.id = id
        self.offset = offset
        self.size = size


class MemoryManager:
    """
    Memory manager with operations
        - memory allocation
        - memory release
        - memory defragmentation
    """
    def __init__(self, capacity):
        """
        Initialize memory manager
        :param capacity: Memory capacity of the manager (in bytes)
        """
        self.capacity = capacity
        # Initially populated with so-called "edge blocks"
        # Simplifies handling first and second block allocation
        self.blocks = [Block(-1, 0, 0), Block(-1, 100, 0)]
        # For id assignment
        self.last_block_id = 0

    def get_available_position(self, amount):
        """
        Find position for block to allocate
        :param amount: Amount of memory to allocate (in bytes)
        :return: None if desired amount could not be found, list index - otherwise
        """
        prev_block = self.blocks[0]
        for i in range(1, len(self.blocks)):
            curr_block = self.blocks[i]
            avail_offset = prev_block.offset + prev_block.size
            avail_amount = curr_block.offset - avail_offset
            if avail_amount >= amount and avail_offset + amount <= capacity:
                return i
            prev_block = curr_block
        return None

    def allocate(self, amount):
        """
        Allocate specified amount of memory
        :param amount: Amount of memory to allocate (in bytes)
        :return: None if desired amount could not be found, block id - otherwise
        """
        avail_position = self.get_available_position(amount)
        if avail_position == None:
            return None
        self.last_block_id += 1
        prev_block = self.blocks[avail_position - 1]
        self.blocks.insert(avail_position, Block(self.last_block_id, prev_block.offset + prev_block.size, amount))
        return self.last_block_id

    def erase(self, block_id):
        """
        Remove the block emulating release of memory
        :param block_id:
        :return: True if removed found block, False - otherwise
        """
        for block in self.blocks:
            if block.id == block_id and block_id != -1:
                self.blocks.remove(block)
                return True
        return False

    def defragment(self):
        """
        Defragment the memory so that all blocks are adjacent preserving the order
        """
        block_count = len(self.blocks)
        prev_block = self.blocks[0]
        for i in range(1, block_count):
            curr_block = self.blocks[i]
            curr_block.offset = prev_block.offset + prev_block.size
            prev_block = curr_block
        # Bring back position of edge block
        self.blocks[block_count - 1].offset = 100


class MemoryManagerConsole:
    """
    Class to wrap all input functionality
    """

    def __init__(self, memory_manager: MemoryManager):
        self.memory_manager = memory_manager

    def read(self):
        """
        Reads single command from input (1 line)
        :return: Command execution readable output
        """
        input = stdin.readline().rstrip().split()
        command = input[0]
        if command == 'alloc':
            # alloc n
            amount = int(input[1])
            block_id = self.memory_manager.allocate(amount)
            return str(block_id or 'NULL')
        elif command == 'erase':
            # erase x
            block_id = int(input[1])
            if self.memory_manager.erase(block_id) == False:
                return 'ILLEGAL_ERASE_ARGUMENT'
        elif command == 'defragment':
            # defragment
            self.memory_manager.defragment()
        return None


# read number of command to be executed (t) and memory capacity in bytes (m)
command_count, capacity = map(int, stdin.readline().rstrip().split())
memory_manager = MemoryManager(capacity)
manager_console = MemoryManagerConsole(memory_manager)
output_batch = list()
# execute commands
for i in range(command_count):
    result = manager_console.read()
    if result != None:
        output_batch.append(result)
# write all the output to stdout
for output in output_batch:
    stdout.write(output + "\n")