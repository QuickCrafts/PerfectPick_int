from lxml import etree

# Definir la estructura de entrada y salida para el método del servicio web SOAP
class GetBooksRequest:
    def __init__(self):
        pass


class GetBooksResponse:
    def __init__(self, data):
        self.data = data

# Generar el archivo WSDL
wsdl = """
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://example.com/bookservice" targetNamespace="http://example.com/bookservice">
    <types>
        <xsd:schema targetNamespace="http://example.com/bookservice">
            <xsd:complexType name="Book">
                <xsd:sequence>
                    <xsd:element name="idBook" type="xsd:string"/>
                    <xsd:element name="author" type="xsd:string"/>
                    <xsd:element name="genres" type="xsd:string"/>
                    <xsd:element name="pages" type="xsd:int"/>
                    <xsd:element name="rating" type="xsd:float"/>
                    <xsd:element name="title" type="xsd:string"/>
                    <xsd:element name="year" type="xsd:int"/>
                    <xsd:element name="__typename" type="xsd:string"/>
                </xsd:sequence>
            </xsd:complexType>
            <xsd:complexType name="GetBooksResponse">
                <xsd:sequence>
                    <xsd:element name="data" type="tns:Book" minOccurs="0" maxOccurs="unbounded"/>
                </xsd:sequence>
            </xsd:complexType>
        </xsd:schema>
    </types>
    <message name="GetBooksRequest">
    </message>
    <message name="GetBooksResponse">
        <part name="data" type="tns:GetBooksResponse"/>
    </message>
    <portType name="BookServicePortType">
        <operation name="getBooks">
            <input message="tns:GetBooksRequest"/>
            <output message="tns:GetBooksResponse"/>
        </operation>
    </portType>
    <binding name="BookServiceBinding" type="tns:BookServicePortType">
        <soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/http"/>
        <operation name="getBooks">
            <soap:operation soapAction="http://example.com/bookservice/getBooks"/>
            <input>
                <soap:body use="encoded" namespace="http://example.com/bookservice" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
            </input>
            <output>
                <soap:body use="encoded" namespace="http://example.com/bookservice" encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"/>
            </output>
        </operation>
    </binding>
    <service name="BookService">
        <port name="BookServicePort" binding="tns:BookServiceBinding">
            <soap:address location="http://localhost:8082"/>
        </port>
    </service>
</definitions>
"""

# Escribir el archivo WSDL en disco
with open("service.wsdl", "w") as file:
    file.write(wsdl)

print("Archivo WSDL generado exitosamente")