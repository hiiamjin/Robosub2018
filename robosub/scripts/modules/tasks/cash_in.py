import time

from threading import Thread, Lock
from collections import Counter
from itertools import combinations

from task import Task

# from modules.sensors.computer_vision import CashInDetector

# from cash_in_maneuver import CashInManeuver

class CashIn(Task):
    
    def __init__(self, Houston):
        """ To initialize CashIn """
        super(CashIn, self).__init__()
        
        ################ INSTANCES ################
        self.houston = Houston
        # self.cash_in_maneuver = CashInManeuver()
        self.detectcashin = None

        ################ THRESHOLD VARIABLES ################

        ################ FLAG VARIABLES ################
        self.is_found = False
        self.is_detect_done = False
        self.is_navigate_done = False
        self.is_done = False
        self.stop_task = False
        self.is_task_running = False
        self.is_complete = False

        ################ TIMER VARIABLES ################
        self.not_found_timer = 0
        self.found_timer = 0

        ################ DICTIONARIES ################
        self.direction_list = []

        ################ AUV MOBILITY VARIABLES ################

        ################ THREAD VARIABLES ################
        self.thread_cash_in = None
        self.mutex = Lock()

    # reset ##################################################################################
    def reset(self): 
        pass
    
    # start ##################################################################################
    def start(self):
        pass

    # stop ##################################################################################
    def stop(self):
        pass
        
    # detect ##################################################################################
    def detect(self, frame):
        print('detect_dice')
        if not self.detectcashin:
            #self.detectcashin = CashInDetector.CashInDetector()
            pass

        found, gate_coordinates = self.detectcashin.detect()
        if gate_coordinates[0] == 0 and gate_coordinates[1] == 0:
            if not found:
                gate_coordinates[0] = 1
            else:
                self.found_timer += 1

        if self.found_timer == 240:
            self.is_gate_found = True
            self.task_num += 1

    # navigate ##################################################################################
    def navigate(self, navigation, found, coordinates, power, rotation):
        pass
    
    # complete ##################################################################################
    def complete(self):
        pass

    # bail_task ##################################################################################
    def bail_task(self):
        pass

    # restart_task ##################################################################################
    def restart_task(self):
        pass
        
    # search ##################################################################################
    def search(self):
        pass

    # run_detect_for_task ##################################################################################
    def run_detect_for_task(self):
        pass

    def reset_thread(self):
        pass

    def get_most_occur_coordinates(self): 
        pass 