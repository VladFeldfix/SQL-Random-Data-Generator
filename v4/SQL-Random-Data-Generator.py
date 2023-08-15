from SmartConsole import *

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("SQL Random Data Generator", "4.0")

        # set-up main memu
        self.sc.main_menu["RUN"] = self.run
        self.sc.main_menu["EDIT SCRIPT"] = self.edit_script

        # get settings
        self.get_settings()

        # test all paths
        self.sc.test_path(self.)

        self.sc.start()

    def get_settings(self):
        # get settings
        self.var1 = self.sc.get_setting("var1")
    
    def run(self):
        # get settigns
        self.get_settings()

        # run script
        functions = {}
        functions["FIELD"] = (self.start, ("NAME", "LIST FILE", "FIELD TYPE"))
        self.sc.run_script("script.txt", functions)

        # restart
        self.sc.restart()
    
    def edit_script(self):
        # restart
        self.sc.restart()

main()