# Download SmartConsole.py from: https://github.com/VladFeldfix/Smart-Console/blob/main/SmartConsole.py
from SmartConsole import *
import random

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("SQL Random Data Generator", "1.0")
        
        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)
        self.sc.add_main_menu_item("CSV -> SQL", self.csv_sql)
        self.sc.add_main_menu_item("EDIT SCRIPT", self.edit_script)

        # get settings
        self.path_main = self.sc.get_setting("Work folder")
        self.rows = int(self.sc.get_setting("Generate values"))

        # test all paths
        self.sc.test_path(self.path_main)
        self.sc.test_path("script.txt")

        # set global variables
        self.table_name = "Unnamed_table"

        # display main menu
        self.sc.start()

    def run(self):
        # run script
        self.values = {}
        functions = {}
        functions["FIELD"] = (self.field, ("NAME", "LIST FILE", "FIELD TYPE"))
        functions["TABLE_NAME"] = (self.name_table, ("NAME",))
        self.sc.run_script("script.txt", functions)
        self.generate()

        # restart
        self.sc.restart()
    
    def edit_script(self):
        # edit script
        os.popen("script.txt")
        # restart
        self.sc.restart()

    def field(self, arguments):
        # get arguments
        name = arguments[0]
        list_file = self.path_main+"/"+arguments[1]
        field_type = arguments[2]

        # get values from list
        self.sc.test_path(list_file)
        data = open(list_file, 'r')
        lines = data.readlines()
        data.close()

        # add new values
        for x in range(self.rows):
            # select a random value from the list
            new_value = random.choice(lines)
            
            # add quotation marks
            if field_type == "VARCHAR":
                new_value = "'"+new_value+"'"
            
            # remove \n
            new_value = new_value.strip()
            new_value = new_value.replace("\n", "")
            
            if not name in self.values:
                self.values[name] = [new_value]
            else:
                self.values[name].append(new_value)
    
    def generate(self):
        data = {}
        fields = []
        outputfile = open(self.path_main+"/output.txt", 'w')
        for field_name, values in self.values.items():
            data[field_name] = []
            fields.append(field_name)
            for val in values:
                data[field_name].append(val)
        for i in range(self.rows):
            output = "INSERT INTO "+self.table_name+" VALUES ("
            add = ""
            for j in range(len(data)):
                add += data[fields[j]][i]+","
            add = add[:-1]
            output += add
            output += ");"
            outputfile.write(output+"\n")
        outputfile.close()
        os.popen(self.path_main+"/output.txt")
        
    def name_table(self,arguments):
        self.table_name = arguments[0]
    
    def csv_sql(self):
        # get path
        path = self.sc.input("Insert path to csv file")
        self.sc.test_path(path)
        path = path.replace("\\", "/")
        filename = path.split("/")
        filename = filename[-1]
        filename = filename.split(".")
        filename = filename[0]

        # read data from csv file
        file = open(path, 'r')
        lines = file.readlines()
        file.close()

        # go over each line
        outputfile = open(self.path_main+"/output.txt", 'w')
        for line in lines:
            output = "INSERT INTO "+filename+" VALUES ("+str(line).replace("\n","")+");"
            outputfile.write(output+"\n")
        outputfile.close()
        os.popen(self.path_main+"/output.txt")
        
        # restart
        self.sc.restart()
main()