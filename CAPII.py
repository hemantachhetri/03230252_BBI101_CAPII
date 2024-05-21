
# This personal Income Tax considers income sources, deductions, child education allowance, and marital status.

class IncomeSource:
    # Represents a source of income for an individual.
    def __init__(self, employee_income, life_insurance, child_education_allowance, other_allowance, spouse_income, house_rent):
        self.employee_income = int(employee_income)  # Converting income to integer
        self.life_insurance = int(life_insurance)
        self.child_education_allowance = child_education_allowance
        self.other_allowance = int(other_allowance)
        self.spouse_income = int(spouse_income)
        self.house_rent = int(house_rent)

    def calculate_PIT(self):
        taxable_income = self.employee_income + self.spouse_income - self.life_insurance - \
                         self.child_education_allowance - self.other_allowance

        Tax_rates = {
            (0, 300000): 0,
            (300001, 400000): 0.1,
            (400001, 650000): 0.15,
            (650001, 1000000): 0.20,
            (1000001, 1500000): 0.25,
            (1500001, float('inf')): 0.30
        }
         # Find the applicable tax rate by iterating through pay slap.
        for min_income, max_income in Tax_rates:
            if min_income <= taxable_income <= max_income:
                tax_rate = Tax_rates[(min_income, max_income)]
                break

        PIT = taxable_income * tax_rate
        if PIT > 300000:
            surcharge = PIT * 0.1
            PIT += surcharge

        return PIT


class Relation_status:
    def __init__(self, married, single, divorce, children: int):
        self.married = married
        self.single = single
        self.divorce = divorce
        self.children = children

    def child_education_allowance(self):
        if self.married or self.single:
            return 350000 * self.children
        else:
            return 0


class Deductions:
    def __init__(self, life_insurance, house_loan_interest, house_rent):
        self.life_insurance = int(life_insurance)
        self.house_loan_interest = int(house_loan_interest)
        self.house_rent = int(house_rent)

    def total_deductions(self):
        return self.life_insurance + self.house_loan_interest + self.house_rent


# Input and calculation
def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


Employee_name = input("Enter your name: ")
Age = input("Enter your age: ")
Job = input("Enter your occupation: ")
Income = get_user_input("Enter your income * 12: ")  
Relation_Status = input("What is your marital status?(single, married or divorce): ")
Children = get_user_input("Number of children enrolled in school?: ")
bonus = get_user_input("Enter bonus amount (if any): ")  # Optional bonus
Life_insurance = get_user_input("Enter life insurance amount: ")
rent_allowance = get_user_input("Enter your rent allowance: ")
other_allowance = get_user_input("Enter your other allowance: ")
spouse_income = get_user_input("Enter your spouse's income * 12 (if any): ")
house_rent = get_user_input("Enter your house rent: ")

# Objects and calculating PIT
Status = Relation_status(Relation_Status == "married", Relation_Status == "single", Relation_Status == "divorce", Children)
child_education_allowance = Status.child_education_allowance()

Deductions_amount = Deductions(Life_insurance, 0, house_rent)  # House loan interest set to 0 (placeholder)

Income_amount = IncomeSource(Income * 12, Life_insurance, child_education_allowance, house_rent, rent_allowance, spouse_income * 12)

pit = Income_amount.calculate_PIT()

print(f"{Employee_name}'s Personal Income Tax (PIT) is: {pit:.2f}")