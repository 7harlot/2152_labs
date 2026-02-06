"""
Author: Ben Morrison
Student ID: 101572409
Assignment: #1
"""

# (b) Four variables 
#string, float, int, boolean
gym_member = "Alex Alliton"       
preferred_weight_kg = 20.5        
highest_reps = 25                 
membership_active = True          

# dict: keys=str (friend names), values=tuple of 3 ints (yoga, run, weights)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 35),
    "Taylor": (40, 30, 25),
}

# Loop: total mins per friend
for friend_name, activity_tuple in list(workout_stats.items()):
    if isinstance(activity_tuple, tuple) and len(activity_tuple) == 3:
        total_minutes = activity_tuple[0] + activity_tuple[1] + activity_tuple[2]
        total_key = f"{friend_name}_Total"
        workout_stats[total_key] = total_minutes

# list of lists: each row = one friend, cols = yoga, running, weightlifting
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"]),
]

# (f) Slice: yoga and running for all friends (cols 0,1)
print("Yoga and running minutes for all friends:")
yoga_running_slice = [row[:2] for row in workout_list]
print(yoga_running_slice)

# (f) Slice: weightlifting for last two friends (col 2, last 2 rows)
print("\nWeightlifting minutes for the last two friends:")
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print(weightlifting_last_two)

# (g) If in loop: total >= 120 -> print encouragement
print("\n--- Activity shoutouts (total >= 120 mins) ---")
for friend_name in ["Alex", "Jamie", "Taylor"]:
    total_key = f"{friend_name}_Total"
    if total_key in workout_stats and workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend_name}!")

# (h) Input friend name: print their stats or "not found"
print("\n--- Friend lookup ---")
lookup_name = input("Enter a friend's name to look up: ").strip()
if lookup_name in workout_stats and isinstance(
        workout_stats.get(lookup_name), tuple):
    t = workout_stats[lookup_name]
    total = workout_stats.get(f"{lookup_name}_Total", t[0] + t[1] + t[2])
    print(f"  Yoga: {t[0]} min, Running: {t[1]} min, "
          f"Weightlifting: {t[2]} min. Total: {total} min.")
else:
    print(f"Friend {lookup_name} not found in the records.")

# (i) Print friend with highest and lowest total workout minutes
print("\n--- Summary ---")
friend_names = ["Alex", "Jamie", "Taylor"]
totals_only = [(n, workout_stats[f"{n}_Total"]) for n in friend_names]
highest_friend = max(totals_only, key=lambda x: x[1])
lowest_friend = min(totals_only, key=lambda x: x[1])
print(f"The friend with the highest total workout minutes: "
      f"{highest_friend[0]} ({highest_friend[1]} min).")
print(f"The friend with the lowest total workout minutes: "
      f"{lowest_friend[0]} ({lowest_friend[1]} min).")
