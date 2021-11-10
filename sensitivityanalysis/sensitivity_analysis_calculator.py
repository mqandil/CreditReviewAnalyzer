import pandas as pd
import tkinter
from loan_payment_calculator import LoanPaymentCalculator as lpc

class SensitivityAnalysis():
    def __init__(self, principal=0, rate=0, period=0, years_until_payment=0, sqft=0, contracted_usd_sqft=0, market_usd_sqft_discount=0, vacancy=0, cap_rate=0):
        self.principal = principal
        self.rate = rate
        self.period = period
        self.years_until_payment = years_until_payment
        self.sqft = sqft
        self.contracted_usd_sqft = contracted_usd_sqft
        self.market_usd_sqft_discount = market_usd_sqft_discount
        self.vacancy = vacancy
        self.cap_rate = cap_rate

        self.monthly_payment = lpc(rate=self.rate, nper=self.period, pv=self.principal).calc_pmt()
        self.total_monthly_payment = 0
        self.total_amount_paid = 0
        self.total_interest = 0
        self.balloon_payment = 0
        
        self.effective_gross_income = 0
        self.net_operating_income = 0
        
        self.debt_service_coverage = 0
        
        self.value = 0
        self.loan_to_value = 0

    def financial_data(self):
        pass

    def balloon_payment_sensitivity(self):
        pass

    def dscr_sensitivity(self):
        pass

    def ltv_sensitivity(self):
        pass


if __name__ == '__main__':
    test = SensitivityAnalysis(1050000, 3.875, 30, 10, 18151, 26, cap_rate=10.25)