import time
import subprocess

def choose_service():
    print("Choose a service:")
    print("1. baseline")
    print("2. energy-s")
    print("3. energy-c")
    print("4. blackstart")

    while True:
        choice = input("Enter the number corresponding to your chosen service: ")
        if choice in ['1', '2', '3', '4']:
            services = ["baseline", "energy-s", "energy-c", "blackstart"]
            selected_service = services[int(choice) - 1]
            return selected_service
        else:
            print("Invalid choice. Please enter a valid number.")

def send_to_tmux(letter):
    tmux_command = f"tmux send-keys -t service '{letter}' Enter"
    subprocess.run(tmux_command, shell=True)

def baseline_service_timer():
    print("Baseline service started. Outputting 'l' at the beginning.")
    
    send_to_tmux("l")

    # Sleep for the initial duration (3 hours - 10 minutes)
    initial_duration = (4 * 60 * 60) - (10 * 60)
    elapsed_time = 0
    
    while elapsed_time < initial_duration:
        time.sleep(min(600, initial_duration - elapsed_time))
        elapsed_time += 600
        
        if elapsed_time % 1200 == 0:  # Send 'o' every 15 minutes
            print("o")
            send_to_tmux("o")
            
            # Sleep for 1 minute
            time.sleep(60)
            
            # Send 'l' one minute after 'o'
            print("l")
            send_to_tmux("l")

    # Output 'e' during the last 10 minutes
    print("e")
    send_to_tmux("e")




def energy_s_service_timer():
    print("Energy-SHED service started. Outputting 'l' at the beginning.")
    
    send_to_tmux("o")

    # Sleep for the initial duration (30 minutes)
    initial_duration = 30 * 60
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(600)
    print("o")
    send_to_tmux("o")
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(600)
    print("o")
    send_to_tmux("o")
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(initial_duration)

    elapsed_time = 0
    remaining_duration = (4 * 60 * 60) - (30 * 60) - (10 * 60)
    
    while elapsed_time < remaining_duration:
        send_to_tmux("s")
        time.sleep(min(600, remaining_duration - elapsed_time))  # Sleep for 10 minutes
        elapsed_time += 600
        
        # Send 'o'
        print("o")
        send_to_tmux("o")

        # Sleep for 1 minute
        time.sleep(60)
        
        # Send 's' one minute after 'o'
        print("s")
        send_to_tmux("s")

    # Output 'e' during the last 10 minutes
    print("e")
    send_to_tmux("e")

        
       


def energy_c_service_timer():
    
    print("Energy-SHED service started. Outputting 'l' at the beginning.")
    
    send_to_tmux("o")

    # Sleep for the initial duration (30 minutes)
    initial_duration = 30 * 60
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(600)
    print("o")
    send_to_tmux("o")
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(600)
    print("o")
    send_to_tmux("o")
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(initial_duration)

    elapsed_time = 0
    remaining_duration = (4 * 60 * 60) - (30 * 60) - (10 * 60)
    
    while elapsed_time < remaining_duration:
        send_to_tmux("c")
        time.sleep(min(600, remaining_duration - elapsed_time))  # Sleep for 10 minutes
        elapsed_time += 600
        
        # Send 'o'
        print("o")
        send_to_tmux("o")

        # Sleep for 1 minute
        time.sleep(60)
        
        # Send 's' one minute after 'o'
        print("c")
        send_to_tmux("c")

    # Output 'e' during the last 10 minutes
    print("e")
    send_to_tmux("e")







def blackstart_service_timer():
    print("Energy-SHED service started. Outputting 'l' at the beginning.")
    
    send_to_tmux("o")

    # Sleep for the initial duration (30 minutes)
    initial_duration = 30 * 60
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(600)
    print("o")
    send_to_tmux("o")
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(600)
    print("o")
    send_to_tmux("o")
    time.sleep(60)
    print("l")
    send_to_tmux("l")
    time.sleep(initial_duration)

    elapsed_time = 0
    remaining_duration = (4 * 60 * 60) - (30 * 60) - (10 * 60)
    
    while elapsed_time < remaining_duration:
        send_to_tmux("g")
        time.sleep(min(600, remaining_duration - elapsed_time))  # Sleep for 10 minutes
        elapsed_time += 600
        
        # Send 'o'
        print("o")
        send_to_tmux("o")

        # Sleep for 1 minute
        time.sleep(60)
        
        # Send 's' one minute after 'o'
        print("g")
        send_to_tmux("g")

    # Output 'e' during the last 10 minutes
    print("e")
    send_to_tmux("e")




def main():
    selected_service = choose_service()
    print(f"You have selected '{selected_service}' service.")

    if selected_service == "baseline":
        baseline_service_timer()
    elif selected_service == "energy-s":
        energy_s_service_timer()
    elif selected_service == "energy-c":
        energy_c_service_timer()
    elif selected_service == "blackstart":
        blackstart_service_timer()
    else:
        # Start timer for 3 hours (in seconds) for other services
        timer_duration = 4 * 60 * 60
        print(f"Timer started for {timer_duration // 60} minutes.")

        # Sleep for the specified duration
        time.sleep(timer_duration)

        print("Timer expired. Service completed.")

if __name__ == "__main__":
    main()
