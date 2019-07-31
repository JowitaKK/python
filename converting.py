print ("How many km did You cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2) # round (thing to round, how many decimal points- ile po przecinku miejsc)
print(f"Your {kms} km ride was {miles} mi ")