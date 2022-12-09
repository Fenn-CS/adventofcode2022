# Problem statement: https://adventofcode.com/2022/day/6
with open('input', 'r') as input:
    for line in input:
        if line in ['\n', '\r\n']:
            pass # Thanks but, I would pass!
        else:
            stream = line.strip('\n')
            packet_marker = []
            for i in range(0, len(stream)):
                if len(packet_marker) < 4:
                    packet_marker.append(stream[i])
                if len(packet_marker) == 4:
                    for item in packet_marker:
                        if packet_marker.count(item) > 1:
                            packet_marker.pop(0)
                            continue
                if len(packet_marker) == 4:
                    break
            print("First compliant byte {} ends at {}".format(''.join(packet_marker), i+1))
