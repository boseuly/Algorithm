import sys
paragraph_list = sys.stdin.readlines()
paragraph_list = [paragraph.rstrip('\n') for paragraph in paragraph_list ]

for data in paragraph_list:
    print(data)
