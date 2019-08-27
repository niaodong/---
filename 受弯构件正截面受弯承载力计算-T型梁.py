# -*- coding: utf-8 -*-
import math
"""
受弯构件正截面受弯承载力计算-T型梁 V0.2
默认单位N,mm
"""
print("受弯构件正截面受弯承载力计算-T型梁 V0.1\n默认单位N,mm")


# 情况1
def T1():
    x = h0 - math.sqrt(h0 ** 2 - ((2 * M) / (a1 * fc * bf1)))
    As = (a1 * fc * bf1 * x) / fy
    print("x=%.2f" % x)
    print("As=%.2f" % As)
    p = As / (b * h0)
    pmin = max(0.002, 0.24 * ft / fy) * (h / h0)
    if p >= pmin:
        print("ρ=%.4f ≥ ρmin=%.4f,可以" % (p, pmin))
    else:
        print("ρ=%.4f < ρmin=%.4f,少筋" % (p, pmin))


# 情况2
def T2():
    M1 = a1 * fc * (bf1 - b) * hf1 * (h0 - hf1 / 2)
    M2 = M - M1
    x = h0 - math.sqrt(h0 ** 2 - ((2 * M2) / (a1 * fc * b)))
    As = (a1 * fc * (bf1 - b) * hf1 + a1 * fc * b * x) / fy
    print("x=%.2f" % x)
    print("As=%.2f" % As)
    xb = Eb * h0
    if x <= xb:
        print("x=%.2f ≤ xb=%.2f，可以" % (x, xb))
    else:
        print("x=%.2f > xb=%.2f，超筋" % (x, xb))


if __name__ == '__main__':
    # 输入参数
    h = float(input("请输入截面高h："))
    b = float(input("请输入界面宽b："))
    hf1 = float(input("请输入缘翼高hf'："))
    bf1 = float(input("请输入缘翼宽bf'："))
    M = float(input("请输入弯矩设计值M："))
    fc = float(input("请输入混凝土抗压强度fc："))
    ft = float(input("请输入混凝土抗拉强度ft："))
    fy = float(input("请输入受拉纵筋抗拉强度设计值fy："))
    a1 = float(input("请输入α1："))
    Eb = float(input("请输入ξb："))
    a1s = float(input("请输入假定as高度："))

    # 选择情况
    h0 = h - a1s
    if a1 * fc * bf1 * hf1 * (h0 - hf1 / 2) >= M:
        print("情况一")
        T1()
    elif a1 * fc * bf1 * hf1 * (h0 - hf1 / 2) < M:
        print("情况二")
        T2()
    else:
        print("请重新输入参数")
