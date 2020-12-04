import binascii

abs_path = "C:\\Users\\root\\Documents\\GitHub\\adventofcode2020\\04\\04.txt"

file_input = open(abs_path)

# Important, due to time concerns you should add a second breakline
# at the end of the input (04.txt) for this solution to work. 
# TODO FIXME

eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

class Credentials:
    byr=""
    iyr=""
    eyr=""
    hgt=""
    hcl=""
    ecl=""
    pid=""
    cid=""
    def is_valid(self):
        result = True # FIXME If I had time i would have reduced all the IF's to a single return statement
        reason = ""
        if self.byr == "":
            result = False
            reason = "Missing BYR"
        if self.iyr == "":
            result = False
            reason = "Missing IYR"
        if self.eyr == "":
            result = False
            reason = "Missing EYR"
        if self.hgt == "":
            result = False
            reason = "Missing HGT"
        if self.hcl == "":
            result = False
            reason = "Missing HCL"
        if self.ecl == "":
            result = False
            reason = "Missing ECL"
        if self.pid == "":
            result = False
            reason = "Mising PID"
        try: # Part 2
            if (int(self.byr) < 1920) or (int(self.byr) > 2002):
                result = False
                reason = "BYR not in range"
            if (int(self.iyr) < 2010) or (int(self.iyr) > 2020):
                result = False
                reason = "IYR not in range"
            if (int(self.eyr) < 2020) or (int(self.eyr) > 2030):
                result = False
                reason = "EYR not in range"
            if self.hgt.endswith("cm"):
                realhgt = int(self.hgt.replace("cm", ""))
                if (realhgt < 150) or (realhgt > 193):
                    reason = "HGT as cm not in range"
                    result = False
            elif self.hgt.endswith("in"):
                realhgt = int(self.hgt.replace("in", ""))
                if (realhgt < 59) or (realhgt > 76):
                    reason = "HGT as inches not in range"
                    result = False
            else:
                reason = "HGT not ending in cm nor in"
                result = False
            if self.hcl.startswith("#"):
                clr = binascii.unhexlify(self.hcl.replace("#", ""))
            else:
                reason = "HCL doesnt start with #"
                result = False
            if self.ecl not in eyecolors:
                reason = "ECL not in eyecolors"
                result = False
            if len(self.pid) != 9:
                reason = "PID length is {}".format(len(self.pid))
                result = False

        except Exception as error:
            result = False
            reason = "Exception ocurred {}".format(error) 

        return (result, reason)

passports = []

valids = 0

local = Credentials()

for line in file_input:
    print("Checking line: {} \n".format(line))
    if line == "\n":
        valid, reason = local.is_valid()
        if valid == True:
            valids = valids + 1
            print("Is valid! \n")
        else:
            print("Is not valid, reason: {} \n".format(reason))
        passports.append(local)
        local = Credentials()
    else:
        d_line = line.split(" ")
        for parts in d_line:
            cred_str = parts.split(":")
            if cred_str[0] == "byr":
                local.byr = cred_str[1].strip()
            if cred_str[0] == "iyr":
                local.iyr = cred_str[1].strip()
            if cred_str[0] == "eyr":
                local.eyr = cred_str[1].strip()
            if cred_str[0] == "hgt":
                local.hgt = cred_str[1].strip()
            if cred_str[0] == "hcl":
                local.hcl = cred_str[1].strip()
            if cred_str[0] == "ecl":
                local.ecl = cred_str[1].strip()
            if cred_str[0] == "pid":
                local.pid = cred_str[1].strip()
            if cred_str[0] == "cid":
                local.cid = cred_str[1].strip()

print(valids)