
fh = open('05.input', 'r')
puzzle = [x.strip() for x in fh.readlines()]

boarding_ids = []
for ticket in puzzle:
    ticket = ticket.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    boarding_id = int(ticket[0:7], 2) * 8 + int(ticket[7:10], 2)
    boarding_ids.append(boarding_id)

print("Biggest boarding id:", str(max(boarding_ids)))

boarding_ids = sorted(boarding_ids)
prev = boarding_ids[0] - 1
for cur in boarding_ids:
    if prev + 1 != cur:
        print("Your seat:", str(prev + 1))
        exit()
    prev = cur
