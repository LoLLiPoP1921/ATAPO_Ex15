import psutil
import time


def main():
    while True:
        cpu_usage = psutil.cpu_percent()
        print(f"CPU%: {cpu_usage}")
        if cpu_usage < 25:
            print("Fan to 20%")
        elif cpu_usage < 50 and cpu_usage >= 25:
            print("Fan to 50%")
        elif cpu_usage < 75 and cpu_usage >= 50:
            print("Fan to 75%")
        else:
            print("Fan to 100%")
    
        time.sleep(1)


if __name__ == "__main__":
    main()
