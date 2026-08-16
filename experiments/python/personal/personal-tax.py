# 2019个人所得税计算器


def personal_tax_calculator(raw_income, insurace_base, free_charge_amount, special_item_free_amount):
    print('month\t total_should_tax_amount\t tax_amount \tincome_of_this_month')

    income_after_insurance = raw_income - (insurace_base * 0.222 + 3)
    tax_rate_table = [
        (0, 36000, 0.03),
        (36000, 144000, 0.10),
        (144000, 300000, 0.20),
        (300000, 420000, 0.25),
        (420000, 660000, 0.30),
        (660000, 960000, 0.35),
        (960000, 9999990000, 0.45)
    ]

    last_month_total_taxed_amount = 0.0
    this_month_total_taxed_amount = 0.0
    yearly_total_tax_amount = 0.0
    yearly_income_amount = 0.0
    monthly_tax_amount = income_after_insurance - free_charge_amount - special_item_free_amount
    for i in range(0, 12):
        this_month_total_taxed_amount = last_month_total_taxed_amount + monthly_tax_amount
        this_month_tax_amount = 0.0
        for begin, end, tax_rate in tax_rate_table:
            if begin > this_month_total_taxed_amount:
                break
            
            if begin <= last_month_total_taxed_amount < end:
                if this_month_total_taxed_amount <= end:
                    this_month_tax_amount += (this_month_total_taxed_amount - last_month_total_taxed_amount) * tax_rate
                else:
                    this_month_tax_amount += (end - last_month_total_taxed_amount) * tax_rate
                    last_month_total_taxed_amount = end
            
        income_of_this_month = income_after_insurance - this_month_tax_amount
        last_month_total_taxed_amount = this_month_total_taxed_amount
        yearly_total_tax_amount += this_month_tax_amount
        yearly_income_amount += income_of_this_month

        this_month_tax_amount = float('%.2f' % this_month_tax_amount)
        income_of_this_month = float('%.2f' % income_of_this_month)
        last_month_total_taxed_amount = float('%.2f' % last_month_total_taxed_amount)
        this_month_total_taxed_amount = float('%.2f' % this_month_total_taxed_amount)

        print('{}\t {}\t\t\t {} \t{}\r\n'.format(i+1, this_month_total_taxed_amount, this_month_tax_amount, income_of_this_month))
    
    print('raw_income = %.2f' % raw_income)
    print('insurace_base = %.2f' % insurace_base)
    print('free_charge_amount = %.2f' % free_charge_amount)
    print('special_item_free_amount = %.2f' % special_item_free_amount)
    print('yearly_income_amount = %.2f' % (yearly_income_amount))
    print('yearly_total_tax_amount = %.2f' % yearly_total_tax_amount)
    print('\r\n')

if __name__ == '__main__':
    personal_tax_calculator(00.00, 25401.10, 5000.00, 00.00)
