class Chef:
    def __init__(self,chef_role):
        self.chef_role = chef_role
    
    def display_info(self):
        print(f"{self.chef_role} is involved in preparing the meal")

class Entertainer:
    def __init__(self,entertainer_role):
        self.entertainer_role=entertainer_role
    
    def display_info(self):
        print(f"{self.entertainer_role} is involved in entertaining the audience")

class Yacht(Chef,Entertainer):
    def __init__(self,chef_role,entertainer_role):
        Chef.__init__(self, chef_role)
        Entertainer.__init__(self, entertainer_role)
    
    def invoke_base_methods(self):
        Chef.display_info(self)
        Entertainer.display_info(self)

def main():
    y1= Yacht("Gordon Ramsay","Michael Jackson")
    y1.invoke_base_methods()

if __name__ == "__main__":
    main()
