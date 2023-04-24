import random
import string

# create letter bank
LowerCaseLetters = string.ascii_lowercase
UpperCaseLetters = string.ascii_uppercase
NumbersBank = "0123456789"

# STR - random assmbly of letters:              MIN_LENGTH, MAX_LENGTH, *UNIQUE, *UPPERCASE, *LOWERCASE, *NUMBERS
# INT - random INT from min to max:             MIN, MAX
# FLOAT - random FLOAT:                         MIN, MAX
# CHAR - random single character:               FIRST_OPTION, SECOND_OPTION ... 
# BOOL - randomly assign true or false:         CHANCE_OF_TRUE, CHANCE_OF_FALSE
# LST - choose random value from an .lst file:  FILE_NAME

class field:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.min_len = ""
        self.max_len = ""
        self.filename = ""
        self.unique = False
        self.uppercase = False
        self.lowercase = False
        self.numbers = False
        self.options = []
        self.used_fields = []
        self.list = []
    
    def get_list(self):
        file = open(self.filename, 'r', encoding="utf-8")
        lines = file.readlines()
        result = []
        for line in lines:
            line = line.replace("\n", "")
            result.append(line)
        file.close()
        return result
    
    def generate_field(self):
        result = self.choose_proper_generation()
        if self.unique:
            if result in self.used_fields:
                self.generate_field()
        self.used_fields.append(result)
        return result
    
    def choose_proper_generation(self):
        # STR
        if self.type == "STR":
            result = self.generate_random_string()
        # INT
        if self.type == "INT":
            result = self.generate_random_int()
        
        # FLOAT
        if self.type == "FLOAT":
            result = self.generate_random_float()
        
        # CHAR
        if self.type == "CHAR":
            result = self.generate_random_char()
        
        # BOOL
        if self.type == "BOOL":
            result = self.generate_random_bool()
        
        # LST
        if self.type == "LST":
            result = self.choose_random_lst_entery()

        return result

    def check_unique(self, text):
        return text in self.used_fields
    
    def generate_random_string(self):
        str = ""
        options = []
        length = random.randint(self.min_len, self.max_len)
        for ch in range(length):
            options = []
            if self.uppercase:
                options.append(random.choice(UpperCaseLetters))
            if self.lowercase:
                options.append(random.choice(LowerCaseLetters))
            if self.numbers:
                options.append(random.choice(NumbersBank))
            ch = random.choice(options)
            str += ch
        return str
    
    def generate_random_int(self):
        return random.randint(self.min_len, self.max_len)
    
    def generate_random_float(self):
        return random.uniform(self.min_len, self.max_len)
    
    def generate_random_char(self):
        return random.choice(self.options)
    
    def generate_random_bool(self):
        return random.choice((0, 1))
    
    def choose_random_lst_entery(self):
        return random.choice(self.list)

class table:
    def __init__(self):
        self.table_name = ""
        self.enteries = 0
        self.fields = []
        self.headers = []
        self.lines = []

    def set_table_name(self, name):
        self.table_name = name
    
    def set_number_of_enteries(self, n):
        self.enteries = int(n)
    
    def set_field(self, name, type, params):
        fld = field()
        fld.name = name
        fld.type = type
        if type == "STR" or type == "INT" or type == "FLOAT":
            fld.min_len = int(params[0])
            fld.max_len = int(params[1])
        if type == "LST" or type == "LST_FULL":
            fld.filename = params[0]
            fld.list = fld.get_list()
        if type == "CHAR":
            fld.options = params

        if "UNIQUE" in params:
            fld.unique = True
        if "UPPERCASE" in params:
            fld.uppercase = True
        if "LOWERCASE" in params:
            fld.lowercase = True
        if "NUMBERS" in params:
            fld.numbers = True
        self.fields.append(fld)
    
    def generate_full_file(self, filename):
        file = open(filename, 'r', encoding="utf-8")
        headers = file.readline()
        headers = headers.replace("\n","")
        headers = headers.split(",")
        lines = file.readlines()
        file.close()
        for h in headers:
            self.headers.append(h)
        for l in lines:
            l = l.replace("\n", "")
            l = l.split(",")
            self.lines.append(l)
        self.generate_sql_query()

    def generate_table(self):
        i = 0
        for f in self.fields:
            self.headers.append(f.name)
        while i < self.enteries:
            i += 1
            line = []
            for f in self.fields:
                line.append(f.generate_field())
            self.lines.append(line)
        self.generate_sql_query()
        
    def generate_sql_query(self):
        file = open(self.table_name+".sql", 'w', encoding="utf-8")
        i = 0
        line_number = 0
        for line in self.lines:
            line_number += 1
            if i == 0:
                file.write("INSERT INTO "+self.table_name+str(tuple(self.headers)).replace("'", "`")+" VALUES\n")
                endian = ","
            if i < 900:
                i += 1
            else:
                i = 0
                endian = ";\n"
            if line_number == len(self.lines):
                endian = ";\n"
            file.write(str(tuple(line))+endian+"\n")
        file.close()

file = open("script.txt")
lines = file.readlines()
file.close()
tbl = table()
for line in lines:
    line = line.replace("\n","")
    line = line.split(" ")
    if line[0] == "TABLE_NAME":
        tbl.set_table_name(line[1])
    if line[0] == "ENTRIES":
        tbl.set_number_of_enteries(line[1])
    if line[0] == "#":
        tbl.set_field(line[1], line[2], line[3:])
    if line[0] == "GENERATE_FULL":
        tbl.generate_full_file(line[1])

tbl.generate_table()
input("DONE!")
