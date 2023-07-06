#Combine two conditions
has_high_income=True
has_good_credit=False
has_criminal_record=False
# and ,or,not

if has_criminal_record and not has_good_credit:
    print("Eligible for loan")

