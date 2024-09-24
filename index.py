from classes.Produto import Produto
from classes.Categoria import Categoria

# Produto.listarTodos()

produto = Produto('005', 'Placa de Vídeo', 123, 3000)
produto.inserir()
produto.listarTodos()

categoria = Categoria('Eletrônico')
categoria.inserir()
categoria.listarTodos()