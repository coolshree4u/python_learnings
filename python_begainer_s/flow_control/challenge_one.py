ip_address=input("please enter an ip address")
segment = 1
segment_length = 0

for character in ip_address:
    if character == '.':
        print("Segment {} contains {} characters".format(segment,segment_length))
        segment+=1
        segment_length = 0
    else:
        segment_length+=1

if character != '.':
    print("Segment {} contains {} characters ".format(segment,segment_length))