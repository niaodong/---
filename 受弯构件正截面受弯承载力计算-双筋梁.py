# -*- coding: utf-8 -*-
import math
"""
受弯构件正截面受弯承载力计算-双筋梁 V0.2
默认单位N,mm
"""
print("受弯构件正截面受弯承载力计算-双筋梁 V0.2\n默认单位N,mm")


# 情况1
def doubleq1():
    h0 = h - a1s
    x = Eb * h0
    print("x=xb=ξb*h0=%.2f" % x)
    # 计算钢筋面积
    As1 = (M - a1 * fc * b * x * (h0 - x / 2)) / (fy1 * (h0 - a2s))
    As = (As1 * fy1 + a1 * fc * b * x) / fy
    print("As=%.2f" % As)
    print("As'=%.2f" % As1)
    # 判断条件
    if x >= 2 * a2s:
        print("x≥2as',可以")


# 情况2
def doubleq2():
    As1 = int(input("请输入受压钢筋面积As'："))
    h0 = h - a1s
    M1 = fy1 * As1 * (h0 - a2s)
    M2 = M - M1
    x = h0 - math.sqrt(h0 ** 2 - ((2 * M2) / (a1 * fc * b)))
    print("x=%.2f" % x)
    As = (As1 * fy1 + a1 * fc * b * x) / fy
    print("As=%.2f" % As)
    print("As'=%.2f" % As1)
    # 判断条件
    if x >= 2 * a2s:
        print("x≥2as',可以")


if __name__ == '__main__':
        # 输入参数
        h = int(input("请输入截面高h："))
        b = int(input("请输入界面宽b："))
        M = int(input("请输入弯矩设计值M："))
        fc = float(input("请输入混凝土抗压强度fc："))
        ft = float(input("请输入混凝土抗拉强度ft："))
        fy = float(input("请输入受拉纵筋抗拉强度设计值fy："))
        fy1 = float(input("请输入受拉纵筋抗拉强度设计值fy'："))
        a1 = float(input("请输入α1："))
        Eb = float(input("请输入ξb："))
        a1s = int(input("请输入假定as高度："))
        a2s = int(input("请输入假定as'高度："))

        # 判断情况一与情况二
        judge = int(input("As'是否已知？（0已知，1未知）"))
        if judge == 0:
                doubleq2()
        elif judge == 1:
                doubleq1()
