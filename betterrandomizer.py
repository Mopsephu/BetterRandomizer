import random;

def generateRandomNumber(From : int = 0, To : int = 1) -> int:
    if From > To:
        From, To = To, From;
    return random.randint(From, To);

def generateSomeRandomNumbers(From : int = 0, To : int = 1, Amount : int = 1) -> list[int]:
    randomNumbers : list[int] = [];
    if From > To:
        From, To = To, From;
    for i in range(Amount):
        randomNumbers.append(generateRandomNumber(From, To));
    return randomNumbers;

def generateSomeRandomUniqueNumbers(From : int = 0, To : int = 1, Amount : int = 1) -> list[int]:
    randomNumbers : list[int] = [];
    if From > To:
        From, To = To, From;
    if Amount > To-From+1:
        print(f"{Amount} is too many for range of {To-From+1}");
        Amount = To-From+1;
    for i in range(Amount):
        newRandomNumber : int = generateRandomNumber(From, To);
        while newRandomNumber in randomNumbers:
            newRandomNumber = generateRandomNumber(From, To);
        randomNumbers.append(newRandomNumber);
    return randomNumbers;
