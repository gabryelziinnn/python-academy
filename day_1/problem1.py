def to_jaden_case(string):
     # Armazeno a palavra da função em outra variavel e capitalizo a primeira letra de cada palavra
     string = result = string.title()
     # O resultado é separado
     result = ""
     # para cada palavra eu deixo minuscula a ultima palavra
     for word in string.split():
        result += word[:-1] + word[-1].lower() + " "
     return result[:-1]  
     
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))