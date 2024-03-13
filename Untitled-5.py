mat = [list(map(int, input().split())) for i in range(3)]
n = 0
if mat[0][3] == None:
    detmat = (mat[0][0] * mat[1][1] * mat[2][2] + mat[0][1] * mat[1][2] * mat[2][0] + mat[0][2] * mat[1][0] * mat[2][1]) - mat[0][2] * mat[1][1] * mat[2][0] - mat[0][0] * mat[1][2] * mat[2][1] - mat[0][1] * mat[1][0] * mat[2][2]
    if detmat == 0:
        print("Столбцы линейно зависимы ")
        for i in mat:
            for j in i:
                print(j, end = " ")
            print()




# mat = []
# for i in range(3):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     mat.append(row[:3:])

# for i in range(-100, 100):
#     for j in range(-100, 100):
#         for z in range(-100, 100):
#             str1 = i * mat[0][0] + j * mat[0][1] + z * mat[0][2] 
#             str2 = i * mat[1][0] + j * mat[1][1] + z * mat[1][2] 
#             str3 = i * mat[2][0] + j * mat[2][1] + z * mat[2][2]
#             if str1 + str2 + str3 == 0:
#                 n = 1
#             break
# if n == 1:
#     print("столбцы линейно зависимы ")

