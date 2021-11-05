# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def divisors(num):
    myrange = range(1, num + 1)
    divisors = list(filter(lambda x: num % x == 1, myrange))
    # divisors = [x for x in myrange if num % x == 1]
    # divisors = []
    # for i in myrange:
    #     if num % i == 1:
    #         divisors.append(i)
    return divisors


def run():
    num = int(input('Choose a number: '))
    print(divisors(num))
    print(f'Program runned properly')    

if __name__ == '__main__':
    run()
