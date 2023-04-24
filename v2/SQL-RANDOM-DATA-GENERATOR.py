from FoxyFunctions import ff
import subprocess
import os
import random

class main:
    def __init__(self):
        # activate GUI
        main_menu = (("RUN", self.run), ("CSV -> SQL", self.csv_to_sql), ("EDIT SCRIPT", self.edit_script), ("RESOURCES", self.resources), ("OUTPUT", self.openoutput))
        self.ff = ff("SQL-RANDOM-DATA-GENERATOR", "1.0", main_menu)

        # run gui
        self.ff.run()
    
    def run(self):
        self.ff.clear()
        # read script
        script = self.ff.read_script("script.txt")

        # get settings
        scr = self.ff.settings_get("Resources location")
        table = self.ff.settings_get("Table Name")
        ent = int(self.ff.settings_get("Enteries"))
        outputfilelocation = self.ff.settings_get("Output location")
        outputfilelocation = outputfilelocation+"/"+"output.sql"

        # read script
        SCRIPT = []
        for line in script:
            # SPLIT LINE TO PARAMETERS
            field_name = line[1][0] # the name of the field you want to generate for. e.g. username
            lst_filename = line[1][1] # name of the .lst file to take data from. e.g. first_names.lst

            # ADD TO SCRIPT
            SCRIPT.append((field_name, lst_filename))
        
        # create datasheet
        DATA = {}
        for line in SCRIPT:
            field_name = line[0]
            lst_filename = line[1]
            data_type = line[2]
            file = open(scr+"/"+lst_filename, 'r', encoding='utf-8')
            lines = file.readlines()
            file.close()
            for l in lines:
                l = l.replace("\n", "")
                l = l.replace("'", "")
                if not field_name in DATA:
                    DATA[field_name] = []
                if data_type == "VARCHAR":
                    DATA[field_name].append("'"+l+"'")
                else:
                    DATA[field_name].append(l)

        # calculate workload
        steps = 0
        for x in range(ent):
            for line in SCRIPT:
                steps += 1
        
        # generate sql
        steps_done = 0
        max_enteries = 0
        output = ""
        entery = 0
        for x in range(ent):
            # display sql command
            if max_enteries == 0:
                max_enteries = 100

                # start a new INSERT
                self.ff.write("")

                output = "INSERT INTO "+table+" ("
                for line in SCRIPT:
                    field_name = line[0]
                    output += field_name+", "
                output = output[:-2]
                output += ") VALUES"
                self.ff.write(output)
            
            # display line
            max_enteries -= 1
            output = "("
            for line in SCRIPT:
                field_name = line[0]
                lst_filename = line[1]

                # update progress bar
                steps_done += 1
                percent = steps_done / steps
                self.ff.progress_bar_value_set(percent*100)
                
                # MAKE OUTPUT
                # select random entity
                i = random.randint(0, len(DATA[field_name])-1)
                selected_column = DATA[field_name][i]
                output += selected_column+", "
            output = output[:-2]
            output += "),"
            
            #self.ff.write("x="+str(x)+" ent="+str(ent)+" entery="+str(entery))
            if x == ent-1 or max_enteries == 0:
                output = output[:-2]
                output += ");"
            entery += 1
            #self.ff.write("["+str(entery)+"] "+output)
            self.ff.write(output)
        
        self.ff.save(outputfilelocation)
        os.popen(outputfilelocation)

    def csv_to_sql(self):
        scr = self.ff.settings_get("Resources location")
        self.ff.form("Transfer .csv to .sql file", ({"LABEL":"File name", "TYPE":"FILEDIALOG", "FD-LOCATION":scr, "FD-FILETYPES":("csv",), "FD-TITLE":"Load .csv file"}, ), self.csv_to_sql_submit)
    
    def csv_to_sql_submit(self, data):
        self.ff.clear()
        # get settings
        scr = self.ff.settings_get("Resources location")
        table = self.ff.settings_get("Table Name")
        outputfilelocation = self.ff.settings_get("Output location")
        outputfilelocation = outputfilelocation+"/"+"output.sql"
        
        # open csv file
        csvfile = data["File name"]
        file = self.ff.csv_to_list(csvfile)
        
        # calculate workload
        steps = 0
        for line in file:
            steps += 1
        
        # generate sql
        steps_done = 0
        max_enteries = 0
        output = ""
        i = 0
        for line in file:
            i += 1
            # update progress bar
            steps_done += 1
            percent = steps_done / steps
            self.ff.progress_bar_value_set(percent*100)
            
            # display sql command
            if max_enteries == 0:
                max_enteries = 100

                # start a new INSERT
                self.ff.write("")
                output = "INSERT INTO "+table+" ("
                headers = file[0]
                for header in headers:
                    output += header+", "
                output = output[:-2]
                output += ") VALUES"
                self.ff.write(output)
            
            # display line
            max_enteries -= 1
            output = "("
            for col in line:
                if not self.isnumber(col):
                    col = col.replace('"', "")
                    col = col.replace("'", "")
                    output += "'"+col+"'"+", "
                else:
                    output += col+", "
            output = output[:-2]
            output += "),"
            
            #self.ff.write("x="+str(x)+" ent="+str(ent)+" entery="+str(entery))
            if i == len(file) or max_enteries == 0:
                output = output[:-2]
                output += ");"
            #self.ff.write("["+str(entery)+"] "+output)
            self.ff.write(output)
        self.ff.save(outputfilelocation)
        os.popen(outputfilelocation)

    def resources(self):
        scr = self.ff.settings_get("Resources location")
        subprocess.Popen(r'explorer /select,"'+scr+'"')

    def edit_script(self):
        os.popen("script.txt")
    
    def openoutput(self):
        scr = self.ff.settings_get("Output location")
        subprocess.Popen(r'explorer /select,"'+scr+'"')
    
    def isnumber(self, txt):
        for ch in txt:
            if not ch in "0123456789":
                return False
        return True

main()