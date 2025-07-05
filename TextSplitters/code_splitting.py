from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text= """
class RandomUtility:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome to the utility class.")

    def calculate_sum(self, numbers):
        total = sum(numbers)
        print(f"The sum of {numbers} is {total}.")
        return total

    def reverse_string(self, s):
        reversed_str = s[::-1]
        print(f"The reverse of '{s}' is '{reversed_str}'.")
        return reversed_str

    def is_prime(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_fibonacci(self, limit):
        fib = [0, 1]
        while len(fib) < limit:
            fib.append(fib[-1] + fib[-2])
        return fib[:limit]

# Example usage
if __name__ == "__main__":
    util = RandomUtility("TestUser")
    util.greet()
    util.calculate_sum([10, 20, 30])
    util.reverse_string("LangChain")
    print(util.is_prime(17))
    print(util.generate_fibonacci(10))

"""
splitter= RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

chunks=splitter.split_text(text)

print(len(chunks))
print(chunks[3])