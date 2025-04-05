import os
import logging
import threading

class SingletonLogger:
    _instance = None    # single instance/object
    _lock = threading.Lock()    # lock for thread safety

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(SingletonLogger, cls).__new__(cls)

                # configure logger only time
                cls._instance.logger  = logging.getLogger("SingletonLogger")
                cls._instance.logger.setLevel(logging.DEBUG)

                # console handler
                console_handler = logging.StreamHandler()
                console_handler.setLevel(logging.DEBUG)

                # creating file path for log file
                file_path = os.path.join(os.getcwd(), 'creational_design_patterns/singleton')
                file_path = os.path.join(file_path, 'singleton.log')

                # file handler
                file_handler = logging.FileHandler(file_path, mode='w')
                file_handler.setLevel(logging.DEBUG)

                # formatter
                formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
                console_handler.setFormatter(formatter)
                file_handler.setFormatter(formatter)

                # add handler to logger
                cls._instance.logger.addHandler(console_handler)
                cls._instance.logger.addHandler(file_handler)
        return cls._instance
    

    # logging methods
    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
    
    def critical(self, message):
        self.logger.critical(message)



def test(thread_name):
    logger = SingletonLogger()
    logger.warn(f"warning coming from {thread_name}")


if __name__ == '__main__':

    # creating multiple thread
    threads = []
    for i in range(5):
        t = threading.Thread(target=test, args=(f'Thread-{i}',))
        threads.append(t)
        t.start()


    # wait for threads to complete
    for t in threads:
        print("thread is >>>> ", t)
        t.join()

    
    # Check if it's still a single instance
    logger1 = SingletonLogger()
    logger2 = SingletonLogger()
    logger3 = SingletonLogger()
    # print(f"Logger1 and Logger2 are same instance: {logger1 is logger2}")
    # print(f"Logger1 and Logger3 are same instance: {logger1 is logger3}")
    # print(f"Logger2 and Logger3 are same instance: {logger2 is logger3}")

    for i in range(1, 6):
        i = SingletonLogger()
        print(f"Logger1 and Logger2 are same instance: logger{i} is logger{i}")



        


    
                


