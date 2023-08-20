import os

file_path = 'rainbow-table.txt'
file_size_bytes = os.path.getsize(file_path)


def convert_bytes(bytes):
    for size in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024.0:
            return "%3.1f %s" % (bytes, size)
        bytes /= 1024.0


file_size_readable = convert_bytes(file_size_bytes)

with open(file_path, 'r') as f:
    x = len(f.readlines())

print('Total lines:', x)
print(f"Size of '{file_path}': {file_size_readable}")
