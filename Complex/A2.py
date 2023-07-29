from A1 import ComplexNumber
import numbers
import math

# construct a matrix of in a ComplexNumber space 
matrix3 = [
    [ComplexNumber(5, 0), ComplexNumber(2, -1)],
    [ComplexNumber(0, 0), ComplexNumber(4, 5)]
]

matrix5 = [
    [ComplexNumber(5, 1), ComplexNumber(2, -7)],
    [ComplexNumber(2, 4), ComplexNumber(3, 5)]
]

matrix4 = [
    [ComplexNumber(5, 0), ComplexNumber(4, 5), ComplexNumber(6, -16)],
    [ComplexNumber(4, -5), ComplexNumber(4, 5), ComplexNumber(7, 0)],
    [ComplexNumber(6, 16), ComplexNumber(7, 0), ComplexNumber(-2, 0)],
    ]

matrix6 = [
    [ComplexNumber(1/math.sqrt(3), 0), ComplexNumber(1/math.sqrt(3), 5), ComplexNumber(1/math.sqrt(3), -16)],
    [ComplexNumber(1/math.sqrt(2), 0), ComplexNumber(0, 0), ComplexNumber(-1/math.sqrt(2))],
    [ComplexNumber(1/math.sqrt(6), 0), ComplexNumber(2/math.sqrt(6), 0), ComplexNumber(1/math.sqrt(6), 0)],
    ]

unitaryMatrix = [
        [ ComplexNumber(1/math.sqrt(2), 0), ComplexNumber(1/math.sqrt(2), 0)],
        [ComplexNumber(1/math.sqrt(2)), ComplexNumber(0, -1/math.sqrt(2))],
    ]

vect4 = [ComplexNumber(6, 1), ComplexNumber(6, 1), ComplexNumber(0, 1)]
vect5 = [ComplexNumber(5, 1), ComplexNumber(3, 1), ComplexNumber(-7, 1)]

def toString(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j].toString()

def matrixMultiply(matrixA, matrixB):
    matrix = []
    for i in range(len(matrixA)):
        rows = []
        for j in range(len(matrixA[0])):
            res = matrixA[i][j].multiply(matrixB[j][i])
            rows.append(res)
        matrix.append(rows)
    return matrix
            

# vector x matrix multiplication
def vectorMultiply(matrix, vector):
    res = []
    for i in range(len(matrix)):
        row = ComplexNumber()
        for j in range(len(matrix[0])):
            # dot product
            c = matrix[i][j]
            v = vector[i]
            row.add(v.multiply(c))
        res.append(row)
        row.toString()
    return res

def transpose(matrix):
    transpose = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    return transpose    

def adjoint(matrix):
    matrix = transpose(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = matrix[i][j].Conjugate()
    return matrix

# two complex vectors of length n and calculates their inner product
def innerProduct(vectorA, vectorB):
    result = ComplexNumber()
    for i in range(len(vectorA)):
        v1 = vectorA[i]
        v2 = vectorB[i].Conjugate()   
        result.add(v1.multiply(v2))
    return result

# calculate the norm of a complex vector
def norm(vector):
    result = ComplexNumber()
    for i in range(len(vector)):
        v1 = vector[i]
        result.add(v1.pow2())
        result.sqrt()
    return result

# calculates the distance of two given complex vectors
def distance(vectorA, vectorB):
    vector = []
    for i in range(len(vectorA)):
        v1 = vectorA[i]
        v2 = vectorB[i]
        vector.append(v1.sub(v2))
    for j in range(len(vector)):
        pass
    #return v3.sqrt()
        
    # square matrix and tells if it is hermitian
def isHermitian(matrix) -> bool:
    for i in range(3):
        for j in range(3):
            if i != j:
                c = matrix[i][j]
                tc = matrix[j][i].Conjugate()
                print(c.compare(tc))
#returns identity matrix
def identity(matrix):
    n = len(matrix)
    identity_matrix = [] 
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(ComplexNumber(1, 0))
            else: 
                row.append(ComplexNumber(0, 0))           
        identity_matrix.append(row)

    return identity_matrix


# inverse X transpose conjugate
def isUnitary(matrix) -> bool:
    tc = transpose(matrix)
    inverse = matrixMultiply(identity(matrix), matrix)

    for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a = inverse[i][j]
                b = tc[i][j].Conjugate()
                
                
                print(b.toString())
                # print(a.compare(b))

    

    # two matrices and constructs their tensor product
def tensorProduct(va, vb):
    tensorProduct = []
    for i in range(len(va)):
        rows = []
        for j in range(len(vb)):
            v1 = va[i].multiply(vb[j])
            print(v1.toString())
            rows.append(v1)
        tensorProduct.append(rows)


identity(matrix3)

print("\t Originial Matrix: ")
toString(matrix3)

print("\t Transpose Matrix: ")
toString(transpose(matrix3))

print("\t Adjoint Matrix: ")
toString(adjoint(matrix3))

print("\t Matrix Multiplication: ")
toString(matrixMultiply(matrix3, matrix5))

print("\t Vector Matrix Multiplication: ")
vectorMultiply(matrix4, vect4)

print("\t InnerProduct of two vectors: \n")
innerProduct(vect4, vect5)

print("\t Norm of a complex vector: \n")
norm(vect4).toString()

print("\t Distance function: ")
distance(vect4, vect5)

print("\nisHermitian: ")
isHermitian(matrix4)
print("\tisUnitary: ") 
isUnitary(unitaryMatrix)
print("\t TensorProduct: ")
# tensorProduct(vect4, vect5)

