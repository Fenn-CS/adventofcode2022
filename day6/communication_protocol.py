# Problem statement: https://adventofcode.com/2022/day/6

def getFirstNUniqueStreamElements(stream, N):
    packet_marker = []
    for i in range(0, len(stream)):
        if len(packet_marker) < N:
            packet_marker.append(stream[i])
        if len(packet_marker) == N:
            for item in packet_marker:
                if packet_marker.count(item) > 1:
                    packet_marker.pop(0)
                    continue
        if len(packet_marker) == N:
            break
    return  packet_marker, i+1

with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            pass # Thanks but, I would pass!
        else:
            stream = line.strip('\n')
            packet_marker, position = getFirstNUniqueStreamElements(stream, 4)
            print("The packet marker is {} and ends at {}".format(''.join(packet_marker), position))
            message, position = getFirstNUniqueStreamElements(stream, 14)
            print("The message is {} and ends at {}".format(''.join(message), position))


