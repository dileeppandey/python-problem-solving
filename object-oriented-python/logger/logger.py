from abc import ABC, abstractmethod


class Process:
    """Class representing Process
    """
    def __init__(self, process_id: str, start_time: int, end_time: int = -1) -> None:
        self.__pid = process_id
        self.__start_time = start_time
        self.__end_time = end_time

    @property
    def pid(self):
        """Getter for id
        """
        return self.__pid

    @property
    def start_time(self):
        """Getter for start_time
        """
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time: int) -> None:
        """Setter for start date
        """
        self.__start_time = start_time

    @property
    def end_time(self):
        """Getter for end_time
        """
        return self.__end_time

    @end_time.setter
    def end_time(self, end_time: int) -> None:
        """Setter for end date
        """
        self.__end_time = end_time

    def __repr__(self):
        return f'Process({self.__pid}, {self.__start_time}, {self.__end_time})'



class ILogClient(ABC):
    """Interface to be used for concrete class implementation
    """

    @abstractmethod
    def start(self, process: Process) -> None:
        """When a process starts, it calls 'start' with process_id
        """
        raise NotImplementedError()

    @abstractmethod
    def end(self, process: Process) -> None:
        """When a process ends, it calls 'end' with process_id
        """
        raise NotImplementedError()

    @abstractmethod
    def poll(self) -> None:
        """Polls the first log entry of a completed process sorted by the start time of processes in the below format:
        {process_id} started at {start_time} and ended at {end_time}

        process_id = 1 --> 12, 15
        process_id = 2 --> 8, 12
        process_id = 3 --> 7, 19

        {3} started at {7} and ended at {19}
        {2} started at {8} and ended at {12}
        {1} started at {12} and ended at {15}

        """
        raise NotImplementedError()


class Logger(ILogClient):
    """Concrete Logger class
    """

    def __init__(self) -> None:
        self.processes: dict[str, Process] = {}
        # List of process_ids, sorted by end_time
        self.end_queue: dict[int, Process] = {}

    def start(self, process: Process) -> None:
        """Overrides super().start() method
        """
        self.processes[process.pid] = process

    def end(self, process_id: str, end_time: int) -> None:
        """Overrides super().end() method
        Updates the end_time of the process in the Logger processes state (self.processes)
        """
        self.processes[process_id].end_time = end_time

    def __get_latest_ended_process(self) -> Process:
        """Return the first entry in processes list which has a end_time not equal to -1
        """
        for _, process in self.processes.items():
            if process.end_time != -1:
                return process
        return None

    def poll(self) -> None:
        """Overrides super().poll()
        Removes process with smallest end time
        """
        ended_process: Process = self.__get_latest_ended_process()
        if (ended_process):
            print(f'{{{ended_process.pid}}} started at {{{ended_process.start_time}}} and ended at {{{ended_process.end_time}}}')
            del self.processes[ended_process.pid]
        else:
            print('No completed processes.')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)

    logger = Logger()
    logger.start(Process('1', 4))
    logger.poll()
    logger.start(Process('2', 1))
    logger.poll()
    logger.start(Process('3', 4))
    logger.poll()
    logger.end('2', 4)
    logger.poll()
    logger.end('1', 5)
    logger.poll()
    logger.end('3', 6)
    logger.poll()
