from zeep import Client

cliente = Client(wsdl='https://www.dataaccess.com/webservicesserver/NumberConversion.wso?wsdl')

print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*==*=*=*")
#Conversion de numero a letras
a = int(input("a:"))
print("=*=*=La Respuesta es:=*=*=*")
print(cliente.service.NumberToWords(a))
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*==*=*=*")

#Conversion de numero a dolares
b = float(input("b:"))
print("=*=*=La Respuesta es:=*=*=*")
print(cliente.service.NumberToDollars(b))
print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*==*=*=*")

