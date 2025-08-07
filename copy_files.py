import os
import shutil

# Go to attached_assets directory
os.chdir('attached_assets')

# Copy files with umlauts to ASCII versions
files = os.listdir('.')

for filename in files:
    if filename.startswith('äus1_'):
        new_name = 'aeusgasthaus1.jpeg'
        shutil.copy2(filename, new_name)
        print(f"Copied {filename} to {new_name}")
    elif filename.startswith('äus4_'):
        new_name = 'aeusgasthaus4.jpeg'
        shutil.copy2(filename, new_name)
        print(f"Copied {filename} to {new_name}")

print("Done copying files")