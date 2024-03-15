import random
import threading

class SchedulingStrategy:
    def schedule(self, computers):
        pass

class RandomScheduling(SchedulingStrategy):
    def schedule(self, computers, Task):
        for computer in computers:
            if Task <= 0:  
                break

            if computer.powered_on:
                continue

            percentage = min(random.random() * 10.0, Task)  
       
            if computer.battery_level > 1 and computer.temperature < 90:
                computer.thread = threading.Thread(target=computer.calculate, args=(percentage,))
                computer.thread.start()
                Task -= percentage
                print(Task)
        return Task    
     
class RoundRobinScheduling(SchedulingStrategy):
    def schedule(self, computers, Task):
        num_computers = len(computers)
        current_index = 0
        while Task > 0:
            if computers[current_index].powered_on:
                current_index = (current_index + 1) % num_computers
                continue

            percentage = min(computers[current_index].strength* 10.0, Task)
            
            if computers[current_index].battery_level > 1 and computers[current_index].temperature < 90:
                computers[current_index].thread = threading.Thread(target=computers[current_index].calculate, args=(percentage,))
                computers[current_index].thread.start()
                Task -= percentage
                print(Task)
            
            current_index = (current_index + 1) % num_computers

        return Task
    
class LowestBatteryScheduling(SchedulingStrategy):
    def schedule(self, computers, Task):
        sorted_computers = sorted(computers, key=lambda x: x.battery_level)
        for computer in sorted_computers:
            if Task <= 0:
                break

            if computer.powered_on:
                continue

            percentage = min(computer.strength* 10.0, Task)

            if computer.battery_level > 1 and computer.temperature < 90:
                computer.thread = threading.Thread(target=computer.calculate, args=(percentage,))
                computer.thread.start()
                Task -= percentage
                print(Task)

        return Task

class TemperatureControlScheduling(SchedulingStrategy):
    def schedule(self, computers, Task):
        sorted_computers = sorted(computers, key=lambda x: x.temperature)
        for computer in sorted_computers:
            if Task <= 0:
                break

            if computer.powered_on:
                continue

            percentage = min(computer.strength* 10.0, Task)


            if computer.battery_level > 1 and computer.temperature < 90:
                computer.thread = threading.Thread(target=computer.calculate, args=(percentage,))
                computer.thread.start()
                Task -= percentage
                print(Task)

        return Task

class StrengthBasedScheduling(SchedulingStrategy):
    def schedule(self, computers, Task):
        sorted_computers = sorted(computers, key=lambda x: x.strength)
        for computer in sorted_computers:
            if Task <= 0:
                break

            if computer.powered_on:
                continue

            percentage = min(computer.strength* 10.0, Task)


            if computer.battery_level > 1 and computer.temperature < 90:
                computer.thread = threading.Thread(target=computer.calculate, args=(percentage,))
                computer.thread.start()
                Task -= percentage
                print(Task)

        return Task

class PriorityScheduling(SchedulingStrategy):
    def schedule(self, computers, Task):
        sorted_computers = sorted(computers, key=lambda x: (x.battery_level, -x.temperature))
        for computer in sorted_computers:
            if Task <= 0:
                break

            if computer.powered_on:
                continue

            percentage = min(computer.strength* 10.0, Task)


            if computer.battery_level > 1 and computer.temperature < 90:
                computer.thread = threading.Thread(target=computer.calculate, args=(percentage,))
                computer.thread.start()
                Task -= percentage
                print(Task)

        return Task