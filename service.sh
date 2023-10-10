#!/bin/bash

# Set the directory paths
left_window_dir="/home/pi/water_heaters_testings/dcs/build/debug"
right_window_dir="/home/pi/client"
csv_file="/home/pi/client/service.csv"

# Create a new tmux session named "service"
tmux new-session -d -s service

# Split the tmux window horizontally
tmux split-window -h -t service

# Function to get the value from the CSV file
get_csv_value() {
  tail -n 1 "$csv_file" | cut -d ',' -f 2
}

# Initial value from the CSV file
old_value=$(get_csv_value)

while true; do
  # Check the current value in the CSV file
  new_value=$(get_csv_value)

  # If the new value is different from the old value, update the right window
  if [[ "$new_value" != "$old_value" ]]; then
    # Update the right window
    tmux send-keys -t service:0.1 "cd $right_window_dir && echo $new_value > current_value.txt" C-m

    # Update the old value
    old_value="$new_value"
  fi

  # Sleep for 1 minute before checking again
  sleep 60
done

# Attach to the tmux session (you can manually detach using Ctrl-b d)
tmux attach-session -t service
