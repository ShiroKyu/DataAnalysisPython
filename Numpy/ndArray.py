import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1.dtype)

# Criar Array só com zeros ou ums

# Pode mandar uma tupla com as dimensões
# arr2 = np.zeros(10)
arr2 = np.zeros((4, 4))
arr3 = np.ones((4, 4))

print(arr2, end='\n\n')
print(arr3, end='\n\n')


# Semelhante a função range
arr4 = np.arange(15)
print(arr4, end='\n\n')

# Converte para ndarray
print(np.asarray([1, 2, 3]), end='\n\n')


# Gera um ndarray só de ums com o mesmo formato e tipo do array passado
arr5 = np.ones_like([[1, 2, 3], [4, 5, 6]])
print(arr5, end='\n\n')

# Gera uma matriz identidade
arr6 = np.identity(10)
print(arr6)
