import os


def analyze_apps(directory):
    # Open the reviewPriority.md file for writing
    with open("reviewPriority.md", "w") as file:
        # Sort order for entries
        sort_order = [
            (5000, "ok"),
            (5000, "stale"),
            (5000, "obsolete"),
            (1000, "ok"),
            (1000, "stale"),
            (1000, "obsolete")
        ]

        # Initialize counts for different parameters
        counts = {
            "5000_ok_wip": 0,
            "5000_stale_wip": 0,
            "5000_obsolete_wip": 0,
            "1000_ok_wip": 0,
            "1000_stale_wip": 0,
            "1000_obsolete_wip": 0
        }

        # Iterate over the sort order
        for users, meta in sort_order:
            # Write the section header
            file.write(f"----------\n")
            file.write(f"users should be >= {users}, meta: {meta}, verdict: wip\n")
            file.write(f"----------\n")

            # Iterate over the files in the directory
            for filename in os.listdir(directory):
                if filename.endswith(".md"):
                    filepath = os.path.join(directory, filename)
                    with open(filepath, "r") as app_file:
                        # Read the app file content
                        app_content = app_file.read()

                        # Extract the fields: users, meta, and verdict
                        app_name = os.path.splitext(filename)[0]
                        users_value = int(extract_field(app_content, "users"))
                        meta_value = extract_field(app_content, "meta")
                        verdict_value = extract_field(app_content, "verdict")

                        # Check if the entry matches the sort criteria
                        if users_value >= users and meta_value == meta and verdict_value == "wip":
                            # Write the entry to the reviewPriority.md file
                            file.write(
                                f"- [ ] {app_name}, users: {users_value}, meta: {meta_value}, verdict: {verdict_value}\n")

                            # Update the count for the corresponding parameter
                            count_key = f"{users}_{meta}_wip"
                            counts[count_key] += 1

        # Print the counts in the terminal
        print("App Counts:")
        for count_key, count_value in counts.items():
            print(f"- **{count_value}** apps with {count_key.replace('_', ', ')}")


def extract_field(content, field_name):
    # Extract the value of the specified field from the content
    start_tag = f"{field_name}: "
    start_index = content.find(start_tag) + len(start_tag)
    end_index = content.find("\n", start_index)
    field_value = content[start_index:end_index].strip()
    return field_value


# Ask the user to input the directory to scan
directory = input("Enter the directory to scan: ")

# Call the analyze_apps function
analyze_apps(directory)
