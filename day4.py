import sys
import os
import re

requirements = set(["byr", 'iyr', 'eyr', 'hgt', 'hcl',
                    'ecl', 'pid'])
eye_colors = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])


def main():
    filepath = sys.argv[1]
    count = 0
    if not os.path.isfile(filepath):
        print("File %s is not a file", filepath)
        sys.exit()
    passport_list = parse_file(filepath)
    for passport in passport_list:
        validity = is_valid(passport)
        if validity == "VALID":
            count += 1
    print(count)
    return None

def parse_file(filepath):
    new_data = []
    individual_data = []
    list_passports = []
    with open(filepath) as f:
        data = f.read()
    data = data.split("\n\n")
    for i in data:
        new_data.append(i.replace("\n", " "))
    for k in new_data:
        individual_data.append(k.split(" "))
    for passport in individual_data:
        d = dict(s.split(":") for s in passport)
        list_passports.append(d)
    return list_passports

def is_valid(passport):
    credentials = passport.keys()
    validity = "VALID"
    for i in requirements:
        if i not in credentials:
            return "NOT VALID"
    for key, value in passport.items():
        if key == "byr":
            if len(value) != 4:
                validity = "NOT VALID"
                break
            if int(value) < 1920 or int(value) > 2002:
                validity = "NOT VALID"
                break
        if key == "iyr":
            if len(value) != 4:
                validity = "NOT VALID"
                break
            if int(value) < 2010 or int(value) > 2020:
                validity = "NOT VALID"
                break
        if key == 'eyr':
            if len(value) != 4:
                validity = "NOT VALID"
                break
            if int(value) < 2020 or int(value) > 2030:
                validity = "NOT VALID"
                break
        if key == 'hgt':
            dimension = 'in'
            height = 0
            if re.search(r'\D+', value) is not None and re.search(r'\d+', value) is not None:
                dimension = re.search(r'\D+', value).group()
                height = int(re.search(r'\d+', value).group())
            if dimension == 'cm':
                if height < 150 or height > 193:
                    validity = "NOT VALID"
                    break
            elif dimension == 'in':
                if height < 59 or height > 76:
                    validity = "NOT VALID"
                    break
            else:
                validity = "NOT VALID"
                break
        if key == 'hcl':
            if len(value) != 7:
                validity = "NOT VALID"
                break
            if not re.match(r"#(\d|[a-f])+", value):
                validity = "NOT VALID"
                break
        if key == 'ecl':
            if value not in eye_colors:
                validity = "NOT VALID"
                break
        if key == "pid":
            if len(value) != 9:
                validity = 'NOT VALID'
                break
    return validity
        
if __name__ == '__main__':
    main()
