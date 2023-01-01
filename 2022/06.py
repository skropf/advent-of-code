
def get_packet_marker(content):
    for i in range(len(content)-3):
        chars = [content[i], content[i+1], content[i+2], content[i+3]]
        
        if len(set(chars)) == 4:
            print(i+4)
            break

def get_message_marker(content):
    for i in range(len(content)-3):
        chars = []
        for j in range(14):
            chars.append(content[i+j])
        
        if len(set(chars)) == 14:
            print(i+14)
            break

content = open('06.input', 'r').readline()
get_packet_marker(content)
get_message_marker(content)