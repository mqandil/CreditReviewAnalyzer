import pandas as pd
from sensitivityanalysis.loan_payment_calculator import LoanPaymentCalculator as lpc

class SensitivityAnalysis():
    def __init__(self, principal=0, rate=0, period=0, years_until_payment=0, sqft=0, contracted_usd_sqft=0, market_usd_sqft_discount=0, vacancy=0, operating_expense_ratio=0, cap_rate=0):
        self.principal = principal
        self.rate = rate
        self.period = period
        self.years_until_payment = years_until_payment
        self.sqft = sqft
        self.contracted_usd_sqft = contracted_usd_sqft
        self.market_usd_sqft_discount = market_usd_sqft_discount
        self.vacancy = vacancy
        self.operating_expense_ratio = operating_expense_ratio
        self.cap_rate = cap_rate/100

        self.monthly_payment = lpc(rate=self.rate, nper=self.period, pv=self.principal).calc_pmt()
        self.total_monthly_payment = round(self.years_until_payment*self.monthly_payment*12, 2)
        self.balloon_payment = lpc(rate=self.rate, nper=self.period, pv=self.principal, years_until_payment=self.years_until_payment).calc_pv()
        self.total_amount_paid = self.total_monthly_payment + self.balloon_payment
        self.total_interest = self.principal + self.total_amount_paid

        self.effective_gross_income = self.sqft*self.contracted_usd_sqft*(1-self.market_usd_sqft_discount)*(1-self.vacancy)
        self.net_operating_income = self.effective_gross_income+(1-(self.effective_gross_income*self.operating_expense_ratio))
        
        self.debt_service_coverage = self.net_operating_income/(-self.monthly_payment*12)
        
        self.value = self.net_operating_income/self.cap_rate
        self.loan_to_value = self.principal/self.value

    def financial_data(self):
        financial_data = [
            f"${-self.monthly_payment:,.2f}", 
            f"${-self.total_monthly_payment:,.2f}",
            f"${-self.total_amount_paid:,.2f}",
            f"${-self.total_interest:,.2f}",
            f"${-self.balloon_payment:,.2f}",
            f"${self.effective_gross_income:,.2f}",
            f"${self.net_operating_income:,.2f}",
            f"{self.debt_service_coverage:.2f}",
            f"${self.value:,.2f}",
            f"{self.loan_to_value*100:.2f}%"
        ]
        
        financial_data_df = pd.DataFrame(
            columns=['Value'],
            index=[
                'Monthly Payment',
                'Total Monthly Payment',
                'Total Amount Paid',
                'Total Interest',
                'Balloon Payment',
                'Effective Gross Income',
                'Net Operating Income',
                'Debt Service Coverage',
                'Value',
                'Loan to Value'
            ],        
        )
        financial_data_df['Value'] = financial_data

        return financial_data_df

    def balloon_payment_sensitivity(self):
        sensitivity_analysis_rates = [
            self.rate-0.125*2, 
            self.rate-0.125, 
            self.rate, 
            self.rate+0.125, 
            self.rate+0.125*2
        ]
        sensitivity_analysis_periods = [
            self.period-10, 
            self.period-5, 
            self.period, 
            self.period+5, 
            self.period+10
        ]
        
        balloon_payment_sensitivity_df = pd.DataFrame(
            columns=sensitivity_analysis_rates,
            index=sensitivity_analysis_periods
        )

        for var_rate in sensitivity_analysis_rates:
            var_rate_list = []

            for var_period in sensitivity_analysis_periods:
                var_final_value = f"${-lpc(rate=var_rate, nper=var_period, pv=self.principal, years_until_payment=self.years_until_payment).calc_pv():,.2f}"
                var_rate_list.append(var_final_value)

            balloon_payment_sensitivity_df[var_rate] = var_rate_list

        sensitivity_analysis_rates_final = [
            f"{self.rate-0.125*2:.3f}%", 
            f"{self.rate-0.125:.3f}%", 
            f"{self.rate:.3f}%", 
            f"{self.rate+0.125:.3f}%", 
            f"{self.rate+0.125*2:.3f}%"
        ]
        sensitivity_analysis_periods_final = [
            f"{self.period-10} Years", 
            f"{self.period-5} Years", 
            f"{self.period} Years", 
            f"{self.period+5} Years", 
            f"{self.period+10} Years"
        ]

        balloon_payment_sensitivity_df.columns = sensitivity_analysis_rates_final
        balloon_payment_sensitivity_df.index = sensitivity_analysis_periods_final

        return balloon_payment_sensitivity_df

    def dscr_sensitivity(self):
        sensitivity_analysis_rates = [
            self.rate-0.125*2, 
            self.rate-0.125, 
            self.rate, 
            self.rate+0.125, 
            self.rate+0.125*2
        ]
        sensitivity_analysis_periods = [
            self.period-10, 
            self.period-5, 
            self.period, 
            self.period+5, 
            self.period+10
        ]
        
        dscr_sensitivity_df = pd.DataFrame(
            columns=sensitivity_analysis_rates,
            index=sensitivity_analysis_periods
        )

        for var_rate in sensitivity_analysis_rates:
            var_rate_list = []

            for var_period in sensitivity_analysis_periods:
                var_final_value = f"{-self.net_operating_income/(lpc(var_rate, var_period, pv=self.principal).calc_pmt()*12):.2f}"
                var_rate_list.append(var_final_value)

            dscr_sensitivity_df[var_rate] = var_rate_list

        sensitivity_analysis_rates_final = [
            f"{self.rate-0.125*2:.3f}%", 
            f"{self.rate-0.125:.3f}%", 
            f"{self.rate:.3f}%", 
            f"{self.rate+0.125:.3f}%", 
            f"{self.rate+0.125*2:.3f}%"
        ]
        sensitivity_analysis_periods_final = [
            f"{self.period-10} Years", 
            f"{self.period-5} Years", 
            f"{self.period} Years", 
            f"{self.period+5} Years", 
            f"{self.period+10} Years"
        ]

        dscr_sensitivity_df.columns = sensitivity_analysis_rates_final
        dscr_sensitivity_df.index = sensitivity_analysis_periods_final

        return dscr_sensitivity_df

    def ltv_sensitivity(self):
        sensitivity_analysis_cap_rates = [
            100*self.cap_rate-0.125*2, 
            100*self.cap_rate-0.125, 
            100*self.cap_rate, 
            100*self.cap_rate+0.125, 
            100*self.cap_rate+0.125*2
        ]
        sensitivity_analysis_rent_sqft = [
            self.contracted_usd_sqft-4, 
            self.contracted_usd_sqft-2, 
            self.contracted_usd_sqft, 
            self.contracted_usd_sqft+2, 
            self.contracted_usd_sqft+4
        ]
        
        balloon_payment_sensitivity_df = pd.DataFrame(
            columns=sensitivity_analysis_cap_rates,
            index=sensitivity_analysis_rent_sqft
        )

        for var_cap_rate in sensitivity_analysis_cap_rates:
            var_rate_list = []

            for var_rent_sqft in sensitivity_analysis_rent_sqft:
                var_effective_gross_income = self.sqft*var_rent_sqft*(1-self.market_usd_sqft_discount)*(1-self.vacancy)
                var_net_operating_income = var_effective_gross_income+(1-(var_effective_gross_income*self.operating_expense_ratio))
                var_value = var_net_operating_income/var_cap_rate

                var_final_value = f"{self.principal/var_value:.2f}%"
                var_rate_list.append(var_final_value)

            balloon_payment_sensitivity_df[var_cap_rate] = var_rate_list

        sensitivity_analysis_cap_rates_final = [
            f"{100*self.cap_rate-0.125*2:.3f}%", 
            f"{100*self.cap_rate-0.125:.3f}%", 
            f"{100*self.cap_rate:.3f}%", 
            f"{100*self.cap_rate+0.125:.3f}%", 
            f"{100*self.cap_rate+0.125*2:.3f}%"
        ]
        sensitivity_analysis_rent_sqft_final = [
            f"${self.contracted_usd_sqft-4:.0f}/sqft", 
            f"${self.contracted_usd_sqft-2:.0f}/sqft", 
            f"${self.contracted_usd_sqft:.0f}/sqft", 
            f"${self.contracted_usd_sqft+2:.0f}/sqft", 
            f"${self.contracted_usd_sqft+4:.0f}/sqft"
        ]

        balloon_payment_sensitivity_df.columns = sensitivity_analysis_cap_rates_final
        balloon_payment_sensitivity_df.index = sensitivity_analysis_rent_sqft_final

        return balloon_payment_sensitivity_df



if __name__ == '__main__':
    test = SensitivityAnalysis(1050000, 3.875, 30, 10, 18151, 26 ,cap_rate=10.25)
    test.ltv_sensitivity()