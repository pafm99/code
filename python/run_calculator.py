total_runs = 0
total_run_time = 0

while True:
  run_time = input("Enter run time: ")
  
  if run_time == "q":
    break
  if run_time.isdigit():
    total_run_time += int(run_time)
    total_runs += 1
  else:
    print("That's not a number")
  
  average_run_time = float(total_run_time)/total_runs

print("You ran {} times, with an average time of {} minutes".format(total_runs, average_run_time))
