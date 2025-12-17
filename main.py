import psutil
import time

def create_bar(percent, bar_length=20, fill="█", empty="░"):
    filled_length = int(bar_length * percent // 100)
    bar = fill * filled_length + empty * (bar_length - filled_length)
    return f"[{bar}] {percent:.1f}%"

def monitor_cpu_usage(interval=1, bar_length=20):
    print("Starting CPU Monitor (Press Ctrl+C to stop)...")
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=interval)
            
            if cpu_percent < 25:
                fan_percent = 25
            elif cpu_percent < 50 and cpu_percent >= 25:
                fan_percent = 50
            elif cpu_percent < 75 and cpu_percent >= 50:
                fan_percent = 75
            else:
                fan_percent = 100

            cpu_bar = create_bar(cpu_percent, bar_length)
            fan_speed = create_bar(fan_percent, bar_length)
            print(f"\rCPU Usage: {cpu_bar} | Fan speed: {fan_speed}", end="")

    except KeyboardInterrupt:
        print("\nCPU Monitor stopped.")


if __name__ == "__main__":
    monitor_cpu_usage()
