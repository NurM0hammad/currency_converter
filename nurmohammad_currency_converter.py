class CurrencyConverter:
    # Class attribute to store exchange rates
    exchange_rates = {
        'USD': {'USD': 1, 'EUR': 0.85, 'GBP': 0.72, 'BDT': 84.50, 'JPY': 110.25},
        'EUR': {'USD': 1.18, 'EUR': 1, 'GBP': 0.85, 'BDT': 99.42, 'JPY': 129.75},
        'GBP': {'USD': 1.39, 'EUR': 1.18, 'GBP': 1, 'BDT': 117.35, 'JPY': 153.20},
        'BDT': {'USD': 0.012, 'EUR': 0.010, 'GBP': 0.0085, 'BDT': 1, 'JPY': 1.30},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0065, 'BDT': 0.77, 'JPY': 1}
    }

    def __init__(self, amount, from_currency, to_currency):
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()

    def convert(self):
        """Instance method to perform conversion"""
        if not self.is_valid_currency(self.from_currency) or not self.is_valid_currency(self.to_currency):
            return None

        rate = self.exchange_rates[self.from_currency][self.to_currency]
        return self.amount * rate

    @classmethod
    def update_exchange_rate(cls, from_curr, to_curr, new_rate):
        """Class method to update exchange rates"""
        if cls.is_valid_currency(from_curr) and cls.is_valid_currency(to_curr):
            cls.exchange_rates[from_curr][to_curr] = new_rate
            return True
        return False

    @staticmethod
    def is_valid_currency(currency_code):
        """Static method to validate currency codes"""
        valid_currencies = ['USD', 'EUR', 'GBP', 'BDT', 'JPY']
        return currency_code in valid_currencies


class Logger:
    """Logger class demonstrating association with CurrencyConverter"""

    def log(self, user, amount, result):
        """Method to log conversion details"""
        with open('conversion_logs.txt', 'a') as file:
            file.write(f"User: {user} | Amount: {amount} | Result: {result}\n")


def main():
    print("💰 Welcome to Currency Converter CLI App 💰")
    print("Supported currencies: USD, EUR, GBP, BDT, JPY")

    # Create logger instance
    logger = Logger()

    while True:
        try:
            amount = float(input("\nEnter amount to convert: "))
            from_curr = input("From currency: ").upper()
            to_curr = input("To currency: ").upper()

            if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
                print("Invalid currency code! Please try again.")
                continue

            converter = CurrencyConverter(amount, from_curr, to_curr)
            result = converter.convert()

            if result is not None:
                print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}")

                # Log the conversion
                user = input("Enter your name for logging: ")
                logger.log(user, f"{amount} {from_curr}",
                           f"{result:.2f} {to_curr}")
            else:
                print("Conversion failed due to invalid input!")

        except ValueError:
            print("Please enter a valid number for amount!")

        choice = input("\nDo another conversion? (y/n): ").lower()
        if choice != 'y':
            print("\nThank you for using Currency Converter!")
            break


if __name__ == "__main__":
    main()
