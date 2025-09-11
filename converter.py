

def currency_converter(amount: float, from_currency: str, to_currency: str, rates: dict) -> float:
    from_currency = from_currency.lower()
    to_currency = to_currency.lower()
    if from_currency not in rates or to_currency not in rates:
        print("Unsupported currency.")
        return None

    # Convert to GHS first if not already
    amount_in_ghs = amount / \
        rates[from_currency] if from_currency != "ghs" else amount
    converted = amount_in_ghs * rates[to_currency]

    print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
    return converted


def main():
    """The main function will collect input from users and run the converter function"""
    print("Welcome to the Currency Converter")

    # Example rates (fixed for now, later we’ll fetch from internet)
    rates = {
        "usd": 0.085,
        "euro": 0.078,
        "yuan": 0.62,
        "cfa": 55.0,
        "ghs": 1.0  # Ghana Cedi base
    }

    print("Please indicate which currency you want to convert from and which one you want to convert to:")
    convert_from = input("Convert From: ")
    convert_to = input("Convert To: ")
    convert_amt = float(input("Amount to Convert: "))

    if convert_amt < 0:
        print("Please you can only convert positive amounts. I will convert your amount into positive")
        convert_amt = abs(convert_amt)

    currency_converter(convert_amt, convert_from, convert_to, rates)


if __name__ == "__main__":
    main()
