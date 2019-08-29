def cmpd_interest(interest_rate, amount, months):
    total_amount = amount
    count = 0
    while count < months:
        monthly_amount = (interest_rate * total_amount) / 12
        total_amount += monthly_amount
        count += 1

    print("You earned " + str(float(total_amount - amount)) +
          " after " + str(months) + " months!")

    return total_amount
