# def ToutLesArcs(data):
#     shape = data.shape
#     lin = shape[0]
#     col = shape[1]
#     a = np.array([], dtype=int)

#     for i in range(3, col+1):
#         for j in range(0, lin):
#             if(data[:, i-1:i][j] >= 0):
#                 a = np.append(a, data[:, i-1:i][j])
#     return a
