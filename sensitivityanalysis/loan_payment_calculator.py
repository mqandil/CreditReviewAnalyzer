class LoanPaymentCalculator():
    def __init__(self, rate=0, nper=0, pmt=0, pv=0, fv=0, type_funct=0):
        self.rate = rate/100/12
        self.nper = nper*12
        self.pmt = pmt
        self.pv = -pv
        self.fv = fv
        self.type_funct = type_funct

    def calc_pmt(self):
        payment = self.pv*self.rate*((1+self.rate)**self.nper)/(((1+self.rate)**self.nper)-1)
        payment_final = round(payment, 2)
        return payment_final

test = LoanPaymentCalculator(rate=3.875, nper=30, pv=1050000)
test.calc_pmt()


