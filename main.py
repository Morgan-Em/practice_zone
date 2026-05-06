def main():
    print("Hello from practice-zone!")


if __name__ == "__main__":
    main()
# A simple Task Manager to practice Python logic
tasks = ["Setup WSL", "Install VS Code", "Configure Git", "Install uv"]

print("--- Emmanuel's Dev Progress ---")

# Add a new task
new_task = "Learn Python Loops"
tasks.append(new_task)

# Loop through the tasks and print them
for index, task in enumerate(tasks, 1):
    print(f"{index}. [Done] {task}")

print("\nStatus: Environment is 100% ready. Moving to logic next!")