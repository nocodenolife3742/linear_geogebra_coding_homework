from matrix import *


def question_a():
    print("question_a:")

    print("A + 3B = " + str(A + B.scalar_multiply(3)))
    print("C - 2B * E^T = " + str(C - B.scalar_multiply(2) * E.transpose()))
    print("A^T = " + str(A.transpose()))

    print()


def question_b():
    print("question_b:")

    M = A * B
    N = B * A
    print("M = " + str(M))
    print("N = " + str(N))

    if M == N:
        print("M is equal to N")
    else:
        print("M is not equal to N")

    print()


def question_c():
    print("question_c:")

    P = C.transpose() * B.transpose()
    Q = (B * C).transpose()
    print("P = " + str(P))
    print("Q = " + str(Q))

    if P == Q:
        print("P is equal to Q")
    else:
        print("P is not equal to Q")

    print()


def question_d():
    print("question_d:")

    print("inverse of A : " + str(A.inverse()))
    print("inverse of B : " + str(B.inverse()))

    print()


def question_e():
    print("question_e:")

    print("A is diagonal : " + str(A.is_diagonal()))
    print("B is diagonal : " + str(B.is_diagonal()))
    print("F is diagonal : " + str(F.is_diagonal()))
    print("I is diagonal : " + str(I.is_diagonal()))

    print()


def question_f():
    print("question_f:")

    print("A is symmetric : " + str(A.is_symmetric()))
    print("B is symmetric : " + str(B.is_symmetric()))
    print("F is symmetric : " + str(F.is_symmetric()))
    print("I is symmetric : " + str(I.is_symmetric()))

    print()


def main():
    question_a()
    question_b()
    question_c()
    question_d()
    question_e()
    question_f()


if __name__ == "__main__":
    main()
