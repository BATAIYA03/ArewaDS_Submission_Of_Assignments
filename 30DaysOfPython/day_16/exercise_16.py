#level 1
#Question 1
class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        middle = n // 2

        if n % 2 == 0:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2
        else:
            return sorted_data[middle]

    def mode(self):
        frequency = {}

        for number in self.data:
            frequency[number] = frequency.get(number, 0) + 1

        highest_frequency = max(frequency.values())

        modes = [
            number for number, count in frequency.items()
            if count == highest_frequency
        ]

        return modes[0], highest_frequency

    def var(self):
        mean = self.mean()

        squared_differences = [
            (number - mean) ** 2 for number in self.data
        ]

        return sum(squared_differences) / self.count()

    def std(self):
        return self.var() ** 0.5

    def freq_dist(self):
        frequency = {}

        for number in self.data:
            frequency[number] = frequency.get(number, 0) + 1

        result = []

        for number, count in frequency.items():
            percentage = (count / self.count()) * 100
            result.append((percentage, number))

        return sorted(result, reverse=True)

    def percentile(self, percentile):
        sorted_data = sorted(self.data)

        index = (percentile / 100) * (self.count() - 1)

        lower = int(index)
        upper = min(lower + 1, self.count() - 1)

        fraction = index - lower

        return (
            sorted_data[lower] * (1 - fraction)
            + sorted_data[upper] * fraction
        )

    def describe(self):
        return (
            f"Count: {self.count()}\n"
            f"Sum: {self.sum()}\n"
            f"Min: {self.min()}\n"
            f"Max: {self.max()}\n"
            f"Range: {self.range()}\n"
            f"Mean: {self.mean()}\n"
            f"Median: {self.median()}\n"
            f"Mode: {self.mode()}\n"
            f"Variance: {round(self.var(), 1)}\n"
            f"Standard Deviation: {round(self.std(), 1)}\n"
            f"Frequency Distribution: {self.freq_dist()}"
        )


ages = [
    31, 26, 34, 37, 27, 26, 32, 32, 26, 27,
    27, 24, 32, 33, 27, 25, 26, 38, 37, 31,
    34, 24, 33, 29, 26
]

data = Statistics(ages)

print(data.describe())

#level 2
class PersonAccount:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def total_income(self):
        return sum(amount for amount, description in self.incomes)

    def total_expense(self):
        return sum(amount for amount, description in self.expenses)

    def account_info(self):
        return (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income()}\n"
            f"Total Expenses: {self.total_expense()}\n"
            f"Account Balance: {self.account_balance()}"
        )

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()


account = PersonAccount("Ahmad", "Muhammad")

account.add_income(50000, "Salary")
account.add_income(20000, "Freelancing")

account.add_expense(10000, "Food")
account.add_expense(5000, "Transport")

print(account.account_info())

print("Income Records:", account.incomes)
print("Expense Records:", account.expenses)