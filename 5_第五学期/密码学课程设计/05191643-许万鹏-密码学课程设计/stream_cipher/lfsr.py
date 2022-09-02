class Lfsr(object):
    def __init__(self, coefficients: list) -> None:
        self._coefficients = coefficients
        self._reg_len = max(self._coefficients)
        self._shift_reg = '1'.zfill(self._reg_len)
        self._regs = [self._shift_reg]
        self._output = []

    @property
    def regs(self) -> list[str]:
        return self._regs

    @property
    def output(self) -> list:
        return self._output

    @staticmethod
    def feedback(reg, taps) -> int:
        res = reg[taps[0] - 1]
        for i in range(1, len(taps)):
            res = int(res) ^ int(reg[taps[i] - 1])
        return res

    def run(self) -> None:
        for i in range(pow(2, self._reg_len) - 1):
            self._output.append(self._shift_reg[-1])
            input = str(self.feedback(self._shift_reg, self._coefficients))
            self._shift_reg = input + self._shift_reg[:-1]
            # if self._shift_reg in self._regs:
            #     break
            # else:
            #     self._regs.append(self._shift_reg)
            self._regs.append(self._shift_reg)


def main():
    # 还有很多逻辑控制没改，再加几个异常处理
    while True:
        # x^16+x^5+x^3+x^2+1
        try:
            coefficients = sorted([int(_) for _ in input('请输入本原多项式x的系数(以空格分隔):\n').split()], reverse=True)
        except ValueError:
            print('请重新输入！')
            continue
        print('输入的本原多项式为:')
        polynomial = [f'x^{str(coefficient)}' for coefficient in coefficients] + ['1']
        print('+'.join(polynomial))
        print(f'其理论最大周期为：{pow(2, max(coefficients)) - 1}')
        mode = input('确认使用这个本原多项式吗？\n[Y]确定\t[N]重新输入\t[Q]退出\n')
        if mode in ('Y', 'y'):
            machine = Lfsr(coefficients)
            machine.run()
            output = machine._output
            regs = machine._regs
            print(f'周期为：{len(output)}')
            while True:
                choice1 = input('是否查看输出序列？\n[Y]是\t[N]否\n')
                if choice1 in ('Y', 'y'):
                    print(''.join(output))
                elif choice1 in ('N', 'n'):
                    pass
                else:
                    print('请重新输入！')
                    continue
                break
            while True:
                choice2 = input('是否输出周期内寄存器各状态？\n[Y]是\t[N]否\n')
                if choice2 in ('Y', 'y'):
                    with open('regs.txt', 'w') as f:
                        for i in regs:
                            f.write(f'{i}\n')
                    print('成功！周期内寄存器各状态保存在regs.txt')
                elif choice2 in ('N', 'n'):
                    pass
                else:
                    print('请重新输入！')
                    continue
                break
        elif mode in ('N', 'n'):
            continue
        elif mode in ('Q', 'q'):
            break
        else:
            print('请重新输入！')
            continue


if __name__ == '__main__':
    main()
