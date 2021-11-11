from sensitivityanalysis.sensitivity_analysis_calculator import SensitivityAnalysis as SA
from IPython.display import display

def main():
    
    run_program = 'Yes'

    while run_program == 'Yes':

        principal=float(input('Principal Amount: '))
        rate=float(input('Interest Rate: '))
        period=float(input('Period: '))
        years_until_payment=float(input('Years Until Payment: '))
        sqft=float(input('Property Square Feet: '))
        contracted_usd_sqft=float(input('Contracted $/sqft: '))
        market_usd_sqft_discount=float(input('Market Value per Square Foot Discount (Pct.): '))
        vacancy=float(input('Vacancy (Pct.): '))
        operating_expense_ratio=float(input('Operating Expense Ratio: '))
        cap_rate=float(input('Cap Rate: '))

        run_current_instance = 'Yes'
        while run_current_instance == 'Yes':
            main_instance = SA(principal, rate, period, years_until_payment, sqft, contracted_usd_sqft, market_usd_sqft_discount, vacancy, operating_expense_ratio, cap_rate)

            run_SA = 'Yes'

            while run_SA == 'Yes':
                program_choice = input(
                    """Please choose an option listed below by entering the corresponding number:
                    1. Financial Data Table
                    2. Balloon Payment Sensitivity Analysis
                    3. DSCR Sensitivity Analysis
                    4. LTV Sensitivity Analysis
                    """
                )

                if program_choice == '1':
                    display(main_instance.financial_data())

                elif program_choice == '2':
                    display(main_instance.balloon_payment_sensitivity())

                elif program_choice == '3':
                    display(main_instance.dscr_sensitivity())

                elif program_choice == '4':
                    display(main_instance.ltv_sensitivity())

                else:
                    raise ValueError('The input did not match any of the given options.')

                run_SA = input('Would you like to see another option? (Yes/No): ').title()

            change_variable = input('Would you like to change a variable? (Yes/No): ').title()
            if change_variable == 'No':
                run_current_instance = 'No'
            while change_variable == 'Yes':
                variable_to_change = input(
                    """Please choose a variable listed below by entering the corresponding number:
                    1. principal
                    2. rate
                    3. period
                    4. years_until_payment
                    5. sqft
                    6. contracted_usd_sqft
                    7. market_usd_sqft_discount
                    8. vacancy
                    9. operating_expense_ratio
                    10. cap_rate
                    """
                )

                if variable_to_change == '1':
                    principal=float(input('Principal Amount: '))
                elif variable_to_change == '2':
                    rate=float(input('Interest Rate: '))
                elif variable_to_change == '3':
                    period=float(input('Period: '))
                elif variable_to_change == '4':
                    years_until_payment=float(input('Years Until Payment: '))
                elif variable_to_change == '5':
                    sqft=float(input('Property Square Feet: '))
                elif variable_to_change == '6':
                    contracted_usd_sqft=float(input('Contracted $/sqft: '))
                elif variable_to_change == '7':
                    market_usd_sqft_discount=float(input('Market Value per Square Foot Discount (Pct.): '))
                elif variable_to_change == '8':
                    vacancy=float(input('Vacancy (Pct.): '))
                elif variable_to_change == '9':
                    operating_expense_ratio=float(input('Operating Expense Ratio: '))
                elif variable_to_change == '10':
                    cap_rate=float(input('Cap Rate: '))
                else:
                    raise ValueError('The input did not match any of the given options.')

                change_variable=input('Would you like to change another variable? (Yes/No): ').title()

        run_program = input('Would you like to start a new session? (Yes/No): ').title()

    print('Session Ended.')

if __name__ == '__main__':
    main()