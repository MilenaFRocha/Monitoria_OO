from views import TelaMain, TelaCreateForms
from models import Point, Line, Circle, Polygon, Triangle
from controller import CartesianBoard

telaform = TelaCreateForms()
telamain = TelaMain()
caminho_ponto = r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\databasePoint.json'
caminho_linha = r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\databaseLine.json'
caminho_circulo = r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\databaseCircle.json'
caminho_triangulo = r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\databaseTriangle.json'
caminho_poligono = r'C:\Users\milen\OneDrive\Documentos\Monitoria (teórica)\Projeto 1\databasePolygon.json'
carte=CartesianBoard(caminho_ponto,caminho_linha,caminho_circulo,caminho_triangulo,caminho_poligono)

comando = -1
while comando != 5:
    telamain.menu()
    comando = telamain.pedir_comando()


    match comando:
        case 1:
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                
                    carte.criar_inserir_forma(Point, carte.caminho_ponto)
                

                case 2:
                    carte.criar_inserir_forma(Line,carte.caminho_linha)
                
                    pass

                case 3:
                    carte.criar_inserir_forma(Circle,carte.caminho_circulo)
                    pass
                
                case 4:
                    carte.criar_inserir_forma(Triangle,carte.caminho_triangulo)
                case 5:
                    carte.criar_inserir_forma(Polygon,carte.caminho_poligono)

                    pass

                

        case 2:
            print("Qual opção deseja ler?")
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                    print("Pontos:")
                    carte.show_form(carte.caminho_ponto,Point.type())
                    pass

                case 2:
                    print("Linhas:")
                    carte.show_form(carte.caminho_linha,Line.type())
                    pass

                case 3:
                    print("Circulos:")
                    carte.show_form(carte.caminho_circulo,Circle.type())
                    pass
                
                case 4:
                    print("Triangulos:")
                    carte.show_form(carte.caminho_triangulo,Triangle.type())
                    pass

                case 5:
                    print("Poligonos:")
                    carte.show_form(carte.caminho_poligono,Polygon.type())
                    pass

        case 3:
            print("Qual opção deseja atualizar?")
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                    #o que deseja atualizar
                    pass

                case 2:
                    #o que deseja atualizar
                    pass

        case 4:
            print("Qual opção deseja deletar?")
            telaform.menu()
            opcao = int(telaform.pedir_comando())
            
            match opcao :
                case 1:
                    ponto_deletar = input("Qual ponto deseja deletar?")
                    carte.remove_forma(carte.caminho_ponto, Point.type(), ponto_deletar)
                    print("Ponto deletado com sucesso!")
                    pass
                case 2: 
                    line_deletar = input("Qual linha deseja deletar?")
                    carte.remove_forma(carte.caminho_linha,Line.type(),line_deletar)
                    print("Linha deletada com sucesso!")
                    pass

                case 3:
                    circulo_deletar = input("Qual circulo deseja deletar?")
                    carte.remove_forma(carte.caminho_circulo, Circle.type(), circulo_deletar)
                    print("Circulo deletado com sucesso!")
                    pass

                case 4:
                    triangulo_deletar = input("Qual triangulo deseja deletar?")
                    carte.remove_forma(carte.caminho_triangulo, Triangle.type(),triangulo_deletar)
                    print("Triangulo deletado com sucesso!")
                    pass

                case 5:
                    poligono_deletar = input("Qual poligono deseja deletar?")
                    carte.remove_forma(carte.caminho_poligono,Polygon.type(),poligono_deletar)
                    print("Poligono deletado com sucesso!")
                    pass
        case 5 :
            print("Saindo...")
            exit()
        case _:
            print("Comando inválido, digite outro número válido")
            
