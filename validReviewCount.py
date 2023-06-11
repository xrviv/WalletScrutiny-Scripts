import os

directory = '/home/dannybuntu/Work/walletscrutiny3/walletScrutinyCom/_android'
output_file = 'tobereviewed.md'
criteria = {
    'users': 1000,
    'meta': ['ok', 'obsolete', 'stale'],
    'verdict': 'wip'
}

files_to_review = []

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()

        # Checking criteria
        users_line = [line for line in content.split('\n') if line.startswith('users:')][0]
        users = int(users_line.split(':')[1].strip())
        meta_line = [line for line in content.split('\n') if line.startswith('meta:')][0]
        meta = meta_line.split(':')[1].strip()
        verdict_line = [line for line in content.split('\n') if line.startswith('verdict:')][0]
        verdict = verdict_line.split(':')[1].strip()

        if (
            users >= criteria['users']
            and meta in criteria['meta']
            and verdict == criteria['verdict']
            and 'defunct' not in content
        ):
            files_to_review.append((filename, users, meta, verdict))

# Writing output to file
with open(output_file, 'w') as file:
    for entry in files_to_review:
        filename, users, meta, verdict = entry
        file.write(f'- [ ] {filename} * users: {users} * meta: {meta} * verdict: {verdict}\n')

# Counting the number of files
count = len(files_to_review)
print(f'🏆🏆🏆 Counted: {count} number of files in list 🏆🏆🏆')
