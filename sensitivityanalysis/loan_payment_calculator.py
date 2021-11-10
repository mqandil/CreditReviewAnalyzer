class LoanPaymentCalculator():
    def __init__(self, rate=0, nper=0, pmt=0, pv=0, fv=0, type_funct=0, years_until_payment=0):
        self.rate = rate
        self.nper = nper
        self.pmt = pmt
        self.pv = pv
        self.fv = fv
        self.type_funct = type_funct
        self.years_until_payment = years_until_payment

    def calc_pmt(self):
        pmt_pv = -self.pv
        pmt_rate = self.rate/100/12
        pmt_nper = self.nper*12
        payment = pmt_pv*pmt_rate*((1+pmt_rate)**pmt_nper)/(((1+pmt_rate)**pmt_nper)-1)
        payment_final = round(payment, 2)
        return payment_final

    
    def calc_pv(self):
        pv_pmt = LoanPaymentCalculator(rate=self.rate, nper=self.nper, pv=self.pv).calc_pmt()
        pv_rate = self.rate/100/12
        pv_nper = (self.nper-self.years_until_payment)*12
        present_value = pv_pmt*((1-(1+pv_rate)**-pv_nper)/pv_rate)
        present_value_final = round(present_value, 2)
        return present_value_final

if __name__ == '__main__':

    test = LoanPaymentCalculator(rate=3.875, nper=30, pv=1050000, years_until_payment=10)
    test.calc_pmt()
    test.calc_pv()


