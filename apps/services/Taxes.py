
Single = [8350,33950,82250,171550,372950]
MarriedfillingjointlyorQualifyingwidow = [16700,67900,137050,208850,372950]
marriedfillingsepared = [8350,33950,68525,104425,186475]
headofhousehold  = [11950,45500,117450,190200,372950]
Percents = [10,15,25,28,33,35]

def GetTax(Income,kind):
    tax = 0
    if kind == 'H':
        Default = headofhousehold
    elif kind == 'MS':
        Default = marriedfillingsepared
    elif kind == 'M':
        Default = MarriedfillingjointlyorQualifyingwidow
    else:
        Default = Single
    for i in range(5):
        if (Income > Default[i]) and (i<6):
            print Default[i]*(Percents[i]/100.0)
            tax += Default[i]*(Percents[i]/100.0)
            Income -= Default[i]
        elif (i>5):
            return tax + Income*(Percents[5]/100.0)

        else:
            return tax + Income*(Percents[i]/100.0)

    return tax

print GetTax(41200,'S')
