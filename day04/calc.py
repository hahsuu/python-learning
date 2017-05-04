import re


def calc(formula):
    flag = True
    while flag:
        m = re.search('\([^()]+\)', formula)
        if m:

            sub_formula = m.group().strip('()')
            print(sub_formula)
        break


if __name__ == "__main__":
    formula = ' 1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    result = calc(formula)