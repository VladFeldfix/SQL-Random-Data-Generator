from SmartConsole import *
import random

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("SQL Random Data Generator", "4.0")
        
        # set-up main memu
        self.sc.add_main_menu_item("RUN", self.run)
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
            self.sc.print(output)
        
    def name_table(self,arguments):
        self.table_name = arguments[0]

main()

"""
from SmartConsole import *

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("SQL Random Data Generator", "4.0")

        # set-up main memu
        self.sc.main_menu["RUN"] = self.run
        self.sc.main_menu["EDIT SCRIPT"] = self.edit_script
        self.sc.add_main_menu_item("ADD NEW BRAID", self.new)

        # get settings
        self.get_settings()

        # test all paths
        #self.sc.test_path(self.var1)

        self.sc.start()

    def get_settings(self):
        # get settings
        #self.var1 = self.sc.get_setting("var1")
        pass
    
    def run(self):
        return
        # get settigns
        self.get_settings()

        # run script
        self.values = {}
        functions = {}
        functions["FIELD"] = (self.field, ("NAME", "LIST FILE", "FIELD TYPE"))
        self.sc.run_script("script.txt", functions)

        # restart
        self.sc.restart()
    
    def edit_script(self):
        # restart
        self.sc.restart()

    def field(self, arguments):
        # get arguments
        name = arguments[0]
        list_file = arguments[1]
        field_type = arguments[2]

        # get values from list
        self.sc.test_path(list_file)
        data = open(list_file, 'r')
        lines = data.readlines()
        data.close()
        print(lines)

        # add new values
        for x in range(200):
            if field_type == "VARCHAR":
                new_value = "'"+new_value+"'"
            
            if not name in self.values:
                self.values[name] = [new_value]
            else:
                self.values[name].append(new_value)
        
main()

"""