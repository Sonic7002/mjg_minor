# main method for containing ui and function calls
from tasks import Queue
from utils import clear_screen, pause

def main():
    data = Queue()
    while True:
        clear_screen()
        print("MENU".center(50, '*'))
        print("1. Add task\n2. View pending tasks\n3. Complete next task\n4. Display no. of tasks\n5. Exit")
        try:
            choice = int(input("Enter your choice (1 to 5):"))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            pause()
            continue
        match(choice):
            case 1:
                data.enqueue(input("Enter task: "))
                print("Entry successful!")
                pause()
            case 2:
                out = data.items()
                if out == []:
                    print("No pending tasks left")
                    pause()
                    continue
                for i,task in enumerate(out, start = 1):
                    print(f"{i}. {task}")
                pause()
            case 3:
                try:
                    print("Task completed:", data.dequeue())
                    pause()
                except ValueError:
                    print("No pending tasks to be completed")
                    pause()
            case 4:
                print("No. of tasks:", data.count())
                pause()
            case 5:
                print("Exiting...")
                break
            case _:
                print("Invalid input. Please enter values given in menu.")
                pause()

if __name__ == "__main__":
    main()