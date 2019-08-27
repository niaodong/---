# -*- coding: utf-8 -*-
import math
"""
受弯构件正截面受弯承载力计算-单筋梁 V0.2
默认单位N,mm
"""
print("受弯构件正截面受弯承载力计算-单筋梁 V0.1\n默认单位N,mm")


def single():
    # 初步计算过程
    h0 = h - a1s
    x = h0 - math.sqrt(h0 ** 2 - ((2 * M) / (a1 * fc * b)))
    print("h0=%.2f" % h0)
    print("x=%.2f" % x)
    # 判断超筋
    # 符合时
    if Eb * h0 >= x:
        print("x=%.2f ≤ xb=%.2f，可以" % (x, Eb * h0))
        As = (a1 * fc * b * x) / fy
        print("As=%.2f" % As)
        # 选用钢筋
        As = int(input("请输入选择的钢筋面积："))
        # 判断少筋
        p = As / (b * h0)
        pmin = max(0.002, (0.24 * ft) / fy) * (ft / fy)
        # 不少筋
        if p >= pmin:
            print("ρ=%.4f ≥ ρmin=%.4f,可以" % (p, pmin))
            print("最终钢筋面积As=%.2f" % As)
        # 少筋
        else:
            print("ρ=%.6f < ρmin=%.6f,少筋" % (p, pmin))
            As = int(input("请重新输入选择钢筋面积："))
    # 超筋时
    else:
        print("xb=%.2f" % Eb * h0)
        print("超筋")


if __name__ == '__main__':
    # 输入参数
    h = int(input("请输入截面高h："))
    b = int(input("请输入界面宽b："))
    M = int(input("请输入弯矩设计值M："))
    fc = float(input("请输入混凝土抗压强度fc："))
    ft = float(input("请输入混凝土抗拉强度ft："))
    fy = float(input("请输入纵筋抗拉强度设计值fy："))
    a1 = float(input("请输入α1："))
    Eb = float(input("请输入ξb："))
    a1s = int(input("请输入假定as高度："))

    # 调用计算函数
    single()
