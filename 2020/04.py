import string

fh = open('04.input', 'r')
puzzle = [x.strip() for x in fh.readlines()]

req_fields = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and int(x[:-2]) >= 150 and int(x[:-2]) <= 193) or
                     (x.endswith("in") and int(x[:-2]) >= 59 and int(x[:-2]) <= 76),
    "hcl": lambda x: x.startswith("#") and len(x) == 7 and all([i in string.hexdigits for i in x[1:]]),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isnumeric(),
    "cid": lambda x: True
}

# Part 1 + 2
valid_passports = 0
valid_passports2 = 0
cur_passport = ""
for line in puzzle:
    if line != "": cur_passport += " " + line
    else:
        if all([x == "cid" or x in cur_passport for x in req_fields.keys()]):
            valid_passports += 1

            fields = cur_passport.strip().split(' ')
            if all([req_fields[x.split(':')[0]](x.split(':')[1]) for x in fields]):
                valid_passports2 += 1

        cur_passport = ""

print("Valid passports:", str(valid_passports))
print("Valid passports 2:", str(valid_passports2))