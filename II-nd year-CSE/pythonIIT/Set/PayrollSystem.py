from abc import ABC, abstractmethod

# ================= BASE CLASS =================
class Employee(ABC):
    def __init__(self, emp_id, name, category, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.category = category  # Manager, HR, Servant, etc.
        self.basic_salary = basic_salary

    def display_info(self):
        print("--------------------------------")
        print("Employee ID   : " + str(self.emp_id))
        print("Employee Name : " + self.name)
        print("Category      : " + self.category)

    @abstractmethod
    def calculate_salary(self):
        pass


# ================= FULL TIME EMPLOYEE =================
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Work Type     : Full Time")
        print("Basic Salary  : " + str(self.basic_salary))
        
        # Taking HRA and DA as input during the calculation phase
        hra_per = float(input("Enter HRA % for " + self.name + ": "))
        da_per = float(input("Enter DA % for " + self.name + ": "))
        
        hra = self.basic_salary * (hra_per / 100)
        da = self.basic_salary * (da_per / 100)
        ta = self.basic_salary * 0.05
        
        gross = self.basic_salary + hra + da + ta
        pf = self.basic_salary * 0.12
        tax = gross * 0.05
        net = gross - pf - tax

        print("Calculated Gross : " + str(gross))
        print("Calculated Net   : " + str(net))


# ================= PART TIME EMPLOYEE =================
class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, category, hours, rate):
        self.hours = hours
        self.rate = rate
        calc_basic = hours * rate
        Employee.__init__(self, emp_id, name, category, calc_basic)

    def calculate_salary(self):
        print("Work Type     : Part Time")
        print("Total Basic   : " + str(self.basic_salary))
        
        hra_per = float(input("Enter HRA % for " + self.name + ": "))
        da_per = float(input("Enter DA % for " + self.name + ": "))
        
        hra = self.basic_salary * (hra_per / 100)
        da = self.basic_salary * (da_per / 100)
        gross = self.basic_salary + hra + da
        net = gross - (gross * 0.05)

        print("Calculated Net   : " + str(net))


# ================= CONTRACT EMPLOYEE =================
class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Work Type     : Contract")
        print("Contract Base : " + str(self.basic_salary))
        
        hra_per = float(input("Enter HRA % for " + self.name + ": "))
        da_per = float(input("Enter DA % for " + self.name + ": "))
        
        hra = self.basic_salary * (hra_per / 100)
        da = self.basic_salary * (da_per / 100)
        gross = self.basic_salary + hra + da
        net = gross - (gross * 0.03)

        print("Calculated Net   : " + str(net))


# ================= PAYROLL SYSTEM =================
class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_emp(self, type_choice):
        print("\n--- ENTER DETAILS ---")
        eid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        cat = input("Enter Category (Manager/HR/Servant): ")
        
        temp_basic = 0
        hrs = 0
        rte = 0

        if type_choice == '1':
            temp_basic = float(input("Enter Basic Salary: "))
        elif type_choice == '2':
            hrs = int(input("Enter Hours: "))
            rte = float(input("Enter Rate: "))
            temp_basic = hrs * rte
        elif type_choice == '3':
            temp_basic = float(input("Enter Contract Amount: "))

        # CONDITION: If salary is 6000 or more, DO NOT ACCEPT
        if temp_basic >= 6000:
            print("!!! REJECTED: Salary " + str(temp_basic) + " is 6000 or more. Entry not saved.")
            return

        # Adding to list only if condition (< 6000) is met
        if type_choice == '1':
            self.employees.append(FullTimeEmployee(eid, name, cat, temp_basic))
        elif type_choice == '2':
            self.employees.append(PartTimeEmployee(eid, name, cat, hrs, rte))
        elif type_choice == '3':
            self.employees.append(ContractEmployee(eid, name, cat, temp_basic))
        
        print("Employee " + name + " added successfully.")

    def display_category_wise(self):
        if not self.employees:
            print("No employees in the system.")
            return
            
        target_cat = input("\nEnter Category to display (e.g., Manager, HR): ")
        found = False
        
        print("\n===== DISPLAYING " + target_cat.upper() + "S =====")
        for emp in self.employees:
            if emp.category.lower() == target_cat.lower():
                emp.display_info()
                # HRA/DA inputs happen INSIDE this call now
                emp.calculate_salary()
                found = True
        
        if not found:
            print("No employees found in category: " + target_cat)


# ================= MAIN =================
def main():
    system = PayrollSystem()
    while True:
        print("\n--- PAYROLL SYSTEM ---")
        print("1. Add Full Time")
        print("2. Add Part Time")
        print("3. Add Contract")
        print("4. Display Category-Wise & Calculate Payroll")
        print("5. Exit")
        
        choice = input("Choice: ")

        if choice in ['1', '2', '3']:
            system.add_emp(choice)
        elif choice == '4':
            system.display_category_wise()
        elif choice == '5':
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()

