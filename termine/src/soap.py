from zeep import Client

cliente = Client(wsdl='http://www.dneonline.com/calculator.asmx?WSDL')

print("========================================")
print("*=*=*=*=AGREGAR*=*=*=*=*")
print(cliente.service.Add(4,5))
print("*=*=*=*=MULTIPLICAR*=*=*=*=*")
print(cliente.service.Multiply(8,2))
print("*=*=*=*=DIVISION*=*=*=*=*")
print(cliente.service.Divide(20,2))
print("*=*=*=*=SUBSTRACCION*=*=*=*=*")
print(cliente.service.Subtract(10,2))
print("======================================")
